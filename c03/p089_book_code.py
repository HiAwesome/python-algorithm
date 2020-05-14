"""
source: https://facert.gitbooks.io/python-data-structure-cn/3.%E5%9F%BA%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/3.14.%E6%A8%A1%E6%8B%9F%EF%BC%9A%E6%89%93%E5%8D%B0%E6%9C%BA/
"""
import random

from pythonds.basic.queue import Queue


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        return self.currentTask is not None

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 5)

"""
Average Wait  48.79 secs   1 tasks remaining.
Average Wait 106.31 secs   3 tasks remaining.
Average Wait 186.12 secs   2 tasks remaining.
Average Wait 110.62 secs   0 tasks remaining.
Average Wait 110.00 secs   2 tasks remaining.
Average Wait 209.67 secs   7 tasks remaining.
Average Wait  78.00 secs   0 tasks remaining.
Average Wait 295.88 secs   0 tasks remaining.
Average Wait 120.29 secs   0 tasks remaining.
Average Wait 700.04 secs   7 tasks remaining.
"""
