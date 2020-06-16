def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if a_list[mid] == item:
            found = True
        elif a_list[mid] < item:
            first = mid + 1
        else:
            last = mid - 1

    return found


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 5))
