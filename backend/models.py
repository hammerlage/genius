#!/usr/bin/env python

"""Genius backend API - Models"""

from google.appengine.ext import ndb

class Click(ndb.Model):

  session = ndb.StringProperty()
  timestamp = ndb.StringProperty()
  button = ndb.StringProperty()

  @classmethod
  def create(cls, params):
    click = cls(
        session=params['session'], 
        timestamp=params['timestamp'],
        button=params['button'])
    click.put()
    return click