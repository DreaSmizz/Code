import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

raw_data = pd.read_csv('/Users/andreasmith/python/Weightlifting_Prediction/input2.csv',index_col='Name')
data = raw_data.copy(deep=True)

print(data) 

# xpoints = np.array([0, 6])
# ypoints = np.array([0,250])
# plt.plot(xpoints, ypoints)
# plt.show()