'''
Advent of Code 2023
14th Dec 2023
day14_2.py by GZ
'''

from itertools import product
from copy import deepcopy

def tilt(platform: list[list[str]], direction: str) -> None:
          
    if direction == 'up':
        for i, j in product(range(len(platform)), range(len(platform[0]))):
            if i > 0 and platform[i][j] == 'O' and platform[i-1][j] == '.':
                z = i
                while z > 0 and platform[z-1][j] == '.':
                    platform[z][j], platform[z-1][j] = platform[z-1][j], platform[z][j]
                    z -= 1
    
    if direction == 'down':
        for i, j in product(reversed(range(len(platform))), reversed(range(len(platform[0])))):
            if i < len(platform)-1 and platform[i][j] == 'O' and platform[i+1][j] == '.':
                z = i
                while z < len(platform)-1 and platform[z+1][j] == '.':
                    platform[z][j], platform[z+1][j] = platform[z+1][j], platform[z][j]
                    z += 1
    
    if direction == 'left':
        for i, j in product(range(len(platform)), range(len(platform[0]))):
            if j > 0 and platform[i][j] == 'O' and platform[i][j-1] == '.':
                z = j
                while z > 0 and platform[i][z-1] == '.':
                    platform[i][z], platform[i][z-1] = platform[i][z-1], platform[i][z]
                    z -= 1

    if direction == 'right':
        for i, j in product(reversed(range(len(platform))), reversed(range(len(platform[0])))):
            if j < len(platform[0])-1 and platform[i][j] == 'O' and platform[i][j+1] == '.':
                z = j
                while z < len(platform[0])-1 and platform[i][z+1] == '.':
                    platform[i][z], platform[i][z+1] = platform[i][z+1], platform[i][z]
                    z += 1


def get_load(platform: list[list[str]]) -> int:
    return (
        sum(len(platform)-i for i, j in product(range(len(platform)), range(len(platform[0]))) if platform[i][j] == 'O')
    )    


if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        platform = [list(row) for row in input.read().split('\n')]
    # sample = 'O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#....'
    # platform = [list(row) for row in sample.split('\n')]
    # print(sample, '\n\n')

    patterns = []
    pattern = platform

    counter = 0
    # for counter in range(10**9):
    while counter < 1000 and pattern not in patterns:
        patterns.append(pattern)
        # print('cycle', counter)
        # tilt(platform, h = 0, v = -1)
        tilt(platform, direction = 'up')
        # print('\n'.join([''.join(row) for row in platform]), end = '\n\n')
        # tilt(platform, h = -1, v = 0)
        tilt(platform, direction = 'left')
        # print('\n'.join([''.join(row) for row in platform]), end = '\n\n')
        # tilt(platform, h = 0, v = 1)
        tilt(platform, direction = 'down')
        # print('\n'.join([''.join(row) for row in platform]), end = '\n\n')
        # tilt(platform, h = 1, v = 0)
        tilt(platform, direction = 'right')
        #print('\n'.join([''.join(row) for row in platform]), end = '\n\n')
        pattern = '\n'.join([''.join(row) for row in platform])        
        # print(get_load(platform))
        counter += 1

    pattern_start = patterns.index(pattern)
    # print(pattern_start)
    # print(counter)
    # print(get_load([list(row) for row in patterns[99 + (10**9 - 99)%(135 - 99)].split('\n')]))

    with open('output_2.txt', 'w') as output:
        output.write(str(get_load(
                            [list(row) for row in 
                            patterns[pattern_start + (10**9 - pattern_start)%(counter - pattern_start)].split('\n')]
                        )
            )
        )