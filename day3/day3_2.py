'''
Advent of Code 2023
3rd Dec 2023
day3_2.py by GZ
'''

from itertools import product
import numpy as np

def part_numbers(schemes: np.array) -> list[int]:
    digits = '1234567890'
    numbers: list[int, list[tuple[int, int]]] = []
    m, n = len(schemes), len(schemes[0])
    for i, scheme in enumerate(schemes):
        j = 0
        while j < len(scheme):
            number = None
            if scheme[j] in digits:
                j_start = j
                number = scheme[j]
                j += 1
                while j < len(scheme) and scheme[j] in digits:
                    number += scheme[j]
                    j += 1
                numbers.append([int(number), list(product([i], range(j_start, j)))])              
            j += 1
        # if i < 5: print(f'row {i}:\n{numbers}')
    return numbers

def surrounding_numbers(schematic: np.array, i: int, j: int) -> tuple[int, int]:
    nums = []
    m, n = len(schematic), len(schematic[0])
    
    surrounding_positions = list(product(range(max(i-1, 0), min(i+2, m)), range(max(j-1, 0), min(j+2, n))))

    for number in part_numbers(schematic):
        if len(set(surrounding_positions) & set(number[1])) > 0 : #number = [number, [(coordinates)]]
            nums.append(number[0])
    
    return nums
                
def gear_ratios(schematic: np.array) -> list[int]:
    ratios = []
    numbers = '0123456789'
    for i,j in product(range(len(schematic)), range(len(schematic[0]))):
        if schematic[i, j] == '*':
            nums = surrounding_numbers(schematic, i, j)
            if len(nums) == 2:
                ratios.append(nums[0]*nums[1])

    return ratios          



if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        schematic = np.array([list(row) for row in input.read().split('\n')])
    with open('output_2.txt', 'w') as output:
        output.write(str(sum(gear_ratios(schematic))))

    