from Repository.repository import Repository
from Controller.controller import Controller
from UI.ui import UI

while True:
	commands = ["1k.txt", "10k.txt", "100k.txt", "example.txt"]
	fileName = input("Insert filename: ")
	if fileName in commands:
		break

repo = Repository(fileName)
repo.readFromFile()
controller = Controller(repo)
new_ui = UI(controller)

new_ui.menu()
new_ui.startapp()