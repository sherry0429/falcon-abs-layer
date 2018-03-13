# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""
from basefalcon import BaseResource
import requests


class ThingsResource(BaseResource):

    def __init__(self):
        super(ThingsResource, self).__init__()

    def on_get(self, req, resp, **kwargs):
        resp.data += "things resource attached %s\n" % str(kwargs)
        resp.status = self.OK

    def on_post(self, req, resp, **kwargs):
        # print req.data
        # 异步任务
        # 异步任务结果返回
        resp.data += "i know your data %s\n" % str(req.media)
        resp.status = self.OK

