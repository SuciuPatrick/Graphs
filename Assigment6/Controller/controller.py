class Controller:
	def __init__(self, repo):
		self.__repo = repo

	@property
	def repo(self):
		return self.__repo

	def checkIsAnEdge(self, pair):
		for i in self.__repo.directedGraph.cost:
			if i == pair:
				return True
		return False


