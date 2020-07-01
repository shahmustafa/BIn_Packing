import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from utils.utils import transform_labels
from utils.utils import read_dataset

root_dir = '/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/code/TIMS/dl_4_tsc/'
# archive_name = 'mts_archive'
# dataset_name = 'ArabicDigits'
#root_dir = '/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/'
archive_name = 'NS'
dataset_name = '21115'

datasets_dict = read_dataset(root_dir, archive_name, dataset_name)

x_train = datasets_dict[dataset_name][0]
#print(x_train[0][0])
y_train = datasets_dict[dataset_name][1]
x_test = datasets_dict[dataset_name][2]
y_test = datasets_dict[dataset_name][3]

y_train, y_test = transform_labels(y_train, y_test)

if len(x_train.shape) == 2:  # if univariate
    # add a dimension to make it multivariate with one dimension
    x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
    x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

#x_train = np.load('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/code/TIMS/dl_4_tsc/archives/mts_archive/AUSLAN/x_train.npy')
#y_train = np.load('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/code/TIMS/dl_4_tsc/archives/mts_archive/AUSLAN/y_train.npy')
samples = range(0,4)  # samples (How many samples want to plot)
length = len(x_train[0])  # Length (Instances)
#print(length)
#print(range(len(samples)))
for i,j in zip(samples, range(len(samples))):
    plt.subplot(len(samples), 1, j + 1)

    plt.ylabel('data[%s]' % i)  # Sample
    #print(y_train[i])
    #plt.ylabel('class_%s' % y_train[i])  # Class
    # plt.text(length + 7, 0.5, ('class_%s' % y_train[i]))  # Class
    plt.text(length + 3, 0.1, ('class_%s' % y_test[i]))  # Class
    plt.plot(x_test[i])


plt.savefig('png/' + dataset_name + '_test.png')

