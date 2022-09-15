from asyncio.windows_events import NULL
import csv

# FilePath = input("Enter the name of the file")

# FilePath = FilePath + ".csv"
FilePath = "FootballDataWeek1.csv"
Budget = 200

file = open(FilePath)

csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

file.close()

QuarterBack = []
RunningBack = []
WideReceiver = []
TightEnd = []
DefensiveTeam = []
Flex = []
Team = []
PreviousTeam = []
AvailableTeams = []

for i in rows:
    if (i[2] == "QB"):
        print("QuarterBack added")
        QuarterBack.append(i)
    elif (i[2] == "RB"):
        print("RunningBack added")
        RunningBack.append(i)
    elif (i[2] == "WR"):
        print("WideReceiver added")
        WideReceiver.append(i)
    elif (i[2] == "TE"):
        print("TightEnd added")
        TightEnd.append(i)
    elif (i[2] == "RB" or i[2] == "WR" or i[2] == "TE"):
        print("Flex added")
        Flex.append(i)
    elif (i[2] == "DEF"):
        print("DefensiveTeam added")
        DefensiveTeam.append(i)

i = 0
for a in QuarterBack:
    for b in RunningBack:
        for c in RunningBack:
            for d in WideReceiver:
                for e in WideReceiver:
                    for f in WideReceiver:
                        for g in TightEnd:
                            for h in Flex:
                                for i in DefensiveTeam:
                                    i += 1

print(i)

print("Done!")

def AddSalary(array):
    TotalSalary = 0
    for Player in array:
        TotalSalary += Player[3]
    return TotalSalary


def AddPoints(array):
    TotalPoints = 0
    for Player in array:
        TotalPoints += Player[4]
    return TotalPoints
