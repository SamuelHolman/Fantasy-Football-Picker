from asyncio.windows_events import NULL
import csv
from inspect import Arguments
from queue import Full
import random
import numpy as np

# FilePath = input("Enter the name of the file")

# FilePath = FilePath + ".csv"
FilePath = "FootballDataWeek2.csv"
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
HighestTeam = [[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
Team = [None] * 9
HallOfFame = []


for i in rows:
    if (i[2] == "QB"):
        print("QuarterBack added")
        QuarterBack.append(i)
    elif (i[2] == "RB"):
        print("RunningBack added")
        RunningBack.append(i)
        Flex.append(i)
    elif (i[2] == "WR"):
        print("WideReceiver added")
        WideReceiver.append(i)
        Flex.append(i)
    elif (i[2] == "TE"):
        print("TightEnd added")
        TightEnd.append(i)
        Flex.append(i)
    elif (i[2] == "DEF"):
        print("DefensiveTeam added")
        DefensiveTeam.append(i)

def AddSalary(array):
    TotalSalary = 0
    for Player in array:
        TotalSalary += int(Player[3])
    return TotalSalary

def AddPoints(array):
    TotalPoints = 0
    for Player in array:
        TotalPoints += float(Player[4])
    return TotalPoints

def GenerateTeam():
    Team[0] = random.choice(QuarterBack)
    Team[1] = random.choice(RunningBack)
    Team[2] = random.choice(RunningBack)

    while (Team[1] == Team[2]):
        Team[2] = random.choice(RunningBack)

    Team[3] = random.choice(WideReceiver)
    Team[4] = random.choice(WideReceiver)
    Team[5] = random.choice(WideReceiver)

    while ((Team[3] == Team[4]) or (Team[3] == Team[5]) or (Team[4] == Team[5])):
        Team[3] = random.choice(WideReceiver)
        Team[4] = random.choice(WideReceiver)
        Team[5] = random.choice(WideReceiver)

    Team[6] = random.choice(TightEnd)

    FlexPick = random.choice(Flex)
    while (FlexPick in Team):
        FlexPick = random.choice(Flex)
    Team[7] = FlexPick
    Team[8] = random.choice(DefensiveTeam)

# z = int(input("Enter the amount of times you want to run the simulation"))
z = 1000000
GenerateTeam()

while(float(AddPoints(HighestTeam)) < 176):
    GenerateTeam()
    if ((float(AddPoints(Team)) > float(AddPoints(HighestTeam))) and int(AddSalary(Team)) <= 200):
        HighestTeam = Team
        del(Team)
        Team = [None] * 9
        for Player in HighestTeam:
            HallOfFame.append(Player[7])
        print("------------------------------")
        print(HighestTeam)
        print(" ")
        print("Found a better team at Team Salary: " + str(AddSalary(HighestTeam)) + ", Average Points: " + str(round((AddPoints(HighestTeam) / 9), 2)) + ", Total Points: " + str(round(AddPoints(HighestTeam), 2)))
    z -= 1

print(" ")
print(" ")
print(" ")
unique, counts = np.unique(HallOfFame, return_counts=True)
result = np.column_stack((unique, counts)) 
print(result)
print(" ")
print(" ")
print("Team Salary: " + str(AddSalary(HighestTeam)) + ", Average Points: " + str(round((AddPoints(HighestTeam) / 9), 2)) + ", Total Points: " + str(round(AddPoints(HighestTeam), 2)))
print(HighestTeam)