INPUT =  open("input.txt", "r")


def get_diff_list(list):
    new_list = []
    for x in range(len(list)):
        if len(list) > x+1:
            num = (list[x+1] - list[x])
            new_list.append(num)
    return(new_list)        

def get_prev_num(diff_list):
    diff_list.reverse()
    next = 0
    for list in diff_list:
        next = list[0] - next
    return(next)


def main(input_list):
    result = 0
    lines = input_list.read().split('\n')
    for list in lines:
        end_list = []
        num_list = [int(x) for x in list.split()]
        end = []
        while end != num_list:
            end_list.append(num_list)
            num_list = get_diff_list(num_list)
            end = [0 for _ in range(len(num_list))]
        next_num = get_prev_num(end_list)
        result += next_num
    print(result)


if __name__=='__main__':
    main(INPUT)
    
