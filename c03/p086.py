from pythonds.basic.queue import Queue


def hotPotato(name_list, num):
    """
    解决约瑟夫环问题
    :param name_list: 姓名列表
    :param num: 每次移动的位数，移动到指定位置后移除姓名
    :return: 最后剩下的姓名
    """
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for _ in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == '__main__':
    """
    可以看到在这个例子中给出的传土豆数要大于列表中人名的个数。
    但这并不是问题，因为队列像是一个圆圈，当计数到达最后一人的时候就会回到开始，并继续计数直到到达给定值。
    同时，我们还注意到列表将按照顺序被读入队列，列表中的第一个名字会在队首出现。
    在这个例子中，Bill是列表中的第一个元素，所以就被移入了队列的第一个。
    这个问题的各种拓展情况会在练习中给出，比如说随机数热土豆问题。
    """
    print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))

"""
Susan
"""
