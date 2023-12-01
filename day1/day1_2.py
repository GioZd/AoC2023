'''
Advent of Code 2023
1 Dec 2023
day1_2.py by GZ
'''

with open('input.txt', 'r', encoding = 'utf8') as data:
    tasks = data.read().split('\n')

coordinates = []
digits = {'0', '1', '2', '3', '4', '5', '6', '7','8', '9'}
spelled_digits = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
                  'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

for string in tasks:
    first_digit: str | None = None
    last_digit: str | None = None
    lowest_first_occurrence = len(string)
    highest_first_occurrence = -1
    for digit in digits.union(spelled_digits.keys()):
        first_occurrence = string.find(digit)
        last_occurrence = string.rfind(digit)
        if first_occurrence >= 0 and first_occurrence < lowest_first_occurrence:
            lowest_first_occurrence = first_occurrence
            first_digit = digit if digit in digits else spelled_digits[digit]
        if last_occurrence > highest_first_occurrence:
            highest_first_occurrence = last_occurrence
            last_digit = digit if digit in digits else spelled_digits[digit]

    coordinates.append(int(first_digit + last_digit))

result = sum(coordinates)

with open('output_2.txt', 'w') as output:
    output.write(str(result))