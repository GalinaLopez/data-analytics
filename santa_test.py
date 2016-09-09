# Student name: Galina Lopez
# Student number: 10333429
# CA4: Helping Santa
# Module: Programming for Big Data

import unittest

from haversine import distance
from santa import *

# Santa test suite
# tests the distance method functionality
class TestDistance(unittest.TestCase):

    # this tests the distance method functionality 
	def test_distance_method(self):
		north_pole=(90,0)
		south_pole=(-90,0)
		pontianak_equator=(0,109.2)
		
		self.assertEqual(0, distance(north_pole,north_pole))
		self.assertEqual(20015, int(distance(north_pole, south_pole))) # cast to an int to get rid of floating point
		self.assertEqual(0, distance(pontianak_equator,pontianak_equator))

# tests the Santa methods functionality        
class TestSanta(unittest.TestCase):
    
    # this tests the shortest path method functionality 
    def test_shortest_path_method(self):	
        np = (90,0)
        sp = (-90,0)
        ind = (0,109.2)
        gl = (77,-15)
        ie = (53,-5)
        places = [np,sp]        
        self.assertEqual((np,0), shortest_path(np,places))        
        self.assertEqual(np, shortest_path(np,places)[0])
        self.assertEqual(0, shortest_path(np,places)[1])
        places = [sp]               
        self.assertEqual(sp, shortest_path(np,places)[0])
        self.assertEqual(20015, int(shortest_path(np,places)[1]))
        places = [np,sp]        
        self.assertEqual((sp,0), shortest_path(sp,places))        
        self.assertEqual(sp, shortest_path(sp,places)[0])
        self.assertEqual(0, shortest_path(sp,places)[1])
        places = [np]               
        self.assertEqual(np, shortest_path(sp,places)[0])
        self.assertEqual(20015, int(shortest_path(sp,places)[1]))
    
    # this tests the plan route method functionality     
    def test_plan_route_method(self):
        np = (90,0)
        sp = (-90,0)
        ind = (0,109.2)
        gl = (77,-15)
        ie = (53,-5)
        places = [np,sp,ind,gl,ie] 
        (route,distance,last_place,weight) = plan_route(np,places,{np:1,sp:1,ind:1,gl:1,ie:1},0,0,[])
        self.assertEqual(0, len(places))
        self.assertEqual(5, len(route)) 
        self.assertEqual([np,gl,ie,ind,sp], route)
        self.assertEqual(25749, int(distance))
        self.assertEqual(sp, last_place)
        self.assertEqual(5, weight)    
    
    # takes too long to run this test so I commented it out
    # this tests the process sleigh rides method functionality
    # def test_process_sleigh_rides_method(self):
        # import glob
        # sleigh_rides = []        
        # for file in glob.glob('gifts_[0-9]*.csv'):    
            # sleigh_rides.append(get_locations_and_weights(file))
        # distance = process_sleigh_rides(sleigh_rides)
        # self.assertEqual(32872144, int(distance))    
     
    # this tests the get locations and weights method functionality
    def test_get_locations_and_weights_method(self):
        filename = 'gifts_with_weight_lat_long_clusters1.csv'
        (locations,weights) = get_locations_and_weights(filename)        
        self.assertEqual(2, len(get_locations_and_weights(filename)))
        self.assertEqual(100000, len(locations))
        self.assertEqual(100000, len(weights))
    
    # this tests the split csv file method functionality
    def test_split_csv_file_method(self):
        filename = 'gifts_with_weight_lat_long_clusters1.csv'
        self.assertEqual(533, split_csv_file(filename))
		
if __name__ == '__main__':
	unittest.main()