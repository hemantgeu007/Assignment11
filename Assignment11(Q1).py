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
        print_time(self.name, 10 , 5)
        print("Exiting" + self.name)
    '''Method to Run the thread'''

def print_time(threadName , counter , delay):
    while counter :
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s running: %s" % (threadName , time.ctime(time.time())))
        counter -= 1
'''Method to print the Thread Statement'''

thread1 = myThread("Thread-1")
'''Creating new Thread'''
thread1.start()
'''Starting new Thread'''