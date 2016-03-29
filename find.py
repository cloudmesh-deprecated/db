from cloudmesh_db import VM
from cloudmesh_db import Database

echo = False


cm = Database()

cm.create()
cm.start()


def populate(_from,_to):
    global cm
    for i in range(_from, _to):
        vm = VM("vm_" + str(i).zfill(3))
        cm.add(vm)

populate(0,10)
populate(10,20)


for name in ["vm_002", "vm_015"]:
    vm = cm.find(VM, name=name)
    if vm is not None:
        print(vm.name)
    else:
        print (name, "not found")

cm1 = Database()
cm1.start()

vm = cm1.find(VM, name="vm_016")

if vm is not None:
    print(vm.name)
