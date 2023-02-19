from itertools import cycle
import math

def get_fare(source: str, destination: str) -> int:

    path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    bus_stops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI","CA" ]

    circular_list = cycle(list(zip(path,bus_stops)))
    distance = 0
    go_next = False

    if source.casefold() == destination.casefold():
        return "INAVLID OUTPUT"
    else:
        for item in circular_list:
            if item[1].casefold() == source.casefold():
                go_next = True
                continue
            if go_next:
                if item[1].casefold() != destination.casefold(): 
                        distance += item[0]
                        continue     
                distance += item[0]       
                cost = math.ceil(0.005* distance)         
                return f"{cost}.0 INR"            
source = input()
destination = input()
print(get_fare(source, destination))

