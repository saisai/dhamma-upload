from queue import Queue
from threading import Thread, Lock

num_worker_threads = 3
list_of_urls = ["http://foo.com", "http://bar.com",
  "http://baz.com", "http://spam.com",
  "http://egg.com",
    ]

def do_work(url):
    from time import sleep
    from random import randrange
    from threading import currentThread
    print("%s downloading %s" % (currentThread().getName(), url))
    sleep(randrange(5))
    print("%s done" % currentThread().getName())
    
# from this point on, copied almost verbatim from the Queue example
# at the end ofhttp://docs.python.org/library/queue.html
count = 0
def worker():
    while True:        
        item = q.get()
        do_work(item)
        q.task_done()
        

q = Queue()
lock = Lock()

for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.setDaemon(True)
    t.start()

for item in list_of_urls:
    print(item)
    q.put(item)

q.join()  # block until all tasks are done
print("Finished")
