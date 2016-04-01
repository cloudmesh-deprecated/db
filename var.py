from cloudmesh_client2 import Var, VAR
from cloudmesh_client2 import CloudmeshDatabase

cm = CloudmeshDatabase()

cm.info(kind=["var"])

cm.set(
    "x",
    "value",
    "42",
    category="general",
    kind="var",
)

cm.info(kind=["var"])

o = VAR("y", value="123")

cm.info(kind=["var"])

'''
Var.set("hallo", "world")

print (Var.list())

cm.info()
'''