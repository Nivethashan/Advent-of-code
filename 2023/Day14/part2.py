from copy import copy, deepcopy

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

#north
def roll_rocks_north(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "O":
                new_row = i
                hit = False
                for k in range(i-1,-1, -1):
                    if arr[k][j] == "O" or arr[k][j] == "#":
                        new_row = k+1
                        arr[i][j] = "."
                        arr[new_row][j] = "O"
                        hit = True
                        break
                if hit == False:
                    arr[i][j] = "."
                    arr[0][j] = "O"
    return arr

#west
def roll_rocks_west(arr):
    for j in range(1, len(arr[0])):
        for i in range(len(arr)):
            if arr[i][j] == "O":
                new_col = j
                hit = False
                for k in range(j-1,-1, -1):
                    if arr[i][k] == "O" or arr[i][k] == "#":
                        new_col = k+1
                        arr[i][j] = "."
                        arr[i][new_col] = "O"
                        hit = True
                        break
                if hit == False:
                    arr[i][j] = "."
                    arr[i][0] = "O"
    return arr

#south
def roll_rocks_south(arr):
    for i in range(len(arr)-2, -1, -1):
        for j in range(len(arr[i])):
            if arr[i][j] == "O":
                new_row = i
                hit = False
                for k in range(i+1,len(arr)):
                    if arr[k][j] == "O" or arr[k][j] == "#":
                        new_row = k-1
                        arr[i][j] = "."
                        arr[new_row][j] = "O"
                        hit = True
                        break
                if hit == False:
                    arr[i][j] = "."
                    arr[len(arr)-1][j] = "O"
    return arr

#east
def roll_rocks_east(arr):
    for j in range(len(arr[0]) - 2, -1, -1):
        for i in range(len(arr)):
            if arr[i][j] == "O":
                new_col = j
                hit = False
                for k in range(j+1,len(arr[0])):
                    if arr[i][k] == "O" or arr[i][k] == "#":
                        new_col = k-1
                        arr[i][j] = "."
                        arr[i][new_col] = "O"
                        hit = True
                        break
                if hit == False:
                    arr[i][j] = "."
                    arr[i][len(arr[0])-1] = "O"
    return arr

def problem(input_list):
    arr = array_2d(input_list)

    cycles = []
    final_arr_index = 0
    for cycle_num in range(1000000000):
        arr = roll_rocks_north(arr)
        arr = roll_rocks_west(arr)
        arr = roll_rocks_south(arr)
        arr = roll_rocks_east(arr)
        for i,each_arr in enumerate(cycles):
            if each_arr == arr:
                repeat_cycles = cycle_num - i
                final_arr_index = i + (1000000000 -1 - i)%repeat_cycles
                break
        if final_arr_index != 0:
            break
        cycles.append(deepcopy(arr))

    final_arr = cycles[final_arr_index]
    sum = 0
    for i in range(len(final_arr)):
        for j in range(len(final_arr[i])):
            if final_arr[i][j] == "O":
                sum = sum + (len(final_arr) - i)
    return sum

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n")
    print('Output:')
    print(problem(input_list))
    print("done")
