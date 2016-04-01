'''
Azure via libcloud
=====

Azure Image
-----------

    {'_uuid': None,
     'driver': <libcloud.compute.drivers.azure.AzureNodeDriver object at 0x7f4b69e32cd0>,
     'extra': {'affinity_group': '',
               'category': u'Public',
               'description': u"Linux VM image with coreclr-x64-beta5-11624 installed to /opt/dnx. This image is based on Ubuntu 14.04 LTS, with prerequisites of CoreCLR installed. It also contains PartsUnlimited demo app which runs on the installed coreclr. The demo app is installed to /opt/demo. To run the demo, please type the command '/opt/demo/Kestrel' in a terminal window. The website is listening on port 5004. Please enable or map a endpoint of HTTP port 5004 for your azure VM.",
               'location': u'East Asia;Southeast Asia;Australia East;Australia Southeast;Brazil South;North Europe;West Europe;Japan East;Japan West;Central US;East US;East US 2;North Central US;South Central US;West US',
               'media_link': '',
               'os': u'Linux',
               'vm_image': False},
     'id': '03f55de797f546a1b29d1b8d66be687a__CoreCLR-x64-Beta5-Linux-PartsUnlimited-Demo-App-201504.29',
     'name': u'CoreCLR x64 Beta5 (11624) with PartsUnlimited Demo App on Ubuntu Server 14.04 LTS'}

Azure Size
----------

    {'_uuid': None,
     'bandwidth': None,
     'disk': 127,
     'driver': <libcloud.compute.drivers.azure.AzureNodeDriver object at 0x7f4b69e32cd0>,
     'extra': {
        'cores': 16,
        'max_data_disks': 32},
     'id': 'Standard_D14',
     'name': 'D14 Faster Compute Instance',
     'price': '1.6261',
     'ram': 114688}


'''