# Inference
from keras.layers import Flatten
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs
import numpy as np
from keras.models import load_model

import tensorflow as tf
from tensorflow.compat.v1 import InteractiveSession
from sklearn.metrics import accuracy_score
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
from utils.utils import transform_labels
from utils.utils import read_dataset

root_dir = '/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/code/TIMS/dl_4_tsc/'
archive_name = 'NS'
dataset_name = 'real_test_files'
net = 'fcn'

datasets_dict = read_dataset(root_dir, archive_name, dataset_name)

x_train = datasets_dict[dataset_name][0]
y_train = datasets_dict[dataset_name][1]
x_test = datasets_dict[dataset_name][2]
y_test = datasets_dict[dataset_name][3]

y_train, y_test = transform_labels(y_train, y_test)

# model = load_model(root_dir + 'results/' + net + '/' + archive_name + '_itr_8' + '/' + dataset_name + '/best_model.hdf5')
model = load_model(root_dir + 'results/' + net + '/' + archive_name + '_itr_10' + '/' + 'sig_constr' + '/best_model.hdf5')

if len(x_train.shape) == 2:  # if univariate
    # add a dimension to make it multivariate with one dimension
    x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
    x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

model.summary()

y_pred = model.predict(x_test)
print(y_pred, 'raw')

y_pred = np.argmax(y_pred, axis=1)
print(y_pred, 'np')
acc = 0
for i in range(len(x_test)):
    print(i, "Predicted=%s" % (y_pred[i]), 'Real=%s' % (y_test[i]))

    if y_pred[i] == y_test[i]:
        acc = acc + 1
        #print(i, "Predicted=%s" % (y_pred[i]), 'Real=%s' % (y_test[i]))
print('Acc_sklearn=%s' % (accuracy_score(y_test, y_pred)))
print("Accuracy=%s" % ((acc / len(x_test)) * 100), "%")

'''
def readucr(filename):
    data = np.genfromtxt(filename, delimiter='  ')  # , usecols=range(160))
    Y = data[:, 0]
    X = data[:, 1:]
    return X, Y

x_train, y_train = readucr('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/code/TIMS/dl_4_tsc/archives/TSC/Car'
                           '/Car_TRAIN.txt')
x_test, y_test = readucr('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/code/TIMS/dl_4_tsc/archives/TSC/Car'
                           '/Car_TEST.txt')
# make the min to zero of labels
y_train, y_test = transform_labels(y_train, y_test)
#datasets_dict = {}
#datasets_dict[0] = (x_train.copy(), y_train.copy())
# print(datasets_dict)
model = load_model(root_dir + 'results/' + net + '/' + archive_name + '_itr_8' + '/' + dataset_name + '/best_model.hdf5')
#x_train = datasets_dict[0][0]

x_test = x_test.reshape((x_test.shape[0], x_train.shape[1], 1))
#y_train = datasets_dict[0][1]
model.summary()
#print(x_train)
y_pred = model.predict(x_test)
print(y_pred,'raw')

y_pred = np.argmax(y_pred, axis=1)
print(y_pred,'np')
acc = 0
for i in range(len(x_test)):
    # print(i, "Predicted=%s" % (y_pred[i]), 'Real=%s' % (y_test[i]))

    if y_pred[i] == y_test[i]:
        acc = acc + 1
        print(i, "Predicted=%s" % (y_pred[i]), 'Real=%s' % (y_test[i]))
print('Acc_sklearn=%s' % (accuracy_score(y_test, y_pred)))
print("Accuracy=%s" % ((acc / len(x_test)) * 100), "%")
'''


# # make a prediction
# ynew = model.predict(Xnew)
# # show the inputs and predicted outputs
# for i in range(len(Xnew)):
# 	print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))

