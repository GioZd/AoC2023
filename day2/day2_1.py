'''
Advent of Code 2023
2nd Dec 2023
day1_1.py by GZ
'''

def ids(games: list[str]) -> list[int]:
    constraints = {'red':12, 'green': 13, 'blue': 14}
    valid_ids = []

    # First step:
    # games = {
    #   1: {
    #       'red': max({3, 3, 2, 1, 2}),
    #       'green': max({3, 1, 12, 5, 7}),
    #       'blue': max({1, 3, 7, 4, 2})
    #   }
    #   2: {...}
    #   ...
    # }

    games = [game.split(': ') for game in games]
    games = {int(id.split()[1]): draws for id, draws in games}
    for id, draws in games.items():
        games[id] = [draw.split() for draw in draws.replace('; ', ', ').split(', ')]
        summary = {
            colour: max(
                int(n_cubes) for n_cubes, cube_colour in games[id] 
                if colour in cube_colour
            ) 
            for colour in ['red', 'green', 'blue']
        }
        games[id] = summary
    
    # Second step:
    # check validity game by game

    for id, summary in games.items():
        if all(summary[colour] <= constraints[colour] for colour in ['red', 'green', 'blue']):
            valid_ids.append(id)

    return valid_ids          

if __name__ == '__main__':
    with open('input.txt', 'r', encoding = 'utf8') as input:
        games = input.readlines()
    with open('output_1.txt', 'w') as output:
        output.write(str(sum(ids(games))))
