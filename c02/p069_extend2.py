"""
几种Python执行时间的计算方法
https://blog.csdn.net/wangshuang1631/article/details/54286551
http://www.manongjc.com/article/139801.html
"""


def get_process_time1():
    """
    datetime.datetime.now()获取的是当前日期，在程序执行结束之后，这个方式获得的时间值为程序执行的时间。
    """
    starttime = datetime.datetime.now()
    # long running
    # do something other
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)


def get_process_time2():
    """
    time.time()获取自纪元以来的当前时间（以秒为单位）。如果系统时钟提供它们，则可能存在秒的分数。
    所以这个地方返回的是一个浮点型类型。这里获取的也是程序的执行时间。
    """
    start = time.time()
    # long running
    # do something other
    end = time.time()
    print(end - start)


def get_process_time3():
    """
    time.clock()返回程序开始或第一次被调用clock（）以来的CPU时间。
    这具有与系统记录一样多的精度。返回的也是一个浮点类型。这里获得的是CPU的执行时间。
    注：程序执行时间=cpu时间 + io时间 + 休眠或者等待时间
    """
    start = time.clock()
    # long running
    # do something other
    end = time.clock()
    print(end - start)
