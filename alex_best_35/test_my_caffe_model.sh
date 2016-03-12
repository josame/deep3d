#!/usr/bin/env sh
~/caffe/build/tools/caffe test -model /mnt/remote_ubuntu/deep3d/alex_best_35/alex_train_v11.prototxt -weights /mnt/remote_ubuntu/deep3d/alex_best_35/alex_best_net_snapshot_iter_60000.caffemodel -gpu 0 -iterations 300
