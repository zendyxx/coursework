import pandas as pd
import matplotlib.pyplot as plt
from pandas import to_datetime
from datetime import datetime, timedelta

plt.figure(figsize=(15, 8))

file_path = 'inter_date_num.txt'
data = pd.read_csv(file_path, delimiter=' ', header=None, names=['X', 'Y'])
data_x = [to_datetime(x, unit='s') for x in data['X']]
data_y = [int(y) for y in data['Y']]
plt.plot(data_x, data_y, color='seagreen', lw=4, label='Количество подписчиков')

start = to_datetime(min(data_x), unit='s')
finish = to_datetime(max(data_x), unit='s')
bar_width = 0.8

date_type = pd.read_csv('date_type.txt', sep=',', header=None, names=['Date', 'Type'])
date_type['Type'] = date_type['Type'].astype(int)
date_type['Date'] = [to_datetime(x, unit='s') for x in date_type['Date']]
date_type['Event_Number'] = date_type.index + 1
date_type['Event_Number'] = date_type['Event_Number'].astype(int)

table_coef = pd.read_csv('table_coef.txt', sep=',', header=None, names=['Event_Number', 'Ak', 'Ck'], skiprows=1)
table_coef['Event_Number'] = table_coef['Event_Number'].astype(int)
table_coef['Ak'] = pd.to_numeric(table_coef['Ak'], errors='coerce').fillna(0).astype(int)
table_coef['Ck'] = pd.to_numeric(table_coef['Ck'], errors='coerce').fillna(0).astype(int)
table_coef['Sum'] = table_coef['Ak'] + table_coef['Ck']
merged_data_1 = pd.merge(table_coef, date_type[['Date', 'Event_Number']], on='Event_Number')
merged_data_1.sort_values('Date', inplace=True)
plt.bar(merged_data_1['Date'] - timedelta(days=0.4), merged_data_1['Sum'] + 200, color='red', label='Результаты 1 модели', width=bar_width)

table_eff = pd.read_csv('table_eff2.txt', sep=',', header=None, names=['Type', 'Efficiency'], skiprows=1)
table_eff['Type'] = table_eff['Type'].astype(int)
table_eff['Efficiency'] = table_eff['Efficiency'].astype(int)
merged_data_2 = pd.merge(date_type, table_eff, on='Type')
merged_data_2.sort_values('Date', inplace=True)
plt.bar(merged_data_2['Date'] + timedelta(days=0.4), merged_data_2['Efficiency'] + 200, color='black', label='Результаты 2 модели', width=bar_width)

plt.title('Визуализация рассчитанной эффективности мероприятий')
plt.xlabel('Дата')
plt.ylabel('Количество подписчиков и увеличение их количества')
plt.legend(loc='upper left')

plt.xlim(start - timedelta(days=5), finish + timedelta(days=5))
plt.ylim(200, 1050)

chart_file_path = 'chart_compare.png'
plt.savefig(chart_file_path)
plt.close()

chart_file_path
