'''
Advent of Code 2023
4th Dec 2023
day4_1.py by GZ
'''

def score(scratchcard: str) -> int:
    matches = set(scratchcard[10:40].split()) & set(scratchcard[42:117].split())
    return int(2**(len(matches)-1))

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        scratchcards = input.readlines()
    with open('output_1.txt', 'w') as output:
        output.write(str(sum(score(scratchcard) for scratchcard in scratchcards)))