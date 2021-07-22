import pandas as pd
import zipfile

from .entity.reader import Reader

class ExcelReader(Reader):
    def __init__(self, filepath):
        assert filepath.endswith('.xls') or filepath.endswith('.xlsx') 
        self.filepath = filepath

    def read(self):
        people_data = pd.read_excel(self.filepath)
        list = people_data.values.tolist()
        return list


class CsvReader(Reader):
    def __init__(self, filepath):
        assert filepath.endswith('.csv') 
        self.filepath = filepath

    def read(self):
        people_data = pd.read_csv(self.filepath)
        list = people_data.values.tolist()
        return list
   

class   ZipReader(Reader):
    def __init__(self, filepath, inner_filename):
        assert filepath.endswith('.zip')
        assert inner_filename.endswith('.xls') or inner_filename.endswith('.xlsx') or inner_filename.endswith('.csv')
        self.filepath = filepath
        self.inner_filename = inner_filename

    def read(self):
        with zipfile.ZipFile(self.filepath, 'r') as file:
            inner_file = file.open(self.inner_filename)
            if(self.inner_filename.endswith('.csv')):
                people_data = pd.read_csv(inner_file)
            elif(self.inner_filename.endswith(".xls") or self.inner_filename.endswith(".xlsx")):
                people_data = pd.read_excel(inner_file)
            list = people_data.values.tolist()
            inner_file.close()
        return list







