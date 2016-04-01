from cloudmesh_client2.provider import Attributes

print (Attributes.get("default"))
print (Attributes.get("var"))

print (Attributes.get("flavor", provider='openstack'))
print (Attributes.get("flavor", provider='libcloud'))

