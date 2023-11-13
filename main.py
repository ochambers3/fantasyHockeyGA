from Manager import *
import pandas as pd

def draftPlayers(manager, playerStats, playerDict):
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
    print(data.head())

    data['fitness'] = data[columns_to_operate_on].sum(axis=1)
    player = data['fitness'].idxmax()
    print("Player selected: ", data.iloc[player, 0], " ranked: ", player+1)
    

playerDict = {}

#B-Name, E-Pos, G-Goals, H-Assists, S-Game Winning Goals, AA-Power Play Points, AR-Shots, AT-Hits, AU-Blocks
playerStats = pd.read_excel('playerStats.xlsx', sheet_name=1, usecols="B,E,G,H,R,S,AA,AR,AT,AU", skiprows=1)
print(playerStats.head())


alec = Manager("alec", [0, 1, 2, 3, 4, 5, 6,7])
owen =  Manager("owen", [6, 4, 0.25, 2, 0.9, 1, 0.5,7])
charlie = Manager("charlie", [6, 4, 0.25, 2, 0.9, 1, 0.5,7])
dave = Manager("Dave", [6, 4, 0.25, 2, 0.9, 1, 0.5,7])
evan = Manager("Evan", [6, 4, 0.25, 2, 0.9, 1, 0.5,7])
fred = Manager("Fred", [4, 5, 0.1, 0.5, 2, 3, 0.2,7])
greg = Manager("Greg", [2, 8, 0.9, 4, 1, 2, 6,7])

draftPlayers(owen, playerStats, playerDict)
print(playerStats.head())
