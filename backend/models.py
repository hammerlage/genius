#!/usr/bin/env python

"""Genius backend API - Models"""

from google.appengine.ext import ndb

class Click(ndb.Model):

  gameId = ndb.StringProperty(default="-")
  userName = ndb.StringProperty(default="-")
  roundSuccess = ndb.StringProperty(default="-")
  roundChallenge = ndb.TextProperty(default="-")
  currClickAnswer = ndb.TextProperty(default="-")
  roundStartAt = ndb.StringProperty(default="-")
  roundStartTimestamp = ndb.StringProperty(default="-")
  clickTimeAt = ndb.StringProperty(default="-")
  clickTimestamp = ndb.StringProperty(default="-")
  totalRoundChallenge = ndb.IntegerProperty(default="-")

  @classmethod
  def create(cls, params):
    click = cls(
        gameId=params.get('gameId'), 
        userName=params.get('userName'),
        roundSuccess=params.get('roundSuccess'),
        roundChallenge=params.get('roundChallenge'),
        currClickAnswer=params.get('currClickAnswer'),
        roundStartAt=params.get('roundStartAt'),
        roundStartTimestamp=params.get('roundStartTimestamp'),
        clickTimeAt=params.get('clickTimeAt'),
        clickTimestamp=params.get('clickTimestamp'),
        totalRoundChallenge=params.get('totalRoundChallenge'))
    click.put()
    return click

  @classmethod
  def getClicks(cls):
    return cls.query().fetch()

  @classmethod
  def getRanking(cls):
    return cls.query(ndb.AND(Click.userName <> None, Click.roundSuccess == 'True')).order(Click.userName, -Click.totalRoundChallenge).fetch(3)

  def to_json(self):
    return {'gameId': self.gameId.decode('utf-8')}
