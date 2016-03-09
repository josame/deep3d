import caffe
import leveldb
import numpy as np
from caffe.proto import caffe_pb2

db = leveldb.LevelDB('./features')
datum = caffe_pb2.Datum()

for key, value in db.RangeIter():
    datum.ParseFromString(value)

    label = datum.label
    data = caffe.io.datum_to_array(datum)
    print label
    print data.shape
    '''
    #CxHxW to HxWxC in cv2
    image = np.transpose(data, (1,2,0))
    '''
