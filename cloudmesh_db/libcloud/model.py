from ..CloudmeshDatabase import CloudmeshDatabase
from sqlalchemy import Column, Date, Integer, String

class VM_LIBCLOUD(CloudmeshDatabase.Base):
    __tablename__ = "vm_libcloud"
    __cloud__ = "libcloud"
    __type__ = 'vm'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class IMAGE_LIBCLOUD(CloudmeshDatabase.Base):
    __tablename__ = "image_libcloud"
    __cloud__ = "libcloud"
    __type__ = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

