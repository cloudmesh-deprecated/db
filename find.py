from cloudmesh_db import CloudmeshDatabase

echo = False


cm = CloudmeshDatabase()

cm.info()

def populate(cloud, _from,_to):
    global cm
    for i in range(_from, _to):
        t = CloudmeshDatabase.table(category=cloud, kind="vm")
        name = "vm_" + str(i).zfill(3)
        print ("FFF", t, name)
        vm = t(name=name)

        cm.add(vm)

populate("openstack", 0,10)
populate("libcloud", 10,20)


for name in ["vm_002", "vm_009"]:
    vm = cm.find(category="openstack", kind="vm", name=name, scope='all')
    print ("FOUND:", name, vm)

cm1 = CloudmeshDatabase()
# cm1.start()

# print cm, cm1, cm.session == cm1.session

vm = cm1.find(category="libcloud", kind="vm", name="vm_016")
print("FOUND:", vm)


vm = cm.x_find(kind="vm", scope="first", name="vm_007" )
print("FOUND:", vm)

vm = cm.x_find(kind="vm", scope="all")

print ("FOUND:", vm)