"""
Ce fichier est le fichier principal.
Il comporte la fonction main qui va appelé la window et contient aussi les
fonction tick executé tout les ticks et la fonction setup executé lorsque
pygame est prêt.
"""

import Window
from globals import all
from events import handleEvents
from input import repeatKey, singleKey
from ui.drawFrame import drawFrame
from ui.drawUI import getFont

def setup():
	all.font = getFont()



def tick():
	# __calculate()
	drawFrame()



def	main():
	Window.init(setup, tick, handleEvents, repeatKey, singleKey)
	Window.start()



if __name__ == '__main__':
	main()