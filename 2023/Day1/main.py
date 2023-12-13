def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def findfirstspellednumber(line):
    index = float("inf")
    value = float("inf")
    arr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, len(arr)):
        first_index = line.find(arr[i])
        if first_index != -1 and first_index < index:
            index = first_index
            value = i + 1
    return index, value

def findlastspellednumber(line):
    index = -1
    value = -1
    arr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, len(arr)):
        last_index = line.rfind(arr[i])
        if last_index != -1 and last_index > index:
            index = last_index
            value = i + 1
    return index, value

def problem1(input_list):
    output = 0
    first_digit = ""
    last_digit = ""
    for line in input_list:
        for i in range(0, len(line)):
            if line[i].isdigit():
                first_digit = line[i]
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                last_digit = line[i]
                break
        num = int(first_digit + last_digit)
        output += num
    return output

def problem2(input_list):
    output = 0
    first_digit = ""
    last_digit = ""
    for line in input_list:
        index, value = findfirstspellednumber(line)
        first_digit = str(value)
        for i in range(0, len(line)):
            if line[i].isdigit() and i < index:
                first_digit = line[i]
                break
        index, value = findlastspellednumber(line)
        last_digit = str(value)
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit() and i > index:
                last_digit = line[i]
                break
        num = int(first_digit + last_digit)
        output += num
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n")
    print('Output 1:')
    print(problem1(input_list))
    print('Output 2:')
    print(problem2(input_list))
