import caffe
import lmdb
import os
import caffe.proto.caffe_pb2
from caffe.io import datum_to_array

lmdb_env = lmdb.open('/mnt/remote_data/mylmdb_test')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    label = datum.label
    data = caffe.io.datum_to_array(datum)
    print label
