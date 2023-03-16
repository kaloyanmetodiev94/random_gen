from random_gen.random_gen import RandomGen
from collections import defaultdict

if __name__=='__main__': # We reproduce the example here
	probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
	random_nums = [-1, 0, 1, 2, 3]
	
	rg = RandomGen(random_nums, probabilities)
	
	# Run the next_num() function 100 times and collect the results to reproduce the example (of course not exactly)
	example_range=100
	example_values={}
	example_values=defaultdict(lambda: 0, example_values) # If key is non-existent, initialize with 0
	for i in range(example_range):
			example_values[rg.next_num()]+=1        
	
	#print out the result
	for k in random_nums:
		print(k,':',example_values[k],'times')