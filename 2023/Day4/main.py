def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def scratch_cards(win_count_arr, copy_arr, total_point):
    for i in range(len(win_count_arr)):
        total_point += copy_arr[i]
        for j in range(1, win_count_arr[i]+1):
            copy_arr[i+j] += 1 * copy_arr[i]
    return total_point

def problem1(input_list):
    output = 0
    for game in input_list:
        game_list = game.split(":")
        num_list = game_list[1].split("|")
        win_num = num_list[0].split(" ")
        my_num = num_list[1].split(" ")
        while ("" in win_num):
            win_num.remove("")
        while ("" in my_num):
            my_num.remove("")
        win_count = 0
        for num in my_num:
            if num in win_num:
                win_count += 1
        if win_count > 0:
            output += pow(2, (win_count - 1))
    return output

def problem2(input_list):
    output = 0
    win_count_arr = []
    for game in input_list:
        game_list = game.split(":")
        num_list = game_list[1].split("|")
        win_num = num_list[0].split(" ")
        my_num = num_list[1].split(" ")
        while ("" in win_num):
            win_num.remove("")
        while ("" in my_num):
            my_num.remove("")
        win_count = 0
        for num in my_num:
            if num in win_num:
                win_count += 1
        win_count_arr.append(win_count)
    copy_arr = [1 for i in range(len(win_count_arr))]
    output = scratch_cards(win_count_arr, copy_arr, 0)
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n")
    print('Output 1:')
    print(problem1(input_list))
    print('Output 2:')
    print(problem2(input_list))
