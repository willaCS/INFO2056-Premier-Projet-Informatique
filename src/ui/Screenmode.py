"""
Ce fichier gère le screenmode ou le mode visuel de la carte.
La carte peux avoir un sous mode. Ce sous mode, si selectionné,
ne touchera pas au mode principale ducoup lorsque le sous mode est fermé,
on revient au mode précédent
"""

SCREENMODE_MAIN				= 1
SCREENMODE_ECONOMY_SUPPLY	= 2
SCREENMODE_ECONOMY_DEMAND	= 3
SCREENMODE_TRANSPORT		= 4

SCREENSUBMODE_NONE			= 0
SCREENSUBMODE_CONSTRUCTION	= 1

SCREENMODE_val = SCREENMODE_MAIN
SCREENMODE_sub = SCREENSUBMODE_NONE

def select(new_mode: int):
	global SCREENMODE_val
	SCREENMODE_val = new_mode