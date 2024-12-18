from ui import gestionMode

DARK_TEXT		    = (228, 231, 234)
DARK_BACKGROUND	    = (9, 13, 17)
DARK_BACKGROUND2	= (20, 24, 28)
DARK_BACKGROUND3	= (47, 56, 66)
DARK_PRIMARY		= (29, 74, 128)
DARK_SECONDARY	    = (38, 47, 58)
DARK_ACCENT	        = (27, 119, 230)


LIGHT_TEXT		    = (14, 17, 22)
LIGHT_BACKGROUND	= (228, 235, 241)
LIGHT_BACKGROUND2	= (217, 224, 230)
LIGHT_BACKGROUND3	= (191, 201, 211)
LIGHT_PRIMARY		= (43, 65, 90)
LIGHT_SECONDARY	    = (134, 168, 203)
LIGHT_ACCENT	    = (62, 111, 163)

TEXT		= LIGHT_TEXT		
BACKGROUND	= LIGHT_BACKGROUND	
BACKGROUND2	= LIGHT_BACKGROUND2	
BACKGROUND3	= LIGHT_BACKGROUND3	
PRIMARY		= LIGHT_PRIMARY		
SECONDARY	= LIGHT_SECONDARY	
ACCENT		= LIGHT_ACCENT		



ROUNDING_SMOOTH = 5
ROUNDING_HARD = 10
MENU_BORDER_WIDTH = 5

PADDING = 5

TOP_BAR_HEIGHT = 60
LARGEUR_SIDEMENU = 470


def change_Background(mode):
	global TEXT, BACKGROUND, BACKGROUND2, BACKGROUND3, PRIMARY, SECONDARY, ACCENT		


	if gestionMode.mode == gestionMode.MODE_DARK:
		TEXT = LIGHT_TEXT
		BACKGROUND = LIGHT_BACKGROUND
		BACKGROUND2 = LIGHT_BACKGROUND2
		BACKGROUND3 = LIGHT_BACKGROUND3
		PRIMARY = LIGHT_PRIMARY
		SECONDARY = LIGHT_SECONDARY
		ACCENT = LIGHT_ACCENT
		gestionMode.change_mode(gestionMode.MODE_LIGHT)
			
	
	
	else:
		TEXT = DARK_TEXT
		BACKGROUND = DARK_BACKGROUND
		BACKGROUND2 = DARK_BACKGROUND2
		BACKGROUND3 = DARK_BACKGROUND3
		PRIMARY = DARK_PRIMARY
		SECONDARY = DARK_SECONDARY
		ACCENT = DARK_ACCENT
		gestionMode.change_mode(gestionMode.MODE_DARK)

		
		