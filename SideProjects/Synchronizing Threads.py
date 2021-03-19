import threading
import time

#todo Code for Locking Threads
"""
x = 8192

#Allows for locking certain threads preventing the other threads from running
lock = threading.Lock()

def double():
    global x, lock

    #Attemps to acquire the lock if lock is available, if lock not available, then it waits for it to be
    lock.acquire()

    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the Maximum")

    #Releases Lock if it has been acquired
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the Minimum")
    lock.release()

h_thread = threading.Thread(target=halve)
d_thread = threading.Thread(target=double)

h_thread.start()
d_thread.start()
"""

#todo Code for Limiting Threads' access to a source (Semaphores)
#Stating the amount of times a source can be accessed by the threads
semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} this thread number is trying to access".format(thread_number))
    #Acquires access to the source
    semaphore.acquire()
    print("{} was granted access".format(thread_number))
    time.sleep(10)
    print("{} is now releasing".format(thread_number))
    #Releases access to the source for other threads to gain access
    semaphore.release()

for thread_number in range(10):
    thread = threading.Thread(target=access, args=(thread_number,))
    thread.start()
    time.sleep(1)