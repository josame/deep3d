#!/usr/bin/env sh
~/caffe/build/tools/extract_features ./alex3d_v11_net_snapshot_iter_64000.caffemodel ./alex_vishakh_v11.prototxt ip1 ./vishakh_features 118 leveldb GPU 0
~/caffe/build/tools/extract_features ./alex3d_v11_net_snapshot_iter_64000.caffemodel ./alex_vishakh_v11.prototxt label ./vishakh_labels 118 leveldb GPU 0
