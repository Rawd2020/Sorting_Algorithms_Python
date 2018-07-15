def insertion_sort(input_list):
    for index in range(1, len(input_list)):
        current_value = input_list[index]
        while index > 0 and input_list[index - 1] > current_value:
            input_list[index] = input_list[index - 1]
            index -= 1
            input_list[index] = current_value
    return input_list

if __name__ == "__main__":
    pass

