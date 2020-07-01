import numpy as np
import os

dir_path = '/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/sig_constr/test'
directory = 'test'


def read(name, path):
    for root, dirs, files in os.walk(path):
        if root.endswith(name):
            for file in files:
                # print(root)

                # change the extension from '.mp3' to
                # the one of your choice.
                if file.endswith('.csv'):
                    # print(root + '/' + str(file))
                    return os.path.join(root, file)


# s = read(directory, dir_path)
# print(s)
m = 0
for root, dirs, files in os.walk(dir_path):
    # if root.endswith(directory):
    # print(root)
    n = len([name for name in os.listdir(root) if os.path.isfile(os.path.join(root, name))])
    m = m + n  # No. of files
tims = np.zeros((m, 121, 54), dtype='float64')  # final array dimensionb
f = 0
w = []
for root, dirs, files in sorted(os.walk(dir_path)):
    # if root.endswith(directory):
    for file in sorted(files):
        var = []
        # change the extension to
        # the one of your choice.
        if file.endswith('.csv'):
            print(root + '/' + str(file))
            data = np.genfromtxt((root + '/' + str(file)), delimiter=',', skip_header=1)  # skip_header for tims-file is 4 and for sig_constr is 1
            e = root.split('_', -1)  # e = file.split('.')
            w.append(int(e[-1]))  # w.append(e[0])
            # print(data)
            # if data.shape > (121,54):  # if file contains the more than 54 parameter values
            #     data = np.delete(data, 54, 1)
            #     print(data.shape,'---')
            var = data[:, 1:]  # removing 1st column
        # tims[f, :, :] = np.transpose(var)
            tims[f, :, :] = var
            f = f + 1

np.save(dir_path + '/' + 'x_' + directory + '.npy', tims)
# with open(dir_path + '/' + directory + '.txt', 'w') as output:
#    for item in w:
#        output.write('%s\n' % item)
np.save(dir_path + '/' + 'y_' + directory + '.npy', w)
'''
#import csv

#f = '/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/21115/TS#02_090419/NNS/02_09_04_19_11_15_100.csv'
# csv_f = csv.reader(f)
# for row in csv_f:
#     content = list(row[i] for i in range(53))
#     print(content)
# with open(f) as fd:
#     reader=csv.reader(fd)
#     interestingrows=[row for idx, row in enumerate(reader) if idx in (28,50)]
#     print(interestingrows)
'''
'''
tims = np.empty([121, 54], dtype='float64')
with open(f, "r") as infile:
    r = csv.reader(infile)
    # for i in range(8): # count from 0 to 2
    #     next(r)     # and discard the rows
    #row = next(r)
    #print(row)
    for idx, lines in enumerate(r):
        if idx > 3:
            m = lines[1:]

            print(m)


with open(f) as fd:
    next(fd)                                  # skip initial line
    rd = csv.reader(fd, delimiter=',')
    arr = np.array([[(i) for i in row[1:]] for row in rd])  # skip initial column

print(repr(arr))


import glob
import numpy as np
import pandas as pd

files = glob.glob(f)
#read each file to list of DataFrames
dfs = [pd.read_csv(fp) for fp in files]
#create names for each file
lst4 = [x[:-4] for x in files]
#create one big df with MultiIndex by files names
df = pd.concat(dfs, keys=lst4)

#print(df)
'''
