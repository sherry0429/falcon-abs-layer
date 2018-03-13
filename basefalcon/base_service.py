# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""
from abc import ABCMeta, abstractmethod


class BaseService(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_service_name(self):
        """
        data return by this method will set as this class's key in out of map
        :return:
        """
        return "base_service"

    @abstractmethod
    def get_service_url(self):
        """
        data return by this method will set as http request's url
        :return:
        """
        return "http:/localhost:8080/base_service"

    @abstractmethod
    def get_service_data(self):
        """
        data return by this method will set as http request's post data
        :return:
        """
        return {
            "param_1": "1",
            "param_2": "2"
        }
