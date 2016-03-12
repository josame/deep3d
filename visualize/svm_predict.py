from sklearn import svm
from sklearn.externals import joblib
import numpy as np
import sys
modelnum = int(sys.argv[1])
clf = joblib.load("mysvm_" + str(modelnum) + ".pkl")
x_test = np.loadtxt("X_test.txt")
y_test = np.loadtxt("Y_test.txt")
print "Done loading"
'''
xtt = x_test[linenum,:].reshape(1,-1)
y_predicted = clf.predict(xtt)
'''
y_predicted = clf.predict(x_test)
np.savetxt("test_" + str(modelnum) + ".out", y_predicted)
