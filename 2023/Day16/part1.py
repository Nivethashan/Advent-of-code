import sys

def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def array_2d(input_list):
    if len(input_list) <= 0:
        return [[]]
    arr = [["."] * len(input_list[0]) for i in range(0, len(input_list))]
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[i])):
            arr[i][j] = input_list[i][j]
    return arr

def pass_beam(arr, row, col, dir, new_arr):
    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]):
        return
    if dir in new_arr[row][col]:
        return
    else:
        new_arr[row][col].append(dir)

    if arr[row][col] == ".":
        if dir == "right":
            pass_beam(arr, row, col + 1, "right", new_arr)
        elif dir == "left":
            pass_beam(arr, row, col - 1, "left", new_arr)
        elif dir == "top":
            pass_beam(arr, row - 1, col, "top", new_arr)
        elif dir == "bottom":
            pass_beam(arr, row + 1, col, "bottom", new_arr)

    if arr[row][col] == "-" and dir == "right":
            pass_beam(arr, row, col + 1,"right", new_arr)
    elif arr[row][col] == "-" and dir == "left":
            pass_beam(arr, row, col - 1, "left", new_arr)
    elif arr[row][col] == "-" and (dir == "top" or dir == "bottom"):
            pass_beam(arr, row, col + 1,"right", new_arr)
            pass_beam(arr, row, col - 1, "left", new_arr)

    if arr[row][col] == "|" and dir == "top":
            pass_beam(arr, row - 1, col,"top", new_arr)
    elif arr[row][col] == "|" and dir == "bottom":
            pass_beam(arr, row + 1, col, "bottom", new_arr)
    elif arr[row][col] == "|" and (dir == "left" or dir == "right"):
            pass_beam(arr, row - 1, col, "top", new_arr)
            pass_beam(arr, row + 1, col, "bottom", new_arr)

    if arr[row][col] == "/" and dir == "right":
            pass_beam(arr, row - 1, col,"top", new_arr)
    elif arr[row][col] == "/" and dir == "left":
            pass_beam(arr, row + 1, col, "bottom", new_arr)
    elif arr[row][col] == "/" and dir == "top":
            pass_beam(arr, row, col + 1,"right", new_arr)
    elif arr[row][col] == "/" and dir == "bottom":
            pass_beam(arr, row, col - 1, "left", new_arr)

    if arr[row][col] == "\\" and dir == "right":
            pass_beam(arr, row + 1, col,"bottom", new_arr)
    elif arr[row][col] == "\\" and dir == "left":
            pass_beam(arr, row - 1, col, "top", new_arr)
    elif arr[row][col] == "\\" and dir == "top":
            pass_beam(arr, row, col - 1,"left", new_arr)
    elif arr[row][col] == "\\" and dir == "bottom":
            pass_beam(arr, row, col + 1, "right", new_arr)

    return


def problem(input_list):
    output = 0
    sys.setrecursionlimit(1000000)
    arr = array_2d(input_list)
    new_arr = [[[] for j in range(len(arr[0]))] for i in range(len(arr))]
    pass_beam(arr, 0, 0, "right", new_arr)

    for i in range(len(new_arr)):
       for j in range(len(new_arr[0])):
           if len(new_arr[i][j]) != 0:
               output += 1
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n")
    print('Output:')
    print(problem(input_list))
    print("done")
