# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""

from abc import ABCMeta, abstractmethod
from base_falcon import BaseFalcon


class BaseMiddleWare(BaseFalcon):

    __metaclass__ =  ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def process_request(self, req, resp):
        pass