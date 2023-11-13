class Manager:
    def __init__(self, name, weights):
        self.name = name
        self.weights = weights
        self.positions = {
                "F": 0,
                "D": 0
                }
        self.roster = {} 

    def getWeight(self, pos):
        return self.weights[pos]

    def updateWeight(self, pos, newVal):
        self.weights[pos] = newVal

    def displayManager(self):
        print(self.name)
        print(self.weights[0], self.weights[1], self.weights[2], self.weights[3], self.weights[4], self.weights[5], self.weights[6])
        print(self.roster)
        return None

    def getF(self):
       return self.roster["F"]

    def getD(self):
       return self.roster["D"]


    def setF(self):
       self.roster["F"] += 1

    def setD(self):
       self.roster["D"] += 1
