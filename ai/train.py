#!/usr/bin/python

import sys
import csv
import repeat as rp
import chunks as ch

GAME_ID = 0
ROUND_CHALLENGE = 3
CLICK_TIMESTAMP = 8

def is_valid(sequence):
    if len(sequence) > 3:
        return True
    return False

def bool_to_int(string):
    if string == 'True':
        return 1
    return 0

def round(row, roundRows):
    result = None

    gameId,userName,roundSuccess,roundChallenge,currClickAnswer,roundStartAt,roundStartTimestamp,clickTimeAt,clickTimestamp,totalRoundChallenge,roundColors,totalRoundColors = row 

    sequence = rp.replace(roundChallenge)

    if is_valid(sequence):

        sequenceNum = len(rp.remove_sequences(sequence))
        sequenceChunk = ch.chunkRound(roundRows)
        if sequenceChunk:
            result = [sequence, sequenceChunk[0], sequenceChunk[1], sequenceChunk[2], bool_to_int(roundSuccess), totalRoundColors, sequenceNum]

    return result

def train(input_csv_file, output_csv_file):

    title = ['sequence', 'totalRoundChallenge', 'gameTime', 'chunks', 'roundSuccess', 'totalRoundColors', 'sequenceNum']

    with open(input_csv_file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(open(output_csv_file, 'w'))
        writer.writerow(title)
        oldRow = None
        roundRows = []
        key = 0
        for row in reader:
            if oldRow and (row[GAME_ID] != oldRow[GAME_ID] or row[ROUND_CHALLENGE] != oldRow[ROUND_CHALLENGE]):
                roundResult = round(oldRow, roundRows)           
                if roundResult:
                    writer.writerow(roundResult)

                roundRows = []
                result = []

            if key != 0:
                roundRows.append(row)
                oldRow = row
            key = key + 1

def main():
    if len(sys.argv) != 3:
        print("Invalid arguments: train.py <input_csv_file> <output_csv_file>")
        exit(1)
    
    train(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()