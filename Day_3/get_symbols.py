import re

INPUT =  open("input.txt", "r")


def remove_nums(input_string):
    matched_strings = []
    pattern = r'\D+'
    matches = re.findall(pattern, input_string)
    matched_strings.extend(matches)
    return matched_strings


def put_in_set(string):
    set = {'*'}
    for char in string:
        set.add(char)
    return set


def main(input_list):
    all_symbol = {'@'}
    lines = input_list.read().split('\n')
    for line in lines:
        symbols = (remove_nums(line.replace('.', '')))
        for symbol in symbols:
            set = put_in_set(symbol)
            all_symbol = all_symbol.union(set)
    print(all_symbol)



if __name__=='__main__':
    main(INPUT)
