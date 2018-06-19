import threading
'''threading module inmported'''
import math
'''math module imported'''

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self , num):
        threading.Thread.__init__(self)
        self.num = num
    '''Method to Initialize myThread class'''

    def run(self):
        global result
        result = math.factorial(self.num)
        '''Calling factorial function'''
        print("%s: " % (self.name))
    '''Method to Run the thread'''

t = myThread(int(input("Enter the number to calculate factorial: ")))
'''Creating new Thread'''
t.start()
'''Starting new Thread'''
print("The factorial of %d is %d" % (t.num,result))