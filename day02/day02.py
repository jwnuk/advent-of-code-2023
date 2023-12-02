"""
PART 1
The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
"""

games = []

with open('input.txt') as in_file:

    for line in in_file:

        start = line.find(':') + 1
        games.append(line[start:].strip())

for ix, game in enumerate(games):

    game_modified = []
    draw_dict = {'b': 0, 'g': 0, 'r': 0}
    colour_count = ''

    for ixx, char in enumerate(game):

        if char.isnumeric():
            colour_count += char

        elif char.isalpha() and not game[ixx - 1].isalnum():
            draw_dict[char] = int(colour_count)

        elif char == ',':
            colour_count = ''
        
        elif char == ';' or ixx == len(game) - 1:
            game_modified.append(draw_dict)
            colour_count = ''
            draw_dict = {'b': 0, 'g': 0, 'r': 0}

        elif not char.isalnum():
            continue

    games[ix] = game_modified

max_count = {'b': 14, 'g': 13, 'r': 12}
possible_sum = 0
impossible = False

for ix, game in enumerate(games):

    for draw in game:

        if draw['b'] > max_count['b'] or draw['g'] > max_count['g'] or draw['r'] > max_count['r']:

            impossible = True

    if impossible == False:

        possible_sum += ix + 1

    impossible = False

print(f'Possible number of games with limited cubes of each colour: {possible_sum}')


"""
PART 2
As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

power_of_sets = 0
cubes_per_game = {'b': [], 'g': [], 'r': []}

for game in games:
    
    for draw in game:

        for colour in cubes_per_game.keys():

            cubes_per_game[colour].append(draw[colour])

    power = max(cubes_per_game['b']) * max(cubes_per_game['g']) * max(cubes_per_game['r'])
    power_of_sets += power
    cubes_per_game = {'b': [], 'g': [], 'r': []}

print(f'Sum of power of cube sets: {power_of_sets}')