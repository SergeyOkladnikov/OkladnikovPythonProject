import json


def open_table_data(table_data):
    tables = {}
    for item in table_data:
        with open(item.data.url[1:], 'r') as file:
            table = json.load(file)
            table = dict(list(table.items())[:item.max_rows])
            tables[item] = table
    return tables


def open_table_series_data(table_series_data):
    series_set = {}
    for series in table_series_data:
        with open(series.data.url[1:], 'r') as file:
            tables = json.load(file)
            series_set[series] = tables

    return series_set
