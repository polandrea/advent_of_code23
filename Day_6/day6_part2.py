INPUT =  open("input.txt", "r")


def dist_dict(time):
    dict = {}
    for x in range(time+1):
        dict[x] = x * (time - x)
    return dict


def better_times(dict, dist):
    result = 0
    for time_key in dict:
        if dict[time_key] > dist:
            result += 1
    return result        


def main(input_list):
    lines = input_list.read().split('\n')
    times = lines[0].split(':')[1].split()
    distances = lines[1].split(':')[1].split()
    time = ''.join(times)
    distance = ''.join(distances)
    time_dict = dist_dict(int(time))
    good_options = better_times(time_dict, int(distance))
    print(good_options)


if __name__=='__main__':
    main(INPUT)
