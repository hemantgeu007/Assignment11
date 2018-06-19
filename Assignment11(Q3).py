import threading
'''threading module inmported'''
import time
'''time module imported'''

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self , name):
        threading.Thread.__init__(self)
        self.name = name
    '''Method to Initialize myThread class'''

    def run(self):
        print("Starting" + self.name)
        print_time(self.name , 2)
        print("Exiting" + self.name)
    '''Method to Run the thread'''

def print_time(threadName , delay):
    for i in range(0 , 5):
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % ((str(l[i])) , time.ctime(time.time())))
        delay += 2
'''Method to print the Thread Statement'''

l = ["Element1" , "Element2" , "Element3" , "Element4" , "Element5"]
'''Creating List'''
thread1 = myThread("Thread-1")
'''Creating new Thread'''
thread1.start()
'''Starting new Thread'''
