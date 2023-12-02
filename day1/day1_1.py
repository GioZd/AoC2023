'''
Advent of Code 2023
1st Dec 2023
day1_1.py by GZ
'''

def sum_coordinates(strings: list[str]) -> int:
    coordinates = []
    digits = "1234567890"
    for string in strings:
        numbers = [char for char in string if char in digits]
        coordinates.append(int(numbers[0]+numbers[-1]))
    return sum(coordinates)

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        strings = input.readlines()
    with open('output_1.txt', 'w') as output:
        output.write(str(sum_coordinates(strings)))
