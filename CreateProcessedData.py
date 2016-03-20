import os
import sys
import numpy as np
import scipy.io as sio
import math

volumetric_dir = sys.argv[1] # This will be the path to the directory "volumetric_dir"


class_list = os.listdir(volumetric_dir) #lists all directories in "volumetric_dir"
i = 0
data_sections = ['test', 'train']
x_train=[]
x_test=[]
y_train=[]
y_test=[]
class_dict = {}
for class_name in class_list:
    if(class_name[0]!='.'):
        class_dict[class_name] = i
        current_class_dir = volumetric_dir + class_name + '/30/'
        for current_data_section in data_sections:
            current_data_section_dir = current_class_dir + current_data_section + '/'
            current_samples_list = os.listdir(current_data_section_dir)
            for current_sample in current_samples_list:
                if(current_sample[0]!='.'):
                    data = sio.loadmat(current_data_section_dir+ current_sample)
                    current_mat = data['instance']
                    if current_data_section == 'test':
                        x_test.append(current_mat)
                        y_test.append(i)
                    else:
                        x_train.append(current_mat)
                        y_train.append(i)
        print class_name, i
        i += 1
a={}

x_test = np.array(x_test)
y_test = np.array(y_test)
x_train = np.array(x_train)
y_train = np.array(y_train)

num_train_sample = int(math.floor(x_train.shape[0]*0.8))
indices = np.random.permutation(x_train.shape[0])
training_idx, val_idx = indices[:num_train_sample], indices[num_train_sample:]

X_trainingset, X_valset = x_train[training_idx,:,:,:], x_train[val_idx,:,:,:]
y_trainingset, y_valset = y_train[training_idx], y_train[val_idx]


a['X_train'] = X_trainingset
a['y_train'] = y_trainingset
a['X_val'] = X_valset
a['y_val'] = y_valset
a['X_test'] = x_test
a['y_test'] = y_test

a['class_dict'] = class_dict
sio.savemat('processed_data',a)


