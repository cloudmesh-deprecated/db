from __future__ import print_function
from pprint import pprint
from cloudmesh_client2 import Default, DEFAULT
from cloudmesh_client2.db import CloudmeshDatabase
from cloudmesh_client2.common.Printer import Printer
echo = False

cm = CloudmeshDatabase()

def populate(cloud, _from, _to, category):
    global cm
    t = CloudmeshDatabase.table(provider=cloud, kind="default")
    for i in range(_from, _to):
        name = "d_" + str(i).zfill(3)
        value = str(i)
        print ("N", name, value, t)
        o = t(name=name, value=value)
        cm.add(o)


populate("general", 0, 10, "default")

#Default.set("cloud", "kilo")
o = DEFAULT(name="cloud", value="kilo")
cm.add(o)

# TODO: this next statement does not work
Default.set("b", "5")


defaults = cm.x_find(kind="default", scope="all")

print (Printer.list(defaults,
                    order=['name', 'value', 'category', 'kind', 'user']
                    ))


cloud = cm.find(provider="general",
                kind="default",
                scope="first",
                name="cloud")

print(cloud.value)

print (Default.get(name="cloud"))
print ("Cloud:", Default.get(name="cloud"))




print ("Cloud:", Default.cloud)


cm.info()


result = cm.all(provider='general', kind='default')
pprint (len(result))
#assert len(result) == 10

for name in ["d_002", "d_009"]:
    vm = cm.find(provider="general", kind="default", name=name)
    pprint(vm)

print ("HHHH")

vm = cm.x_find(kind="default", scope="first", name="d_007")
pprint(vm)

vm = cm.x_find(kind="default", scope="all")

pprint(vm)

cm.delete(kind="default", provider="general", name="d_003")
cm.delete(kind="default", provider="general", label="d_004")

cm.info()

cm.update(kind="default",
          provider="general",
          filter={'name': "d_002"},
          update={'label': 'x'}
          )

vm = cm.x_find(kind="default", scope="first", name="d_002")
pprint(vm)

print ("KKKK")
cm.update(kind="default",
          provider="general",
          filter={'name': "d_002"},
          update={'label': 'x',
                  'value': 'a'}
          )

vm = cm.x_find(kind="default", scope="first", name="d_002")
pprint(vm)

cm.update(kind="default",
          provider="general",
          filter={'name': "d_002",
                  'name': "d_009"},
          update={'label': 'x',
                  'value': 'a'}
          )

Default.set("iamge", "i")
Default.set("flavor", "f")
Default.set("vm", "v")
Default.set("group", "g")
Default.set("key", "k")
Default.set("debug", "True")
Default.set("refresh", "True")
Default.set("loglevel", "debug")

print(Default.refresh)

defaults = cm.x_find(kind="default", scope="all")
print(Printer.list(defaults,
                   order=['name', 'label', 'value', 'category', 'kind', 'user']
                   ))

# print (Default.list())