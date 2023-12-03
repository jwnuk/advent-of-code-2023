"""
PART 1
There are lots of numbers and symbols you don't really understand, but apparently any number 
adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)
What is the sum of all of the part numbers in the engine schematic?
"""

from string import punctuation

schematic = []

with open('input.txt') as in_file:

    for line in in_file:
        
        schematic.append(list(line.strip()))

symbols = list(punctuation)
symbols.remove('.')


def check_for_symbols(char: str, jx: int, curr_line: list, prev_line: list, next_line: list):

    # print(f'\nSearching for char :{char}')

    if jx == 0:
        search_range = range(0, 2)

    elif jx == len(line) - 1:
        search_range = range(-1, 1)

    else:
        search_range = range(-1, 2)
    
    # print(list(search_range))

    for j in search_range:

        if prev_line[jx + j] in symbols or curr_line[jx + j] in symbols or next_line[jx + j] in symbols:
            # print('Symbol found')
            return True
        
        else:
            pass
            # print('No matching symbol')

    if char.isnumeric() and jx != len(curr_line) - 1 and curr_line[jx + 1].isnumeric():
        # print('Looking for symbol for next char')
        return check_for_symbols(curr_line[jx + 1], jx + 1, curr_line, prev_line, next_line)
    
    return False

parts_sum = 0

for ix, line in enumerate(schematic):
    
    part_num = ''
    curr_line = line
    adj_symbol = False

    if ix == 0:
        print('first line')
        prev_line = ['.' for _ in range(len(line))]
        next_line = schematic[ix + 1]

    elif ix == len(schematic) - 1:
        print('last line')
        prev_line = schematic[ix - 1]
        next_line = ['.' for _ in range(len(line))]

    else:
        print(f'middle line, index {ix}')
        prev_line = schematic[ix - 1]
        next_line = schematic[ix + 1]

    print(line)

    for jx, char in enumerate(curr_line):
        
        if not char.isnumeric():
            # print(part_num)
            adj_symbol = False
            part_num = ''

        elif char.isnumeric() and adj_symbol == True:
            part_num += char

        elif char.isnumeric():
            adj_symbol = check_for_symbols(char, jx, curr_line, prev_line, next_line)
    
            # print(char, adj_symbol, '\n')

            if adj_symbol:
                part_num += char

        if char.isnumeric() and (jx == len(curr_line) - 1 or not curr_line[jx + 1].isnumeric()) and adj_symbol:
            print(part_num)
            parts_sum += int(part_num)
            adj_symbol = False

print(parts_sum)