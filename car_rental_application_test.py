import unittest

from car import *
from car_rental import *
from car_rental_application import *

# DBS Car Rental Application test suite
# tests the DBS car rental application functionality
class TestCarRentalApplication(unittest.TestCase):    
    
    # this tests the show main menu function
    def test_car_rental_application_showMainMenu_function(self):
        self.assertEqual(True, showMainMenu())
     
    # this tests the show next menu function     
    def test_car_rental_application_showNextMenu_function(self):
        self.assertEqual(True, showNextMenu())
        
    # this tests the enter convert validate functionality
    def test_car_rental_application_enterConvertValidate_function(self):
        self.assertEqual(10, enterConvertValidate("To test the function enter 10 "))
     
    # this tests the calculate mileage functionality
    def test_car_rental_application_calculateMileageSurcharge_function(self):
        self.assertEqual(80, calculateMileageSurcharge(500))
    
    # this tests the print transaction details function
    def test_car_rental_application_printTransactionDetails_function(self):
        customer = Customer()
        customer.id = 10
        customer.name = 'Gala'
        car = Car()
        car.reg = '151 D 1775'
        car.make = 'Mercedes'
        car.model = 'e230'
        car.colour = 'Silver'
        car.mileage = 1000
        self.assertEqual(True, printTransactionDetails(customer, car))   
    
    # this tests the print transaction receipt function
    def test_car_rental_application_printTransactionReceipt_function(self):
        customer = Customer()
        customer.id = 10
        customer.name = 'Gala'
        self.assertEqual(True, printTransactionReceipt(customer, 100, 50))  
    
     
    # this tests the fill car details function
    def test_car_rental_application_fillCarDetails_function(self):
        data[0] = '151 D 4090,Audi,R8,Silver,10000,0'        
        car = fillCarDetails(data, 0, Car())
        self.assertEqual('151 D 4090', car.reg)
        self.assertEqual('Audi', car.make)
        self.assertEqual('R8', car.model)
        self.assertEqual('Silver', car.colour)
        self.assertEqual(10000, car.mileage)
        self.assertEqual(0, car.type)     
    
if __name__ == '__main__':
	unittest.main()