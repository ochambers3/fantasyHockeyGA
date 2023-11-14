from Manager import *
import pandas as pd

def sortPlayer(manager, playerStats):
    data = playerStats.copy()
    operations = {
            'G': lambda x: x * manager.weights[0],
            'A': lambda x: x * manager.weights[1],
            'SHG': lambda x: x * manager.weights[2],           
            'GWG': lambda x: x * manager.weights[3],
            'PPP': lambda x: x * manager.weights[4],
            'SHOTS': lambda x: x * manager.weights[5],
            'HITS': lambda x: x * manager.weights[6],
            'BS': lambda x: x * manager.weights[7]}
    columns_to_operate_on = ['G', 'A', 'SHG', 'GWG', 'PPP',  'SHOTS', 'HITS', 'BS']

    for column in columns_to_operate_on:
        if column in operations:
            operation = operations[column]
            data[column] = operation(data[column])

    data['fitness'] = data[columns_to_operate_on].sum(axis=1)
    sortedData = data.sort_values(by='fitness', ascending=False)
    return sortedData
   
#column 0 is Name, 1 is Pos. Excel formats that column name weird for some reason.
def selectPlayer(manager, data, playerDict, size): 
    FLAG = True
    forwards = False
    defense = False
    count = size
    if manager.positions['F'] == 9:
        forwards = True
    if manager.positions['D'] == 6:
        defense = True
    while(FLAG):
        if data.iloc[count, 0] in playerDict: 
            #print(manager.name, " Skipping Player: ", data.iloc[count, 0], data.iloc[count, 1], " already selected")
            count += 1
        elif data.iloc[count, 1] == 'F' and forwards == True:
            #print(manager.name, " Skipping Player: ", data.iloc[count, 0], data.iloc[count, 1], " too many forwards")
            count += 1
        elif data.iloc[count, 1] == 'D' and defense == True:
            print(manager.name, " Skipping Player: ", data.iloc[count, 0], data.iloc[count, 1], " too many defensemen") 
            count += 1
            
        else:
            print(manager.name, " Selecting Player: ", data.iloc[count, 0], data.iloc[count, 1])
            if data.iloc[count, 1] == 'F':
                manager.setF()
            else:
                manager.setD()
            #manager.positions[data.iloc[count, 1]] += 1
            #manager.roster[data.iloc[count, 0]] = 1
            manager.setRoster(data.iloc[count, 0])
            playerDict[data.iloc[count, 0]] = 1
            FLAG = False

def calcFitness(manager, leagueRank, roster):
   mask = leagueRank['Name'].isin(roster)
   fitness = leagueRank.loc[mask, 'fitness'].sum()
   manager.setFitness(fitness)

playerDict = {}

#B-Name, E-Pos, G-Goals, H-Assists, S-Game Winning Goals, AA-Power Play Points, AR-Shots, AT-Hits, AU-Blocks
playerStats = pd.read_excel('playerStats1.xlsx', sheet_name=1, usecols="B,E,G,H,R,S,AA,AR,AT,AU", skiprows=1)
print("Players by Points")
print(playerStats.head())
#comish is manager that uses the leagues rankings
comish = Manager("Commishiner", [6, 4, 2, 0.25, 2, 0.9, 1, 0.5])
leagueRank = sortPlayer(comish, playerStats)

alec = Manager("Alec", [0, 0, 0, 0, 0, 0, 0,7])
owen =  Manager("Owen", [6, 4, 0.25, 2, 0.9, 1, 0.5,7])
charlie = Manager("charlie", [6, 4, 0.25, 2, 0.9, 1, 50,70])
dave = Manager("Dave", [15, 40, 3, 8, 2, 18, 6, 13])
evan = Manager("Evan", [6, 4, 0.25, 2, 0.9, 1, 0.5,7])
fred = Manager("Fred", [4, 5, 0.1, 0.5, 2, 3, 0.2,7])
greg = Manager("Greg", [2, 8, 0.9, 4, 1, 2, 6,7])

owenPlayers = sortPlayer(owen, playerStats)
alecPlayers = sortPlayer(alec, playerStats)
charliePlayers = sortPlayer(charlie, playerStats)
davePlayers = sortPlayer(dave, playerStats)
evanPlayers = sortPlayer(evan, playerStats)
fredPlayers = sortPlayer(fred, playerStats)

print(alecPlayers.head())
print(owenPlayers.head())
print(charliePlayers.head())
print(davePlayers.head())
print(evanPlayers.head())
print(fredPlayers.head())


selectPlayer(alec, alecPlayers, playerDict, 0)
selectPlayer(owen, owenPlayers, playerDict, 0)
selectPlayer(charlie, charliePlayers, playerDict, 0)
selectPlayer(dave, davePlayers, playerDict, 0)
selectPlayer(evan, evanPlayers, playerDict, 0)
selectPlayer(fred, fredPlayers, playerDict, 0)
selectPlayer(alec, alecPlayers, playerDict, 1)
selectPlayer(owen, owenPlayers, playerDict, 1)
selectPlayer(charlie, charliePlayers, playerDict, 1)
selectPlayer(dave, davePlayers, playerDict, 1)
selectPlayer(evan, evanPlayers, playerDict, 1)
selectPlayer(fred, fredPlayers, playerDict, 1)
selectPlayer(alec, alecPlayers, playerDict, 2)
selectPlayer(owen, owenPlayers, playerDict, 2)
selectPlayer(charlie, charliePlayers, playerDict, 2)
selectPlayer(dave, davePlayers, playerDict, 2)
selectPlayer(evan, evanPlayers, playerDict, 2)
selectPlayer(fred, fredPlayers, playerDict, 2)
selectPlayer(alec, alecPlayers, playerDict, 3)
selectPlayer(owen, owenPlayers, playerDict, 3)
selectPlayer(charlie, charliePlayers, playerDict, 3)
selectPlayer(dave, davePlayers, playerDict, 3)
selectPlayer(evan, evanPlayers, playerDict, 3)
selectPlayer(fred, fredPlayers, playerDict, 3)
selectPlayer(alec, alecPlayers, playerDict, 4)
selectPlayer(owen, owenPlayers, playerDict, 4)
selectPlayer(charlie, charliePlayers, playerDict, 4)
selectPlayer(dave, davePlayers, playerDict, 4)
selectPlayer(evan, evanPlayers, playerDict, 4)
selectPlayer(fred, fredPlayers, playerDict, 4)
selectPlayer(alec, alecPlayers, playerDict, 5)
selectPlayer(owen, owenPlayers, playerDict, 5)
selectPlayer(charlie, charliePlayers, playerDict, 5)
selectPlayer(dave, davePlayers, playerDict, 5)
selectPlayer(evan, evanPlayers, playerDict, 5)
selectPlayer(fred, fredPlayers, playerDict, 5)



print(alec.roster, alec.positions)
print(owen.roster, owen.positions)
print(charlie.roster, charlie.positions)
print(dave.roster, dave.positions)
print(evan.roster, evan.positions)
print(fred.roster, fred.positions)


print("Player Dict: ", playerDict)

calcFitness(alec, leagueRank, alec.roster)
calcFitness(owen, leagueRank, owen.roster)
calcFitness(charlie, leagueRank, charlie.roster)
calcFitness(dave, leagueRank, dave.roster)
calcFitness(evan, leagueRank, evan.roster)
calcFitness(fred, leagueRank, fred.roster)


print("Alec fitness: ", alec.fitness)
print("Owen fitness: ", owen.fitness)
print("Charlie fitness: ", charlie.fitness)
print("Dave fitness: ", dave.fitness)
print("Evan fitness: ", evan.fitness)
print("Fred fitness: ", fred.fitness)


