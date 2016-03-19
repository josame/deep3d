import numpy as np
import scipy.io as sio
import lmdb
import caffe

data = sio.loadmat('processed_data.mat')
x_train = data['X_train']
x_test = data['X_test']
x_val = data['X_val']

y_train = data['y_train'][0]
y_test = data['y_test'][0]
y_val = data['y_val'][0]

X = x_val
y = y_val
N = len(y)

map_size = X.nbytes * 10
env = lmdb.open('mylmdb_val', map_size=map_size)
with env.begin(write=True) as txn:
        for i in range(N):
                datum = caffe.proto.caffe_pb2.Datum()
                datum.channels = X.shape[1]
                datum.height = X.shape[2]
                datum.width = X.shape[3]
                datum.data = X[i].tobytes()
                datum.label = int(y[i])
                str_id = '{:08}'.format(i)
                txn.put(str_id.encode('ascii'), datum.SerializeToString())
