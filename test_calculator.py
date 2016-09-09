# Assignment 1 - Calculator with test suite
# Module - Programming for Big Data
# Student - Galina Lopez 10333429

import unittest

from calculator import Calculator

# Calculator test suite
# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # this tests the add functionality
    def test_calculator_add_method(self):
        # testing integers
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)
        result = self.calc.add(-2, 2)
        self.assertEqual(0, result)
        result = self.calc.add(-2, -2)
        self.assertEqual(-4, result)
        
        # testing floats
        result = self.calc.add(2.0, 2.0)
        self.assertEqual(4.0, result)
        result = self.calc.add(2.0, -2.0)
        self.assertEqual(0.0, result)
        result = self.calc.add(-2.0, 2.0)
        self.assertEqual(0.0, result)
        result = self.calc.add(-2.0, -2.0)
        self.assertEqual(-4.0, result)
        
        # testing integers with floats
        result = self.calc.add(2, 2.0)
        self.assertEqual(4.0, result)
        result = self.calc.add(-2, -2.0)
        self.assertEqual(-4.0, result)
        result = self.calc.add(-2.0, 2)
        self.assertEqual(0.0, result) 
        result = self.calc.add(2.0, -2)
        self.assertEqual(0.0, result) 
        
        # testing ValueError is raised if both arguments are not integers or floats 
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.add, 'two', 0)
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        self.assertRaises(ValueError, self.calc.add, 'two', 3.0)
        self.assertRaises(ValueError, self.calc.add, 2.0, 'three')
        self.assertRaises(ValueError, self.calc.add, '1+1j', '1+1j')
        self.assertRaises(ValueError, self.calc.add, '1+1j', 3)
        self.assertRaises(ValueError, self.calc.add, 2, '1+1j')
        self.assertRaises(ValueError, self.calc.add, '1+1j', 3.0)
        self.assertRaises(ValueError, self.calc.add, 2.0, '1+1j')
        
        
    # this tests the subtract functionality 
    def test_calculator_subtract_method(self):
        # testing integers
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2, -2)
        self.assertEqual(4, result)
        result = self.calc.subtract(-2, 2)
        self.assertEqual(-4, result)  
        result = self.calc.subtract(-2, -2)
        self.assertEqual(0, result) 
        
        # testing floats
        result = self.calc.subtract(2.0, 2.0)
        self.assertEqual(0.0, result)
        result = self.calc.subtract(2.0, -2.0)
        self.assertEqual(4.0, result)
        result = self.calc.subtract(-2.0, 2.0)
        self.assertEqual(-4.0, result)  
        result = self.calc.subtract(-2.0, -2.0)
        self.assertEqual(0.0, result) 

        # testing integers with floats        
        result = self.calc.subtract(2, 2.0)
        self.assertEqual(0.0, result)
        result = self.calc.subtract(-2, -2.0)
        self.assertEqual(0.0, result)
        result = self.calc.subtract(-2.0, 2)
        self.assertEqual(-4.0, result) 
        result = self.calc.subtract(2.0, -2)
        self.assertEqual(4.0, result) 
        
        # testing ValueError is raised if both arguments are not integers or floats 
        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 0)
        self.assertRaises(ValueError, self.calc.subtract, 2, 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 3.0)
        self.assertRaises(ValueError, self.calc.subtract, 2.0, 'three')
        self.assertRaises(ValueError, self.calc.subtract, '1+1j', '1+1j')
        self.assertRaises(ValueError, self.calc.subtract, '1+1j', 3)
        self.assertRaises(ValueError, self.calc.subtract, 2, '1+1j')
        self.assertRaises(ValueError, self.calc.subtract, '1+1j', 3.0)
        self.assertRaises(ValueError, self.calc.subtract, 2.0, '1+1j')

    # this tests the multiply functionality 
    def test_calculator_multiply_method(self):
        #testing integers
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)
        result = self.calc.multiply(-2, 2)
        self.assertEqual(-4, result)
        result = self.calc.multiply(-2, -2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(0, 2)
        self.assertEqual(0, result)
        result = self.calc.multiply(-2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(0, -2)
        self.assertEqual(0, result)
        result = self.calc.multiply(0, 0)
        self.assertEqual(0, result)
        
        #testing floats
        result = self.calc.multiply(2.0, 2.0)
        self.assertEqual(4.0, result)
        result = self.calc.multiply(2.0, -2.0)
        self.assertEqual(-4.0, result)
        result = self.calc.multiply(-2.0, 2.0)
        self.assertEqual(-4.0, result)
        result = self.calc.multiply(-2.0, -2.0)
        self.assertEqual(4.0, result)
        result = self.calc.multiply(2.0, 0.0)
        self.assertEqual(0.0, result)
        result = self.calc.multiply(0.0, 2.0)
        self.assertEqual(0.0, result)
        result = self.calc.multiply(-2.0, 0.0)
        self.assertEqual(0.0, result)
        result = self.calc.multiply(0.0, -2.0)
        self.assertEqual(0.0, result)
        result = self.calc.multiply(0.0, 0.0)
        self.assertEqual(0.0, result)
        
        #testing integers with floats
        result = self.calc.multiply(2, 2.0)
        self.assertEqual(4.0, result)
        result = self.calc.multiply(-2, -2.0)
        self.assertEqual(4.0, result)
        result = self.calc.multiply(-2.0, 2)
        self.assertEqual(-4.0, result) 
        result = self.calc.multiply(2.0, -2)
        self.assertEqual(-4.0, result) 
        
        # testing ValueError is raised if both arguments are not integers or floats 
        self.assertRaises(ValueError, self.calc.multiply, 'two', 'three')
        self.assertRaises(ValueError, self.calc.multiply, 'two', 3)
        self.assertRaises(ValueError, self.calc.multiply, 2, 'three')
        self.assertRaises(ValueError, self.calc.multiply, 'two', 3.0)
        self.assertRaises(ValueError, self.calc.multiply, 2.0, 'three')
        self.assertRaises(ValueError, self.calc.multiply, '1+1j', '1+1j')
        self.assertRaises(ValueError, self.calc.multiply, '1+1j', 3)
        self.assertRaises(ValueError, self.calc.multiply, 2, '1+1j')
        self.assertRaises(ValueError, self.calc.multiply, '1+1j', 3.0)
        self.assertRaises(ValueError, self.calc.multiply, 2.0, '1+1j')

    # this tests the divide functionality 
    def test_calculator_divide_method(self):
        #testing integers
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(2, -2)
        self.assertEqual(-1, result)
        result = self.calc.divide(-2, 2)
        self.assertEqual(-1, result)
        result = self.calc.divide(-2, -2)
        self.assertEqual(1, result)
        result = self.calc.divide(0, 2)
        self.assertEqual(0, result)
        result = self.calc.divide(0, -2)
        self.assertEqual(0, result)        
        result = self.calc.divide(0, 0)
        self.assertEqual('NaN', result)
        result = self.calc.divide(2, 0)
        self.assertEqual('NaN', result)
        result = self.calc.divide(-2, 0)
        self.assertEqual('NaN', result)
        
        #testing floats
        result = self.calc.divide(2.0, 2.0)
        self.assertEqual(1.0, result)
        result = self.calc.divide(2.0, -2.0)
        self.assertEqual(-1.0, result)
        result = self.calc.divide(-2.0, 2.0)
        self.assertEqual(-1.0, result)
        result = self.calc.divide(-2.0, -2.0)
        self.assertEqual(1.0, result) 
        result = self.calc.divide(0.0, 2.0)
        self.assertEqual(0.0, result)
        result = self.calc.divide(0.0, -2.0)
        self.assertEqual(0.0, result)  
        result = self.calc.divide(0.0, 0.0)
        self.assertEqual('NaN', result)
        result = self.calc.divide(2.0, 0.0)
        self.assertEqual('NaN', result)
        result = self.calc.divide(-2.0, 0.0)
        self.assertEqual('NaN', result)
        
        #testing integers with floats        
        result = self.calc.divide(2, 2.0)
        self.assertEqual(1.0, result)
        result = self.calc.divide(-2, -2.0)
        self.assertEqual(1.0, result)
        result = self.calc.divide(-2.0, 2)
        self.assertEqual(-1.0, result) 
        result = self.calc.divide(2.0, -2)
        self.assertEqual(-1.0, result) 
        
        # testing ValueError is raised if both arguments are not integers or floats 
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
        self.assertRaises(ValueError, self.calc.divide, 'two', 3)
        self.assertRaises(ValueError, self.calc.divide, 2, 'three')        
        self.assertRaises(ValueError, self.calc.divide, 'two', 3.0)
        self.assertRaises(ValueError, self.calc.divide, 2.0, 'three')
        self.assertRaises(ValueError, self.calc.divide, '1+1j', '1+1j')
        self.assertRaises(ValueError, self.calc.divide, '1+1j', 3)
        self.assertRaises(ValueError, self.calc.divide, 2, '1+1j')
        self.assertRaises(ValueError, self.calc.divide, '1+1j', 3.0)
        self.assertRaises(ValueError, self.calc.divide, 2.0, '1+1j')

    # this tests the exponent functionality 
    def test_calculator_exponent_method(self):
        #testing integers
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2, 4)
        self.assertEqual(16, result)
        result = self.calc.exponent(4, 2)
        self.assertEqual(16, result)
        result = self.calc.exponent(2, -2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(-2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(-2, -2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)
        result = self.calc.exponent(-2, 0)
        self.assertEqual(1, result)
        result = self.calc.exponent(0, 0)
        self.assertEqual(1, result)
        result = self.calc.exponent(0, 2)
        self.assertEqual(0, result) 
        result = self.calc.exponent(0, -2)
        self.assertEqual('NaN', result)

        #testing floats
        result = self.calc.exponent(2.0, 2.0)
        self.assertEqual(4.0, result)
        result = self.calc.exponent(2.0, -2.0)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(-2.0, 2.0)
        self.assertEqual(4.0, result)
        result = self.calc.exponent(-2.0, -2.0)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(2.0, 0.0)
        self.assertEqual(1.0, result)
        result = self.calc.exponent(-2.0, 0.0)
        self.assertEqual(1.0, result)
        result = self.calc.exponent(0.0, 0.0)
        self.assertEqual(1.0, result)
        result = self.calc.exponent(0.0, 2.0)
        self.assertEqual(0.0, result)
        result = self.calc.exponent(0.0, -2.0)
        self.assertEqual('NaN', result)
        
        #testing integers with floats
        result = self.calc.exponent(2, 2.0)
        self.assertEqual(4.0, result)
        result = self.calc.exponent(-2, -2.0)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(-2.0, 2)
        self.assertEqual(4.0, result) 
        result = self.calc.exponent(2.0, -2)
        self.assertEqual(0.25, result)        
        
        # testing ValueError is raised if both arguments are not integers or floats         
        self.assertRaises(ValueError, self.calc.exponent, 'two', 'three')
        self.assertRaises(ValueError, self.calc.exponent, 'two', 3)
        self.assertRaises(ValueError, self.calc.exponent, 2, 'three')
        self.assertRaises(ValueError, self.calc.exponent, 'two', 3.0)
        self.assertRaises(ValueError, self.calc.exponent, 2.0, 'three')
        self.assertRaises(ValueError, self.calc.exponent, '1+1j', '1+1j')
        self.assertRaises(ValueError, self.calc.exponent, '1+1j', 3)
        self.assertRaises(ValueError, self.calc.exponent, 2, '1+1j')
        self.assertRaises(ValueError, self.calc.exponent, '1+1j', 3.0)
        self.assertRaises(ValueError, self.calc.exponent, 2.0, '1+1j')
        
    # this tests the my_factorial functionality    
    def test_calculator_my_factorial_method(self):
        #testing positive integers
        result = self.calc.my_factorial(5)
        self.assertEqual(120, result)
        result = self.calc.my_factorial(3)
        self.assertEqual(6, result)
        result = self.calc.my_factorial(2)
        self.assertEqual(2, result)
        result = self.calc.my_factorial(1)
        self.assertEqual(1, result)
        result = self.calc.my_factorial(0)
        self.assertEqual(1, result)
        
        # testing ValueError is raised if argument is not a positive integer 
        self.assertRaises(ValueError, self.calc.my_factorial, -2)
        self.assertRaises(ValueError, self.calc.my_factorial, 'two')
        self.assertRaises(ValueError, self.calc.my_factorial, '')
        self.assertRaises(ValueError, self.calc.my_factorial, 2.0)
        self.assertRaises(ValueError, self.calc.my_factorial, -2.0)
        self.assertRaises(ValueError, self.calc.my_factorial, 2+2j)
        self.assertRaises(ValueError, self.calc.my_factorial, 2-2j)
        self.assertRaises(ValueError, self.calc.my_factorial, -2+2j)
        self.assertRaises(ValueError, self.calc.my_factorial, -2-2j)
        
        
    # this tests the permutation functionality    
    def test_calculator_permutation_method(self):
        # testing positive integers where first arg bigger or equal to second arg.
        result = self.calc.permutation(5,5)
        self.assertEqual(120, result)
        result = self.calc.permutation(5,3)
        self.assertEqual(60, result)
        result = self.calc.permutation(5,2)
        self.assertEqual(20, result)
        result = self.calc.permutation(5,0)
        self.assertEqual(1, result)
        result = self.calc.permutation(0,0)
        self.assertEqual(1, result)        
        
        # testing ValueError is raised if both args are positive integers but first arg less than second arg.
        self.assertRaises(ValueError, self.calc.permutation, 0,5)
        self.assertRaises(ValueError, self.calc.permutation, 2,5)
        
        # testing ValueError is raised if both arguments are not positive integers
        self.assertRaises(ValueError, self.calc.permutation, -5,-5)
        self.assertRaises(ValueError, self.calc.permutation, 5,-5)
        self.assertRaises(ValueError, self.calc.permutation, -5,5)        
        self.assertRaises(ValueError, self.calc.permutation, 5.0, 5.0)
        self.assertRaises(ValueError, self.calc.permutation, 5, 5.0)
        self.assertRaises(ValueError, self.calc.permutation, 5.0, 5)
        self.assertRaises(ValueError, self.calc.permutation, 1+1j, 1-1j)
        self.assertRaises(ValueError, self.calc.permutation, 5, 1+1j)
        self.assertRaises(ValueError, self.calc.permutation, 1+1j, 5)
        self.assertRaises(ValueError, self.calc.permutation, 'two', 'three')
        self.assertRaises(ValueError, self.calc.permutation, 'two', 3)
        self.assertRaises(ValueError, self.calc.permutation, 2, 'three') 
        self.assertRaises(ValueError, self.calc.permutation, 'two', -3)
        self.assertRaises(ValueError, self.calc.permutation, -2, 'three')        
        self.assertRaises(ValueError, self.calc.permutation, 'two', 3.0)
        self.assertRaises(ValueError, self.calc.permutation, 2.0, 'three')
        self.assertRaises(ValueError, self.calc.permutation, 'two', 1+1j)
        self.assertRaises(ValueError, self.calc.permutation, 1-1j, 'three')
        self.assertRaises(ValueError, self.calc.permutation, 5.0, 1+1j)
        self.assertRaises(ValueError, self.calc.permutation, 1+1j, 5.0)
        self.assertRaises(ValueError, self.calc.permutation, -5, 1+1j)
        self.assertRaises(ValueError, self.calc.permutation, 1+1j, -5)
        self.assertRaises(ValueError, self.calc.permutation, -5, 5.0)
        self.assertRaises(ValueError, self.calc.permutation, 5.0, -5)
        
    # this tests the combination functionality    
    def test_calculator_combination_method(self):
        #testing positive integers where first arg bigger or equal to second arg.
        result = self.calc.combination(5,5)
        self.assertEqual(1, result)
        result = self.calc.combination(5,3)
        self.assertEqual(10, result)
        result = self.calc.combination(5,2)
        self.assertEqual(10, result)
        result = self.calc.combination(5,0)
        self.assertEqual(1, result)
        result = self.calc.combination(0,0)
        self.assertEqual(1, result)        
        
        # testing ValueError is raised if both args are positive integers but first arg less than second arg.
        self.assertRaises(ValueError, self.calc.combination, 0,5)
        self.assertRaises(ValueError, self.calc.combination, 2,5)
        
        # testing ValueError is raised if both arguments are not positive integers
        self.assertRaises(ValueError, self.calc.combination, -5,-5)
        self.assertRaises(ValueError, self.calc.combination, 5,-5)
        self.assertRaises(ValueError, self.calc.combination, -5,5)         
        self.assertRaises(ValueError, self.calc.combination, 5.0, 5.0)
        self.assertRaises(ValueError, self.calc.combination, 5, 5.0)
        self.assertRaises(ValueError, self.calc.combination, 5.0, 5)
        self.assertRaises(ValueError, self.calc.combination, 1+1j, 1-1j)
        self.assertRaises(ValueError, self.calc.combination, 5, 1+1j)
        self.assertRaises(ValueError, self.calc.combination, 1+1j, 5)
        self.assertRaises(ValueError, self.calc.combination, 'two', 'three')
        self.assertRaises(ValueError, self.calc.combination, 'two', 3)
        self.assertRaises(ValueError, self.calc.combination, 2, 'three') 
        self.assertRaises(ValueError, self.calc.combination, 'two', -3)
        self.assertRaises(ValueError, self.calc.combination, -2, 'three')        
        self.assertRaises(ValueError, self.calc.combination, 'two', 3.0)
        self.assertRaises(ValueError, self.calc.combination, 2.0, 'three')
        self.assertRaises(ValueError, self.calc.combination, 'two', 1+1j)
        self.assertRaises(ValueError, self.calc.combination, 1-1j, 'three')
        self.assertRaises(ValueError, self.calc.combination, 5.0, 1+1j)
        self.assertRaises(ValueError, self.calc.combination, 1+1j, 5.0)
        self.assertRaises(ValueError, self.calc.combination, -5, 1+1j)
        self.assertRaises(ValueError, self.calc.combination, 1+1j, -5)
        self.assertRaises(ValueError, self.calc.combination, -5, 5.0)
        self.assertRaises(ValueError, self.calc.combination, 5.0, -5)
        
    # this tests the square_root functionality 
    def test_calculator_square_root_method(self):
        #testing integer
        result = self.calc.square_root(1)
        self.assertEqual(1, result)
        result = self.calc.square_root(4)
        self.assertEqual(2, result)
        result = self.calc.square_root(0)
        self.assertEqual(0, result)
        result = self.calc.square_root(-1)
        self.assertEqual(1j, result)
        result = self.calc.square_root(-4)
        self.assertEqual(2j, result)
        
        #testing float
        result = self.calc.square_root(1.0)
        self.assertEqual(1, result)
        result = self.calc.square_root(-1.0)
        self.assertEqual(1j, result)
        result = self.calc.square_root(0.0)
        self.assertEqual(0.0, result)
        
        #testing complex
        result = self.calc.square_root(1+0j)
        self.assertEqual(1+0j, result)
        result = self.calc.square_root(1-0j)
        self.assertEqual(1+0j, result)
        result = self.calc.square_root(-1+0j)
        self.assertEqual(1j, result)
        result = self.calc.square_root(-1-0j)
        self.assertEqual(1j, result)
        result = self.calc.square_root(0+0j)
        self.assertEqual(0j, result)
                
        # testing ValueError is raised if argument is not a number
        self.assertRaises(ValueError, self.calc.square_root, 'two')
        self.assertRaises(ValueError, self.calc.square_root, '')
        
    # this tests the square functionality 
    def test_calculator_square_method(self):
        #testing integer
        result = self.calc.square(1)
        self.assertEqual(1, result)
        result = self.calc.square(2)
        self.assertEqual(4, result)
        result = self.calc.square(0)
        self.assertEqual(0, result)
        result = self.calc.square(-1)
        self.assertEqual(1, result)
        result = self.calc.square(-2)
        self.assertEqual(4, result)
        
        #testing float
        result = self.calc.square(1.5)
        self.assertEqual(2.25, result)
        result = self.calc.square(-1.5)
        self.assertEqual(2.25, result)
        result = self.calc.square(0.0)        
        self.assertEqual(0.0, result)
        
        #testing complex
        result = self.calc.square(1+1j)
        self.assertEqual(2j, result)
        result = self.calc.square(1-1j)
        self.assertEqual(-2j, result)
        result = self.calc.square(-1+1j)
        self.assertEqual(-2j, result)
        result = self.calc.square(-1-1j)
        self.assertEqual(2j, result)
        result = self.calc.square(0+0j)
        self.assertEqual(0j, result)
        
        # testing ValueError is raised if argument is not a number        
        self.assertRaises(ValueError, self.calc.square, 'two')
        self.assertRaises(ValueError, self.calc.square, '')
 
    # this tests the cube functionality 
    def test_calculator_cube_method(self):
        #testing integer
        result = self.calc.cube(1)
        self.assertEqual(1, result)
        result = self.calc.cube(2)
        self.assertEqual(8, result)
        result = self.calc.cube(0)
        self.assertEqual(0, result)
        result = self.calc.cube(-1)
        self.assertEqual(-1, result)
        result = self.calc.cube(-2)
        self.assertEqual(-8, result)
        
        #testing float
        result = self.calc.cube(1.5)
        self.assertEqual(3.375, result)
        result = self.calc.cube(-1.5)
        self.assertEqual(-3.375, result)
        result = self.calc.cube(0.0)
        self.assertEqual(0.0, result)
        
        #testing complex
        result = self.calc.cube(1+1j)
        self.assertEqual(-2+2j, result)
        result = self.calc.cube(1-1j)
        self.assertEqual(-2-2j, result)
        result = self.calc.cube(-1+1j)
        self.assertEqual(2+2j, result)
        result = self.calc.cube(-1-1j)
        self.assertEqual(2-2j, result)
        result = self.calc.cube(0+0j)
        self.assertEqual(0j, result)
        
        # testing ValueError is raised if argument is not a number     
        self.assertRaises(ValueError, self.calc.cube, 'two')
        self.assertRaises(ValueError, self.calc.cube, '')
        
if __name__ == '__main__':
    unittest.main()
