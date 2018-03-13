# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""

from abc import ABCMeta, abstractmethod
from base_falcon import BaseFalcon


class BaseError(BaseFalcon):

    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, ex, req, resp, params):
        pass
