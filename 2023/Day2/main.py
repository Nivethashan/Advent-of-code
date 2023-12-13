def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def check_eligible(arr, num):
    for i in arr:
        if i > num:
            return False
    return True

def find_max(arr):
    arr.sort(reverse = True)
    return arr[0]

def problem1(input_list):
    output = 0
    for index,game in enumerate(input_list):
        id_and_draws = game.split(":")
        draws = id_and_draws[1]
        draw_list = draws.split(" ")
        draw_list.remove("")
        blue = []
        green = []
        red = []
        for j, word in enumerate(draw_list):
            draw_list[j] = word.strip(";,")
            if draw_list[j] == "blue":
                blue.append(int(draw_list[j-1]))
            elif draw_list[j] == "green":
                green.append(int(draw_list[j-1]))
            elif draw_list[j] == "red":
                red.append(int(draw_list[j-1]))
        bred = check_eligible(red, 12)
        bgreen = check_eligible(green, 13)
        bblue = check_eligible(blue, 14)
        if bred and bgreen and bblue:
            output += index+1;
    return output

def problem2(input_list):
    output = 0
    for index, game in enumerate(input_list):
        id_and_draws = game.split(":")
        draws = id_and_draws[1]
        draw_list = draws.split(" ")
        draw_list.remove("")
        blue = []
        green = []
        red = []
        for j, word in enumerate(draw_list):
            draw_list[j] = word.strip(";,")
            if draw_list[j] == "blue":
                blue.append(int(draw_list[j - 1]))
            elif draw_list[j] == "green":
                green.append(int(draw_list[j - 1]))
            elif draw_list[j] == "red":
                red.append(int(draw_list[j - 1]))
        red_val = find_max(red)
        green_val = find_max(green)
        blue_val = find_max(blue)
        output += red_val * green_val * blue_val;
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n")
    print('Output 1:')
    print(problem1(input_list))
    print('Output 2:')
    print(problem2(input_list))
