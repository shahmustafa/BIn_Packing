import numpy as np
import string
import pandas as pd

x_train = np.load('archives/mts_archive/ArabicDigits/' + 'x_test.npy')


def using_multiindex(A, columns):
    shape = A.shape
    index = pd.MultiIndex.from_product([range(s) for s in shape], names=columns)
    df = pd.DataFrame({'A': A.flatten()}, index=index).reset_index()
    return df


df = using_multiindex(x_train, list('ZYX'))
# z-samples
# Y-Instances
# x-Paramters
# A-Magnitude
df.to_csv('stacked.csv', index=False)

