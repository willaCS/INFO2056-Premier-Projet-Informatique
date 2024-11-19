def isInRectangle(pos, rect):
    return rect[0][0] <= pos[0] and pos[0] <= rect[0][0] + rect[1][0]\
        and rect[0][1] <= pos[1] and pos[1] <= rect[0][1] + rect[1][1]

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