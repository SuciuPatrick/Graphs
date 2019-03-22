from Domain.directed_graph import DirectedGraph
from Controller.controller import Controller
from Repository.repository import Repository

class UI:
	def __init__(self, controller):
		self.__controller = controller

	def menu(self):
		print("\n0. Exit.")
		print("1. Display the number of vertices.")
		print("2. Iterate the set of vertices. ")
		print("3. Check if an edge exists.")
		print("4. Get the in degree and the out degree of a specified vertex.")
		print("5. Display the inbound vertices for a given vertex.")
		print("6. Display the outbound vertices for a given vertex.")
		print("7. Display the cost of an edge.")
		print("8. Modify the cost of an edge.")
		print("9. Add vertex.")
		print("10. Remove vertex.")
		print("11. Add edge.")
		print("12. Remove edge.")
		print("13. Copy graph.")
		print("14. Print graph.")

	def command_1(self):
		print ("The number of vertices is: " + str(self.__controller.repo.directedGraph.numberOfVertices))

	def command_2(self):
		self.__controller.repo.directedGraph.getVertices()
		print(self.__controller.repo.directedGraph.vertices)

	def command_3(self):
		origin = int(input("insert origin-> "))
		target = int(input("insert target-> "))
		pair = (origin, target)

		if self.__controller.checkIsAnEdge(pair) is True:
			print(str(pair) + " is an edge. ")

	def command_4(self):
		vertex = int(input("insert vertex-> "))
		print("in degree is: " + str(len(self.__controller.repo.directedGraph.ini[vertex])) + " out degree is: " + str(len(self.__controller.repo.directedGraph.out[vertex])))

	def command_5(self):
		pass

	def command_6(self):
		pass

	def command_7(self):
		pass

	def command_8(self):
		pass

	def command_9(self):
		pass

	def command_10(self):
		pass

	def command_11(self):
		pass

	def command_12(self):
		pass

	def command_13(self):
		pass

	def command_14(self):
		print(str(self.__controller.repo.directedGraph))

	def startapp(self):
		while True:
			commands = {"1": self.command_1, "2": self.command_2, "3": self.command_3,  "4": self.command_4, "5": self.command_5, "6": self.command_6, "7": self.command_7, "8": self.command_8, "9": self.command_9, "10": self.command_10, "11": self.command_11, "12": self.command_12, "13": self.command_13, "14": self.command_14}
			value = input("insert a command from the list-> ")
			if value in commands:
				commands[value]()
			elif value == "0":
				break
			else:
				print("Invalid command.")