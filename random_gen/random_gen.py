import random
import warnings

class RandomGen:
	def __init__(self, random_nums: list, probabilities: list):
		"""
		Initializes the RandomGenerator class with a list of values and their corresponding probabilities.
		
		Args:
		- values (list): A list of values to choose from.
		- probabilities (list): A list of probabilities for each value.

        Raises:
        TypeError: If values or probabilities are not numeric.
        ValueError: If the sum of probabilities is greater than 1.0.

		"""
		self._random_nums = random_nums
		self._probabilities = probabilities

		# Since it is not specified whether the inputted values need to be numeric or not, this is just a warning for now 
		if not all(isinstance(x, (int, float)) for x in self._random_nums):
			warnings.warn("Input values should be numeric")
			
		if not all(isinstance(x, (int, float)) for x in self._probabilities): 
			raise TypeError("Probabilities must be numeric")
		
		# Check that the lengths of the two input lists match
		if len(self._random_nums) != len(self._probabilities):
			raise ValueError("The length of the 'values' list must match the length of the 'probabilities' list.")

		self._len=len(self._random_nums) # Save the length of both sequences, so that it is not recalculated anymore
		
		# Check that the probabilities add up to 1
		if abs(sum(self._probabilities) - 1.0) > 0.00001:
			raise ValueError("The probabilities must add up to exactly 1.")

	
	def next_num(self):
		"""
		Returns a randomly selected value from the 'values' list based on the corresponding probabilities.
		
		Returns:
		- A randomly selected value from the 'values' list.
		"""
		rand_val = random.random() # Generate a random number between 0 and 1
		cum_prob = 0.0 # Initialize the cumulative probability
		
		# Iterate over the values and their corresponding probabilities
		for i in range(self._len):
			cum_prob += self._probabilities[i] # Add the current probability to the cumulative probability
			
			# If the cumulative probability is greater than the random number, return the corresponding value
			if rand_val < cum_prob:
				return self._random_nums[i]
		
		# If we get here, something went wrong
		raise ValueError("The probabilities did not add up to 1.")
		

