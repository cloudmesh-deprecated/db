from __future__ import print_function

from cloudmesh_client.common import Printer
from cloudmesh_client2.db import CloudmeshDatabase
# from cloudmesh_client.cloud.ListResource import ListResource
from cloudmesh_client.common.ConfigDict import ConfigDict
from .provider import Attributes
from cloudmesh_client.shell.console import Console
from cloudmesh_client.common.dotdict import dotdict
# noinspection PyBroadException
class Var(object):
    """
    Cloudmesh contains the concept of defaults. Defaults can have
    categories (we will rename cloud to categories). A category can be a
    cloud name or the name 'general'. The category general is a 'global'
    name space and contains defaults of global value (in future we will
    rename the value to global).

    """

    __category__ = "general"
    __kind__ = "var"
    __provider__ = "general"

    cm = CloudmeshDatabase()
    """cm is  a static variable so that db is used uniformly."""

    @classmethod
    def list(cls,
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
        print ("KKKKK")
        if order is None:
            order, header = None, None
            # order, header = Attributes(cls.__kind__, provider=cls.__provider__)
        try:
            print ("search")
            result = cls.cm.all(category=cls.__category__, kind=cls.__kind__)
            print ("ok")
            print ("LLLL", result, cls.__category__, cls.__kind__)

            return (Printer.list_printer(result,
                                         order=order,
                                         output=output))
        except:
            Console.error("?")
            return None

    #
    # GENERAL SETTER AND GETTER METHOD
    #

    @classmethod
    def set(cls, key, value, user=None):
        """
        sets the default value for a given category
        :param key: the dictionary key of the value to store it at.
        :param value: the value
        :param user: the username to store this default value at.
        :return:
        """
        try:
            o = cls.get(name=key)
            if o is not None:
                cls.cm.update(kind=cls.__kind__,
                              category=cls.__category__,
                              filter={'name': key},
                              update={'value': value})

            else:
                t = cls.cm.table(category=cls.__category__, kind=cls.__kind__)
                o = t(name=key, value=value)
                cls.cm.add(o)
            cls.cm.save()
        except Exception as e:
            Console.error("problem setting key value {}={}".format(key, value))

    @classmethod
    def get(cls, name=None, output='dict', scope='first'):
        """
        returns the value of the first objects matching the key
        with the given category.

        :param key: The dictionary key
        :param category: The category
        :return:
        """
        o = cls.cm.find(kind=cls.__kind__,
                        category=cls.__category__,
                        output=output,
                        scope=scope,
                        name=name)
        return o


    @classmethod
    def delete(cls, name):
        cls.cm.delete(name=name, category=cls.__category__, kind=cls.__kind__)


    @classmethod
    def clear(cls):
        """
        deletes all default values in the database.
        :return:
        """
        cls.cm.delete(category=cls.__category__, kind=cls.__kind__)

