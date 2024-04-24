# Исследование эффективности маркетинговых мероприятий при неточной атрибуции

## Описание проекта

Данный репозиторий содержит код курсовой работы, цель которой заключается в оценке эффективности маркетинговых мероприятий на основе изменения числа подписчиков в социальных сетях. В работе рассматриваются данные о подписчиках (файл ds.csv) и информация о мероприятиях (файл events.csv). Осуществляется обработка данных, их интерполяция для заполнения пропущенных значений и анализ влияния маркетинговых мероприятий посредством двух различных моделей.

## Структура репозитория

main.py - основной скрипт для обработки и интерполяции данных.
model.py - первая модель, рассчитывающая коэффициенты влияния мероприятий на количество подписчиков в день мероприятия (A) и на следующий день (C).
visual.py - скрипт для визуализации результатов модели.
table.py - скрипт для создания итоговой таблицы коэффициентов.
model2.py - вторая модель, основанная на сложной непрерывной функции для оценки долгосрочного влияния мероприятий.
table2.py - скрипт для создания таблицы с результатами интеграции функции второй модели.
ds.csv - данные о количестве подписчиков.
events.csv - данные о мероприятиях.
inter_date_num.txt, date_type.txt - результаты обработки данных.
chart.png, table_image.txt, table_image2.txt - визуализации и итоговые таблицы результатов.
