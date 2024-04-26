import pandas as pd
import matplotlib.pyplot as plt

table_eff = pd.read_csv('table_eff2.txt', sep=',', header=None, names=['Type', 'Efficiency'], skiprows=1)
table_eff['Type'] = pd.to_numeric(table_eff['Type'], errors='coerce').fillna(0).astype(int)
table_eff['Efficiency'] = pd.to_numeric(table_eff['Efficiency'], errors='coerce').fillna(0).astype(int)
date_type = pd.read_csv('date_type.txt', sep=',', header=None, names=['Date', 'Type'])
date_type['Date'] = pd.to_numeric(date_type['Date'], errors='coerce').fillna(0).astype(int)
date_type['Type'] = pd.to_numeric(date_type['Type'], errors='coerce').fillna(0).astype(int)

date_type = date_type.sort_values(by='Date')
date_type['Event_Number'] = range(1, len(date_type) + 1)

type_to_numbers = date_type.groupby('Type')['Event_Number'].apply(list).to_dict()

plot_data = pd.DataFrame()

for event_type, numbers in type_to_numbers.items():
    efficiency = table_eff[table_eff['Type'] == event_type]['Efficiency'].iloc[0]
    for number in numbers:
        temp_df = pd.DataFrame({'Event_Number': [number], 'Efficiency': [efficiency]})
        plot_data = pd.concat([plot_data, temp_df], ignore_index=True)
plot_data = plot_data.sort_values(by='Event_Number')

plt.figure(figsize=(10, 5))
plt.bar(plot_data['Event_Number'], plot_data['Efficiency'], tick_label=plot_data['Event_Number'].astype(int))
plt.xlabel('Номер мероприятия')
plt.ylabel('Эффективность мероприятия')
plt.title('Эффективность мероприятий')
plt.grid(True)

chart_file_path = 'bar2.png'
plt.savefig(chart_file_path)
plt.close()

chart_file_path
