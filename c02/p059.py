"""
对于输出我们需要关注两个关键点。第一，这种算法的运行时间比之前任何例子都短很多。
第二，不管 n 取值多少运行时间都非常一致。看上去 sum_of_n_3 的运行时间几乎不受需要累计的数目的影响。
"""
import time


def sum_of_n_3(n):
    """
    :param n: 1 到 n 的和
    :return: 元组（元素的组合），第一位为值，第二位为所花时间
    """
    start = time.time()
    the_sum = (n * (n + 1)) / 2
    end = time.time()
    return the_sum, end - start


for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n_3(10000))
print()

for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n_3(1000000))
print()

print('Sum is %d required %10.7f seconds' % sum_of_n_3(10000))
print('Sum is %d required %10.7f seconds' % sum_of_n_3(100000))
print('Sum is %d required %10.7f seconds' % sum_of_n_3(1000000))
print('Sum is %d required %10.7f seconds' % sum_of_n_3(10000000))
print('Sum is %d required %10.7f seconds' % sum_of_n_3(100000000))

"""
Sum is 50005000 required  0.0000010 seconds
Sum is 50005000 required  0.0000012 seconds
Sum is 50005000 required  0.0000010 seconds
Sum is 50005000 required  0.0000000 seconds
Sum is 50005000 required  0.0000010 seconds

Sum is 500000500000 required  0.0000000 seconds
Sum is 500000500000 required  0.0000000 seconds
Sum is 500000500000 required  0.0000010 seconds
Sum is 500000500000 required  0.0000000 seconds
Sum is 500000500000 required  0.0000012 seconds

Sum is 50005000 required  0.0000000 seconds
Sum is 5000050000 required  0.0000000 seconds
Sum is 500000500000 required  0.0000000 seconds
Sum is 50000005000000 required  0.0000012 seconds
Sum is 5000000050000000 required  0.0000110 seconds
"""
