import unittest

from car import Car, EngineCar, PetrolCar, DieselCar, ElectricCar, HybridCar

# Car test suite
# tests the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        
    # this tests the default constructors    
    def test_car_default_constructors(self):
        self.assertEqual('', self.car.reg) 
        self.assertEqual('', self.car.make)        
        self.assertEqual('', self.car.model)
        self.assertEqual('', self.car.colour) 
        self.assertEqual(0, self.car.mileage) 
        self.assertEqual(-1, self.car.type)

    # this tests the getters functionality
    def test_car_getters(self):    
        self.assertEqual('', self.car.getReg()) 
        self.assertEqual('', self.car.getMake())        
        self.assertEqual('', self.car.getModel())
        self.assertEqual('', self.car.getColour()) 
        self.assertEqual(0, self.car.getMileage()) 
        self.assertEqual(-1, self.car.getType())
        
    # this tests the setters functionality    
    def test_car_setters(self):
        self.car.setReg('151 D 10257')
        self.car.setMake('Mercedes')      
        self.car.setModel('e230')
        self.car.setColour('silver')
        self.car.setMileage(10000)
        self.car.setType(0)
        self.assertEqual('151 D 10257', self.car.getReg())
        self.assertEqual('Mercedes', self.car.getMake())        
        self.assertEqual('e230', self.car.getModel())
        self.assertEqual('silver', self.car.getColour())
        self.assertEqual(10000, self.car.getMileage())
        self.assertEqual(0, self.car.getType())
      
    # this tests the move car functionality
    def test_car_move_car_method(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.moveCar(500)
        self.assertEqual(500, self.car.getMileage())

# tests the engine car functionality
class TestEngineCar(TestCar):
    
    def setUp(self):
        self.car = EngineCar()
     
    # this tests the default constructor
    def test_engine_default_constructor(self):
        self.assertEqual(0, self.car.engine_size)
        
    # this tests the getter functionality   
    def test_engine_getter(self):    
        self.assertEqual(0, self.car.engine_size)   
        
    # this tests the setter functionality   
    def test_engine_setter(self):
        self.car.setEngine(1400)         
        self.assertEqual(1400, self.car.getEngine())        

# tests the petrol car functionality        
class TestPetrolCar(TestEngineCar):

    def setUp(self):
        self.car = PetrolCar()

    # this tests the default constructor
    def test_petrol_default_constructor(self):
        self.assertEqual('', self.car.petrol_type)
        
    # this tests the getter functionality   
    def test_petrol_getter(self):
        self.assertEqual('', self.car.getPetrol())
      
    # this tests the setter functionality      
    def test_petrol_setter(self):
        self.car.setPetrol('unleaded')
        self.assertEqual('unleaded', self.car.getPetrol())
 
# tests the diesel car functionality 
class TestDieselCar(TestEngineCar):
    
    def setUp(self):
        self.car = DieselCar()
        
    # this tests the default constructor    
    def test_diesel_default_constructor(self):
        self.assertEqual(False, self.car.has_turbo_enabled)  
     
    # this tests the getter functionality     
    def test_diesel_getter(self):    
        self.assertEqual(False, self.car.has_turbo_enabled)             
    
    # this tests the setter functionality    
    def test_diesel_setter(self):
        self.car.setTurbo(True)         
        self.assertEqual(True, self.car.getTurbo())

# tests the electric car functionality
class TestElectricCar(TestCar):
    
    def setUp(self):
        self.car = ElectricCar()
        
    # this tests the default constructor   
    def test_electric_default_constructor(self):
        self.assertEqual(0, self.car.fuel_cells)  
     
    # this tests the getter functionality 
    def test_electric_getter(self):    
        self.assertEqual(0, self.car.fuel_cells)       
     
    # this tests the setter functionality      
    def test_electric_setter(self):
        self.car.setFuelCells(2)         
        self.assertEqual(2, self.car.getFuelCells())        

# tests the hybrid car functionality        
class TestHybridCar(TestPetrolCar,TestElectricCar):
    
    def setUp(self):
        self.car = HybridCar()
        
    # this tests the default constructor    
    def test_hybrid_default_constructor(self):
        self.assertEqual(False, self.car.electric_brake_regeneration)  
        
    # this tests the getter functionality    
    def test_hybrid_getter(self):    
        self.assertEqual(False, self.car.electric_brake_regeneration) 
        
    # this tests the setter functionality   
    def test_hybrid_setter(self):
        self.car.setBrake(True)         
        self.assertEqual(True, self.car.getBrake())        


if __name__ == '__main__':
    unittest.main()
    