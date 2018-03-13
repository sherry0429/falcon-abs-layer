# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""
from basefalcon import BaseService


class ThingsService(BaseService):

    def __init__(self):
        pass

    def get_service_name(self):
        return "things"

    def get_service_url(self):
        return "http://localhost:8080/aaa/things"

    def get_service_data(self):
        return {
            'a':'b'
        }
