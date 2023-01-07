import json


def prepare_table_data(table_data):
    tables = {}
    for item in table_data:
        with open(item.data.url[1:], 'r') as file:
            table = json.load(file)
            table = dict(list(table.items())[:item.max_rows])
            tables[item] = table
    return tables
