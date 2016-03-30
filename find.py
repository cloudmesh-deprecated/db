from cloudmesh_db import VM_OPENSTACK, VM_LIBCLOUD
from cloudmesh_db import CloudmeshDatabase

echo = False


cm = CloudmeshDatabase()

cm.info()

def populate(cloud, _from,_to):
    global cm
    for i in range(_from, _to):
        t = CloudmeshDatabase.table(category=cloud, type="vm")
        vm = t("vm_" + str(i).zfill(3))

        cm.add(vm)

populate("openstack", 0,10)
populate("libcloud", 10,20)


for name in ["vm_002", "vm_009"]:
    vm = cm.find(category="openstack", kind="vm", name=name)
    if vm is not None:
        print(vm.name)
    else:
        print (name, "not found")

cm1 = CloudmeshDatabase()
# cm1.start()

# print cm, cm1, cm.session == cm1.session

vm = cm1.find("libcloud", "vm", name="vm_016")

if vm is not None:
    print(vm.name)


vm = cm.x_find(kind="vm", scope="first", name="vm_007" )

if vm is not None:
    print(vm.name)
