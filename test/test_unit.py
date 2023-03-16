import unittest
from random_gen.random_gen import RandomGen

class TestRandomGenMain(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self._typical_runs=10_000_000 # Asssume a use case would call the next_num 10_000_000 times for some of the tests
        super(TestRandomGenMain, self).__init__(*args, **kwargs)

    def test_init(self):
        # Test that the constructor raises a ValueError when the input lists have different lengths
        with self.assertRaises(ValueError):
            RandomGen([1, 2, 3], [0.1, 0.2, 0.3, 0.4])
        
        # Test that the constructor raises a ValueError when the probabilities less than 1
        with self.assertRaises(ValueError):
            RandomGen([1, 2, 3], [0.1, 0.2, 0.3])

        # Test that the class raises an error if any probability is greater than 1
        with self.assertRaises(ValueError):
            rg = RandomGen([1, 2, 3], [0.5, 0.25, 1.1])
    
    def test_next_num_distribution(self):
        # Test that the next_num function returns the correct values based on the input probabilities
        rg = RandomGen([1, 2, 3], [0.1, 0.2, 0.7])
        vals_dict={1:0,2:0,3:0}
        total_values=self._typical_runs//100 
        for _ in range(total_values):
            vals_dict[rg.next_num()]+=1
        self.assertAlmostEqual(vals_dict[1]/total_values, 0.1, delta=0.01)
        self.assertAlmostEqual(vals_dict[2]/total_values, 0.2, delta=0.01)
        self.assertAlmostEqual(vals_dict[3]/total_values, 0.7, delta=0.01)

    def test_next_num_input_values(self):
        # Test that the next_num function returns a value from the input list
        rg = RandomGen([1, 2, 3], [0.3, 0.4, 0.3])
        for _ in range(self._typical_runs//10): 
            self.assertIn(rg.next_num(), [1, 2, 3])
        

    def test_next_num_probability_equal_1(self):
        # Test that the next_num function raises a ValueError when the probabilities do not add up to 1
        rg = RandomGen([1, 2, 3], [0.8, 0.1, 0.1])
        with self.assertRaises(ValueError):
            rg._probabilities[0]=0.2 # Intentionally change probability to pass the check in the constructor
            for _ in range(self._typical_runs): # Call next_num {self._typical_runs} times with 60% fail chance
                rg.next_num()

class TestRandomGenEdgeCases(unittest.TestCase):
    def test_empty_input_lists(self):
        # Test that the class raises an error if both input lists are empty
        with self.assertRaises(ValueError):
            rg = RandomGen([], [])

    def test_non_numeric_input_values(self):
        # Test that the class raises an error if any input value is non-numeric
        with self.assertWarns(Warning):
            rg = RandomGen(["a", "b", "c"], [0.3, 0.5, 0.2])

    def test_non_numeric_probabilities(self):
        # Test that the class raises an error if any of the inputted is non-numeric even if it is convertible to numeric
        with self.assertRaises(TypeError):
            rg = RandomGen([1, 2, 3], [0.3, "0.5", 0.2])

if __name__ == '__main__':
    unittest.main()
