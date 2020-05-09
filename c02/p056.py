def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
    return the_sum


print(sum_of_n(10))
print()


def foo(tom):
    fred = 0
    for bill in range(1, tom + 1):
        barney = bill
        fred = fred + barney
    return fred


print(foo(10))
print()

"""
55

55

"""
