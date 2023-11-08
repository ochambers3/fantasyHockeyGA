from Manager import *

startWeights = [0] * 6

alec = Manager("alec", startWeights)

print(alec.getWeight(2))
alec.updateWeight(2, 5)
print(alec.getWeight(2))
print(alec.displayManager())

