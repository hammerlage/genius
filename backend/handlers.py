#!/usr/bin/env python

"""Genius backend API - Handlers"""

from base_handler import BaseHandler
import models
import json
import csv

class IndexHandler(BaseHandler):
  """Displays the 'home' page."""

  def get(self):
    self.render_json("Hello world")

class ClicksHandler(BaseHandler):

  def options(self):      
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    self.response.headers['Access-Control-Allow-Methods'] = 'POST'

  def post(self):

    for request in json.loads(self.request.body):
      roundChallenge = request.get('roundChallenge')
      currClickAnswer = request.get('currClickAnswer')

      if roundChallenge is not None and len(roundChallenge) >= 1:
        request['totalRoundChallenge'] = len(roundChallenge)
        request['roundChallenge'] = ','.join(roundChallenge)

      if currClickAnswer is not None and len(currClickAnswer) >= 1:
        request['currClickAnswer'] = ','.join(currClickAnswer)

      request['roundSuccess'] = str(request.get('roundSuccess'))
      click = models.Click.create(request)

    response = {'success': False}
    if click is not None:
      response = {'success': True, 'data': click.to_json()}
    self.render_json(response)

class ExportClicksHandler(BaseHandler):

  def get(self):
    self.response.headers['Content-Type'] = 'application/csv'
    writer = csv.writer(self.response.out)
    for click in models.Click.getClicks():
      writer.writerow([click.gameId,
        click.userName,
        click.roundSuccess,
        click.roundChallenge,
        click.currClickAnswer,
        click.roundStartAt,
        click.roundStartTimestamp,
        click.clickTimeAt,
        click.clickTimestamp,
        click.totalRoundChallenge])

class RankingHandler(BaseHandler):

  def get(self):
    response = []
    for c in models.Click.getRanking():
      response.append({'name': c.userName, 'score': c.totalRoundChallenge})
    self.render_json(response)