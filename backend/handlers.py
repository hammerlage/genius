#!/usr/bin/env python

"""Genius backend API - Handlers"""

from base_handler import BaseHandler
import models

class IndexHandler(BaseHandler):
  """Displays the 'home' page."""

  def get(self):
    self.render_json("Hello world")

class ClicksHandler(BaseHandler):
  """Displays the 'home' page."""

  def post(self):
    click = models.Click.create(self.request)
    response = {'success': False}
    if click is not None:
      response = {'success': True, 'data': click.to_json()}
    self.render_json(response)