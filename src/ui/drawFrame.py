"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

import Window
from ui.drawMap import drawMap
from globals import all, testing
# from ui.drawUI import drawUI

def drawFrame():
	drawMap()
	# drawUI()
	selectedbuilding = all.font.render(testing.activeBuilding()['name'], True, (255, 0, 0)) # type: ignore
	Window.inst.blit(selectedbuilding, (Window.resolution[0] // 8, Window.resolution[0] // 10))
