import csv
import datetime
import time
from pandas import read_csv
from pandas import to_datetime
from pandas import date_range

date_type_data = []

with open('events.csv', 'r', newline='') as file1:
    csvreader1 = csv.reader(file1)
    next(file1)
    next(file1)
    for row in csvreader1:
        for i in range(len(row)):
            if i != 0 and row[i] != '':
                date_str = row[i].strip('/')
                day, month = [int(part) for part in date_str.split('/')]
                dt = datetime.datetime(2023, month, day)
                unix_dt = time.mktime(dt.timetuple())
                date_type_data.append((unix_dt, int(row[0])))

date_type_data.sort(key=lambda x: x[0])

with open('date_type.txt', 'w') as file_date_type:
    for unix_dt, value in date_type_data:
        file_date_type.write(f"{unix_dt}, {value}\n")

with open('date_num.txt', 'w') as file_date_num:
    with open('ds.csv', 'r', newline='') as file2:
        csvreader2 = csv.reader(file2)
        for row in csvreader2:
            info_str = row[0].strip()
            date_str, nm = info_str.split()
            date_str = date_str.strip('.')
            day, month, year = [int(part) for part in date_str.split('.')]
            dt = datetime.datetime(year, month, day)
            unix_dt = time.mktime(dt.timetuple())
            file_date_num.write(f"{unix_dt}, {int(nm)}\n")

with open('inter_date_num.txt', 'w') as file_inter_date_num:
    with open('date_num.txt', 'r', newline='') as file3:
        def read_data(filename):
            df = read_csv(filename, header=None, names=['timestamp', 'value'])
            df['timestamp'] = to_datetime(df['timestamp'], unit='s')
            return df

        series = read_data(file3)
        series['timestamp'] = to_datetime(series['timestamp'], unit='s')
        series.set_index('timestamp', inplace=True)
        upsampled = series.resample('D').mean()

        new_index = date_range(start=upsampled.index.min(), end=upsampled.index.max(), freq='D')
        interpolated = upsampled.reindex(new_index)
        interpolated.interpolate(method='pchip', inplace=True)

        interpolated = interpolated.reset_index()
        interpolated.rename(columns={'index': 'timestamp'}, inplace=True)
        interpolated['timestamp'] = to_datetime(interpolated['timestamp'], unit='s')
        interpolated['timestamp'] = interpolated['timestamp'].apply(lambda x: time.mktime(x.timetuple()))
        interpolated['value'] = interpolated['value'].astype(int)
        interpolated.to_csv(file_inter_date_num, index=False, sep=' ', header=False)
