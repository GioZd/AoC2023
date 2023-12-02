'''
Advent of Code 2023
1st Dec 2023
day1_2.py by GZ
'''

digits = {'0', '1', '2', '3', '4', '5', '6', '7','8', '9'}
spelled_digits = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
                  'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def get_first_digit(string: str) -> int:
    global digits, spelled_digits
    lowest_first_occurrence = len(string)
    first_digit: str | None = None
    for digit in digits.union(spelled_digits.keys()):
        first_occurrence = string.find(digit)

        if first_occurrence >= 0 and first_occurrence < lowest_first_occurrence:
                    lowest_first_occurrence = first_occurrence
                    first_digit = digit if digit in digits else spelled_digits[digit]
    
    return first_digit

def get_last_digit(string: str) -> int:
    global digits, spelled_digits
    highest_last_occurrence = -1
    last_digit: str | None = None
    for digit in digits.union(spelled_digits.keys()):
        last_occurrence = string.rfind(digit)

        if last_occurrence > highest_last_occurrence:
                highest_last_occurrence = last_occurrence
                last_digit = digit if digit in digits else spelled_digits[digit]

    return last_digit

def sum_coordinates(strings: list[str]) -> int:
    return (
        sum ( 
            int(get_first_digit(string) + get_last_digit(string)) 
            for string in strings
        )
    )

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as data:
        strings = data.readlines()
    with open('output_2.txt', 'w') as output:
        output.write(str(sum_coordinates(strings)))
