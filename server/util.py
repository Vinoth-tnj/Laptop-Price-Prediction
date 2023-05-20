import pickle
import json
import numpy as np

__manufacturer = None
__category = None
__screen = None
__cpu = None
__storage = None
__gpu = None
__data_columns = None
__model = None

def get_estimated_price(screen_size,ram,manufaturer,category,screen,cpu,storage,gpu):
    try:
        manufaturer_index = __data_columns.index(manufaturer.lower())
        category_index = __data_columns.index(category.lower())
        screen_index = __data_columns.index(screen.lower())
        cpu_index = __data_columns.index(cpu.lower())
        storage_index = __data_columns.index(storage.lower())
        gpu_index = __data_columns.index(gpu.lower())
    except:
        manufaturer_index = -1
        category_index = -1
        screen_index = -1
        cpu_index = -1
        storage_index = -1
        gpu_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = screen_size
    x[1] = ram
    if manufaturer_index >= 0:
        x[manufaturer_index] = 1
    if category_index >= 0:
        x[category_index] = 1
    if screen_index >= 0:
        x[screen_index] = 1
    if cpu_index >= 0:
        x[cpu_index] = 1
    if storage_index >= 0:
        x[storage_index] = 1
    if gpu_index >= 0:
        x[gpu_index] = 1

    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __manufacturer
    global __category
    global __screen
    global __cpu
    global __storage
    global __gpu

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __manufacturer = __data_columns[2:21]
        __category = __data_columns[21:27]
        __screen = __data_columns[27:65]
        __cpu = __data_columns[65:171]
        __storage = __data_columns[171:269]
        __gpu = __data_columns[269:305]# first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/laptops_price_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_manufacturer_names():
    return __manufacturer

def get_category_names():
    return __category

def get_screen_names():
    return __screen

def get_cpu_names():
    return __cpu

def get_storage_names():
    return __storage

def get_gpu_names():
    return __gpu

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_manufacturer_names())
    print(get_category_names())
    print(get_screen_names())
    print(get_cpu_names())
    print(get_storage_names())
    print(get_gpu_names())
    print(get_estimated_price(15.6,8,'HP','Notebook','Full HD 1920x1080','Intel Core i5 7200U 2.5GHz','256 GB SSD','Intel HD Graphics 620'))
    print(get_estimated_price(15.6,8,'HP','Notebook','Full HD 1920x1080','Intel Core i5 7200U 2.5GHz','256 GB SSD','Intel HD Graphics 620')) # other location
    print(get_estimated_price(15.6,8,'HP','Notebook','Full HD 1920x1080','Intel Core i5 7200U 2.5GHz','256 GB SSD','Intel HD Graphics 620'))  # other location
