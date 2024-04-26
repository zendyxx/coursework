import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('table_coef.txt', delimiter=',', header=None, names=['Ak', 'Ck', 'Dk'], skiprows=1)
data['Ak'] = pd.to_numeric(data['Ak'], errors='coerce').fillna(0).astype(int)
data['Ck'] = pd.to_numeric(data['Ck'], errors='coerce').fillna(0).astype(int)
data['Dk'] = pd.to_numeric(data['Dk'], errors='coerce').fillna(0).astype(int)
data['Sum'] = data['Ck'] + data['Dk']

plt.figure(figsize=(10, 5))
plt.bar(data['Ak'], data['Sum'], color='blue')
plt.xlabel('Номер мероприятия')
plt.ylabel('Эффективность мероприятия')
plt.title('Эффективность мероприятий')
plt.xlim(20, 50)
plt.grid(True)

chart_file_path = 'bar1.png'
plt.savefig(chart_file_path)
plt.close()

chart_file_path
