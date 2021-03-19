import threading

def function1():
    for i in range(50):
        print("ONE")

def function2():
    for j in range (50):
        print("TWO")

#Specifying which functions will be use by the stated threads
#If only using 1 thread, then you can do: thread1 = threading.Thread(target=function1).start()
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

#Allows both functions to run at once;parallel to one another
thread1.start()
thread2.start()

#Prevents the rest of code from running until specified function is completed
thread1.join()
thread2.join()

print("Control")