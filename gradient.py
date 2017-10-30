# -*- coding: utf8 -*-
import pandas as pd
import numpy as np
import functools as ft

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
        print("day = {}, col = {}".format(day, col))
        row_start = Measure.DayStride * day
        return self.data_frame.iloc[row_start: row_start+Measure.DayStride, Measure.HourField+col]


measure = Measure()
df = measure.convert_data()
d1 = measure.get_row_data(2*Measure.DayStride + Measure.RainFallField)


def w_loss(w,x,b,y_hat):
    y_star = sum(np.add(np.dot(w, x), b))
    return pow(y_hat - y_star, 2)

def b_loss(b,x,w,y_hat):
    y_star = sum(np.add(np.dot(w, x), b))
    return pow(y_hat - y_star, 2)

def partial_difference_quotient(f, v, i, h):
    """計算 f 在 v 中第 i 個元素所對應的差商"""
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


"""learning rate"""
eta = 0.001
w = list([0])
b = list([0])
y = list([0])

for day in range(30):
    for hour in range(24):
        for k, _ in enumerate(range(len(w))):
            data = list(measure.get_column_data(day, hour))
            x = [int(data[9])]
            w_fn = ft.partial(w_loss, y_hat=x[k], x=x, b=b)
            dw = partial_difference_quotient(w_fn, w, k, 0.001)

            b_fn = ft.partial(b_loss, y_hat=x[k], w=w, x=x)
            db = partial_difference_quotient(b_fn, b, k, 0.001)

            w[k] = w[k] - eta * dw
            b[k] = b[k] - eta * db
            y = x

print("w = {}, b = {}".format(w,b))