"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

from ui.drawMap import drawMap
from ui.drawUI import drawUI

def drawFrame():
	drawMap()
	drawUI()
