from ..CloudmeshDatabase import CloudmeshDatabase
from sqlalchemy import Column, Date, Integer, String

class VM_OPENSTACK(CloudmeshDatabase.Base):
    __tablename__ = "vm_openstack"
    __category__ = "openstack"
    __type__ = 'vm'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class IMAGE_OPENSTACK(CloudmeshDatabase.Base):
    __tablename__ = "image_openstack"
    __category__ = "openstack"
    __type__ = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
