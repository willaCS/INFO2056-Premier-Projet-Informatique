"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

import Window
from ui.drawMap import drawMap
from ui.drawUI import drawUI
from globals import Screenmode, Speed, all, testing

def drawFrame():
	drawMap()
	# drawUI()
	selectedbuilding = all.font.render(testing.activeBuilding()['name'], True, (255, 0, 0))
	Window.inst.blit(selectedbuilding, (Window.resolution[0] // 8, Window.resolution[0] // 10))
