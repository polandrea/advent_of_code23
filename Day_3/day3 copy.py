import re

INPUT =  open("input.txt", "r")
SYMBOLS = ['+', '@', '$', '/', '%', '=', '&', '*', '-', '#']


def find_nums(input_string):
    matched_strings = []
    pattern = r'\d+'
    matches = re.findall(pattern, input_string)
    matched_strings.extend(matches)
    return matched_strings
            

def is_symbol_neighbour(num, lines, row):
    index = lines[row].find(num)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for x in range(len(num)):
        for dx, dy in directions:
                new_x, new_y = row + dx, index + dy
                if 0 <= new_x < len(lines) and 0 <= new_y < len(lines[0]) and lines[new_x][new_y] in SYMBOLS:
                    return True
        index += 1
    return False


def main(input_list):
    result = 0
    lines = input_list.read().split('\n')
    lenght = len(lines)
    for x in range(lenght):
        nums = find_nums(lines[x])
        for num in nums:
            print(num)
            print(is_symbol_neighbour(num, lines, x))
            if is_symbol_neighbour(num, lines, x):
                result += int(num)
    print(result)
            

if __name__=='__main__':
    main(INPUT)
