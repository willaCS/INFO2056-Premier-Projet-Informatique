import pygame
import Window

fonts = {}

def loadFont(id: str, name: str, size: int, bold: bool = False):
	fonts[id] = pygame.font.SysFont(name, size, bold)

def longNumber(number: int) -> str:
	if abs(number / (10 ** 12)) >= 1:
		return str((number // (10 ** (12 - 2))) / 100) + "T"
	elif abs(number / (10 ** 9)) >= 1:
		return str((number // (10 ** (9 - 2))) / 100) + "B"
	elif abs(number / (10 ** 6)) >= 1:
		return str((number // (10 ** (6 - 2))) / 100) + "M"
	elif abs(number / (10 ** 3)) >= 1:
		return str((number // (10 ** (3 - 2))) / 100) + "K"
	else:
		return str(number)

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
