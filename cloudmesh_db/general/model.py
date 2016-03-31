from __future__ import print_function
from ..CloudmeshDatabase import CloudmeshDatabase
from sqlalchemy import Column, Date, Integer, String


class COUNTER(CloudmeshDatabase.CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "counter"
    category = "general"
    kind = 'counter'

    value = Column(Integer)
    kind = "counter"
    type = Column(String, default=int)

    def __init__(self,
                 name=None,
                 value=None,
                 user=None):

        self.label = name
        self.name = name
        self.user = user or  CloudmeshDatabase.user
        self.value = int(value)


class DEFAULT(CloudmeshDatabase.CloudmeshMixin, CloudmeshDatabase.Base):
    """table to store default values

    if the category is "global" it is meant to be a global variable

    todo: check if its global or general
    """
    __tablename__ = "default"
    category = "general"
    kind = 'default'

    value = Column(String)
    type = Column(String, default="string")

    def __init__(self,
                 name=None,
                 value=None,
                 category=None,
                 type=str,
                 user=None):

        self.label = name
        self.category = category or "general"
        self.name = name
        self.user = user or  CloudmeshDatabase.user
        self.type = type or str
        self.value = self.type(value)



class VAR(CloudmeshDatabase.CloudmeshMixin, CloudmeshDatabase.Base):
    """table to store peristant variable values
    """
    # name defined in mixin

    __tablename__ = "var"
    category = "general"
    kind = 'var'

    value = Column(String)
    type = Column(String, default="string")

    def __init__(self,
                 name=None,
                 value=None,
                 category="var",
                 type=str,
                 user=None):

        self.label = name
        self.category = category or "var"
        self.name = name
        self.user = user or  CloudmeshDatabase.user
        self.type = type or str
        self.value = self.type(value)

