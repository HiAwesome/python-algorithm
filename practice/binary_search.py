def binary_search(a_list, item):
    left, right = 0, len(a_list) - 1
    found = False

    while left <= right and not found:
        mid = left + (right - left) // 2

        if a_list[mid] == item:
            found = True
        elif a_list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return found


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 5))
