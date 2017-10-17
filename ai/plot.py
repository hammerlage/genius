import matplotlib.pyplot as plt
import csv

mGameId = raw_input("ID do jogo: ")

oldRow = None
values = []

with open('clicks.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        gameId,userName,roundSuccess,roundChallenge,currClickAnswer,roundStartAt,roundStartTimestamp,clickTimeAt,clickTimestamp,totalRoundChallenge,roundColors,totalRoundColors = row 
        if gameId == mGameId and roundSuccess == 'True':
            if oldRow:
                old_gameId,old_userName,old_roundSuccess,old_roundChallenge,old_currClickAnswer,old_roundStartAt,old_roundStartTimestamp,old_clickTimeAt,old_clickTimestamp,old_totalRoundChallenge,old_roundColors,old_totalRoundColors = oldRow 
            else:
                old_clickTimestamp = clickTimestamp
            values.append(float(clickTimestamp)-float(old_clickTimestamp))
            oldRow = row

plt.plot(values)
plt.show()