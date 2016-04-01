""" run with

nosetests -v --nocapture

or

nosetests -v

"""

from cloudmesh_client.util import HEADING

from pprint import pprint


from cloudmesh_client2.db import CloudmeshDatabase
from cloudmesh_client2.common.Printer import Printer
echo = False

cm = CloudmeshDatabase()

class Test_vm:
    def setup(self):
        pass


    def populate(cloud, _from, _to, category):
        global cm
        for i in range(_from, _to):
            t = CloudmeshDatabase.table(provider=cloud, kind="vm")
            name = "vm_" + str(i).zfill(3)
            print ("N", name, t)
            vm = t(name=name, category=category)

            cm.add(vm)

    # noinspection PyPep8Naming
    def tearDown(self):
        pass

    def test_dummy(self):
        HEADING()
        assert True

    def test_000(self):
        # HEADING("Populate")
        global cm
        self.populate("openstack", 0, 10, "kilo")
        self.populate("libcloud", 10, 20, "cloud_b")
        cm.info()

        vms = cm.x_find(kind="vm", scope="all")
        result = Printer.list(
            vms,
            order=['name',
                   'status',
                   'category',
                   'user',
                   'provider',
                   'kind',
                   'xx']
            )
        assert 'vm_001' in result
        assert len(vms) == 20

    def test_001(self):
        global cm
        result = cm.all(provider='openstack', kind='vm')
        assert len(result) == 10

    def test_002(self):
        global cm
        result = cm.all(provider='libcloud', kind='vm')
        assert len(result) == 10

    def test_003(self):
        global cm
        for name in ["vm_002", "vm_009"]:
            vm = cm.find(provider="openstack", kind="vm", name=name)
            pprint(vm)
            assert name in str(vm)

    def test_004(self):
        global cm
        cm1 = CloudmeshDatabase()
        assert cm.session == cm1.session
        assert cm1 != cm

        vm = cm1.find(provider="libcloud", kind="vm", name="vm_016")
        pprint(vm)
        assert "16" in str(vm)

    def test_005(self):
        global cm
        vm = cm.x_find(kind="vm", scope="first", name="vm_007")
        pprint(vm)
        assert "007" in str(vm)

    def test_006(self):
        global cm
        vm = cm.x_find(kind="vm", scope="all")
        pprint(vm)

    def test_007(self):
        global cm
        cm.delete(kind="vm", provider="openstack", name="vm_003")
        cm.delete(kind="vm", provider="openstack", label="vm_004")

        cm.info()

    def test_008(self):
        global cm
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

    def test_009(self):
        global cm
        vm = cm.x_find(kind="vm", scope="first", name="vm_002")
        pprint(vm)
        vm = cm.x_find(kind="vm", scope="first", name="vm_009")
        pprint(vm)

        cm.set("vm_009", 'user', 'gregor', provider='openstack', kind='vm')

        vm = cm.x_find(kind="vm", scope="first", name="vm_009")
        pprint(vm)

        vm = cm.filter_by(name="vm_011")
        pprint(vm)

        vm = cm.filter_by(label="x", scope='all', id=3)
        pprint(vm)

        cm.set("vm_002", 'user', 'world')

        vm = cm.x_find(kind="vm", scope="first", name="vm_002")
        pprint(vm)


        vms = cm.x_find(kind="vm", scope="all")
        print (len(vms))



        print (Printer.list(vms,
                            order=['name', 'status', 'category', 'user', 'provider', 'kind', 'xx']
                            ))

