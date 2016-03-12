from __future__ import division
import numpy as np
y_test = np.loadtxt("Y_test.txt")
predicted_labels = np.loadtxt("test.out")
print y_test.shape, predicted_labels.shape
print np.sum(np.equal(y_test, predicted_labels))/y_test.shape[0]
