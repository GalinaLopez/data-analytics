# Car functionality
class Car(object):
    
    # initialising default constructors
    def __init__(self):
        self.reg = ''
        self.make = ''
        self.model = '' 
        self.colour = ''
        self.mileage = 0
        self.type = -1

    # adding getters to my car
    def getReg(self):
        return self.reg
        
    def getMake(self):
        return self.make
        
    def getModel(self):
        return self.model
        
    def getColour(self):
        return self.colour
        
    def getMileage(self):
        return self.mileage    

    def getType(self):
        return self.type     
     
    # adding setters to my car
    def setReg(self, reg):
        self.reg = reg
        
    def setMake(self, make):
        self.make = make
        
    def setModel(self, model):
        self.model = model  

    def setColour(self, colour):
        self.colour = colour
        
    def setMileage(self, mileage):
        self.mileage = mileage
        
    def setType(self, type):
        self.type = type
      
    # adding the move car to my car
    def moveCar(self, miles):
        print 'Car moved', miles, 'miles.'
        self.mileage += miles
 
# Engine Car functionality  
class EngineCar(Car):

    # initialising default constructor
    def __init__(self):
        Car.__init__(self) # to avoid overwriting superclass __init__ method ie Car.__init__
        self.engine_size = 0 
     
    # adding getter and setter to my engine car
    def getEngine(self):
        return self.engine_size
        
    def setEngine(self, engine_size):
        self.engine_size = engine_size

# Petrol Car functionality
class PetrolCar(EngineCar):

    # initialising default constructor
    def __init__(self):
        EngineCar.__init__(self)
        self.petrol_type = ''
    
    # adding getter and setter to my petrol car
    def getPetrol(self):
        return self.petrol_type

    def setPetrol(self, petrol_type):
        self.petrol_type = petrol_type

# Diesel Car functionality
class DieselCar(EngineCar):
    
    # initialising default constructor
    def __init__(self):
        EngineCar.__init__(self)
        self.has_turbo_enabled = False
     
    # adding getter and setter to my diesel car
    def getTurbo(self):
        return self.has_turbo_enabled
        
    def setTurbo(self, has_turbo_enabled):
        self.has_turbo_enabled = has_turbo_enabled

# Electric Car functionality        
class ElectricCar(Car):

    # initialising default constructor
    def __init__(self):
        Car.__init__(self)
        self.fuel_cells = 0
     
    # adding getter and setter to my electric car
    def getFuelCells(self):
        return self.fuel_cells
        
    def setFuelCells(self, fuel_cells):
        self.fuel_cells = fuel_cells        
    
# Hybrid Car functionality        
class HybridCar(PetrolCar,ElectricCar):

    # initialising default constructor
    def __init__(self):
        ElectricCar.__init__(self)
        PetrolCar.__init__(self)
        self.electric_brake_regeneration = False
     
    # adding getter and setter to my hybrid car
    def getBrake(self):
        return self.electric_brake_regeneration
        
    def setBrake(self, electric_brake_regeneration):
        self.electric_brake_regeneration = electric_brake_regeneration
