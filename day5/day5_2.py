'''
Advent of Code 2023
5th Dec 2023
day4_2.py by GZ
'''

from itertools import chain

def get_closest_location(seedbook: str) -> int:
    stoi  = lambda v: [int(e) for e in v]
    seeds = stoi(seedbook[0][7:].split())
    # seeds = []
    # for i, seed in enumerate(seeds_tmp):
    #     if i%2 == 0:
    #         seeds.extend(range(seeds_tmp[i], seeds_tmp[i+1]))
    seed_to_soil = sorted([stoi(line.split()) for line in seedbook[3:25]], key = lambda r: r[0])
    soil_to_fertilizer = sorted([stoi(line.split()) for line in seedbook[27:55]], key = lambda r: r[0])
    fertilizer_to_water = sorted([stoi(line.split()) for line in seedbook[57:105]], key = lambda r: r[0])
    water_to_light = sorted([stoi(line.split()) for line in seedbook[107:145]], key = lambda r: r[0])
    light_to_temperature = sorted([stoi(line.split()) for line in seedbook[147:194]], key = lambda r: r[0])
    temperature_to_humidity = sorted([stoi(line.split()) for line in seedbook[196:236]], key = lambda r: r[0])
    humidity_to_location = sorted([stoi(line.split()) for line in seedbook[238:261]], key = lambda r: r[0])

    # def map_feature(source: int, maps: list[list[int, int, int]]) -> int:
    #     for maprow in maps:
    #         if source in range(maprow[1], maprow[1]+maprow[2]):
    #             return maprow[0] + (source - maprow[1])
    #     return source  

    def map_source(feature: int, maps: list[list[int, int, int]]) -> int:
        lower = 0
        upper = len(maps)-1
        mid = (lower+upper)//2
        maprow = maps[mid]
        while not (feature >= maprow[0] and feature < maprow[0]+maprow[2]) and lower<=upper:
            if feature < maprow[0]:
                upper = mid - 1
            if feature >= maprow[0]+maprow[2]:
                lower = mid + 1
            mid = (lower+upper)//2
            maprow = maps[mid]
        
        if feature >= maprow[0] and feature < maprow[0]+maprow[2]: # in range(maprow[0], maprow[0]+maprow[2]):
            return maprow[1] + feature - maprow[0]
        
        return feature
      
    # soils = [map_feature(seed, seed_to_soil) for seed in seeds]
    # print('soils mapped')
    # fertilizers = [map_feature(soil, soil_to_fertilizer) for soil in soils]
    # print('fertilizers mapped')
    # waters = [map_feature(fertilizer, fertilizer_to_water) for fertilizer in fertilizers]
    # print('waters mapped')
    # lights = [map_feature(water, water_to_light) for water in waters]
    # print('lights mapped')
    # temperatures = [map_feature(light, light_to_temperature) for light in lights]
    # print('temperatures mapped')
    # humidities = [map_feature(temperature, temperature_to_humidity) for temperature in temperatures]
    # print('humidities mapped')
    # locations = [map_feature(humidity, humidity_to_location) for humidity in humidities]
    # print('waters mapped')
    # # print(soils, fertilizers, locations, sep='\n')
    # return min(locations)
    loc = 0
    while loc < 200_000_000:
        hum = map_source(loc, humidity_to_location)
        temp = map_source(hum, temperature_to_humidity)
        light = map_source(temp, light_to_temperature)
        water = map_source(light, water_to_light)
        fert = map_source(water, fertilizer_to_water)
        soil = map_source(fert, soil_to_fertilizer)
        seed = map_source(soil, seed_to_soil)
        if any(seed >= seeds[i] and seed < seeds[i]+seeds[i+1] for i in range(0, len(seeds), 2)): 
            return loc
        if loc % 1E5 == 0: 
            print(loc, 'seeds checked')
        loc += 1

if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        seedbook = [line.strip() for line in input.readlines()]
    with open('output_2.txt', 'w') as output:
        output.write(str(get_closest_location(seedbook)))
        
