from cloudmesh_client2 import Var, VAR
from cloudmesh_client2 import CloudmeshDatabase
from cloudmesh_client2 import Printer

cm = CloudmeshDatabase()

cm.info(kind=["var"])

for v in range(0,5):

    o = VAR(name="a_{}".format(v), value=v)
    print (o)
    cm.add(o)
    print ("{}={}".format(o.name, o.value))

result = cm.all(provider='general', kind='var')

print (Printer.write(result))


cm.info(kind=["var"])


print (result)


Var.set("y", "456", type='int')
Var.set("z", "890", type='int')


Var.set("z", "789", type='int')

result = cm.all(provider='general', kind='var')
print (result)


r = Var.get("y")

print ("y", r.value)

cm.set("y","value","42",kind="var")


print(Var.list())

