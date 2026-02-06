"""
The program uses the math module and several helper functions to determine
the greatest distance between two city bike stations in Helsinki, Finland.

The files are CSV files with values separated by semicolons.  While the files
contain other columns, the only data of importance are station names and
geographical coordinates.
"""

import math

def get_station_data(filename: str):
    stations = {}

    with open(filename) as new_file:
        for line in new_file:

            # Remove leading and trailing whitespaces
            line = line.strip()
            # The CSV splits the values by semicolon
            parts = line.split(';')
            # Skip the header line
            if parts[0] == "Longitude":
                continue
            # Add to the dictionary the station name as the key and the coordinates as a tuple
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
    
    return stations
    

def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]

    longitude2, latitude2 = stations[station2]

    # The multiplication factors are approximate values for converting
    # lat. and long. to distances in kilometers in the region of Helsinki, Finland
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations:dict):
    max_distance = 0
    # Convert the dictionary keys to a list
    station_names = list(stations.keys())
    result_station_pair = ("", "", 0)

    # Loop through pairs of stations to find the greatest distance between two stations
    # The inner loop looks at the next station after the one in the outer loop
    for i in range(len(station_names)):
        for j in range(i+1, len(station_names)):
            st1 = station_names[i]
            st2 = station_names[j]

            # Use helper function to calculate distance between the two stations
            current_distance = distance(stations, st1, st2)

            if current_distance > max_distance:
                max_distance = current_distance
                result_station_pair = (st1, st2, max_distance)
    
    return result_station_pair


def main():
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(f"Greatest distance between two stations: {greatest:.3f}km, between {station1} and {station2}")

if __name__ == "__main__":
    main()