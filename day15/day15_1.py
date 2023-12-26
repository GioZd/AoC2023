'''
Advent of Code 2023
15th Dec 2023
day15_1.py by GZ
'''

def hash2(string: str) -> int:
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        strings = input.read().strip('\n').split(',')
    with open('output_1.txt', 'w') as output:
        output.write(str(sum(hash2(string) for string in strings)))