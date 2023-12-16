def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def problem(input_list):
    output = 0
    for str in input_list:
        hash_val = 0
        for char in str:
            hash_val = ((hash_val + ord(char))*17)%256
        output += hash_val
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split(",")
    print('Output:')
    print(problem(input_list))
    print("done")
