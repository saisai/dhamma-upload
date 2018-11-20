import threading
import datetime

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        # Acquire lock to synchronize thread
        threadLock.acquire()
        print_date(self.name, self.counter)
        # Release lock for the next thread
        threadLock.release()
        print("Exiting " + self.name)

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("%s[%d]: %s" % ( threadName, counter, datefields[0] ))

threadLock = threading.Lock()
threads = []

# Create new threads
"""
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
"""

for i in range(1, 3):
    t = myThread("Thread", i)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting the Program!!!")
