import time


def sum_of_n_2(n):
    """
    :param n: 1 到 n 的和
    :return: 元组（元素的组合），第一位为值，第二位为所花时间
    """
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end - start


for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n_2(10000))
print()

for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n_2(1000000))

"""
Sum is 50005000 required  0.0006449 seconds
Sum is 50005000 required  0.0006080 seconds
Sum is 50005000 required  0.0006089 seconds
Sum is 50005000 required  0.0006161 seconds
Sum is 50005000 required  0.0006239 seconds

Sum is 500000500000 required  0.0476000 seconds
Sum is 500000500000 required  0.0550399 seconds
Sum is 500000500000 required  0.0564568 seconds
Sum is 500000500000 required  0.0504000 seconds
Sum is 500000500000 required  0.0536993 seconds
"""
