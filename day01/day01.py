"""
PART 1
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
Consider your entire calibration document. What is the sum of all of the calibration values?
"""

lines = []
calibration_sum = 0

with open('input.txt') as input_file:
    for line in input_file:
        lines.append(line.strip())
        calibration_val = ''

        for char in line:
        
            if char.isnumeric():
                calibration_val += char
        
        calibration_val = int(calibration_val[0] + calibration_val[-1])
        calibration_sum += calibration_val

print(calibration_sum)

"""
PART 2
It looks like some of the digits are actually spelled out with letters: one, two, c also count as valid "digits".
What is the sum of all of the calibration values?
"""

calibration_sum_2 = 0

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for line in lines:
    calibration_val = ''

    for key in digits.keys():
        line = line.replace(key, key + digits[key] + key)

    # for key in digits.keys():
    #     if line.find(key) > -1:
    #         print(line, key)
    #         line = line[:line.find(key)] + digits[key] + line[line.find(key) + 1:]
    
    for char in line:

        if char.isnumeric():
            calibration_val += char
    
    # print(calibration_val)
    calibration_val = int(calibration_val[0] + calibration_val[-1])
    print(line, line, calibration_val, '\n')
    calibration_sum_2 += calibration_val

print(calibration_sum_2)

