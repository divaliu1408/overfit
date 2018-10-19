#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
import matplotlib as mpl
import sys
import pandas as pd

#strname = sys.argv[1]
name = sys.argv[1]
path = "D:\\2018BK\\overfit\\"
x = np.matrix(np.loadtxt(path+name, delimiter=",", skiprows=1, usecols=(1, 2, 3, 4)))
N = x.shape[0]
M = x.shape[1]
A = np.random.rand(M)
A.shape = -1, 1
B = np.random.randn(N)
B.shape = -1, 1
x.sort(0)
y = x * A + B

model = Pipeline([
    ('poly', PolynomialFeatures()),
    ('linear', LinearRegression(fit_intercept=False))])
np.set_printoptions(suppress=True)

model.set_params(poly__degree=1)
model.fit(x, y)
lin = model.get_params('linear')['linear']
print u'系数为：', lin.coef_.ravel()
temp = lin.coef_.ravel()
df = pd.DataFrame(temp)
df.to_csv(path+name[:-4]+"_model.csv")
y_hat = model.predict(x)
s = model.score(x, y)
print "s = ", s, '\n'
x_pot = np.arange(200)
y_pot = y
plt.plot(x_pot, y_pot)
plt.plot(x_pot, y_hat)
plt.savefig(path+name[:-4]+".jpg")

