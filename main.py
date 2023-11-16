import pandas as pd
import random
from Manager import *

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
            #print(manager.name, " Skipping Player: ", data.iloc[count, 0], data.iloc[count, 1], " too many defensemen") 
            count += 1
            
        else:
            #print(manager.name, " Selecting Player: ", data.iloc[count, 0], data.iloc[count, 1])
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

def mutate(manager):
    randNum = 0
    for x in range(8):
        randNum = random.randint(1, 12)
        if randNum <= 2:
            if randNum % 2 == 0:
                manager.mutateWeight(x, manager.rank/4)
            else:
                manager.mutateWeight(x, manager.rank/4*-1)
                if manager.getWeight(x) < 0:
                    manager.updateWeight(x, 0)

def getRank(man1, man2, man3, man4, man5, man6):
    n = 6
    mans = [man1, man2, man3, man4, man5, man6]
    for i in range(n):
        for j in range(0, n-i-1):
            if mans[j].fitness < mans[j+1].fitness:
                mans[j], mans[j+1] = mans[j+1], mans[j]
    print("Rakings in order:")
    print(mans[0].name, mans[1].name, mans[2].name, mans[3].name, mans[4].name, mans[5].name)
    for x in range(n):
        mans[x].rank = x+1
    for x in range(n-1):
        swapWeights(mans[x], mans[x+1])

def swapWeights(man1, man2):
    for x in range(8):
        randNum = random.randint(1, 24)
        if randNum == 1:
            man2.updateWeight(x, man1.getWeight(x))

def printWeights(manager):
    print(manager.name, " Weights: Goals: ", manager.getWeight(0), " Assists: ", manager.getWeight(1), " Short Handed Goals: ", manager.getWeight(2), " Game Winning Goals: ", manager.getWeight(3), " Power Play Points: ", manager.getWeight(4), "Shots: ", manager.getWeight(5), " Hits: ", manager.getWeight(6), " Blocks: ", manager.getWeight(7))



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

rounds = 0
while(rounds < 500):
    rounds += 1
    print("Round: ", rounds)

    playerDict = {}
    alec.resetMan()
    owen.resetMan()
    charlie.resetMan()
    dave.resetMan()
    evan.resetMan()
    fred.resetMan()


    owenPlayers = sortPlayer(owen, playerStats)
    alecPlayers = sortPlayer(alec, playerStats)
    charliePlayers = sortPlayer(charlie, playerStats)
    davePlayers = sortPlayer(dave, playerStats)
    evanPlayers = sortPlayer(evan, playerStats)
    fredPlayers = sortPlayer(fred, playerStats)

    #print(alecPlayers.head())
    #print(owenPlayers.head())
    #print(charliePlayers.head())
    #print(davePlayers.head())
    #print(evanPlayers.head())
    #print(fredPlayers.head())

#    for x in range(0, 15):
#        selectPlayer(alec, alecPlayers, playerDict, x)
#        selectPlayer(owen, owenPlayers, playerDict, x)
#        selectPlayer(charlie, charliePlayers, playerDict, x)
#        selectPlayer(dave, davePlayers, playerDict, x)
#        selectPlayer(evan, evanPlayers, playerDict, x)
#        selectPlayer(fred, fredPlayers, playerDict, x)
#        #selectPlayer(fred, fredPlayers, playerDict, x)
#        #selectPlayer(evan, evanPlayers, playerDict, x)
#        #selectPlayer(dave, davePlayers, playerDict, x)
#        #selectPlayer(charlie, charliePlayers, playerDict, x)
#        #selectPlayer(owen, owenPlayers, playerDict, x)
#        #selectPlayer(alec, alecPlayers, playerDict, x)
    z = 0
    while(z < 14):
        selectPlayer(alec, alecPlayers, playerDict, z)
        selectPlayer(owen, owenPlayers, playerDict, z)
        selectPlayer(charlie, charliePlayers, playerDict, z)
        selectPlayer(dave, davePlayers, playerDict, z)
        selectPlayer(evan, evanPlayers, playerDict, z)
        selectPlayer(fred, fredPlayers, playerDict, z)
        z = z+1
        selectPlayer(fred, fredPlayers, playerDict, z)
        selectPlayer(evan, evanPlayers, playerDict, z)
        selectPlayer(dave, davePlayers, playerDict, z)
        selectPlayer(charlie, charliePlayers, playerDict, z)
        selectPlayer(owen, owenPlayers, playerDict, z)
        selectPlayer(alec, alecPlayers, playerDict, z)
        z = z+1
    selectPlayer(alec, alecPlayers, playerDict, z)
    selectPlayer(owen, owenPlayers, playerDict, z)
    selectPlayer(charlie, charliePlayers, playerDict, z)
    selectPlayer(dave, davePlayers, playerDict, z)
    selectPlayer(evan, evanPlayers, playerDict, z)
    selectPlayer(fred, fredPlayers, playerDict, z)





    #print(alec.roster, alec.positions)
    #print(owen.roster, owen.positions)
    #print(charlie.roster, charlie.positions)
    #print(dave.roster, dave.positions)
    #print(evan.roster, evan.positions)
    #print(fred.roster, fred.positions)


    #print("player dict: ", playerDict)

    calcFitness(alec, leagueRank, alec.roster)
    calcFitness(owen, leagueRank, owen.roster)
    calcFitness(charlie, leagueRank, charlie.roster)
    calcFitness(dave, leagueRank, dave.roster)
    calcFitness(evan, leagueRank, evan.roster)
    calcFitness(fred, leagueRank, fred.roster)


    print("alec fitness: ", alec.fitness)
    print("owen fitness: ", owen.fitness)
    print("charlie fitness: ", charlie.fitness)
    print("dave fitness: ", dave.fitness)
    print("evan fitness: ", evan.fitness)
    print("fred fitness: ", fred.fitness)

    getRank(alec, owen, charlie, dave, evan, fred)
    mutate(alec)
    mutate(owen)
    mutate(charlie)
    mutate(dave)
    mutate(evan)
    mutate(fred)
    
if alec.rank == 1:
    print("Alec's Roster: ", alec.roster)
    winner = alec
if owen.rank == 1:
    print("Owen's Roster: ", owen.roster)
    winner = owen
if charlie.rank == 1:
    print("Charlie's Roster: ", charlie.roster)
    winner = charlie
if dave.rank == 1:
    print("Dave's Roster: ", dave.roster)
    winner = dave
if evan.rank == 1:
    print("Evan's Roster: ", evan.roster)
    winner = evan
if fred.rank == 1:
    print("Fred's Roster: ", fred.roster)
    winner = fred

printWeights(alec)
printWeights(owen)
printWeights(charlie)
printWeights(dave)
printWeights(evan)
printWeights(fred)
