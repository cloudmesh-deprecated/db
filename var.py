from cloudmesh_client2 import Var
from cloudmesh_client2 import CloudmeshDatabase

cm = CloudmeshDatabase()

Var.set("hallo", "world")

print (Var.list())

cm.info()
