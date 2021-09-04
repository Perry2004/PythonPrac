import pandas as pd
import numpy as np
import random as rnd

train_df = pd.read_csv('datasets/train.csv')
test_df = pd.read_csv('datasets/test.csv')
combine = [train_df, test_df]

print(train_df.columns.values)

# preview the data
train_df.head()
train_df.tail()

train_df.info()
print('_'*40)
test_df.info()
