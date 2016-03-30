from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cloudmesh_client.common.dotdict import dotdict

class CloudmeshDatabase(object):

    __shared_state = {}
    data = {"filename": "data.db"}
    initialized = None
    engine = create_engine('sqlite:///{filename}'.format(**data), echo=False)
    Base = declarative_base()
    session = None
    tables = None

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
        print ("Info")
        for t in cls.tables:
            print (t.__cloud__, t.__tablename__)

    @classmethod
    def table(cls, cloud=None, type=None):
        """
        :return: the table class based on a given table name.
                 In case the table does not exist an exception is thrown
        """
        for t in cls.tables:
            if (t.__type__ == type) and (t.__cloud__ == cloud):
                return t

        ValueError("ERROR: unkown table {} {}".format(cloud, type))
    #
    # SESSION
    #
    @classmethod
    def start(cls):
        if cls.session is None:
            print ("start session")
            Session = sessionmaker(bind=cls.engine)
            cls.session = Session()

    @classmethod
    def find(cls, cloud, kind, **kwargs):
        t = cls.table(cloud=cloud, type=kind)
        return cls.session.query(t).filter_by(**kwargs).first()


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
            if (t.__type__ == kind):
                part = cls.session.query(t).filter_by(**kwargs)
                print("PPP", cls.to_list(part))
                result.extend(cls.to_list(part))

        objects = result
        print("OOO", objects)
        if scope == "first" and objects is not None:
            objects = dotdict(result[0])

        return objects

    @classmethod
    def add(cls, o):
        cls.session.add(o)
        cls.session.commit()

    @classmethod
    def to_list(cls, obj):
        """
        convert the object to dict

        :param obj:
        :return:
        """
        result = list()
        for u in obj:
            _id = u.id
            print("ID", u.id)
            values = {}
            for key in list(u.__dict__.keys()):
                if not key.startswith("_sa"):
                    values[key] = u.__dict__[key]
            result.append(values)
        # pprint(result)
        return result

