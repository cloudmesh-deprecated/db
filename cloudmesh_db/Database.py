from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database(object):

    engine = create_engine('sqlite:///data.db', echo=False)
    Base = declarative_base()

    #
    # MODEL
    #
    @classmethod
    def create(cls):
        # cls.clean()
        if not os.path.isfile("data.db"):
            cls.create_model()

    @classmethod
    def create_model(cls):
        cls.Base.metadata.create_all(cls.engine)
        print ("Model created")

    @classmethod
    def clean(cls):
        os.system("rm -f data.db")

    #
    # SESSION
    #
    @classmethod
    def start(cls):
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def find(cls, table, **kwargs):
        return cls.session.query(table).filter_by(**kwargs).first()


    @classmethod
    def add(cls, o):
        cls.session.add(o)
        cls.session.commit()


