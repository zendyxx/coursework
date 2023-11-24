import csv
import datetime

events = []
people_by_date = {}
types_of_events = {}

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
                events.append(dt)
                types_of_events[dt] = row[0]

with open('ds.csv', 'r', newline='') as file2:
    csvreader2 = csv.reader(file2)
    for row in csvreader2:
        info_str = row[0].strip()
        date_str, nm = info_str.split()
        date_str = date_str.strip('.')
        day, month, year = [int(part) for part in date_str.split('.')]
        dt = datetime.datetime(year, month, day)
        people_by_date[dt] = nm