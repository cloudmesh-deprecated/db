from pprint import pprint

from cloudmesh_client2.db import CloudmeshDatabase

echo = False


cm = CloudmeshDatabase()


def populate(cloud, _from,_to):
    global cm
    for i in range(_from, _to):
        t = CloudmeshDatabase.table(category=cloud, kind="vm")
        name = "vm_" + str(i).zfill(3)
        print ("N", name, t)
        vm = t(name=name)

        cm.add(vm)

populate("openstack", 0,10)
populate("libcloud", 10,20)

cm.info()


result = cm.all(category='openstack', kind='vm')
# pprint (result)
assert len(result) == 10


result = cm.all(category='libcloud', kind='vm')
# pprint (result)
assert len(result) == 10


for name in ["vm_002", "vm_009"]:
    vm = cm.find(category="openstack", kind="vm", name=name)
    pprint (vm)

cm1 = CloudmeshDatabase()
# cm1.start()

# print cm, cm1, cm.session == cm1.session

vm = cm1.find(category="libcloud", kind="vm", name="vm_016")
pprint(vm)


vm = cm.x_find(kind="vm", scope="first", name="vm_007" )
pprint(vm)

vm = cm.x_find(kind="vm", scope="all")

pprint (vm)

cm.delete(kind="vm", category="openstack", name="vm_003")
cm.delete(kind="vm", category="openstack", label="vm_004")

cm.info()

cm.update(kind="vm",
          category="openstack",
          filter={'name': "vm_002"},
          update={'label': 'x'}
)

vm = cm.x_find(kind="vm", scope="first", name="vm_002" )
pprint(vm)

cm.update(kind="vm",
          category="openstack",
          filter={'name': "vm_002"},
          update={'label': 'x',
                  'uuid': 'a'}
          )

vm = cm.x_find(kind="vm", scope="first", name="vm_002")
pprint(vm)

cm.update(kind="vm",
          category="openstack",
          filter={'name': "vm_002",
                  'name': "vm_009",},
          update={'label': 'x',
                  'uuid': 'a'}
          )

vm = cm.x_find(kind="vm", scope="first", name="vm_002")
pprint(vm)
vm = cm.x_find(kind="vm", scope="first", name="vm_009")
pprint(vm)




cm.set("vm_009", 'user', 'gregor', category='openstack', kind='vm')

vm = cm.x_find(kind="vm", scope="first", name="vm_009")
pprint(vm)

vm = cm.filter_by(name="vm_011")
pprint(vm)

vm = cm.filter_by(label="x", scope='all', id=3)
pprint(vm)


cm.set("vm_002", 'user', 'world')

vm = cm.x_find(kind="vm", scope="first", name="vm_002")
pprint(vm)

