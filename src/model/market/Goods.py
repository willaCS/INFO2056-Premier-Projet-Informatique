from enum import Enum

class GoodsType(Enum):
	FISH					= 1
	SALT					= 2
	WHEAT					= 3
	POTATO					= 4
	COTTON					= 5
	RICE					= 6
	FUR						= 7
	WOOD					= 8
	OIL						= 9
	COAL					= 10
	IRON					= 11
	COPPER					= 12
	PRECIOUS_METAL			= 13
	RARE_METAL				= 14
	BREAD					= 15
	ALCOHOL					= 16
	SUSHI					= 17
	TEXTILE					= 18
	CLOTHES					= 19
	FURNITURE				= 20
	STEEL					= 21
	TOOLS					= 22
	CEMENT					= 23
	FUEL					= 24
	PLASTIC					= 25
	GLASS					= 26
	ELECTRONICS_COMPONENT	= 27
	RADIO					= 28
	COMPUTER				= 29
	GUNS					= 30
	ENGINE					= 31
	CAR						= 32
	PLANES					= 33
	JEWELRY					= 34
	PHONE					= 35
	STONE					= 36
	SAND					= 37

def print_goods(type):
	match type:
		case GoodsType.FISH:
			return 'fish'
		case GoodsType.SALT:
			return 'salt'
		case GoodsType.WHEAT:
			return 'wheat'
		case GoodsType.POTATO:
			return 'potato'
		case GoodsType.COTTON:
			return 'cotton'
		case GoodsType.RICE:
			return 'rice'
		case GoodsType.FUR:
			return 'fur'
		case GoodsType.WOOD:
			return 'wood'
		case GoodsType.OIL:
			return 'oil'
		case GoodsType.COAL:
			return 'coal'
		case GoodsType.IRON:
			return 'iron'
		case GoodsType.COPPER:
			return 'copper'
		case GoodsType.PRECIOUS_METAL:
			return 'precious metal'
		case GoodsType.RARE_METAL:
			return 'rare metal'
		case GoodsType.BREAD:
			return 'bread'
		case GoodsType.ALCOHOL:
			return 'alcohol'
		case GoodsType.SUSHI:
			return 'sushi'
		case GoodsType.TEXTILE:
			return 'textile'
		case GoodsType.CLOTHES:
			return 'clothes'
		case GoodsType.FURNITURE:
			return 'furniture'
		case GoodsType.STEEL:
			return 'steel'
		case GoodsType.TOOLS:
			return 'tools'
		case GoodsType.CEMENT:
			return 'cement'
		case GoodsType.FUEL:
			return 'fuel'
		case GoodsType.PLASTIC:
			return 'plastic'
		case GoodsType.GLASS:
			return 'glass'
		case GoodsType.ELECTRONICS_COMPONENT:
			return 'electronics component'
		case GoodsType.RADIO:
			return 'radio'
		case GoodsType.COMPUTER:
			return 'computer'
		case GoodsType.GUNS:
			return 'guns'
		case GoodsType.ENGINE:
			return 'engine'
		case GoodsType.CAR:
			return 'car'
		case GoodsType.PLANES:
			return 'planes'
		case GoodsType.JEWELRY:
			return 'jewelry'
		case GoodsType.PHONE:
			return 'phone'
		case GoodsType.STONE:
			return 'stone'
		case GoodsType.SAND:
			return 'sand'
		case _:
			return 'unknown'