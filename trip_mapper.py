north_pole = (90,0)

import pandas as pd
import numpy as np
from haversine import distance 

def create_gift_dict(gift_id, latitude, longitude):
    return {'GiftId': gift_id, 'Latitude': latitude, 'Longitude': longitude}

def find_closest(area, current_point):
    return min(area, key=lambda x:(distance((x['Latitude'], x['Longitude']), current_point)))

def get_point_tuple(gift):
    return (gift['Latitude'], gift['Longitude'])

def find_close_by(areas, values, index, clusters, close_by):
    current_points = (values['Latitude'][index], values['Longitude'][index])
    gift = {'GiftId': values['GiftId'][index],'Latitude': values['Latitude'][index],'Longitude': values['Longitude'][index]}
    for index, area in enumerate(areas[str(close_by)]):
        if distance(current_points, (area[0]['Latitude'], area[0]['Longitude'])) <= close_by:
            area.append(gift)
            clusters[str(close_by)].append(index)
            return
    clusters[str(close_by)].append(len(areas))
    areas[str(close_by)].append([gift])

def get_areas(gift):
    print gifts.columns.values
    areas = {} 
    clusters = {}
    clusters['500'] = []
    areas['500'] = []
    clusters['1000'] = []
    areas['1000'] = []
    values = {}
    values['GiftId'] = gifts.GiftId.tolist()
    values['Latitude'] = gifts.Latitude.tolist()
    values['Longitude'] = gifts.Longitude.tolist()
    values['Weight'] = gifts.Weight.tolist()
    distance_from_north_pole(values, gifts)
    for index, gift_id in enumerate(values['GiftId']): #index 8
        find_close_by(areas, values, index, clusters, 500)
    for index, gift_id in enumerate(values['GiftId']): #index 9
        find_close_by(areas, values, index, clusters, 1000)
    for index, gift_id in enumerate(values['GiftId']): #index 10 in excel file
        find_close_by(areas, values, index, clusters, 400)
    for value in clusters.keys():
        gifts['close_by_' + value] = clusters[value]
    return areas

def distance_from_north_pole(values, gifts):
    distances = []
    latitude_num = []
    longitude_num = []
    for index, gift_id in enumerate(values['GiftId']):
        current_points = (values['Latitude'][index], values['Longitude'][index])
        distance_to_north_pole = distance(current_points, north_pole)
        print distance_to_north_pole
        distances.append(distance_to_north_pole)
        latitude_num.append(int(current_points[0]))
        longitude_num.append(int(current_points[1]))
    gifts['distance_to_np'] = distances
    gifts['latitude_num'] = latitude_num 
    gifts['longitude_num'] = longitude_num 

if __name__ == "__main__":
    gifts = pd.read_csv('gifts.csv')
    areas = get_areas(gifts)
    print(len(areas))
    value = ''
    weights = gifts.groupby('close_by_500').Weight.sum()
    print weights
    for value in areas.keys():
        for index, area in enumerate(areas[value]):
            value += str(len(area)) + ', '
            print(find_closest(area, north_pole))

    print value

    gifts.to_csv('gifts_with_weight_lat_long_clusters.csv')
