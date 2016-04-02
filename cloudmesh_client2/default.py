from __future__ import print_function

from cloudmesh_client.common import Printer
# from cloudmesh_client.db.SSHKeyDBManager import SSHKeyDBManager
import cloudmesh_client
from cloudmesh_client.cloud.ListResource import ListResource
from cloudmesh_client.common.ConfigDict import ConfigDict

# from cloudmesh_client.cloud.iaas.CloudProvider import CloudProvider
from cloudmesh_client.db import CloudmeshDatabase
from cloudmesh_client.shell.console import Console
from cloudmesh_client.common.dotdict import dotdict

# noinspection PyBroadException
class Default(ListResource):
    """
    Cloudmesh contains the concept of defaults. Defaults can have
    categories (we will rename cloud to categories). A category can be a
    cloud name or the name 'general'. The category general is a 'global'
    name space and contains defaults of global value (in future we will
    rename the value to global).

    """

    __kind__ = "default"
    __provider__ = "general"

    cm = CloudmeshDatabase()


    @classmethod
    def list(cls,
             category=None,
             order=None,
             header=None,
             output='table'):
        """
        lists the default values in the specified format.
        TODO: This method has a bug as it uses format and output,
        only one should be used.

        :param category: the category of the default value. If general is used
                      it is a special category that is used for global values.
        :param format: json, table, yaml, dict, csv
        :param order: The order in which the attributes are returned
        :param output: The output format.
        :return:
        """
        if order is None:
            order, header = None, None
            order = ['user',
                     'category',
                     'name',
                     'value',
                     'updated_at']
            # order, header = Attributes(cls.__kind__, provider=cls.__provider__)
        try:
            if category is None:
                result = cls.cm.all(cls.__kind__)
            else:
                result = cls.cm.all(category=category, kind=cls.__kind__)

            return (Printer.write(result,
                                  order=order,
                                  output=output))
        except:
            Console.error("Error creating list")
            return None



    #
    # GENERAL SETTER AND GETTER METHOD
    #
    '''
    @classmethod
    def set(cls, key, value, category=None, user=None):
        """
        sets the default value for a given category
        :param key: the dictionary key of the value to store it at.
        :param value: the value
        :param category: the name of the category
        :param user: the username to store this default value at.
        :return:
        """

        try:

            o = cls.get_object(key, category)
            me = cls.cm.user or user
            if o is None:
                o = cls.cm.db_obj_dict(cls.__kind__,
                                       name=key,
                                       value=value,
                                       category=category,
                                       user=me)
                cls.cm.add_obj(o)
            else:
                o.value = value
                cls.cm.add(o)
                # cls.cm.update(o)
            cls.cm.save()
        except:
            return None

    @classmethod
    def get_object(cls, key, category="general"):
        """
        returns the first object that matches the key in teh Default
        database.

        :param key: The dictionary key
        :param category: The category
        :return:
        """

        try:
            o = cls.cm.find(category=category,
                            kind=cls.__kind__,
                            output='object',
                            name=key,
                            scope='first')
            return o
        except Exception:
            return None

    @classmethod
    def get(cls, key, category="general"):
        """
        returns the value of the first objects matching the key
        with the given category.

        :param key: The dictionary key
        :param category: The category
        :return:
        """

        o = cls.cm.find(category=category,
                        kind=cls.__kind__,
                        output='dict',
                        scope='first',
                        name=key)
        if o is not None:
            return o['value']
        else:
            return None

    @classmethod
    def delete(cls, key, category):
        #
        # TODO: this is wrong implemented,
        #
        try:
            o = Default.get_object(key, category)
            if o is not None:
                cls.cm.delete(o)
                return "Deletion. ok."
            else:
                return None
        except:
            return None

    @classmethod
    def clear(cls):
        """
        deletes all default values in the database.
        :return:
        """
        try:
            d = cls.cm.all(cls.__kind__)
            for item in d:
                name = d[item]["name"]
                cls.cm.delete_by_name(cls.__kind__, name)
            cls.cm.save()
        except:
            return None

    #
    # Set the default category
    #
    @classmethod
    def get_cloud(cls):
        """
        returns the cloud in teh category general
        :return:
        """
        o = cls.get("cloud", category="general")
        return o

    @classmethod
    def set_cloud(cls, value):
        """
        sets the cloud in the category general
        :param value: the cloud as defined in cloudmesh.yaml
        :return:
        """
        cls.set("cloud", value, category="general")

    #
    # Set the default last_vm_name
    #
    @classmethod
    def get_last_vm_name(cls):
        """
        returns the last_vm_name in teh category general
        :return:
        """
        o = cls.get("last_vm_name", category="general")
        return o

    @classmethod
    def set_last_vm_name(cls, value):
        """
        sets the cloud in the category general
        :param value: the cloud as defined in cloudmesh.yaml
        :return:
        """
        cls.set("last_vm_name", value, category="general")

    #
    # Set the default image
    #

    @classmethod
    def set_image(cls, value, category):
        """
        sets the default image for a specific category.
        :param value: the image uuid or name
        :param category: the category
        :return:
        """
        cls.set("image", value, category=category)

    @classmethod
    def get_image(cls, category=None):
        """
        returns the image for a particular category
        :param category: the category
        :return:
        """
        if category is None:
            category = cls.get_cloud()
        return cls.get("image", category)

    #
    # Set the default flavor
    #

    @classmethod
    def set_flavor(cls, value, category):
        """
        sets the default flavor for a particular category
        :param value: teh flavor name or uuid
        :param category: the category
        :return:
        """
        cls.set("flavor", value, category=category)

    @classmethod
    def get_flavor(cls, category=None):
        """
        gets ths flavor default for a category
        :param category: the category
        :return:
        """
        if category is None:
            category = cls.get_cloud()
        return cls.get("flavor", category)

    #
    # Set the default group
    #

    @classmethod
    def set_group(cls, value):
        """
        sets the default group
        :param value: the group name
        :return:
        """
        cls.set("group", value, category="general")

    @classmethod
    def get_group(cls):
        """
        get the default group
        :return:
        """
        try:
            group = cls.get("group", "general")
            if group is None:
                return "default"
            else:
                return group
        except:
            return "default"

    #
    # Set the default key
    #

    @classmethod
    def set_key(cls, name):
        """
        :param name: the key name
        :return:
        """
        cls.set("key", name, category="general")

    @classmethod
    def get_key(cls):
        """
        get the default key name
        :return:
        """
        return cls.get("key", "general")

    #
    # Set the default cluster
    #

    @classmethod
    def set_cluster(cls, value):
        """
        sets the default cluster
        :param value: the cluster name as defined in the cloudmesh yaml file.
        :return:
        """
        cls.set("cluster", value, category="general")

    @classmethod
    def get_cluster(cls):
        """
        gets the default cluster name.

        :return:
        """
        return cls.get("cluster", "general")

    #
    # Set the default key
    #

    @classmethod
    def set_debug(cls, value):
        """
        enables debugging
        :param value: True/False
        :return:
        """
        cls.set("debug", value, category="general")

    @classmethod
    def get_debug(cls):
        """
        is debugging switched on?
        :return:
        """
        return cls.get("debug", "general")

    @classmethod
    def debug(cls):
        """
        :return: returns True if debugging is on
        """
        return cls.get("debug", "general")

    #
    # Set the default for refresh
    #

    @classmethod
    def set_refresh(cls, value):
        """
        sets the default for all clouds to refresh
        :param value:
        :return:
        """
        cls.set("refresh", value, "general")

    @classmethod
    def get_refresh(cls):
        """
        is refresh switched on?
        :return:
        """
        return cls.get("refresh", "general")

    @classmethod
    def refresh(cls):
        """
        :return: "on" if refresh is True, "off" otherwise
        """
        try:
            value = cls.get_refresh()
        except:
            cls.set_refresh("on")
            value = "on"
        return value == "on"

    # set default for timer

    @classmethod
    def set_timer(cls, value):
        """
        sets the default for all clouds to timer
        :param value:
        :return:
        """
        cls.set("timer", value, "general")

    @classmethod
    def get_timer(cls):
        """
        gets the timer
        :return: "on" if timer is True, "off" otherwise
        """
        try:
            value = cls.get("timer", "general")
        except:
            cls.set_timer("off")
            value = "off"
        return value

    @classmethod
    def timer(cls):
        """
        :return: "on" if timer is True, "off" otherwise
        """
        value = cls.get_timer()
        return value == "on"

    @classmethod
    def load(cls, filename):

        config = ConfigDict(filename=filename)["cloudmesh"]
        clouds = config["clouds"]

        # FINDING DEFAULTS FOR CLOUDS

        for cloud in clouds:

            db = {
                "image": cls.get("image", cloud),
                "flavor": cls.get("flavor", cloud),
            }
            defaults = clouds[cloud]["default"]
            for attribute in ["image", "flavor"]:
                value = db[attribute]
                if attribute in defaults:
                    value = db[attribute] or defaults[attribute]
                Default.set(attribute, value, category=cloud)

        # FINDING DEFAUlTS FOR KEYS
        # keys:
        #     default: id_rsa
        #     keylist:
        #       id_rsa: ~/.ssh/id_rsa.pub

        # key_db = SSHKeyDBManager()

        name_key = cls.get("key")

        keys = config["keys"]
        name = keys["default"]
        if name in keys["keylist"]:
            value = name_key or keys["keylist"][name]
            # key_db.add(value, keyname=name)

        # Check if the key is already set
        exist_key = cls.get_key()

        # Set the key only if there is no existing value in the DB.
        if exist_key is None:
            Default.set_key(name)
    '''