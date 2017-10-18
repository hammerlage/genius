#!/usr/bin/env python

import numpy
import pandas as pd
import os,sys
import re


CLICK_TIMESTAMP = 8
TOTAL_ROUND_CHALLENGE = 10

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def chunkRound(rowIn, roundRows):
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

    gameId,userName,roundSuccess,roundChallenge,currClickAnswer,roundStartAt,roundStartTimestamp,clickTimeAt,clickTimestamp,totalRoundChallenge,roundColors,totalRoundColors = rowIn

    for row in roundRows:
        # a.append(float(r[CLICK_TIMESTAMP]))
        
        intervalClick = float(row[CLICK_TIMESTAMP]) - lastTimestamp
        
        ## tuple
        t = row[TOTAL_ROUND_CHALLENGE], indexRound, lastTimestamp, intervalClick, float(row[CLICK_TIMESTAMP])

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

    if (len(transposed) > 1):
        #calc media
        mediaRound = (sumMediaRound / (currentRound-1))

        #calc mediana
        mediaList.sort()
        meio = round(len(mediaList)/2)
        mediana = 0
        if (meio > 2):
            mediana = (mediaList[meio] + mediaList[meio + 1])/2
        else:
            mediana = (mediaList[meio] + mediaList[meio - 1])/2

        #time Round
        timestampRoundList.sort()
        timeRound = (timestampRoundList[len(mediaList) - 1] - timestampRoundList[0])/1000
        
        #cut media or mediana
        mediaCut = (mediana + mediaRound)/2#mediaRound

        #iterate round calculate chunks
        for myTuple in transposed:
            #chunks
            if (float(myTuple[3]) > mediaCut):
                chunksRound += 1

            print("round: {0} clickIndex: {1} timestamp: {2} interval: {3} mediaRound: {4} mediana: {5} mediaCut: {6} timeRound:{7} chunk: {8}".format(myTuple[0], myTuple[1], myTuple[2], myTuple[3], mediaRound, mediana, mediaCut, timeRound, chunksRound))

        print("End round")

        lastTuple = transposed[len(transposed)-1]

        result = [lastTuple[0], timeRound, chunksRound]
        
    return result


"""
df = pd.read_csv('D:/newclicks.csv', names=['gameId', 'userName', 'roundSuccess', 'roundChallenge', 'currClickAnswer', 'roundStartAt', 'roundStartTimestamp', 'clickTimeAt', 'clickTimestamp', 'totalRoundChallenge', 'roundColors' , 'totalRoundColors'])



for index, row in df.iterrows():
    if (lastGameId != row['gameId']):
        #new gameId
        lastGameId = row['gameId']
        lastRound = row['totalRoundChallenge']
        if isfloat(row['clickTimestamp']):
            lastTimestamp = float(row['clickTimestamp'])
    else:
        #continue game
        if (row['totalRoundChallenge'] != lastRound):
            #iterate round
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

            if (len(transposed) > 1):
                #calc media
                mediaRound = (sumMediaRound / (currentRound-1))

                #calc mediana
                mediaList.sort()
                meio = round(len(mediaList)/2)
                mediana = 0
                if (meio > 2):
                    mediana = (mediaList[meio] + mediaList[meio + 1])/2
                else:
                    mediana = (mediaList[meio] + mediaList[meio - 1])/2

                #time Round
                timestampRoundList.sort()
                timeRound = (timestampRoundList[len(mediaList) - 1] - timestampRoundList[0])/1000
                
                #cut media or mediana
                mediaCut = (mediana + mediaRound)/2#mediaRound

                #iterate round calculate chunks
                for myTuple in transposed:
                    #chunks
                    if (float(myTuple[3]) > mediaCut):
                        chunksRound += 1

                    print("round: {0} clickIndex: {1} timestamp: {2} interval: {3} mediaRound: {4} mediana: {5} mediaCut: {6} timeRound:{7} chunk: {8}".format(myTuple[0], myTuple[1], myTuple[2], myTuple[3], mediaRound, mediana, mediaCut, timeRound, chunksRound))

                print("End round")

            transposed = []
            sumMediaRound = 0
            maxRound = 0
            chunksRound = 1
            mediaList = []
            
            #return chunks and info about round


            
            #new round
            lastRound = row['totalRoundChallenge']
            lastTimestamp = float(row['clickTimestamp'])
            indexRound = 1
        else:
            indexRound += 1

            intervalClick = float(row['clickTimestamp']) - lastTimestamp
            
            ## tuple
            t = row['totalRoundChallenge'], indexRound, lastTimestamp, intervalClick, float(row['clickTimestamp'])

            #matrix
            transposed.append(t)

            lastTimestamp = float(row['clickTimestamp'])
        
            
"""            


