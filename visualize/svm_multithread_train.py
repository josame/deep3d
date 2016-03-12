#!/usr/bin/python
from sklearn import svm
from sklearn.externals import joblib
import threading
import time
import numpy as np
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, gamma, cost, training_examples, training_labels):
        threading.Thread.__init__(self)
        self.threadID = threadID
	self.name = name
        self.g = gamma
        self.c = cost
	self.X = training_examples
	self.Y = training_labels
    def run(self):
        print "Starting " + str(self.name) +" Gamma: " + str(self.g) + " C: " + str(self.c)
        print_time(self.name, self.g, self.c, self.X, self.Y)
        print "Exiting " + str(self.name) + " Gamma: " + str(self.g) + " C: " + str(self.c)

def print_time(thread_name, gamma, cost, training_examples, training_labels):
    if exitFlag:
    	thread_name.exit()
    # Do the action
    clf = svm.SVC(cache_size=300, C=cost, gamma=gamma, kernel='rbf')
    clf.fit(x_train, y_train)
    joblib.dump(clf, "mysvm_" + thread_name + ".pkl")    
# Create new threads
x_train = np.loadtxt("X.txt")
y_train = np.loadtxt("Y.txt")

thread1 = myThread(7, "7", 0.000005, 5, x_train, y_train)
thread2 = myThread(8, "8", 0.000005, 50, x_train, y_train)
thread3 = myThread(9, "9", 0.000015, 5, x_train, y_train)
thread4 = myThread(10, "10", 0.000015, 50, x_train, y_train)
thread5 = myThread(11, "11", 0.000005, 25, x_train, y_train)
thread6 = myThread(12, "12", 0.000015, 25, x_train, y_train)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
print "Exiting Main Thread"
