#!/usr/bin/python

import sys
import csv
import repeat as rp

def is_valid(sequence):
    if len(sequence) > 2:
        return True
    return False

def bool_to_int(string):
    if string == 'True':
        return 1
    return 0

def train(input_csv_file, output_csv_file):

    title = ['sequence', 'roundSuccess', 'totalRoundChallenge', 'totalRoundColors']

    with open(input_csv_file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(open(output_csv_file, 'w'))
        writer.writerow(title)
        oldRow = None
        for row in reader:
            gameId,userName,roundSuccess,roundChallenge,currClickAnswer,roundStartAt,roundStartTimestamp,clickTimeAt,clickTimestamp,totalRoundChallenge,roundColors,totalRoundColors = row 

            sequence = rp.replace(roundChallenge)

            if is_valid(sequence):

                repetitions = rp.find(sequence, 0)

                result = [sequence, bool_to_int(roundSuccess), totalRoundChallenge, totalRoundColors]
                        
                writer.writerow(result)

            oldRow = row


def main():
    if len(sys.argv) != 3:
        print "Invalid arguments: train.py <input_csv_file> <output_csv_file>"
        exit(1)
    
    train(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()