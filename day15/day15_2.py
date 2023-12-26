'''
Advent of Code 2023
15th Dec 2023
day15_2.py by GZ
'''

def hash2(string: str) -> int:
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current

def fix(lenses: list[str]) -> dict[int, list[tuple[str, int]]]:
    boxes = {i: [] for i in range(256)}
    for lens in lenses:
        if '-' in lens:
            label = lens.strip('-')
            for i, pair in enumerate(boxes[hash2(label)]):
                if pair[0] == label:
                    boxes[hash2(label)].remove(pair)
        if '=' in lens:
            substitution = False
            label = lens.split('=')[0]
            focus = lens.split('=')[1]
            for i, pair in enumerate(boxes[hash2(label)]):
                if pair[0] == label:
                    substitution = True
                    boxes[hash2(label)][i] = (label, int(focus))
            if not substitution:
                boxes[hash2(label)].append((label, int(focus)))
    return boxes
                    

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        lenses = input.read().strip('\n').split(',')
    boxes = fix(lenses)
    sumproduct = 0
    for key, values in boxes.items():
        for i, pair in enumerate(values):
            sumproduct += (key+1)*(i+1)*pair[1]

    with open('output_2.txt', 'w') as output:
        output.write(str(sumproduct))