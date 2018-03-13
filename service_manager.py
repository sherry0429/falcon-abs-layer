# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""
import requests
import json


class ServiceManager(object):

    def __init__(self):
        self.service_map = dict()
        from service_map import __dep__
        for (k, v) in __dep__.items():
            self.service_map[k] = v()

    def call(self, service_name):
        url = self.service_map[service_name].get_service_url()
        data = self.service_map[service_name].get_service_data()
        request = requests.post(url, json.dumps(data))
        response = request.content
        return response
        print "request %s, data %s\nresponse data %s\n" % (url, data, response)
