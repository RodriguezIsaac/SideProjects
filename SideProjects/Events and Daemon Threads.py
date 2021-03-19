import threading

#todo Code for using Events
"""
#Creates an event assigned to the variable "event" (events can be triggered)
event = threading.Event()

def myfunction():
    print("Waiting for event to trigger...")

    #Causes function to wait for the event to trigger
    event.wait()

    # What happens when the event is triggered
    print("Performing action XYZ now...")

thread1 = threading.Thread(target=myfunction)
thread1.start()

trigger = input("Do you want to to trigger the event? (y/n) ").lower()

if trigger == "y":

    #Triggers the event to occur
    event.set()
"""

#todo Code for using Daemon Threads
#Daemon Threads run in the background & ends once script is terminated since daemon threads are deemed to the program as not important
import time

path = "text.txt"
text = ""

def readFile():
    global path, text

    #Endless loop
    while True:
        #Opens the text file in reading mode & assigns it to variable f
        with open("text.txt", "r") as f:
            #Reads the text within the stated file
            text = f.read()
        time.sleep(3)

def printLoop():
    for x in range(10):
        print(text)
        time.sleep(1)

#"daemon=True" classifies the created thread as a daemon thread
thread1 = threading.Thread(target=readFile, daemon=True)
thread2 = threading.Thread(target=printLoop)

thread1.start()
thread2.start()