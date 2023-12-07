'''
Advent of Code 2023
6th Dec 2023
day6_1.py by GZ
'''

from math import sqrt, prod

def permutations(records: list[tuple[int, int]]) -> int:
    int_diff = lambda t, d: int(t/2 + sqrt(t**2-4*d)/2) - int(t/2 - sqrt(t**2-4*d)/2)
    n_solutions = lambda t, d: int_diff(t, d) - 1 if int(t/2 + sqrt(t**2-4*d)/2) == (t/2 + sqrt(t**2-4*d)/2) else int_diff(t, d)
    print(n_solutions(55, 246))
    return prod(n_solutions(time, distance) for time, distance in records)

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        records = input.read().split('\n')
        time = [int(t) for t in records[0][12:].split()]
        distance = [int(d) for d in records[1][12:].split()]

    print(time, distance)
    with open('output_1.txt', 'w') as output:
        output.write(str(permutations(zip(time, distance))))