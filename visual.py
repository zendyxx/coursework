import pandas as pd
import matplotlib.pyplot as plt
from pandas import to_datetime
from datetime import datetime, timedelta

plt.figure(figsize=(12, 8))

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
data = pd.read_csv(file_path, delimiter=',', header=None, names=['X', 'Type'])
data_x = [to_datetime(x, unit='s') for x in data['X']]
data_types = data['Type'].tolist()

data_y = [1200 for _ in data_x]
plt.bar(data_x, data_y, color='grey', lw=1, label='Events')

# coef_data = pd.read_csv('table_coef.txt', delimiter=',', header=None, names=['Index', 'Num1', 'Num2'])
# coef_data['Sum'] = int(coef_data['Num1']) + int(coef_data['Num2'])
#
# for idx, row in coef_data.iterrows():
#     if idx == 0:
#         continue
#     event_index = int(row['Index']) - 1
#     if 0 <= event_index < len(data_x):
#         plt.bar(data_x[event_index], -row['Sum'], color='red', width=0.02, label='Negative Bar' if idx == 0 else "")

for i, (x, type_text) in enumerate(zip(data_x, data_types)):
    if start <= x <= finish:
        plt.text(x, 1100, str(i+1), rotation=90, ha='center', va='bottom', fontsize=9, color='darkblue')
        plt.text(x, 1150, type_text, rotation=90, ha='center', va='bottom', fontsize=9, color='darkgreen')

plt.text(start - timedelta(days=3), 1100, 'Num', fontsize=10, color='darkblue', ha='left', va='bottom')
plt.text(start - timedelta(days=3), 1150, 'Type', fontsize=10, color='darkgreen', ha='left', va='bottom')

plt.xlim(start - timedelta(days=5), finish + timedelta(days=5))
plt.ylim(-1500, 1250)

plt.title('Data Comparison')
plt.xlabel('Date')
plt.ylabel('Number')
plt.legend(loc='upper right')

chart_file_path = 'chart.png'
plt.savefig(chart_file_path)
plt.close()

chart_file_path
