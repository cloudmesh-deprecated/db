from ..CloudmeshDatabase import CloudmeshDatabase
from sqlalchemy import Column, Date, Integer, String

class VM_LIBCLOUD(CloudmeshDatabase.Base):
    __tablename__ = "vm_libcloud"
    category = "libcloud"
    kind = 'vm'

    id = Column(Integer, primary_key=True)
    name = Column(String)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print ("{} {} {} {}".format(self.id, self.name, self.kind, self.category))

class IMAGE_LIBCLOUD(CloudmeshDatabase.Base):
    __tablename__ = "image_libcloud"
    category = "libcloud"
    kind = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print ("{} {} {} {}".format(self.id, self.name, self.kind, self.category))
