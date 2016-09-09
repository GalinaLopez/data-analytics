from car import *

# Customer functionality
class Customer(object):

    # initialising default constructors
    def __init__(self):
        self.car = None
        self.id = ''
        self.name = ''
        self.cash_spend = 0
    
    # adding getters to my customer
    def getCar(self):
        return self.car
            
    def getId(self):
        return self.id
        
    def getName(self):
        return self.name
        
    def getCashSpend(self):
        return self.cash_spend 
     
    # adding setters to my customer
    def setId(self, id):
        self.id = id
        
    def setName(self, name):
        self.name = name
        
    def setCashSpend(self, cash_spend):
        self.cash_spend = cash_spend
    
    # adding rent car to my customer
    def rentCar(self,car):
        self.car = car

    # adding return car to my customer
    def returnCar(self):
        car=self.car
        self.car=None
        return car  
    
    # adding make payment to my customer
    def makePayment(self,amount):
        self.cash_spend += amount
    
    # adding move car to my customer    
    def moveCar(self, car, miles):
        car.moveCar(miles)

# Car Rental functionality        
class CarRental(object):

    # initialising default constructors
    def __init__(self):
        self.customers = []
        self.cars = []        
        self.cars.append([])
        self.cars.append([])
        self.cars.append([])
        self.cars.append([])
        self.cash_earned = 0              
    
    # adding getter to my car rental 
    def getCashEarned(self):
        return self.cash_earned 
     
    # adding setter to my car rental 
    def setCashEarned(self, cash_earned):
        self.cash_earned = cash_earned
    
    # adding customer to my car rental 
    def addCustomer(self,customer):
        self.customers.append(customer)
    
    # adding getting customer to my car rental 
    def getCustomer(self,id):
        return self.customers[id]      
       
    # adding rent car to my car rental 
    def rentCar(self,type):
        if len(self.cars[type])==0:
            print "Sorry no car of that type to rent. Try again."
            return None
        return self.cars[type].pop()

    # adding return car to my car rental 
    def returnCar(self,type,car):
        self.cars[type].append(car)
       
    # adding receive payment to my car rental 
    def receivePayment(self,amount):
        self.cash_earned += amount
        
