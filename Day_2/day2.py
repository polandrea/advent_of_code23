INPUT =  open("input.txt", "r")
ALL_STONE = {'red': 12, 'green': 13, 'blue': 14 } 


def winning_match(match):
    for stones in match.split(','):
        key = stones.split()[1]
        if int(stones.split()[0]) > ALL_STONE[key]:
            return False
    return True


def winning_game(games):
    for matches in games:
        if not winning_match(matches):
            return False
    return True


def main(input_list):
    result = 0
    for line in input_list:
        game_num = line.split(':')[0].split()[1]
        games = line.split(':')[1].strip('\n').split(';')
        if winning_game(games):
            result += int(game_num)
    print(result) 


if __name__=='__main__':
    main(INPUT)
