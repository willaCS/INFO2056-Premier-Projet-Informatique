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
	match TerrainTile.type(tile):
		case TerrainTile.TERRAINTILETYPE_DEEPSEA:
			return (0, 0, 255 + (TerrainTile.height(tile) * 4))
		
		case TerrainTile.TERRAINTILETYPE_SEA:
			return (0, 0, 255 + (TerrainTile.height(tile) * 4))
		
		case TerrainTile.TERRAINTILETYPE_BEACH:
			return (255 - (TerrainTile.height(tile) % 4 * 16), 255 - (TerrainTile.height(tile) % 4 * 16), 0)
		
		case TerrainTile.TERRAINTILETYPE_PLAIN:
			return (0, 255 - (TerrainTile.height(tile) % 4 * 16), 0)
		
		case TerrainTile.TERRAINTILETYPE_FOREST:
			return (64 - (TerrainTile.height(tile) % 4 * 16), 128 - (TerrainTile.height(tile) % 4 * 16), 0)
		
		case TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE:
			return (150 - (TerrainTile.height(tile) % 4 * 16), 150 - (TerrainTile.height(tile) % 4 * 16), 150 - (TerrainTile.height(tile) % 4 * 16))
		
		case TerrainTile.TERRAINTILETYPE_MOUNTAIN_TOP:
			return (255 - (TerrainTile.height(tile) % 4 * 16), 255 - (TerrainTile.height(tile) % 4 * 16), 255 - (TerrainTile.height(tile) % 4 * 16))
		
		case _:
			return (0, 0, 0)

def ressource(ressource: Ressource.types):
	match (Ressource.type(ressource)):
		case Ressource.RESSOURCE_FISH:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_SALT:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_FERTILE_LAND:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_HUNTING_GROUNDS:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_WOOD:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_OIL:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_COAL:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_IRON:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_COPPER:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_PRECIOUS_METALS:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_RARE_METALS:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_SAND:
			return (80, 80, 80)
			
		case Ressource.RESSOURCE_STONE:
			return (80, 80, 80)
			
		case _:
			return (0, 0, 0)