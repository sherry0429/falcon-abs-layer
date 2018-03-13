# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""
from base_falcon import BaseFalcon
import requests
from abc import ABCMeta, abstractmethod
import json


class BaseSinkAdapter(BaseFalcon):
    """
    think this:
        I want to get 3 results, but i only want to request 1 urls from client.
    Sink Adapter can help us, translate 1 url -> 3 url by engines (dict), and
    request them, get result and return.
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    engines = {
        'key': 'url'
    }

    @abstractmethod
    def __call__(self, req, resp, **kwargs):
        pass
