# Assignment 1 - Calculator with test suite
# Module - Programming for Big Data
# Student - Galina Lopez 10333429

from math import factorial
from cmath import sqrt

# Calculator functionality
class Calculator(object):

    # adding addition to my calculator
    def add(self, x, y):
        number_types = (int, long, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
    
    # adding subtraction to my calculator
    def subtract(self, x, y):
        number_types = (int, long, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
            
    # adding multiplication to my calculator
    def multiply(self, x, y):
        number_types = (int, long, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError  

    # adding division to my calculator
    def divide(self, x, y):
        number_types = (int, long, float)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return 'NaN'
            return x / float(y)
        else:
            raise ValueError

    # adding exponent to my calculator
    def exponent(self, x, y):
        number_types = (int, long, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            if x == 0 and y < 0:
                return 'NaN'
            return x ** y
        else:
            raise ValueError 
    
    # adding factorial to my calculator
    def my_factorial(self, n):
                
        if isinstance(n, int) and n >= 0:
            return factorial(n)
        else:
            raise ValueError
    
    # adding permutation to my calculator
    def permutation(self, n, r):
    
        if isinstance(n, int) and isinstance(r, int) and n >=0 and r >=0 and n >= r:
            return factorial(n) / factorial (n - r)
        else:
            raise ValueError
        
    # adding combination to my calculator        
    def combination(self, n, r):
    
        if isinstance(n, int) and isinstance(r, int) and n >= 0 and r >=0 and n >= r:
            return factorial(n) / factorial (n - r) / factorial(r)
        else:
            raise ValueError
            
    # adding square root to my calculator
    def square_root(self, n):
        number_types = (int, long, float, complex)
        
        if isinstance(n, number_types):            
            return sqrt(n)
        else:
            raise ValueError
            
    # adding square to my calculator
    def square(self, n):
        number_types = (int, long, float, complex)
        
        if isinstance(n, number_types):            
            return n * n
        else:
            raise ValueError
            
    # adding cube to my calculator
    def cube(self, n):
        number_types = (int, long, float, complex)
        
        if isinstance(n, number_types):            
            return n * n * n
        else:
            raise ValueError

