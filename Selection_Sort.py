def selection_sort(unsorted_list):
    for index in range(0, len(unsorted_list)):
        smallest_element = min(unsorted_list[index:])
        smallest_element_index = unsorted_list[index:].index(smallest_element)
        unsorted_list[index + smallest_element_index] = unsorted_list[index]
        unsorted_list[index] = smallest_element
    return unsorted_list

if __name__ == '__main__':
    pass

