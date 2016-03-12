import sys
import caffe
import leveldb
import numpy as np
from caffe.proto import caffe_pb2

db = leveldb.LevelDB('./vishakh_labels')
datum = caffe_pb2.Datum()
i = 0
one_in_x = int(sys.argv[1])
np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
with open('Y_vishakh.txt', 'w') as f:
	for key, value in db.RangeIter():
    		datum.ParseFromString(value)
    		label = datum.label
    		data = caffe.io.datum_to_array(datum)
		if(i%one_in_x==0):
			f.write("%d\n"  %(data))
		i=i+1
