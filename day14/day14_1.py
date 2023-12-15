'''
Advent of Code 2023
14th Dec 2023
day14_1.py by GZ
'''

from itertools import product

def tilt(platform: list[list[str]]) -> None:
    for i, j in product(range(len(platform)), range(len(platform[0]))):
        if i > 0 and platform[i][j] == 'O' and platform[i-1][j] == '.':
            z = i
            while z > 0 and platform[z-1][j] == '.':
                platform[z][j], platform[z-1][j] = platform[z-1][j], platform[z][j]
                z -= 1

def get_load(platform: list[list[str]]) -> int:
    return (
        sum(len(platform)-i for i, j in product(range(len(platform)), range(len(platform[0]))) if platform[i][j] == 'O')
    )    


if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        platform = [list(row) for row in input.read().split('\n')]
        tilt(platform)
    with open('output_1.txt', 'w') as output:
        output.write(str(get_load(platform)))