from ..CloudmeshDatabase import CloudmeshDatabase
from sqlalchemy import Column, Date, Integer, String

class VM_OPENSTACK(CloudmeshDatabase.Base):
    __tablename__ = "vm_openstack"
    category = "openstack"
    kind = 'vm'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print ("{} {} {} {}".format(self.id, self.name, self.kind, self.category))


class IMAGE_OPENSTACK(CloudmeshDatabase.Base):
    __tablename__ = "image_openstack"
    category = "openstack"
    kind = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print ("{} {} {} {}".format(self.id, self.name, self.kind, self.category))

