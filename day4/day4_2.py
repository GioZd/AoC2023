'''
Advent of Code 2023
4th Dec 2023
day4_2.py by GZ
'''

def score(scratchcard: str) -> int:
    matches = set(scratchcard[10:40].split()) & set(scratchcard[42:117].split())
    return len(matches)

def scratch_scratchcards(scratchcards: list[str]) -> int:
    wins = {i: 1 for i in range(len(scratchcards))}
    for i in range(len(scratchcards)):
        for j in range(score(scratchcards[i])):
            if i+j+1 < len(scratchcards):
                wins[i+j+1] += wins[i]

    return sum(wins.values())


if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        scratchcards = input.readlines()
    with open('output_2.txt', 'w') as output:
        output.write(str(scratch_scratchcards(scratchcards)))