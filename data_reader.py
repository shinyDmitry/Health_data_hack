import pandas as pd
from pathlib import Path


class DataReader:

    def __init__(self, path_to_file: Path):
        self.path_to_file = path_to_file

    def _file_reader(self, seporator: str, name: str):
        dataframe = pd.read_csv(self.path_to_file/name, sep=seporator)
        flag = True if dataframe.shape[1] > 1 else False
        return dataframe, flag

    def csv_reader(self, name: str):
        sep = [';', ',']
        cnt = 0
        for elem in sep:
            dataframe, flag = self._file_reader(seporator=elem, name=name)
            if flag:
                return dataframe