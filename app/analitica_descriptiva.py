import datetime
import pandas as pd
import numpy as np
import csv

def update(file_name):
    data = data_read(file_name)

    function_MAX(data, file_name)
    function_MIN(data, file_name)
    function_MED(data, file_name)
    function_AVG(data, file_name)
    function_DEV(data, file_name)
    function_VAR(data, file_name)
    
    data_to_graph = data_read(file_name)
    return data_to_graph


def function_MAX(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    temperature_values = data[data["sensor"] == "Temperatura"]["value"]
    
    max_values = max(temperature_values)

    data_to_save = [1, date_string, "Maximo", max_values]
    to_save(data_to_save, file_name)


def function_MIN(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    temperature_values = data[data["sensor"] == "Temperatura"]["value"]
    
    min_values = min(temperature_values)

    data_to_save = [1, date_string, "Minimo", min_values]
    to_save(data_to_save, file_name)


def function_MED(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    temperature_values = data[data["sensor"] == "Temperatura"]["value"]
    
    med_value = np.median(temperature_values)

    data_to_save = [1, date_string, "Mediana", med_value]
    to_save(data_to_save, file_name)


def function_AVG(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    temperature_values = data[data["sensor"] == "Temperatura"]["value"]
    
    avg_value = np.mean(temperature_values)

    data_to_save = [1, date_string, "Promedio", avg_value]
    to_save(data_to_save, file_name)


def function_DEV(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    temperature_values = data[data["sensor"] == "Temperatura"]["value"]
    
    dev_value = np.std(temperature_values)

    data_to_save = [1, date_string, "Desviacion", dev_value]
    to_save(data_to_save, file_name)


def function_VAR(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    temperature_values = data[data["sensor"] == "Temperatura"]["value"]
    
    var_value = np.var(temperature_values)

    data_to_save = [1, date_string, "Varianza", var_value]
    to_save(data_to_save, file_name)


def data_read(file_name):
    data = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return data


def to_save(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)
