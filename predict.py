import sys
import pandas as pd
import numpy as np

name = sys.argv[1]
package = 'D:\\2018BK\\overfit\\'
model_path = package + name
model_coefficient = pd.read_csv(model_path)
matrix = [int(sys.argv[i]) for i in range(2, len(sys.argv))]
test_data = np.matrix(matrix)
model_coefficient = np.matrix(model_coefficient.values[1:, 1])
test_data.shape = [1, -1]
model_coefficient.shape = [-1, 1]
result = (test_data*model_coefficient+model_coefficient.values[0:, 1])[0, 0]
print result

