INPUT =  open("input.txt", "r")


def biggest_stones(games):
    biggest_dict = {'red': 0, 'green': 0, 'blue': 0 }
    for matches in games:
        for stones in matches.split(','):
            key = stones.split()[1]
            if int(stones.split()[0]) > biggest_dict[key]:
                biggest_dict[key] = int(stones.split()[0])  
    return biggest_dict


def power_of_set(dict):
    power = 1
    for stone in dict:
        power *= dict[stone]
    return power


def main(input_list):
    result = 0
    for line in input_list:
        games = line.split(':')[1].strip('\n').split(';')
        set_dict =  biggest_stones(games)
        set_power = power_of_set(set_dict)
        result += set_power
    print(result)


if __name__=='__main__':
    main(INPUT)
