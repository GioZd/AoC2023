'''
Advent of Code 2023
24th Dec 2023
day24_2.py by GZ
'''

import sympy as sym

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        coordinates = input.read().split('\n')
    
    coordinates = [row.split(' @ ') for row in coordinates]
    # row = ['px, py, pz', 'vx, vy, vz']
    coordinates = [[
                    list(map(float, pos.split(', '))), 
                    list(map(float, v.split(', ')))
                ] for pos, v in coordinates
    ]
    # row = [[px, py, pz], [vx, vy, vz]]
    coordinates = [row[0]+row[1] for row in coordinates]
    # row = [px, py, pz, vx, vy, vz]

    '''
    xs + vsx*t1 = x1 + v1x*t1
    ys + vsy*t1 = y1 + v1y*t1
    zs + vsz*t1 = z1 + v1z*t1
    xs + vsx*t2 = x2 + v2x*t2
    ys + vsy*t2 = y2 + v2y*t2
    zs + vsz*t2 = z2 + v2z*t2
    xs + vsx*t3 = x3 + v3x*t3
    ys + vsy*t3 = y3 + v3y*t3
    zs + vsz*t3 = z3 + v3z*t3 

    - 9 equations with 9 variables (xs, ys, zs, vsx, vsy, vsz, t1, t2, t3)
    - non-linear system
    - solvable with numeric methods within the sympy library
    '''
    x1, y1, z1 = coordinates[0][0], coordinates[0][1], coordinates[0][2]
    v1x, v1y, v1z = coordinates[0][3], coordinates[0][4], coordinates[0][5]
    x2, y2, z2 = coordinates[1][0], coordinates[1][1], coordinates[1][2]
    v2x, v2y, v2z = coordinates[1][3], coordinates[1][4], coordinates[1][5]
    x3, y3, z3 = coordinates[2][0], coordinates[2][1], coordinates[2][2]
    v3x, v3y, v3z = coordinates[2][3], coordinates[2][4], coordinates[2][5]

    xs, ys, zs, vsx, vsy, vsz, t1, t2, t3 = sym.symbols('xs,ys,zs,vsx,vsy,vsz,t1,t2,t3')
    equations = [sym.Eq(xs + vsx*t1, x1+v1x*t1), sym.Eq(ys + vsy*t1, y1+v1y*t1), sym.Eq(zs + vsz*t1, z1+v1z*t1)]
    equations += [sym.Eq(xs + vsx*t2, x2+v2x*t2), sym.Eq(ys + vsy*t2, y2+v2y*t2), sym.Eq(zs + vsz*t2, z2+v2z*t2)]
    equations += [sym.Eq(xs + vsx*t3, x3+v3x*t3), sym.Eq(ys + vsy*t3, y3+v3y*t3), sym.Eq(zs + vsz*t3, z3+v3z*t3)]
    result = sym.solve(equations, (xs, ys, zs, vsx, vsy, vsz, t1, t2, t3))
    x, y, z = result[0][0], result[0][1], result[0][2]
    with open('output_2.txt', 'w') as output:
        output.write(str(int(x+y+z)))




