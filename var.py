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



print (result)

cm.info(kind=["var"])


Var.set("y", "456")
#Var.set("z", "789")

result = cm.all(provider='general', kind='var')
print (result)


#r = Var.get("y")

#print ("RRRR", r.value)



print(Var.list())

# print (o)

'''
cm.set(
    "x",
    "value",
    "42",
    category="general",
    kind="var",
)



print (o)
#cm.add(o)
#cm.info(kind=["var"])


print (Var.list())

cm.info()
'''
