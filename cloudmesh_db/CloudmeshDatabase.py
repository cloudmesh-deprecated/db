from __future__ import print_function
import os
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

from cloudmesh_client.common.dotdict import dotdict
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pprint import pprint
from sqlalchemy import update

class CloudmeshMixin(object):
    __mapper_args__ = {'always_refresh': True}

    category = Column(String, default="undefined")
    kind = Column(String, default="undefined")
    type = Column(String, default="undefined")

    provider = Column(String, default="undefined")

    id = Column(Integer, primary_key=True)
    # created_at = Column(DateTime, default=datetime.now)
    # updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_at = Column(String,
                        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(String,
                        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        onupdate=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    label = Column(String, default="undefined")
    name = Column(String, default="undefined")
    user = Column(String, default="undefined")
    project = Column(String, default="undefined")

    def set_defaults(self, **kwargs):
        self.user = kwargs.get('user') or  CloudmeshDatabase.user
        self.name = kwargs['name']
        self.label = kwargs['name']
        self.category = self.__category__
        self.kind = self.__kind__
        self.provider = self.__provider__


    def __repr__(self):
        print ("{} {} {} {}".format(self.id, self.name, self.kind, self.category))


class CloudmeshDatabase(object):

    __shared_state = {}
    data = {"filename": "data.db"}
    initialized = None
    engine = create_engine('sqlite:///{filename}'.format(**data), echo=False)
    Base = declarative_base()
    session = None
    tables = None
    user = "gvonlasz"

    def __init__(self):
        self.__dict__ = self.__shared_state

        if self.initialized is None:
            self.create()
            self.create_tables()
            self.start()

    #
    # MODEL
    #
    @classmethod
    def create(cls):
        # cls.clean()
        if not os.path.isfile("{filename}".format(**cls.data)):
            cls.create_model()

    @classmethod
    def create_model(cls):
        cls.Base.metadata.create_all(cls.engine)
        print ("Model created")

    @classmethod
    def clean(cls):
        os.system("rm -f {filename}".format(**cls.data))

    @classmethod
    def create_tables(cls):
        """
        :return: the list of tables in model
        """
        cls.tables = [c for c in cls.Base.__subclasses__()]

    @classmethod
    def info(cls):
        print ()
        print ("Info")
        print ()
        print("{:<20} {:<15} {:<15} {:<4}".format("tablename", "category", "kind", "count"))
        print (70 * "=")

        for t in cls.tables:
            count = cls.session.query(t).count()
            print ("{:<20} {:<15} {:<15} {:<4}".format(t.__tablename__, t.__category__, t.__kind__, count))
        print()


    @classmethod
    def table(cls, category=None, kind=None):
        """

        :param category:
        :param kind:
        :return: the table class based on a given table name.
                 In case the table does not exist an exception is thrown
        """
        for t in cls.tables:
            if (t.__kind__ == kind) and (t.__category__ == category):
                return t
        ValueError("ERROR: unkown table {} {}".format(category, kind))
    #
    # SESSION
    #
    # noinspection PyPep8Naming
    @classmethod
    def start(cls):
        if cls.session is None:
            print ("start session")
            Session = sessionmaker(bind=cls.engine)
            cls.session = Session()
    @classmethod
    def all(cls,
            category='general',
            kind=None,
            table=None):

        t = table

        if category is not None and kind is not None:
            t = cls.table(category=category, kind=kind)
        else:
            data = {
                "category": category,
                "kind": kind,
            }
            ValueError("find is improperly used category={category} kind={kind}"
                       .format(**data))
        result = cls.session.query(t).all()
        return cls.to_list(result)

    @classmethod
    def find(cls,
             scope='first',
             category='general',
             kind=None,
             output='dict',
             table=None,
             **kwargs
            ):
        """
        find (category="openstack", kind="vm", name="vm_002")
        find (VM_OPENSTACK, kind="vm", name="vm_002") # do not use this one its only used internally

        :param category:
        :param kind:
        :param table:
        :param kwargs:
        :return:
        """

        t = table

        if category is not None and kind is not None:
            t = cls.table(category=category, kind=kind)
        else:
            data = {
                "category": category,
                "kind": kind,
                "table": table,
                "args": kwargs
            }
            ValueError("find is improperly used category={category} kind={kind} table={table} args={args}"
                       .format(**data))

        result = cls.session.query(t).filter_by(**kwargs)

        if scope=='first':
            result =  result.first()
            if output == 'dict':
                result = cls.to_list([result])[0]
        elif output == 'dict':
            return cls.to_list(result)
        else:
            return result

    @classmethod
    def x_find(cls, **kwargs):
        """
        This method returns either
        a) an array of objects from the database in dict format, that match a particular kind.
           If the kind is not specified vm is used. one of the arguments must be scope="all"
        b) a single entry that matches the first occurance of the query specified by kwargs,
           such as name="vm_001"

        :param kwargs: the arguments to be matched, scope defines if all or just the first value
               is returned. first is default.
        :return: a list of objects, if scope is first a single object in dotdict format is returned
        """
        kind = kwargs.pop("kind", "vm")
        scope = kwargs.pop("scope", "first")

        result = []

        for t in cls.tables:
            if (t.__kind__ == kind):
                part = cls.session.query(t).filter_by(**kwargs)
                result.extend(cls.to_list(part))

        objects = result
        if scope == "first" and objects is not None:
            objects = dotdict(result[0])

        return objects

    @classmethod
    def filter_by(cls, **kwargs):
        """
        This method returns either
        a) an array of objects from the database in dict format, that match a particular kind.
           If the kind is not specified vm is used. one of the arguments must be scope="all"
        b) a single entry that matches the first occurance of the query specified by kwargs,
           such as name="vm_001"

        :param kwargs: the arguments to be matched, scope defines if all or just the first value
               is returned. first is default.
        :return: a list of objects, if scope is first a single object in dotdict format is returned
        """
        scope = kwargs.pop("scope", "first")

        result = []

        for t in cls.tables:
            part = cls.session.query(t).filter_by(**kwargs)
            result.extend(cls.to_list(part))

        objects = result
        if scope == "first" and objects is not None:
            objects = dotdict(result[0])

        return objects

    @classmethod
    def add(cls, o):
        cls.session.add(o)
        cls.save()

    @classmethod
    def save(cls):
        cls.session.commit()
        cls.session.flush()

    @classmethod
    def to_list(cls, obj):
        """
        convert the object to dict

        :param obj:
        :return:
        """
        result = list()
        for u in obj:
            if u is not None:
                values = {}
                for key in list(u.__dict__.keys()):
                    if not key.startswith("_sa"):
                        values[key] = u.__dict__[key]
                result.append(values)
            # pprint(result)
        return result

    #
    # DELETE
    #

    def delete(cls,
               category=None,
               kind=None,
               **kwargs):
        """
        :param kind:
        :return:
        """
        #
        # BUG does not look for user related data
        # user = self.user or Username()
        #
        if category is not None and kind is not None:
            t = cls.table(category=category, kind=kind)
        else:
            data = {
                "category": category,
                "kind": kind,
            }
            ValueError("find is improperly used category={category} kind={kind}"
                       .format(**data))
        if len(kwargs) == 0:
            cls.session.query(t).delete()
        else:
            cls.session.query(t).filter_by(**kwargs).delete()
        cls.save()

    @classmethod
    def update(cls,
               category=None,
               kind=None,
               **kwargs):
        """

        :param kind:
        :param kwargs:
        :return:
        """
        # bug: user = self.user or Username()
        if category is not None and kind is not None:
            t = cls.table(category=category, kind=kind)
        else:
            data = {
                "category": category,
                "kind": kind,
            }
            ValueError("find is improperly used category={category} kind={kind}"
                       .format(**data))
        filter = kwargs['filter']
        values = kwargs['update']

        cls.session.query(t).filter_by(**filter).update(values)
        cls.save()

    @classmethod
    def set(cls,
            name,
            attribute,
            value,
            category=None,
            kind=None,
            ):

        if category is None or kind is None:
            o = cls.filter_by(name=name)
            print (o)
            print (o.name)
            print (o.kind)
        '''
        cls.update(kind=kind,
                  category=category,
                  filter={'name': name},
                  update={'label': 'x',
                          attribute: value}
                  )
        '''