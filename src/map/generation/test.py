import random


seed = random.randint(0, 0x7fffffff)

M = 0x7fffffff
A = 48271

NB_ITERATIONS = 100

def random_lcg(n: int):
	n = n % (M - 1) + 1

	# Iteration with only x
	iteration = NB_ITERATIONS
	while (iteration > 0):
		n = (n * A) % M
		iteration -= 1
		
	return int(n / M * 100)
	
for i in range(-1000, 1000):
    res = ''
    for j in range (8):
        res += f'{random_lcg(i * 8 + seed + j)}\t'
    print(res)