import pandas as pd
import matplotlib.pyplot as plt
from pandas import to_datetime
from datetime import datetime, timedelta

plt.figure(figsize=(12, 6))

file_path = 'date_num.txt'
data = pd.read_csv(file_path, delimiter=',', header=None, names=['X', 'Y'])
data_x = [to_datetime(x, unit='s') for x in data['X']]
data_y = [int(y) for y in data['Y']]
plt.scatter(data_x, data_y, c='black', s=50, marker="o", linewidth=1, label='Known Data')

start = to_datetime(min(data_x), unit='s')
finish = to_datetime(max(data_x), unit='s')

file_path = 'inter_date_num.txt'
data = pd.read_csv(file_path, delimiter=' ', header=None, names=['X', 'Y'])
data_x = [to_datetime(x, unit='s') for x in data['X']]
data_y = [int(y) for y in data['Y']]
plt.plot(data_x, data_y, color='seagreen', lw=4, label='Interpolated Data')

file_path = 'date_type.txt'
data = pd.read_csv(file_path, delimiter=',', header=None, names=['X', 'Y'])
data_x = [to_datetime(x, unit='s') for x in data['X']]
data_y = [1200 for i in data_x]
plt.bar(data_x, data_y, color='grey', lw=1, label='Events')

for i, x in enumerate(data_x):
    if start <= x <= finish:
        plt.text(x, 300, str(i+1), rotation=90, ha='center')

plt.xlim(start - timedelta(days=5), finish + timedelta(days=5))
plt.ylim(250, 1050)

plt.title('Data Comparison')
plt.xlabel('Date')
plt.ylabel('Number')
plt.legend()

chart_file_path = 'chart.png'
plt.savefig(chart_file_path)
plt.close()

chart_file_path
