#!/usr/bin/env sh
~/caffe/build/tools/extract_features ./alex3d_v11_net_snapshot_iter_64000.caffemodel ./alex_train_v11.prototxt ip1 ./features 100 leveldb GPU 0
