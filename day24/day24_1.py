'''
Advent of Code 2023
24th Dec 2023
day24_1.py by GZ
'''

import numpy as np
from itertools import combinations

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        coordinates = input.read().split('\n')
    
    x_min, x_max = 2E14, 4E14
    y_min, y_max = 2E14, 4E14
    coordinates = [row.split(' @ ') for row in coordinates]
    # row = ['px, py, pz', 'vx, vy, vz']
    coordinates = [[
                    list(map(float, pos.split(', '))), 
                    list(map(float, v.split(', ')))
                ] for pos, v in coordinates
    ]
    # row = [[px, py, pz], [vx, vy, vz]]
    coordinates = [[row[0][0], row[0][1], row[1][0], row[1][1]] for row in coordinates]
    # row = [px, py, vx, vy]

    n_intersections = 0
    for hailstone_1, hailstone_2 in combinations(coordinates, 2):
        # for each pair of hailstones solve the system of the
        # equations of their respective paths
        # y-y1 = v1y/v1x (x-x1)
        # y-y2 = v2y/v2x (x-x2)
        v1x, v1y =  hailstone_1[2], hailstone_1[3]
        v2x, v2y =  hailstone_2[2], hailstone_2[3]
        r1 = v1y/v1x # v1y/v1x
        r2 = v2y/v2x # v2y/v2x
        x1, y1 = hailstone_1[0], hailstone_1[1]
        x2, y2 = hailstone_2[0], hailstone_2[1]
        A = np.array([[r1, -1.0], [r2, -1.0]])
        b = np.array([r1*x1-y1, r2*x2-y2])
        if np.linalg.det(A) != 0:
            x,y = np.linalg.solve(A, b)
            if  all([
                x >= x_min, x <= x_max,
                y >= y_min, y <= y_max,
                x >= x1 if v1x >= 0 else x < x1,
                y >= y1 if v1y >= 0 else y < y1,
                x >= x2 if v2x >= 0 else x < x2,
                y >= y2 if v2y >= 0 else y < y2
                ]):
                n_intersections += 1

    with open('output_1.txt', 'w') as output:
        output.write(str(n_intersections))




