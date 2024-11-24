import pygame
import Window

fonts = {}

def loadFont(id: str, name: str, size: int, bold: bool = False):
	fonts[id] = pygame.font.SysFont(name, size, bold)

def longNumber(number: int) -> str:
	if number < 1000:
		return str(number)
	elif number < 1000000:
		return str((number // 10) / 100) + "K"
	elif number < 1000000000:
		return str((number // 10000) / 100) + "M"
	elif number < 1000000000000:
		return str((number // 10000000) / 100) + "B"
	else:
		return str((number // 10000000000) / 100) + "T"

# anchor can be one of the following:
# topleft, bottomleft, topright, bottomright
# midtop, midleft, midbottom, midright
# center, centerx, centery
def drawText(
	fontId: str,
	coord,
	text: str,
	color,
	anchor: str = "topleft"
):
	font = fonts.get(fontId) # type: pygame.font.Font
	if font is None:
		raise ValueError(f"Font {fontId} not loaded")
	text_prepared = font.render(text, True, color)
	rect = text_prepared.get_rect()
	setattr(rect, anchor, coord)
	Window.inst.blit(text_prepared, rect)
