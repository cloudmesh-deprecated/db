from ..Database import Database
from sqlalchemy import Column, Date, Integer, String

class VM(Database.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

