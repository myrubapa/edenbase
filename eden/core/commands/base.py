"""
    {{ docs }}
"""
__author__ = "Bekhzod Tillakhanov"
__copyright__ = "Copyright 2015, The Eden Project"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "bekhzod.tillakhanov@gmail.com"
__status__ = "Development"

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class CommandBase(object):
    @property
    @abc.abstractmethod
    def helper(self):
        pass

    @abc.abstractmethod
    def handler(self, *args, **kwargs):
        pass
