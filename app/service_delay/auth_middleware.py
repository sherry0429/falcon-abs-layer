# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""
from basefalcon import BaseMiddleWare


class AuthMiddleware(BaseMiddleWare):

    def process_request(self, req, resp):
        resp.data = "auth done\n"
