'''
Advent of Code 2023
9th Dec 2023
day9_1+2.py by GZ
'''


def prediction(history: list[int]) -> int:
    reduce = lambda v: [v[i+1]-v[i] for i in range(len(v)-1)]
    return (
        0 if all(value == 0 for value in history)
        else history[-1] + prediction(reduce(history))
    )

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        histories = [
            [int(value) for value in history.split()] 
            for history in input.read().split('\n')
        ]
    with open('output_1.txt', 'w') as output:
        output.write(str(sum(prediction(history) for history in histories)))
    with open('output_2.txt', 'w') as output:
        output.write(str(sum(prediction(history[::-1]) for history in histories)))