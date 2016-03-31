from ..CloudmeshDatabase import CloudmeshDatabase, CloudmeshMixin
from sqlalchemy import Column, Date, Integer, String


# noinspection PyPep8Naming
class VM_OPENSTACK(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "vm_openstack"
    category = "openstack"
    kind = 'vm'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None, user=None):
        self.set_defaults(name=name, user=user)

# noinspection PyPep8Naming
class IMAGE_OPENSTACK(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "image_openstack"
    category = "openstack"
    kind = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None, user=None):
        self.set_defaults(name=name, user=user)


