def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum += i
    return the_sum


def recursion_list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + recursion_list_sum(num_list[1:])


if __name__ == '__main__':
    a_list = [1, 3, 5, 7, 9]
    print(list_sum(a_list), recursion_list_sum(a_list))
