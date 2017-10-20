#!/usr/bin/python

import sys
import csv
import repeat as rp
import chunks as ch

GAME_ID = 0
ROUND_SUCCESS = 2
ROUND_CHALLENGE = 3
CLICK_TIMESTAMP = 8
TOTAL_ROUND_CHALLENGE = 9

def is_valid(sequence):
    if len(sequence) > 3:
        return True
    return False

def bool_to_int(string):
    if string == 'True':
        return 1
    return 0

def round(row, roundRows, totalRoundVictory):
    result = None

    gameId,userName,roundSuccess,roundChallenge,currClickAnswer,roundStartAt,roundStartTimestamp,clickTimeAt,clickTimestamp,totalRoundChallenge,roundColors,totalRoundColors = row 

    sequence = rp.replace(roundChallenge)

    if is_valid(sequence):

        sequenceNum = len(rp.remove_sequences(sequence))
        sequenceChunk = ch.chunkRound(roundRows)
        if sequenceChunk:
            result = [sequence, totalRoundVictory, sequenceChunk[0], sequenceChunk[1], sequenceChunk[2], bool_to_int(roundSuccess), totalRoundColors, sequenceNum]

    return result

def print_round(writer, oldRow, roundRows, total, key):
    roundResult = round(oldRow, roundRows, total[oldRow[GAME_ID]])           
    if roundResult:
        roundResult.insert(0, key)
        writer.writerow(roundResult)

def train(input_csv_file, output_csv_file):

    title = ['id', 'sequence', 'totalRoundVictory', 'totalRoundChallenge', 'gameTime', 'chunks', 'roundSuccess', 'totalRoundColors', 'sequenceNum']

    with open(input_csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        oldRow = None
        lastSuccess = None
        total = {}
        key = 0
        for row in reader:
            if oldRow and row[GAME_ID] != oldRow[GAME_ID]:
                if lastSuccess:
                    total[lastSuccess[GAME_ID]] = lastSuccess[TOTAL_ROUND_CHALLENGE]
                else:
                    total[oldRow[GAME_ID]] = 0
                lastSuccess = None
            if bool_to_int(row[ROUND_SUCCESS]):
                lastSuccess = row
            if key > 0:
                oldRow = row
            key = key + 1
        
        if lastSuccess:
            total[lastSuccess[GAME_ID]] = lastSuccess[TOTAL_ROUND_CHALLENGE]
        else:
            total[oldRow[GAME_ID]] = 0

    with open(input_csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(open(output_csv_file, 'w'), delimiter=',', lineterminator='\n')
        writer.writerow(title)
        oldRow = None
        roundRows = []
        key = 0
        for row in reader:
            if oldRow and (row[GAME_ID] != oldRow[GAME_ID] or row[ROUND_CHALLENGE] != oldRow[ROUND_CHALLENGE]):
                print_round(writer, oldRow, roundRows, total, key)

                roundRows = []
                result = []

            if key != 0:
                roundRows.append(row)
                oldRow = row
            key = key + 1
        
        #print last line
        print_round(writer, oldRow, roundRows, total, key)

def main():
    if len(sys.argv) != 3:
        print("Invalid arguments: train.py <input_csv_file> <output_csv_file>")
        exit(1)
    
    train(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()