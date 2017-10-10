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
        session=params.get('session'), 
        timestamp=params.get('timestamp'),
        button=params.get('button'))
    click.put()
    return click

  def to_json(self):
    return {'session': self.session.decode('utf-8'), 
      'timestamp': self.timestamp.decode('utf-8'), 'button': self.button.decode('utf-8')}
