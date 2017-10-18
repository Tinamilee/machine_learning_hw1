# -*- coding: utf8 -*-
import pandas as pd

fname = "/Users/tom/Downloads/train.csv"
data = pd.read_csv(fname, encoding = 'utf-8')
print(type(data))
print(data)
