import numpy as np
import pandas as pd
from pandas import to_datetime
import matplotlib.pyplot as plt

from model2 import get_coefficients
final_coefficients = get_coefficients()

num_event_types = len(final_coefficients)
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
