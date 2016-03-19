# deep3d 
This document describes step by step procedure to download the dataset, process the data, 
feed it to a caffe neural network and test it. Since "alex3d_v11" was the best model, we are describing the procedure 
to train and test that model on caffe.

## Data and pre-processing

1. Download the data set using the following link: http://vision.princeton.edu/projects/2014/3DShapeNets/3DShapeNetsCode.zip

2. Use the "CreateProcessedData.py" script to combine all the .mat files containing data in the volumetric 
into one giant dictionary containing training, validation and test sets. The way to run it is "python CreateProcessedData.py <path to directory containing volumetric data>. This creates a file "processed_data.mat"

NOTE: The training and validation sets in the dictionary are a part of the training split of the original data set.

3. We then use createLMDB_train.py, createLMDB_test.py, createLMDB_val.py to create lmdb folders (namely mylmdb, mylmdb_test, mylmdb_val.py) which can be fed into the caffe code as input.


## Training the neural network

There are two components to training:

1. Defining the model

2. Defining the solver which has information about the location of the LMDB data (for training and testing) and 
the model .prototxt file

Open the file "alex3d_v11" (NOTE: It has nothing to do with AlexNet, it was just a naming convention that we ended up using)

It should contain the following main files:

1. alex_solver_v11.prototxt - this is the prototxt file in which the solver is defined

2. alex_train_v11.prototxt - this contains the model definition

3. train_alex3d_v11.sh - this script runs the training part

Before running the "train_alex3d_v11.sh" script, the following are to be ensured:

1. The first layer in the "alex_train_v11.prototxt" should contain the path to the training lmdb file.

2. The second layer in the "alex_train_v11.prototxt" should contain the path to the test lmdb file.

3. The correct caffe folder is used.

OPTIONAL: Remove all the .solverstate and .caffemodel files before training (so that there is no ambiguity when it comes to tesitng these models)

The output of training will be .solverstate and .caffemodel files for different epochs of training. It also prints on screen 
the loss and accuracy. The frequency of printing these can be set in the "alex_solver_v11.prototxt" file.


## Testing the neural network 

We obtain the test accuracies while training the neural network. However, the training process also outputs .solverstate and 
.caffemodel files which can be used to find the test accuracies. The number of epochs to be tested for can also be set while
tesitng.

To find the test accuracies, you should do the following:

1. The the main file, go to directory named "tester". You should see "test_my_caffe_model.sh" in it.

2. Before running it, you need to input the path to "alex_train_v11.prototxt" file for the model and the path to the .caffemodel snapshot. Also make sure that the correct caffe folder is used.

3. Run the "test_my_caffe_model.sh" file. It will output the test accuracy on the screen.


