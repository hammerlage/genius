#!/usr/bin/env python

"""Genius backend API - Models"""

from google.appengine.ext import ndb

class JsonResponse(object):
  success = True
  data = None

  def __init__(self, data):
    if data is None:
        self.success = False
    else:
      self.data = data

class Click(ndb.Model):

  session = ndb.StringProperty()
  timestamp = ndb.StringProperty()
  button = ndb.StringProperty()

  @classmethod
  def create(cls, params):
    click = cls(
        session=params.get('session'), 
        timestamp=params.get('timestamp'),
        button=params.get('button'))
    click.put()
    return click

  def to_json(self):
    return "{'session': '%s', 'timestamp': '%s', 'button': '%s'}" % 
        self.session.decode('utf-8'),
        self.timestamp.decode('utf-8'),
        self.button.decode('utf-8')
