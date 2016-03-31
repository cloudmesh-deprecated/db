from ..CloudmeshDatabase import CloudmeshDatabase, CloudmeshMixin
from sqlalchemy import Column, Date, Integer, String


# noinspection PyPep8Naming
class VM_LIBCLOUD(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "vm_libcloud"
    category = "libcloud"
    kind = 'vm'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None, user=None):
        self.set_defaults(name=name, user=user)


# noinspection PyPep8Naming
class IMAGE_LIBCLOUD(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "image_libcloud"
    category = "libcloud"
    kind = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None, user=None):
        self.set_defaults(name=name, user=user)
