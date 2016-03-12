from sklearn import svm
from sklearn.externals import joblib
import numpy as np
import sys
modelnum = 9
clf = joblib.load("mysvm_" + str(modelnum) + ".pkl")
x_test = np.loadtxt("X_vishakh.txt")
y_test = np.loadtxt("Y_vishakh.txt")
print "Done loading"
'''
xtt = x_test[linenum,:].reshape(1,-1)
y_predicted = clf.predict(xtt)
'''
y_predicted = clf.predict(x_test)
modelnum=0
np.savetxt("test_" + str(modelnum) + ".out", y_predicted)
