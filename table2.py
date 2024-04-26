import numpy as np
import pandas as pd
from pandas import to_datetime
import matplotlib.pyplot as plt

from model2 import get_coefficients
final_coefficients = get_coefficients()
num_event_types = len(final_coefficients)

file1 = 'inter_date_num.txt'
data1 = pd.read_csv(file1, delimiter=' ', header=None, names=['X', 'Y'])
sub_time = [int(x) for x in data1['X']]
sub_cnt = [int(y) for y in data1['Y']]

file2 = 'date_type.txt'
data2 = pd.read_csv(file2, delimiter=',', header=None, names=['X', 'Y'])
event_time = [int(x) for x in data2['X']]
event_type = [int(y) for y in data2['Y']]

min_time = min(sub_time)
max_time = max(sub_time)

check_index = np.zeros(len(final_coefficients) + 1)
for i in range(len(event_time)):
    if min_time <= event_time[i] <= max_time:
        check_index[event_type[i]] = 1

for i in range(num_event_types):
    if check_index[i+1] == 0:
        final_coefficients[i+1][1] = 0

data = []

for event_type in range(num_event_types):
    data.append({
        'Тип мероприятия': int(final_coefficients[event_type][0]),
        'Эффективность': int(final_coefficients[event_type][1]),
    })

df = pd.DataFrame(data)
df.to_csv('table_eff2.txt', index=False)

fig, ax = plt.subplots(figsize=(10, 0.5 * len(df) - 10))
ax.axis('tight')
ax.axis('off')
cell_text = [[str(int(item)) if i == 0 else item for i, item in enumerate(row)] for row in df.values]
the_table = ax.table(cellText=cell_text, colLabels=df.columns, cellLoc='center', loc='center')
plt.subplots_adjust(left=0.05, right=0.95, top=1, bottom=0, hspace=0, wspace=0)

plt.savefig('table_image2.png', dpi=300, bbox_inches='tight')
