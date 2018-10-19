#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    path = "D:\\2018BK\\overfit\\"+name

    # pandas读入
    data = pd.read_csv(path)    # TV、Radio、Newspaper、Sales
    print(data)
    
    x = data[['0', '1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39']]
    # x = data[['TV', 'Radio']]
    y = data[['40']]
    print(x)
    print(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1) 
    print('x_test',x_test)

    # print x_train, y_train
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    print(model)
    print("系数为:",linreg.coef_)
    print(linreg.intercept_)

    y_hat = linreg.predict(np.array(x_test))

    t = np.arange(len(x_test))
    print(t)
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
    plt.savefig(path[:-3]+"jpg")