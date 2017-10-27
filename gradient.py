# -*- coding: utf8 -*-
import pandas as pd

class Measure:
    Hour = 3
    Date = 0
    ItemName = 2
    TotalItems = 18
    def __init__(self):
        file = "/Users/tom/Downloads/train.csv"
        df = pd.read_csv(file, encoding='utf-8')
        self.data_frame = df
        print("shape = {}".format(df.shape))
        print(df.iloc[0:Measure.TotalItems, 0:3])
        print('----')
        print ("type = {}".format(type(df.iloc[:,0])))
        print('----')

    def purify_data(self):
        """convert RAINFALL NR to 0"""
        i,j = self.data_frame.shape

    def get_data(self, row, start=0, end=27):
        return self.data_frame.iloc[row, Measure.Hour+start:Measure.Hour+end]


measure = Measure()
d1 = measure.get_data(0)
measure.purify_data()

