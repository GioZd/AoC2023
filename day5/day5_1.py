'''
Advent of Code 2023
5th Dec 2023
day4_2.py by GZ
'''

def get_closest_location(seedbook: str) -> int:
    stoi  = lambda v: [int(e) for e in v]
    seeds = stoi(seedbook[0][7:].split())
    seed_to_soil = [stoi(line.split()) for line in seedbook[3:25]]
    soil_to_fertilizer = [stoi(line.split()) for line in seedbook[27:55]]
    fertilizer_to_water = [stoi(line.split()) for line in seedbook[57:105]]
    water_to_light = [stoi(line.split()) for line in seedbook[107:145]]
    light_to_temperature = [stoi(line.split()) for line in seedbook[147:194]]
    temperature_to_humidity = [stoi(line.split()) for line in seedbook[196:236]]
    humidity_to_location = [stoi(line.split()) for line in seedbook[238:261]]

    def map_feature(source: int, maps: list[list[int, int, int]]) -> int:
        for maprow in maps:
            if source in range(maprow[1], maprow[1]+maprow[2]):
                return maprow[0] + (source - maprow[1])
        return source  
      
    soils = [map_feature(seed, seed_to_soil) for seed in seeds]
    fertilizers = [map_feature(soil, soil_to_fertilizer) for soil in soils]
    waters = [map_feature(fertilizer, fertilizer_to_water) for fertilizer in fertilizers]
    lights = [map_feature(water, water_to_light) for water in waters]
    temperatures = [map_feature(light, light_to_temperature) for light in lights]
    humidities = [map_feature(temperature, temperature_to_humidity) for temperature in temperatures]
    locations = [map_feature(humidity, humidity_to_location) for humidity in humidities]
    print(soils, fertilizers, locations, sep='\n')
    return min(locations)

if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        seedbook = [line.strip() for line in input.readlines()]
    with open('output_1.txt', 'w') as output:
        output.write(str(get_closest_location(seedbook)))
        
