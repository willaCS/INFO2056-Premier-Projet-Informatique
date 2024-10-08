import globals.all
import window
from events import handleEvents
from input import repeatKey, singleKey
from ui.drawFrame import drawFrame
from ui.drawUI import getFont

def setup():
	globals.all.font = getFont()

def tick():
	# __calculate()
	drawFrame()

def	main():
	window.init(setup, tick, handleEvents, repeatKey, singleKey)
	window.start()
	

if __name__ == '__main__':
	main()