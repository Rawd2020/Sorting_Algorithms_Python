def bubble_sort(input_list):
    while True:
        swaps = 0
        for i in range(0, len(input_list) - 1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                swaps += 1
        if not swaps:
            break
    return input_list

if __name__ == '__main__':
    pass

