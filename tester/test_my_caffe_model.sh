#!/usr/bin/env sh
~/caffe/build/tools/caffe test -model ~/base_station/alex3d_v16/alex_train_v16.prototxt -weights ~/base_station/alex3d_v16/alex3d_v16_net_snapshot_iter_16000.caffemodel -gpu 0 -iterations 300
