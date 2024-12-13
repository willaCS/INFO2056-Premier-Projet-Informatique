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