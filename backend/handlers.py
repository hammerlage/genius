#!/usr/bin/env python

"""Genius backend API - Handlers"""

from base_handler import BaseHandler

class IndexHandler(BaseHandler):
  """Displays the 'home' page."""

  def get(self):
      self.render_json("Hello world")

class ClicksHandler(BaseHandler):
  """Displays the 'home' page."""

  def post(self):
      self.render_json(self.request)