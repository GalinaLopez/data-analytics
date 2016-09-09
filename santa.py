# Student name: Galina Lopez
# Student number: 10333429
# CA4: Helping Santa
# Module: Programming for Big Data

from haversine import distance

location = ()
#open a file and process it for reading the lines and putting into buckets
def split_csv_file(file_name):
    fhand = open(file_name)
    my_buckets = {}
    fhand.readline()
    for line in fhand:
        line = line.rstrip()
        giftsList = line.split(',')        
        location = (float(giftsList[2]),float(giftsList[3]))         
        if giftsList[8] not in my_buckets:
            my_buckets[giftsList[8]] = []
        my_buckets[giftsList[8]].append(line)
        # index can be changed to 10 to get grouping close_by_400 added to the trip_mapper.py file
        # if giftsList[10] not in my_buckets:
            # my_buckets[giftsList[10]] = []
        # my_buckets[giftsList[10]].append(line)
    print len(my_buckets)
    # I have my buckets
    for key in my_buckets.keys():
        current_file = open('gifts_' + key + '.csv', 'w')
        for line in my_buckets[key]:
            current_file.write(line + '\n')
        current_file.close()
    return len(my_buckets) # added for unit testing the code
    
#get list of locations and dictionary of weights
def get_locations_and_weights(file_name):
    locations = []
    weights = {}
    fhand = open(file_name)
    for line in fhand:
        line = line.rstrip()
        giftsList = line.split(',')        
        location = (float(giftsList[2]),float(giftsList[3]))        
        locations.append(location)
        weights[location] = float(giftsList[4])        
    return (locations,weights) #return a tuple with list of locations and dictionary of weights
    

np = (90,0)
#process each sleight ride in the list of sleigh rides
def process_sleigh_rides(sleigh_rides):
    route = []
    total_distance = 0
    total_weight = 0
    current_place = np
    for sleigh_ride in sleigh_rides:        
        places = sleigh_ride[0]
        weights = sleigh_ride[1]        
        the_route = plan_route(current_place, places, weights, total_weight, total_distance, route)        
        route = the_route[0]
        total_distance = the_route[1] # last total distance
        current_place = the_route[2] # last current_place
        total_weight = the_route[3] # last total weight         
    return total_distance
 
#find the nearest location from a list of locations
def shortest_path(current_place,places):
    nearest_distance = 22000
    nearest_place = None
    for place in places:        
        try:
            place_distance = distance(current_place, place)
        except:
            place_distance = nearest_distance
        if place_distance < nearest_distance:
            nearest_distance = place_distance
            nearest_place = place        
    return (nearest_place, nearest_distance)
          
current_place = np

#plan the shortest route from given location to all locations in the list of places
def plan_route(current_place, places, weights, total_weight, total_distance, route):    
    while len(places) > 0:        
        the_place = shortest_path(current_place,places)        
        total_weight += weights[the_place[0]]              
        # taking into account sleight weight - 10kg so total_weight of gifts must be <= 990
        if total_weight <= 990:
            current_place = the_place[0]
            route.append(current_place)
            places.remove(current_place)
            total_distance += the_place[1]
        else:             
            total_distance += distance(current_place, np)             
            current_place = np
            total_weight = 0 
        print total_distance
    return (route, total_distance, current_place, total_weight)
    
if __name__ == '__main__':
    
    #read and split csv file into 533 new csv files
    split_csv_file('gifts_with_weight_lat_long_clusters.csv')

    #import files one at a time and put them in a list of sleigh rides
    import glob

    sleigh_rides = []
    for file in glob.glob('gifts_[0-9]*.csv'):    
        sleigh_rides.append(get_locations_and_weights(file))
        
    #process sleigh rides and print result
    print process_sleigh_rides(sleigh_rides)

    # result: 32873361.6696


