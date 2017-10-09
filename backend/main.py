#!/usr/bin/env python
"""Genius backend API"""

# [START imports]
from handlers import *
import webapp2
# [END imports]

application = webapp2.WSGIApplication(
    [('/', IndexHandler),
     ('/api/clicks', ClicksHandler)
    ],
    debug=False)