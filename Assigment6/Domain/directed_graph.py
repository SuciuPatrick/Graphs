class DirectedGraph:
	def __init__(self, numberOfVertices):
		self.__numberOfVertices = numberOfVertices
		self.__out = {}
		self.__in = {}
		self.__cost = {}
		self.__vertices = []
		for i in range(numberOfVertices):
			self.__out[i] = []
			self.__in[i] = []
			self.__vertices.append(i)

	def getVertices(self):
		for vertex in self.__vertices:
			yield vertex

	@property
	def vertices(self):
		return self.__vertices

	@property
	def out(self):
		return self.__out

	@property
	def ini(self):
		return self.__in

	@property
	def numberOfVertices(self):
		return self.__numberOfVertices

	@property
	def cost(self):
		return self.__cost

	def addEdge(self, origin, target, cost):
		self.__out[origin].append(target)
		self.__in[target].append(origin)
		self.__cost[(origin, target)] = cost

	def __str__(self):
		result = "The Graph is:\n"
		for key in self.__cost.keys():
			result += str(key) + "-> " + str(self.__cost[key]) + '\n'
		return result



