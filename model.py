import numpy as np
import pandas as pd
from pandas import to_datetime
from scipy.optimize import minimize

file1 = 'inter_date_num.txt'
data1 = pd.read_csv(file1, delimiter=' ', header=None, names=['X', 'Y'])
sub_time = [int(x) for x in data1['X']]
sub_cnt = [int(y) for y in data1['Y']]

file2 = 'date_type.txt'
data2 = pd.read_csv(file2, delimiter=',', header=None, names=['X', 'Y'])
event_time = [int(x) for x in data2['X']]
event_type = [int(y) for y in data2['Y']]

timestamps_subscribers = np.array([[x, y] for x, y in zip(sub_time, sub_cnt)])
timestamps_events = np.array([[x, y] for x, y in zip(event_time, event_type)])

def loss_function(coefficients):
    total_subscribers = np.zeros(len(timestamps_subscribers)) + timestamps_subscribers[0][1]

    for i, (t, subscribers) in enumerate(timestamps_subscribers):
        for j, (event_time, event_type) in enumerate(timestamps_events):
            if t < event_time:
                continue
            if event_time <= t:
                total_subscribers[i] += coefficients[j]
            if event_time + 86400 <= t:
                total_subscribers[i] += coefficients[j + len(timestamps_events[:, 1])]

    return np.sum((total_subscribers - timestamps_subscribers[:, 1]) ** 2)

num_event_types = len(timestamps_events[:, 1])
initial_coefficients = np.zeros(num_event_types * 2)
bounds = [(0, None)] * len(initial_coefficients)

result = minimize(loss_function, initial_coefficients, bounds=bounds)
final_coefficients = result.x

for event_type in range(num_event_types):
    print(f"Коэффициенты для события {event_type+1}:")
    print(f"  День события: {final_coefficients[event_type]:.2f}")
    print(f"  Следующий день: {final_coefficients[event_type + num_event_types]:.2f}")

def get_coefficients():
    return final_coefficients
