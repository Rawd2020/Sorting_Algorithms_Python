def merge(list_a, list_b):
    merged_list = []
    while list_a and list_b:
        if list_a[0] < list_b[0]:
            merged_list.append(list_a[0])
            list_a = list_a[1:]
        else:
            merged_list.append(list_b[0])
            list_b = list_b[1:]
    while list_a:
        merged_list.append(list_a[0])
        list_a = list_a[1:]
    while list_b:
        merged_list.append(list_b[0])
        list_b = list_b[1:]
    return merged_list

def merge_sort(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        mid_point = len(input_list)//2
        list_a = merge_sort(input_list[0:mid_point])
        list_b = merge_sort(input_list[mid_point:])
        return merge(list_a, list_b)

if __name__ == '__main__':
    pass

