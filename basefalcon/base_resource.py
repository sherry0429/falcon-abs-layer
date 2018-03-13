# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""

from abc import ABCMeta, abstractmethod
from base_falcon import BaseFalcon


class BaseResource(BaseFalcon):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def on_get(self, req, resp, **kwargs):
        pass

    @abstractmethod
    def on_post(self, req, resp, **kwargs):
        pass


