import sys
import caffe
import leveldb
import numpy as np
from caffe.proto import caffe_pb2

db = leveldb.LevelDB('./features')
datum = caffe_pb2.Datum()
i = 0
one_in_x = int(sys.argv[1])
np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
with open('X.txt', 'w') as f:
	for key, value in db.RangeIter():
    		datum.ParseFromString(value)
    		label = datum.label
    		data = np.sum(caffe.io.datum_to_array(datum), axis=1)
		if(i%one_in_x==0):
			for x in np.nditer(data):
				f.write("   " + "{:1.7e}".format(float(x)))
			f.write("\n")
		i=i+1
