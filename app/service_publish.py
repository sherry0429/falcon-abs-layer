# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""

import falcon
from service_delay import AuthMiddleware
from service_delay import ExampleError
from service_delay import ThingsResource
from waitress import create_server


# Configure your WSGI server to load "things.app" (app is a WSGI callable)
app = falcon.API(middleware=[
    AuthMiddleware()
])

things = ThingsResource()
app.add_route('/{args}/things', things)

# If a responder ever raised an instance of StorageError, pass control to
# the given handler.
app.add_error_handler(ExampleError, ExampleError.handle)

if __name__ == '__main__':
    server = create_server(app, host="localhost", port=8080)
    server.run()
