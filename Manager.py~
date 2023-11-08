class Manager:
	def __init__(self, name, weights):
		self.name = name
		self.weights = weights

	def getWeight(self, pos):
		return self.weights[pos]

	def updateWeight(self, pos, newVal):
		self.weights[pos] = newVal

	def displayManager(self):
		print(self.name)
		for i in range(0, len(self.weights)):
			print("Weight ", i, ": ", self.getWeight(i))
		return 10
