#!/usr/bin/env sh
~/caffe/build/tools/caffe test -model ~/base_station/alex3d_v17/alex_train_v17.prototxt -weights ~/base_station/alex3d_v17/alex3d_v17_net_snapshot_iter_24000.caffemodel -gpu 0 -iterations 1000
