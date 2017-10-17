import csv

oldGameId = None

title = ['gameId', 'totalRoundChallenge', 'totalRoundColors']

with open('clicks.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(open('clicks_train.csv', 'w'))
    writer.writerow(title)
    for row in reader:
        gameId,userName,roundSuccess,roundChallenge,currClickAnswer,roundStartAt,roundStartTimestamp,clickTimeAt,clickTimestamp,totalRoundChallenge,roundColors,totalRoundColors = row 

        result = [gameId, totalRoundChallenge, totalRoundColors]
        
        if oldGameId and oldGameId != gameId:
            writer.writerow(result)

        oldGameId = gameId