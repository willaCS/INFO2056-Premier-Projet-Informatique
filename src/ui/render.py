from globals.all import COLOR_BLACK, COLOR_ORANGE, COLOR_PURPLE, COLOR_RED
from map import Ressource, TerrainTile, Tile
from map import Industry

def tile(tile: Tile.types):
	match Tile.type(tile):
		case Tile.TILETYPE_TRANSPORT:
			return COLOR_PURPLE
		
		case Tile.TILETYPE_TRANSPORTHUB:
			return COLOR_RED
		
		case Tile.TILETYPE_INDUSTRY:
			match Tile.subtype(tile):
				case Industry.INDUSTRY_FISHINGBOAT:
					return (0, 0, 0)
				case Industry.INDUSTRY_SALTEXTRACTION:
					return (230, 230, 230)
				case Industry.INDUSTRY_WHEAT_FIELDS:
					return (255, 222, 19)
				case Industry.INDUSTRY_POTATO_FIELDS:
					return (227, 164, 68)
				case Industry.INDUSTRY_COTTON_FIELDS:
					return (149, 255, 140)
				case Industry.INDUSTRY_RICE_FIELDS:
					return (144, 228, 245)
				case Industry.INDUSTRY_FURHUNTINGGROUNDS:
					return (156, 105, 28)
				case Industry.INDUSTRY_LUMBERMILL:
					return (102, 64, 7)
				case Industry.INDUSTRY_OILWELL:
					return (80, 80, 80)
				case Industry.INDUSTRY_COALMINE:
					return (20, 20, 20)
				case Industry.INDUSTRY_IRONMINE:
					return (0, 0, 0)
				case Industry.INDUSTRY_COPPERMINE:
					return (255, 89, 0)
				case Industry.INDUSTRY_PRECIOUSMETALMINE:
					return (0, 150, 161)
				case Industry.INDUSTRY_RAREMETALMINE:
					return (101, 135, 101)
				case Industry.INDUSTRY_BREADFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_ALCOHOLFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_SUSHIFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_TEXTILEFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_CLOTHESFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_FURNITUREFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_STEELMILL:
					return (0, 0, 0)
				case Industry.INDUSTRY_TOOLINGFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_CEMENTFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_REFINARY:
					return (0, 0, 0)
				case Industry.INDUSTRY_PLASTICFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_GLASSFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_ELECTRONICCOMPONENTSFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_RADIOFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_COMPUTERFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_GUNFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_ENGINEFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_CARFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_PLANESFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_JEWELRYWORKSHOP:
					return (0, 0, 0)
				case Industry.INDUSTRY_PHONEFACTORY:
					return (0, 0, 0)
				case Industry.INDUSTRY_STONEQUERY:
					return (0, 0, 0)
				case Industry.INDUSTRY_SANDQUERY:
					return (0, 0, 0)
		
		case Tile.TILETYPE_CITY:
			return (22, 17, 84)
		
		case Tile.TILETYPE_CITYCENTER:
			return (163, 28, 53)
		
		case _:
			return COLOR_BLACK
		
def terrainTile(tile: TerrainTile.types):
	hhh = TerrainTile.height(tile) % 4 * 16
	match TerrainTile.type(tile):
		case TerrainTile.TERRAINTILETYPE_DEEPSEA:
			return (0, 0, 255 + (TerrainTile.height(tile) * 4))
		
		case TerrainTile.TERRAINTILETYPE_SEA:
			return (0, 0, 255 + (TerrainTile.height(tile) * 4))
		
		case TerrainTile.TERRAINTILETYPE_BEACH:
			return (255 - hhh, 255 - hhh, 0)
		
		case TerrainTile.TERRAINTILETYPE_PLAIN:
			return (0, 255 - hhh, 0)
		
		case TerrainTile.TERRAINTILETYPE_FOREST:
			return (64 - hhh, 128 - hhh, 0)
		
		case TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE:
			return (150 - hhh, 150 - hhh, 150 - hhh)
		
		case TerrainTile.TERRAINTILETYPE_MOUNTAIN_TOP:
			return (255 - hhh, 255 - hhh, 255 - hhh)
		
		case _:
			return (0, 0, 0)

def ressource(ressource: Ressource.types):
	hhh = Ressource.height(ressource) % 4 * 16
	match (Ressource.type(ressource)):
		case Ressource.RESSOURCE_FISH:
			return (0, 0, 230 + (Ressource.height(ressource) * 4))
			
		case Ressource.RESSOURCE_SALT:
			return (252, 255, 129)
			
		case Ressource.RESSOURCE_FERTILE_LAND:
			return (134 - hhh, 255 - hhh, 0)
			
		case Ressource.RESSOURCE_HUNTING_GROUNDS:
			return (0, 82, 0)
			
		case Ressource.RESSOURCE_WOOD:
			return (0, 102 + hhh, 0)
			
		case Ressource.RESSOURCE_OIL:
			return (191, 196, 0)
			
		case Ressource.RESSOURCE_COAL:
			return (70, 70, 70)
			
		case Ressource.RESSOURCE_IRON:
			return (218, 227, 227)
			
		case Ressource.RESSOURCE_COPPER:
			return (197, 106, 57)
			
		case Ressource.RESSOURCE_PRECIOUS_METALS:
			return (78, 226, 236)
			
		case Ressource.RESSOURCE_RARE_METALS:
			return (88, 156, 88)
			
		case Ressource.RESSOURCE_SAND:
			return (255 - hhh, 255 - hhh, 0)
			
		case Ressource.RESSOURCE_STONE:
			return (150 - hhh, 150 - hhh, 150 - hhh)
			
		case _:
			return (0, 0, 0)