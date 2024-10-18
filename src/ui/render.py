from globals.all import COLOR_BLACK, COLOR_ORANGE, COLOR_PURPLE, COLOR_RED
from map import Ressource, TerrainTile, Tile

def tile(tile: Tile.types):
	match Tile.type(tile):
		case Tile.TILETYPE_TRANSPORT:
			return COLOR_PURPLE
		
		case Tile.TILETYPE_TRANSPORTHUB:
			return COLOR_RED
		
		case Tile.TILETYPE_INDUSTRY:
			return COLOR_ORANGE
		
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
			return (230, 230, 230)
			
		case Ressource.RESSOURCE_FERTILE_LAND:
			return (255 - hhh, 204 - hhh, 0)
			
		case Ressource.RESSOURCE_HUNTING_GROUNDS:
			return (0, 82, 0)
			
		case Ressource.RESSOURCE_WOOD:
			return (0, 102 + hhh, 0)
			
		case Ressource.RESSOURCE_OIL:
			return (20, 20, 20)
			
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