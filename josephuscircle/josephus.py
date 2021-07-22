import pandas as pd
import zipfile

class Reader(object):
    def __init__(self,filepath):
        self.filepath = filepath
    
    def read(self):
        pass


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

class Person(object):
    def __init__(self, last_name, first_name, id):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id

    def __str__(self):
        return "姓:%s 名:%s 编号:%s" %(self.last_name, self.first_name, self.id)

class JosephusCircle():
    def __init__(self, people_list, interval, start_pos):
        assert type(people_list)==list  and type(interval)==int and type(start_pos)==int
        assert interval > 0
        self.people_list = people_list
        self.interval = interval
        self.start_pos = start_pos
    
    def __iter__(self):
        return self 

    def __next__(self):
        if len(self.people_list)>0:
            out_pos = (self.start_pos+self.interval-1) % len(self.people_list)
            self.out_person = self.people_list.pop(out_pos)
            self.start_pos = out_pos
            return self.out_person
        else:
            raise StopIteration

def get_people_list(read_list):
    assert type(read_list)==list

    people_list=[]
    for i in range(len(read_list)):
        people_list.append(Person(read_list[i][0], read_list[i][1], read_list[i][2]))
    return people_list


if __name__ == '__main__':
    #reader = ExcelReader("resources\lastname&firstname&id.xls")
    #reader = CsvReader("resources\lastname&firstname&id.csv")
    reader = ZipReader("resources\lastname&firstname&id.zip","lastname&firstname&id.csv")

    read_list = reader.read()
    people_list = get_people_list(read_list)
    
    josephus_circle = JosephusCircle(people_list,3,3)

    for person in josephus_circle:
        print(person.__str__())
