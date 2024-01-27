import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import to_datetime
from datetime import datetime, timedelta
from scipy.optimize import minimize

file1 = 'inter_date_num.txt'
data1 = pd.read_csv(file1, delimiter=' ', header=None, names=['X', 'Y'])
sub_time = [int(x) for x in data1['X']]
sub_cnt = [int(y) for y in data1['Y']]

file2 = 'date_type.txt'
data2 = pd.read_csv(file2, delimiter=',', header=None, names=['X', 'Y'])
event_time = [int(x) for x in data2['X']]
event_type = [int(y) for y in data2['Y']]

start = to_datetime(min(sub_time), unit='s')
finish = to_datetime(max(sub_time), unit='s')

timestamps_subscribers = np.array([[x, y] for x, y in zip(sub_time, sub_cnt)])
timestamps_events = np.array([[x, y] for x, y in zip(event_time, event_type)])

def loss_function(coefficients):
    total_subscribers = np.zeros(len(timestamps_subscribers))

    for i, (t, subscribers) in enumerate(timestamps_subscribers):
        for event_time, event_type in timestamps_events:
            if event_time <= t:
                total_subscribers[i] += coefficients[event_type - 1]
            else:
                break

    return np.sum((total_subscribers - timestamps_subscribers[:, 1]) ** 2)


initial_coefficients = np.ones(len(np.unique(timestamps_events[:, 1])))
bounds = [(0, None)] * len(initial_coefficients)

result = minimize(loss_function, initial_coefficients, bounds=bounds)
final_coefficients = result.x
#print("Коэффициенты: ", final_coefficients)
for index, coefficient in enumerate(final_coefficients):
    print(f"Коэффициент {index + 1}: {coefficient:.2f}")

