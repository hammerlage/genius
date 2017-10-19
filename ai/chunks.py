#!/usr/bin/env python
import os,sys
import re


CLICK_TIMESTAMP = 8
TOTAL_ROUND_CHALLENGE = 9

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def chunkRound(roundRows):
    lastRound = 0
    lastTimestamp = 0
    indexRound = 0
    transposed = []
    mediaList = []
    timestampRoundList = []
    sumMediaRound = 0
    mediaRound = 0
    mediaCut = 0
    maxRound = 0
    currentRound = 0
    chunksRound = 0
    clickTimestamp = 8
    totalRoundChallenge = 10

    result = None

    for row in roundRows:
        intervalClick = float(row[CLICK_TIMESTAMP]) - lastTimestamp
        
        ## tuple
        t = row[TOTAL_ROUND_CHALLENGE], indexRound, lastTimestamp, intervalClick, float(row[CLICK_TIMESTAMP]), row[0]

        #matrix
        transposed.append(t)

        lastTimestamp = float(row[CLICK_TIMESTAMP])

    for myTuple in transposed:
        #sum media
        sumMediaRound += float(myTuple[3])

        #media list
        mediaList.append(float(myTuple[3]))

        #timestamp list
        timestampRoundList.append(float(myTuple[4]))
        
        #math max
        if(maxRound < float(myTuple[3])):
            maxRound = float(myTuple[3])

        #current round
        currentRound = int(myTuple[0])

    if (len(transposed) > 1) and currentRound == len(transposed):
        #calc media
        #mediaRound = (sumMediaRound / (currentRound-1))

        #calc mediana
        mediaList.sort()
        meio = int(round(len(mediaList)/2))
        mediana = 0
        if (meio > 2):
            mediana = (mediaList[meio] + mediaList[meio + 1])/2
        else:
            mediana = (mediaList[meio] + mediaList[meio - 1])/2

        #time Round
        timestampRoundList.sort()
        timeRound = (timestampRoundList[len(mediaList) - 1] - timestampRoundList[0])/1000
        
        #cut media or mediana
        mediaCut = mediana#mediaRound

        #iterate round calculate chunks
        for myTuple in transposed:
            #chunks
            if (float(myTuple[3]) > mediaCut):
                chunksRound += 1

        lastTuple = transposed[len(transposed)-1]

        result = [lastTuple[0], timeRound, chunksRound]

    transposed = []
    sumMediaRound = 0
    maxRound = 0
    chunksRound = 1
    mediaList = []
        
    return result
