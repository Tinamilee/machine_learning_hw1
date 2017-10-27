# -*- coding: utf8 -*-
import pandas as pd

class Measure:
    HourField = 3
    DateField = 0
    ItemNameField = 2
    RainFallField = 10
    DayStride = 18
    def __init__(self):
        file = "/Users/tom/Downloads/train.csv"
        df = pd.read_csv(file, encoding='utf-8')
        self.data_frame = df
        # print("shape() = {}".format(df.shape))
        # print(df.iloc[Measure.DayStride:Measure.DayStride*2, 0:4])
        # print('----')
        # print ("type = {}".format(type(df.iloc[:,0])))
        # print('----')

    def convert_data(self):
        """convert RAINFALL NR to 0"""
        df = self.data_frame
        rows,cols = df.shape
        for r in range(rows):
            if df.iloc[r, 2] == 'RAINFALL':
                for c in range(3, cols):
                    if df.iloc[r, c] == 'NR':
                        df.iloc[r, c] = 0
        return df


    def get_row_data(self, row, start=0, end=27):
        return self.data_frame.iloc[row, Measure.HourField+start:Measure.HourField+end]

    def get_column_data(self, day, col=0):
        row_start = Measure.DayStride * day
        return self.data_frame.iloc[row_start: row_start+Measure.DayStride, Measure.HourField+col]


measure = Measure()
df = measure.convert_data()
d1 = measure.get_row_data(2*Measure.DayStride+Measure.RainFallField)
print(d1)



