'''
Advent of Code 2023
3rd Dec 2023
day3_1.py by GZ
'''

# 467..114..        [[467, [(0, 0), (0, 1), (0, 2)]], [114, [(0, 5), (0, 6), (0, 7)]]]
# ...*......    ->  []
# ..35..633.        [[35, [(2, 2), (2, 3)]], [663, [(2, 6), (2, 7), (2, 8)]]]

from itertools import product

def part_numbers(schemes: list[str]) -> list[int]:
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

    part_numbers_list = []

    for number, positions in numbers:
        surrounding_chars = set()
        for i, j in positions:
            if i != 0:
                surrounding_chars.add(schemes[i-1][j])
            if i < m - 1:
                surrounding_chars.add(schemes[i+1][j])
            
            if positions[0][1] != 0:
                surrounding_chars.add(schemes[i][j-1])
            if positions[-1][1] < n - 1:
                surrounding_chars.add(schemes[i][j+1])

            if positions[0][1] != 0 and i != 0:
                surrounding_chars.add(schemes[i-1][j-1])
            if positions[0][1] != 0 and i < m - 1:
                surrounding_chars.add(schemes[i+1][j-1])
            if positions[-1][1] < n - 1 and i != 0:
                surrounding_chars.add(schemes[i-1][j+1])
            if positions[-1][1] < n - 1 and i < m - 1:
                surrounding_chars.add(schemes[i+1][j+1])

        surrounding_chars.difference_update(set(digits), {'\n'})

        # if number % 5 == 0:
        #     print(
        #         f'number: {number}\n'
        #         f'positions: {positions}\n'
        #         f'surrounding: {surrounding_chars}\n'
        #     )

        if surrounding_chars > {'.'}:
            part_numbers_list.append(number)

    # print(part_numbers_list)
    # print(sum(part_numbers_list))

    return part_numbers_list


if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        schemes = input.readlines()
    with open('output_1.txt', 'w') as output:
        output.write(str(sum(part_numbers(schemes))))