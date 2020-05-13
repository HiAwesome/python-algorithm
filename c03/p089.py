"""
fixme 目前没有实现书中的效果，回头检查代码在哪里出了问题
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

    def waitTime(self, currentTime):
        return currentTime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    labpriter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labpriter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labpriter.startNext(nexttask)
            labpriter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print('Average Wait %6.2f secs %3d tasks remaining.' % (averageWait, printQueue.size()))


def newPrintTask():
    num = random.randrange(1, 181)
    return num == 180


if __name__ == '__main__':
    for _ in range(10):
        simulation(3600, 10)

"""
Average Wait   0.00 secs  19 tasks remaining.
Average Wait   0.00 secs  14 tasks remaining.
Average Wait   0.00 secs  17 tasks remaining.
Average Wait   0.00 secs  20 tasks remaining.
Average Wait   0.00 secs  21 tasks remaining.
Average Wait   0.00 secs  22 tasks remaining.
Average Wait   0.00 secs  23 tasks remaining.
Average Wait   0.00 secs  24 tasks remaining.
Average Wait   0.00 secs  26 tasks remaining.
Average Wait   0.00 secs  18 tasks remaining.
"""
