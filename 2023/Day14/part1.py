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

def roll_rocks(arr):
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

def problem(input_list):
    arr = array_2d(input_list)
    arr = roll_rocks(arr)
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "O":
                sum = sum + (len(arr) - i)
    return sum

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n")
    print('Output:')
    print(problem(input_list))
    print("done")
