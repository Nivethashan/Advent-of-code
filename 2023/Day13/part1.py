def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def array_2d(input_set):
    input_list = input_set.split("\n")
    arr = [[0] * len(input_list[0]) for i in range(0, len(input_list))]
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[i])):
            arr[i][j] = input_list[i][j]
    return arr

def check_row_valid_reflection(arr, row_num):
    match = True
    for row in range(0,row_num+1):
        for col in range(len(arr[row])):
            match_row = row + ((row_num - row)*2) + 1
            if match_row >= len(arr):
                continue
            if(arr[row][col] != arr[match_row][col]):
                match = False
                break
    return match

def check_col_valid_reflection(arr, col_num):
    match = True
    for col in range(0,col_num+1):
        for row in range(len(arr)):
            match_col = col + ((col_num - col)*2) + 1
            if match_col >= len(arr[row]):
                continue
            if(arr[row][col] != arr[row][match_col]):
                match = False
                break
    return match

def check_row_match(arr, row_num):
    for row in range(len(arr) - 1):
        if check_row_valid_reflection(arr, row):
            return True, row
    return False, row

def check_col_match(arr, col_num):
    for col in range(len(arr[0]) - 1):
        if check_col_valid_reflection(arr, col):
            return True, col
    return False, col

def problem(input_list):
    row_sum, col_sum = 0,0
    for list in input_list:
        arr = array_2d(list)
        row_num, col_num = 0,0
        valid, row_num = check_row_match(arr, row_num)
        if valid:
            row_sum = row_sum + (row_num + 1)*100
        valid, col_num = check_col_match(arr, col_num)
        if valid:
            col_sum = col_sum + (col_num + 1)
    return row_sum + col_sum

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n\n")
    print('Output:')
    print(problem(input_list))
    print("done")
