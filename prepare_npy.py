import numpy as np

# tims = np.zeros((24, 121, 54), dtype='float64')  # size of final array

a = np.load('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/sig_constr/gen_signals_new.npy')
b = np.load('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/21115/ans.npy')

[s,l,p] = a.shape  # samples, length, parameters
test_size = 14
train_size = s - test_size
xtrain = np.zeros((train_size,l,p), dtype='float64')
xtest = np.zeros((test_size,l,p), dtype='float64')

for j,i,m in range(s),range(test_size),range(train_size):
    if 20 <= j <= 21:
        xtest[i,:,:] = a[j,:,:]
    elif 41 <= j <= 42:
        xtest[i, :, :] = a[j, :, :]
    elif 56 <= j <= 57:
        xtest[i, :, :] = a[j, :, :]
    elif 76 <= j <= 77:
        xtest[i, :, :] = a[j, :, :]
    elif 86 <= j <= 87:
        xtest[i, :, :] = a[j, :, :]
    elif 98 <= j <= 99:
        xtest[i, :, :] = a[j, :, :]
    elif 102 <= j <= 103:
        xtest[i, :, :] = a[j, :, :]
    else:
        xtrain[m, :, :] = a[j, :, :]


for j in range(5):
    xtrain[j+15,:,:] = b[j,:,:]

ytrain = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])

np.save('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/21115/x_train.npy',xtrain)
np.save('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/21115/y_train.npy',ytrain)

for j in range(2):
    xtest[j, :, :] = a[j + 15, :, :]

for j in range(2):
    xtest[j + 2, :, :] = b[j + 5, :, :]

ytest = np.array([0, 0, 1, 1])

np.save('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/21115/x_test.npy',xtest)
np.save('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/21115/y_test.npy',ytest)


data = np.genfromtxt(('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/Data_Reports/TS#11_020119/ANS/11_02_01_19_18_02_000_apcr2_2apcr2.csv'), delimiter=',', skip_header=4)
var = []
var = data[:, 1:]
tims[1, :, :] = var
w.append(int(1))