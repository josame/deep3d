#!/usr/bin/env sh
~/caffe/build/tools/caffe test -model /mnt/remote_ubuntu/deep3d/alex3d/alex_train.prototxt -weights /mnt/remote_ubuntu/deep3d/alex3d/alex3d_net_snapshot_iter_400000.caffemodel -gpu 0 -iterations 300
