from random import randrange

def partition(input_list, pivot):
    less_than_pivot = []
    greater_than_pivot = []
    equals_pivot = []
    for value in input_list:
        if value < pivot:
            less_than_pivot.append(value)
        elif value > pivot:
            greater_than_pivot.append(value)
        else:
            equals_pivot.append(value)
    return less_than_pivot, equals_pivot, greater_than_pivot

def quick_sort(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        less, equal, greater = partition(input_list, input_list[randrange(0, len(input_list))])
        return quick_sort(less) + equal + quick_sort(greater)

if __name__ == '__main__':
    pass

