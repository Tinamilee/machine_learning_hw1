# -*- coding: utf8 -*-
import pandas as pd

class Measure:
    def __init__(self):
        file = "/Users/tom/Downloads/train.csv"
        df = pd.read_csv(file, encoding='utf-8')
        self.data_frame = df
        print("shape = {}".format(df.shape))
        print(df.iloc[0:4, 0:6])

    def get_measured_data(self, row, hour = 0):
        return self.data_frame.iloc[row, 3+hour:]



measure = Measure()
d1 = measure.get_measured_data(0)
print(d1)
d2 = measure.get_measured_data(1)
print(d2)
