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

thread1 = myThread(1, "1", 0.000001, 0.1, x_train, y_train)
thread2 = myThread(2, "2", 0.000001, 10.0, x_train, y_train)
thread3 = myThread(3, "3", 0.0001, 0.1, x_train, y_train)
thread4 = myThread(4, "4", 0.0001, 10.0, x_train, y_train)
thread5 = myThread(5, "5", 0.00001, 10.0, x_train, y_train)
thread6 = myThread(6, "6", 0.00001, 0.1, x_train, y_train)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
print "Exiting Main Thread"
