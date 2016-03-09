#!/usr/bin/env sh
~/caffe/build/tools/caffe test -model /mnt/remote_ubuntu/parameter_search/lr_15_wd_00100/alex_train_v11.prototxt -weights /mnt/remote_ubuntu/parameter_search/lr_15_wd_00100/alex3d_v11_net_snapshot_iter_20000.caffemodel -gpu 0 -iterations 300
