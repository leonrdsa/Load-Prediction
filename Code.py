# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:32:17 2021

@author: Lab716A
"""

from matplotlib import pyplot as plt
import numpy as np

import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
file = pd.read_excel('Final/Actuals.xlsx',parse_dates=['Time'])

# df = file.set_index('Time')

# df[month] = df.month

# file['month'] = file.index.month
plt.plot(file["Load (kW)"])

rolling_mean = file["Load (kW)"].rolling(window = 12).mean()
rolling_std = file["Load (kW)"].rolling(window = 12).std()

# plt.plot(file["Load (kW)"], color = 'blue', label = 'Original')
plt.plot(rolling_mean, color = 'red', label = 'Rolling Mean')
plt.plot(rolling_std, color = 'black', label = 'Rolling Std')
plt.legend(loc = 'best')
plt.title('Rolling Mean & Rolling Standard Deviation')
plt.show()

#adfuller statistic
result = adfuller(file['Load (kW)'])
print('ADF Statistic: {}'.format(result[0]))
print('p-value: {}'.format(result[1]))
print('Critical Values:')
for key, value in result[4].items():
    print('\t{}: {}'.format(key, value))