from pprint import pprint

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




defaults = cm.x_find(kind="default", scope="all")

print (Printer.list(defaults,
                    order=['name', 'value', 'category', 'user']
                    ))


import sys; sys.exit()

cm.info()


result = cm.all(provider='openstack', kind='vm')
# pprint (result)
#assert len(result) == 10

result = cm.all(provider='libcloud', kind='vm')
# pprint (result)
# assert len(result) == 10

for name in ["vm_002", "vm_009"]:
    vm = cm.find(provider="openstack", kind="vm", name=name)
    pprint(vm)

cm1 = CloudmeshDatabase()
# cm1.start()

# print cm, cm1, cm.session == cm1.session

vm = cm1.find(provider="libcloud", kind="vm", name="vm_016")
pprint(vm)

vm = cm.x_find(kind="vm", scope="first", name="vm_007")
pprint(vm)

vm = cm.x_find(kind="vm", scope="all")

pprint(vm)

cm.delete(kind="vm", provider="openstack", name="vm_003")
cm.delete(kind="vm", provider="openstack", label="vm_004")

cm.info()

cm.update(kind="vm",
          provider="openstack",
          filter={'name': "vm_002"},
          update={'label': 'x'}
          )

vm = cm.x_find(kind="vm", scope="first", name="vm_002")
pprint(vm)

cm.update(kind="vm",
          provider="openstack",
          filter={'name': "vm_002"},
          update={'label': 'x',
                  'uuid': 'a'}
          )

vm = cm.x_find(kind="vm", scope="first", name="vm_002")
pprint(vm)

cm.update(kind="vm",
          provider="openstack",
          filter={'name': "vm_002",
                  'name': "vm_009",},
          update={'label': 'x',
                  'uuid': 'a'}
          )

vm = cm.x_find(kind="vm", scope="first", name="vm_002")
pprint(vm)
vm = cm.x_find(kind="vm", scope="first", name="vm_009")
pprint(vm)

cm.set("vm_009", 'user', 'gregor', provider='openstack', kind='vm')

vm = cm.x_find(kind="vm", scope="first", name="vm_009")
pprint(vm)

vm = cm.filter_by(name="vm_011")
pprint(vm)

vm = cm.filter_by(label="x", scope='all', cm_id=3)
pprint(vm)

cm.set("vm_002", 'user', 'world')

vm = cm.x_find(kind="vm", scope="first", name="vm_002")
pprint(vm)


vms = cm.x_find(kind="vm", scope="all")
print (len(vms))



print (Printer.list(vms,
                    order=['name', 'status', 'category', 'user', 'provider', 'kind', 'xx']
                    ))

