from copy import copy, deepcopy

def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def problem(input_list):
    output = 0
    box_hash = []
    input_list_temp = deepcopy(input_list)
    for str in input_list_temp:
        hash_val = 0
        if '-' in str:
            str = str.replace("-", "")
        if '=' in str:
            str, val = str.split("=")
        for char in str:
            hash_val = ((hash_val + ord(char))*17)%256
        box_hash.append(hash_val)

    boxes = [{} for i in range(256)]
    for i,str in enumerate(input_list):
        box = deepcopy(boxes[box_hash[i]])
        if '-' in str:
            str = str.replace("-", "")
            if str in box.keys():
                box.pop(str)
        if '=' in str:
            key, val = str.split("=")
            box[key] = val
        boxes[box_hash[i]] = deepcopy(box)

    for i,box in enumerate(boxes):
        for key in box:
            pos = list(box.keys()).index(key)
            focal_power = (i+1) * (pos+1) * int(box[key])
            output += focal_power
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split(",")
    print('Output:')
    print(problem(input_list))
    print("done")
