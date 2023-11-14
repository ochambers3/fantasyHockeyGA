class Manager:
    def __init__(self, name, weights):
        self.name = name
        self.weights = weights
        self.positions = {
                'F': 0,
                'D': 0
                }
        self.roster = {} 
        self.fitness = 0

    def getWeight(self, pos):
        return self.weights[pos]

    def updateWeight(self, pos, newVal):
        self.weights[pos] = newVal

    def setRoster(self, name):
        self.roster[name] = 1

    def displayManager(self):
        print(self.name)
        print(self.weights[0], self.weights[1], self.weights[2], self.weights[3], self.weights[4], self.weights[5], self.weights[6])
        print(self.roster)
        print(self.positions)
        return None

    def getF(self):
       return self.positions['F']

    def getD(self):
       return self.positions['D']

    def setFitness(self, num):
       self.fitness = num

    def setF(self):
       self.positions['F'] += 1

    def setD(self):
       self.positions['D'] += 1
