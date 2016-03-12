import numpy as np
from sklearn import svm
from sklearn.externals import joblib
x_train = np.loadtxt("X.txt")
y_train = np.loadtxt("Y.txt")
x_test = np.loadtxt("X_test.txt")
y_test = np.loadtxt("Y_test.txt")
print x_train.shape, y_train.shape, x_test.shape, y_test.shape
clf = svm.SVC(cache_size=10000)
clf.fit(x_train, y_train)
joblib.dump(clf, 'mysvm.pkl') 
y_predicted = clf.predict(x_test)
print np.sum(y_predicted==x_test)
