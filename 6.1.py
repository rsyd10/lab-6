import random
from multiprocessing import Pool,cpu_count
from math import sqrt
from timeit import default_timer as timer

def pi_part(n):
	print (n)

	count = 0

	for i in range(int(n)):

		x,y = random.random(), random.random()
		r = sqrt(pow(x,2) + pow(y,2))

		if r < 1:
			count += 1

	return count

if __name__=='__main__':

	start = timer()

	np = cpu_count()
	print (f'You have {np} cores')

	n = 100_000_000

	part_count = [n/np for i in range(np)]

	with Pool(processes = np) as pool:

		count = pool.map(pi_part,part_count)
		pi_est = sum(count) / (n * 1.0) * 4

	print ("Extimated value of PI : " , pi_est)
	print ("Time taken : " , start )
