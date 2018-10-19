import sys
import pandas as pd
import numpy as np

name = sys.argv[1]
package = 'D:\\2018BK\\overfit\\'
model_path = package + name

try:
    f = open(package + name)
    model_coefficient = f.read()
    x = model_coefficient.split('\n')
    x = x[1:len(x) - 1]
    x = [float(str.split(":")[-1].split(",")[0]) for str in x]
    x = np.matrix(x)
    f.close()

    matrix = [int(sys.argv[i]) for i in range(2, len(sys.argv))]
    test_data = np.matrix(matrix)
    test_data.shape = [-1, 1]
    if x.shape[1] != test_data.shape[0]:
        print "valuesError:shapes " + "{}".format(x.shape) + " and " + "{}".format(test_data.shape) + " not equals."
    else:
        result = (x * test_data)[0, 0]
        print result
except IOError:
    print "no such model file:" + model_path


