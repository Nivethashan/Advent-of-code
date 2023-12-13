import copy

def read_input():
    input_file = open("input_file", "r")
    input_string = input_file.read()
    input_file.close()
    return input_string

def get_dest_ranges(init_range, maps_str):
    mapped_range = []
    for i in range (0,len(init_range)):
        low =  init_range[i][0]
        high = init_range[i][1]
        maps = maps_str.split("\n")
        final_range = []
        for j in range(1, len(maps)):  # all pairs
            pair = maps[j].split(" ")
            source = int(pair[1])
            range_val = int(pair[2])
            if (low >= source and low  < source + range_val):
                if(high >= source and high < source + range_val):
                    final_range.append([low, high])
                else:
                    final_range.append([low, source + range_val - 1])
            elif (high >= source and high < source + range_val):
                final_range.append([source, high])
        final_range_temp = copy.copy(final_range)
        final_range_temp.sort()
        #print(final_range_temp)

        new_low = low
        for ranges in final_range_temp:
            if new_low < high:
                if new_low < ranges[0]:
                    new_high = ranges[0] - 1
                    final_range.append([new_low, new_high])
                new_low = ranges[1] + 1
        if new_low <= high:
            final_range.append([new_low, high])
        final_range.sort()

        for ranges in final_range:
            new_low = ranges[0]
            new_high = ranges[1]
            for j in range(1, len(maps)):
                pair = maps[j].split(" ")
                dest = int(pair[0])
                source = int(pair[1])
                range_val = int(pair[2])
                if (new_low >= source and new_high < source + range_val):
                    new_low = dest + (new_low - source)
                    new_high = dest + (new_high - source)
                    break
            mapped_range.append([new_low, new_high])
        mapped_range.sort()
        #print(final_range)
        #print(mapped_range)
    return mapped_range

def problem1(input_list):
    output = float("inf")
    init_list = input_list[0].split()
    init_list.remove("seeds:")
    print(init_list)
    for seed in init_list:
        mapped_value = int(seed)
        for i in range (1,len(input_list)):
            maps = input_list[i].split("\n")
            for j in range(1, len(maps)):
                pair = maps[j].split(" ")
                dest = int(pair[0])
                source = int(pair[1])
                range_val = int(pair[2])
                if(mapped_value >= source and mapped_value < source + range_val):
                    mapped_value = dest + (mapped_value - source)
                    break
        if(mapped_value < output):
            output = mapped_value
    return output

def problem2(input_list):
    output = 0
    output = float("inf")
    init_list = input_list[0].split()
    init_list.remove("seeds:")
    print(init_list)
    for n in range(0, len(init_list), 2):
        low = int(init_list[n])
        high =  low + int(init_list[n+1]) - 1
        mapped_range = [[low, high]]
        for i in range(1, len(input_list)):
            mapped_range = get_dest_ranges(mapped_range, input_list[i])
        #print(i,mapped_range)
        if (mapped_range[0][0] < output):
            output = mapped_range[0][0]
    return output

if __name__ == '__main__':
    input_string = read_input()
    input_list = input_string.split("\n\n")
    print('Output 1:')
    print(problem1(input_list))
    print('Output 2:')
    print(problem2(input_list))
    print("done")
