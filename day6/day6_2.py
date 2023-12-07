'''
Advent of Code 2023
6th Dec 2023
day6_2.py by GZ
'''

from math import sqrt

def n_solutions(time: int, distance: int) -> int:
    int_diff = lambda t, d: int(t/2 + sqrt(t**2-4*d)/2) - int(t/2 - sqrt(t**2-4*d)/2)
    return (
        int_diff(time, distance) - 1 
        if int(time/2 + sqrt(time**2-4*distance)/2) == (time/2 + sqrt(time**2-4*distance)/2)
        else int_diff(time, distance)
    )

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        records = input.read().split('\n')
        time = int(records[0][12:].replace(' ', ''))
        distance = int(records[1][12:].replace(' ', ''))

    print(time, distance)
    with open('output_2.txt', 'w') as output:
        output.write(str(n_solutions(time, distance)))