import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.zeros([1500, 5])
location = ['Edmonton', 'Lamont', 'Redwater', 'Birch Cove', 'Smoky Lake', 'Westlock', 'Morinville']

data = pd.DataFrame(data,
                    columns=['Output pressure (kPa)', 'Input pressure (kPa)', 'Motor Vibration', 'Fault', 'Location',
                             'Operating Cost ($USD)', 'Date'])

# Generate locations and input pressures
for i in range(data.shape[0]):
    data.loc[i, 'Input pressure (kPa)'] = np.random.normal(200, 10)
    data.loc[i, 'Location'] = np.random.choice(location)
    data.loc[i, 'Output pressure (kPa)'] = np.random.normal(900, 30)
    data.loc[i, 'Motor Vibration'] = np.random.uniform(40, 60)

# Introduce faults
for i in range(data.shape[0]):
    if i % 225 == 0 and i != 0:
        index = np.random.randint(30, 60)
        data.loc[i:(i + index), 'Output pressure (kPa)'] = 0
        for j in range(i, i + index, 1):
            data.loc[j, 'Motor Vibration'] = np.random.normal(250, 15)

# Identify faults
for i in range(data.shape[0]):
    if data.loc[i, 'Output pressure (kPa)'] == 0:
        data.loc[i, 'Fault'] = 1

data.to_csv('datasets/dataset.csv', sep=',')
