import unittest

from car_rental import *

# Car Rental test suite
# tests the customer functionality
class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer() 
	
    # this tests the default constructors 
    def test_customer_default_constructors(self):
        self.assertEqual(None,self.customer.car)
        self.assertEqual('',self.customer.id)
        self.assertEqual('',self.customer.name)
        self.assertEqual(0,self.customer.cash_spend) 
    
    # this tests the getters functionality
    def test_customer_getters(self):    
        self.assertEqual(None,self.customer.getCar())
        self.assertEqual('',self.customer.getId())
        self.assertEqual('',self.customer.getName())
        self.assertEqual(0,self.customer.getCashSpend()) 
     
    # this tests the setters functionality
    def test_customer_setters(self):
        self.customer.setId('11')
        self.customer.setName('Gala')
        self.customer.setCashSpend(100)
        self.assertEqual('11',self.customer.getId())
        self.assertEqual('Gala',self.customer.getName())
        self.assertEqual(100,self.customer.getCashSpend())
 
    # this tests the rent car and return car functionalities
    def test_customer_rentCar_and_returnCar_methods(self):
		self.assertEqual(None,self.customer.getCar())
		car = PetrolCar()
		self.customer.rentCar(car)
		self.assertEqual(car,self.customer.getCar())
		returnedCar = self.customer.returnCar()
		self.assertEqual(car, returnedCar)
     
    # this tests the make payment functionality
    def test_customer_makePayment_method(self):
        self.assertEqual(0,self.customer.getCashSpend())        
        self.customer.makePayment(100.50)
        self.assertEqual(100.50,self.customer.getCashSpend())
       
    # this tests the move car functionality
    def test_customer_moveCar_method(self):
        car = PetrolCar()
        self.assertEqual(0, car.getMileage())
        self.customer.moveCar(car, 500)
        self.assertEqual(500, car.getMileage())


# tests the car rental functionality
class TestCarRental(unittest.TestCase):

    def setUp(self):
        self.carRental = CarRental()
     
    # this tests the default constructors 
    def test_car_rental_default_constructors(self):
        type_petrol = 0
        type_diesel = 1
        type_electric = 2
        type_hybrid = 3
        self.assertEqual(0, len(self.carRental.customers))
        self.assertEqual(0, len(self.carRental.cars[type_petrol])\
                             +len(self.carRental.cars[type_diesel])\
                             +len(self.carRental.cars[type_electric])\
                             +len(self.carRental.cars[type_hybrid]))
        self.assertEqual(0, len(self.carRental.cars[type_petrol]))
        self.assertEqual(0, len(self.carRental.cars[type_diesel]))
        self.assertEqual(0, len(self.carRental.cars[type_electric]))
        self.assertEqual(0, len(self.carRental.cars[type_hybrid]))
        self.assertEqual(0, self.carRental.cash_earned) 

    # this tests the getter functionality
    def test_car_rental_getter(self):    
        self.assertEqual(0,self.carRental.getCashEarned())
     
    # this tests the setter functionality     
    def test_car_rental_setter(self):        
        self.carRental.setCashEarned(100)
        self.assertEqual(100,self.carRental.getCashEarned())
     
    # this tests the add customer and get customer functionalities
    def test_car_rental_addCustomer_and_getCustomer_methods(self):
        self.assertEqual(0, len(self.carRental.customers))
        customer = Customer()
        self.carRental.addCustomer(customer)
        self.assertEqual(1, len(self.carRental.customers))
        addedCustomer = self.carRental.getCustomer(0)
        self.assertEqual(customer, addedCustomer)
     
    # this tests the rent car and return car functionalities     
    def test_car_rental_returnCar_and_rentCar_methods(self):
        type_petrol = 0
        self.assertEqual(0, len(self.carRental.cars[type_petrol]))
        car = PetrolCar()
        self.carRental.returnCar(type_petrol,car)
        self.assertEqual(1, len(self.carRental.cars[type_petrol]))
        rentedCar = self.carRental.rentCar(type_petrol)
        self.assertEqual(0, len(self.carRental.cars[type_petrol]))
        self.assertEqual(car, rentedCar)
        
	# this tests the receive payment functionality	
    def test_car_rental_receivePayment_method(self):
        self.assertEqual(0,self.carRental.getCashEarned())        
        self.carRental.receivePayment(250.75)
        self.assertEqual(250.75,self.carRental.getCashEarned())
        
if __name__ == '__main__':
	unittest.main()