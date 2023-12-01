'''
Advent of Code 2023
1 Dec 2023
day1_1.py by GZ
'''

with open('input.txt', 'r', encoding = 'utf8') as data:
    tasks = data.read().split('\n')
    
coordinates = []
digits = "1234567890"
for string in tasks:
    numbers = [char for char in string if char in digits]
    coordinates.append(int(numbers[0]+numbers[-1]))

result = sum(coordinates)

with open('output_1.txt', 'w') as output:
    output.write(str(result))
