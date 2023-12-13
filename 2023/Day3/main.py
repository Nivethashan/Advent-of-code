def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def array_2d(input_list):
    if len(input_list) <= 0:
        return [[]]
    arr = [[0] * len(input_list[0]) for i in range(0, len(input_list))]
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[i])):
            arr[i][j] = input_list[i][j]
    return arr

def get_full_number(arr, row, col):
    str_num = arr[row][col]
    skip = 0
    for i in range(col + 1,len(arr[row])):
        if arr[row][i].isdigit():
            str_num = str_num + arr[row][i]
            skip = skip + 1
        else:
            break
    for i in range(col - 1, -1, -1):
        if arr[row][i].isdigit():
            str_num = arr[row][i] + str_num
        else:
            break
    return str_num, skip

def problem1(input_list):
    output = 0
    arr = array_2d(input_list)
    for row in range(0, len(arr)):
        skip = 0
        for col in range(0, len(arr[row])):
            str_num = ""
            if skip != 0:
                skip = skip - 1
                continue
            if arr[row][col].isdigit():
                if col > 0 and not(arr[row][col-1].isdigit()) and arr[row][col-1] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                elif row > 0 and col > 0 and not(arr[row-1][col-1].isdigit()) and arr[row-1][col-1] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                elif row > 0 and not(arr[row-1][col].isdigit()) and arr[row-1][col] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                elif row > 0 and col < len(arr[0])-1 and not(arr[row-1][col+1].isdigit()) and arr[row-1][col+1] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                elif col < len(arr[0])-1 and not(arr[row][col+1].isdigit()) and arr[row][col+1] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                elif row < len(arr)-1 and col < len(arr[0])-1 and not(arr[row+1][col+1].isdigit()) and arr[row+1][col+1] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                elif row < len(arr)-1 and not(arr[row+1][col].isdigit()) and arr[row+1][col] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                elif row < len(arr)-1 and col > 0 and not(arr[row+1][col-1].isdigit()) and arr[row+1][col-1] != ".":
                    str_num, skip = get_full_number(arr, row, col)
                if str_num != "":
                    output += int(str_num)
    return output

def problem2(input_list):
    output = 0
    arr = array_2d(input_list)
    for row in range(0, len(arr)):
        for col in range(0, len(arr[row])):
            str_num_list = []
            count = 0
            skip = 0
            if arr[row][col] == "*":
                if col > 0 and  arr[row][col - 1].isdigit():
                    str_num, skip = get_full_number(arr, row, col-1)
                    str_num_list.append(str_num)
                if row > 0 and col > 0 and arr[row - 1][col - 1].isdigit():
                    str_num, skip = get_full_number(arr, row-1, col-1)
                    str_num_list.append(str_num)
                if skip == 0:
                    if row > 0 and arr[row - 1][col].isdigit():
                        str_num, skip = get_full_number(arr, row-1, col)
                        str_num_list.append(str_num)
                else:
                    skip = skip - 1
                if skip == 0:
                    if row > 0 and col < len(arr[0]) - 1 and arr[row - 1][col + 1].isdigit():
                        str_num, skip = get_full_number(arr, row-1, col+1)
                        str_num_list.append(str_num)
                else:
                    skip = skip - 1
                if col < len(arr[0]) - 1 and arr[row][col + 1].isdigit():
                    str_num, skip = get_full_number(arr, row, col+1)
                    str_num_list.append(str_num)
                skip = 0
                if row < len(arr) - 1 and col > 0 and arr[row + 1][col - 1].isdigit():
                    str_num, skip = get_full_number(arr, row+1, col-1)
                    str_num_list.append(str_num)
                if skip == 0:
                    if row < len(arr) - 1 and arr[row + 1][col].isdigit():
                        str_num, skip = get_full_number(arr, row+1, col)
                        str_num_list.append(str_num)
                else:
                    skip = skip - 1
                if skip == 0:
                    if row < len(arr) - 1 and col < len(arr[0]) - 1 and arr[row + 1][col + 1].isdigit():
                        str_num, skip = get_full_number(arr, row+1, col+1)
                        str_num_list.append(str_num)
                else:
                    skip = skip - 1
            if(len(str_num_list) == 2):
                output = output + (int(str_num_list[0]) * int(str_num_list[1]))
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n")
    print('Output 1:')
    print(problem1(input_list))
    print('Output 2:')
    print(problem2(input_list))
