import os
from config import DataConfig
from data_reader import DataReader


if __name__ == '__main__':

    config = DataConfig()

    data_reader = DataReader(config.data_path)

    files = os.listdir(config.data_path)
    files = files[1:]

    isFirst = True
    for elem in files:
        if isFirst:
            data = data_reader.csv_reader(elem)
        else:
            tmp = data_reader.csv_reader(elem)
            data = data.merge(tmp, left_on='idx', right_on='idx', how='inner')

    print(data.head())
    data.to_csv('test.csv')
