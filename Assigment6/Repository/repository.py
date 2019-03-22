from Domain.directed_graph import DirectedGraph


class Repository:
	def __init__(self, fileName):
		self.__directedGraph = None
		self.__fileName = fileName

	def readFromFile(self):
		fd = open(self.__fileName, "r")

		line = fd.readline() #the line with the nr of vertices and edges
		parts = line.split()
		vertices = int(parts[0])
		edges = int(parts[1])
		self.__directedGraph = DirectedGraph(vertices)
		for i in range(edges):
			line = fd.readline()
			line.strip()
			parts = line.split()
			self.__directedGraph.addEdge(int(parts[0]), int(parts[1]), int(parts[2]))

	@property
	def directedGraph(self):
		return self.__directedGraph