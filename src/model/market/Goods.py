model_market_goods_GOODS_FISH					= 1
model_market_goods_GOODS_SALT					= 2
model_market_goods_GOODS_WHEAT					= 3
model_market_goods_GOODS_POTATO				= 4
model_market_goods_GOODS_COTTON				= 5
model_market_goods_GOODS_RICE					= 6
model_market_goods_GOODS_FUR					= 7
model_market_goods_GOODS_WOOD					= 8
model_market_goods_GOODS_OIL					= 9
model_market_goods_GOODS_COAL					= 10
model_market_goods_GOODS_IRON					= 11
model_market_goods_GOODS_COPPER				= 12
model_market_goods_GOODS_PRECIOUS_METAL		= 13
model_market_goods_GOODS_RARE_METAL			= 14
model_market_goods_GOODS_BREAD					= 15
model_market_goods_GOODS_ALCOHOL				= 16
model_market_goods_GOODS_SUSHI					= 17
model_market_goods_GOODS_TEXTILE				= 18
model_market_goods_GOODS_CLOTHES				= 19
model_market_goods_GOODS_FURNITURE				= 20
model_market_goods_GOODS_STEEL					= 21
model_market_goods_GOODS_TOOLS					= 22
model_market_goods_GOODS_CEMENT				= 23
model_market_goods_GOODS_FUEL					= 24
model_market_goods_GOODS_PLASTIC				= 25
model_market_goods_GOODS_GLASS					= 26
model_market_goods_GOODS_ELECTRONICS_COMPONENT	= 27
model_market_goods_GOODS_RADIO					= 28
model_market_goods_GOODS_COMPUTER				= 29
model_market_goods_GOODS_GUNS					= 30
model_market_goods_GOODS_ENGINE				= 31
model_market_goods_GOODS_CAR					= 32
model_market_goods_GOODS_PLANES				= 33
model_market_goods_GOODS_JEWELRY				= 34
model_market_goods_GOODS_PHONE					= 35
model_market_goods_GOODS_STONE					= 36
model_market_goods_GOODS_SAND					= 37

def model_market_goods_print_goods(type):
	if type == model_market_goods_GOODS_FISH:
		return 'fish'
	elif type == model_market_goods_GOODS_SALT:
		return 'salt'
	elif type == model_market_goods_GOODS_WHEAT:
		return 'wheat'
	elif type == model_market_goods_GOODS_POTATO:
		return 'potato'
	elif type == model_market_goods_GOODS_COTTON:
		return 'cotton'
	elif type == model_market_goods_GOODS_RICE:
		return 'rice'
	elif type == model_market_goods_GOODS_FUR:
		return 'fur'
	elif type == model_market_goods_GOODS_WOOD:
		return 'wood'
	elif type == model_market_goods_GOODS_OIL:
		return 'oil'
	elif type == model_market_goods_GOODS_COAL:
		return 'coal'
	elif type == model_market_goods_GOODS_IRON:
		return 'iron'
	elif type == model_market_goods_GOODS_COPPER:
		return 'copper'
	elif type == model_market_goods_GOODS_PRECIOUS_METAL:
		return 'precious metal'
	elif type == model_market_goods_GOODS_RARE_METAL:
		return 'rare metal'
	elif type == model_market_goods_GOODS_BREAD:
		return 'bread'
	elif type == model_market_goods_GOODS_ALCOHOL:
		return 'alcohol'
	elif type == model_market_goods_GOODS_SUSHI:
		return 'sushi'
	elif type == model_market_goods_GOODS_TEXTILE:
		return 'textile'
	elif type == model_market_goods_GOODS_CLOTHES:
		return 'clothes'
	elif type == model_market_goods_GOODS_FURNITURE:
		return 'furniture'
	elif type == model_market_goods_GOODS_STEEL:
		return 'steel'
	elif type == model_market_goods_GOODS_TOOLS:
		return 'tools'
	elif type == model_market_goods_GOODS_CEMENT:
		return 'cement'
	elif type == model_market_goods_GOODS_FUEL:
		return 'fuel'
	elif type == model_market_goods_GOODS_PLASTIC:
		return 'plastic'
	elif type == model_market_goods_GOODS_GLASS:
		return 'glass'
	elif type == model_market_goods_GOODS_ELECTRONICS_COMPONENT:
		return 'electronics component'
	elif type == model_market_goods_GOODS_RADIO:
		return 'radio'
	elif type == model_market_goods_GOODS_COMPUTER:
		return 'computer'
	elif type == model_market_goods_GOODS_GUNS:
		return 'guns'
	elif type == model_market_goods_GOODS_ENGINE:
		return 'engine'
	elif type == model_market_goods_GOODS_CAR:
		return 'car'
	elif type == model_market_goods_GOODS_PLANES:
		return 'planes'
	elif type == model_market_goods_GOODS_JEWELRY:
		return 'jewelry'
	elif type == model_market_goods_GOODS_PHONE:
		return 'phone'
	elif type == model_market_goods_GOODS_STONE:
		return 'stone'
	elif type == model_market_goods_GOODS_SAND:
		return 'sand'
	else:
		return 'unknown'