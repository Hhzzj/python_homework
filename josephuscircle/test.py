from typing import Iterable
from josephus import Person
from josephus import JosephusCircle
from josephus import ExcelReader
from josephus import CsvReader
from josephus import ZipReader
from josephus import get_people_list

import unittest

CORRECT_LIST = [['A','a',1],['B','b',2],['C','c',3],['D','d',4],['E','e',5],['F','f',6],['G','g',7],['H','h',8],['I','i',9],['J','j',10],['K','k',11]]

class TestPerson(unittest.TestCase):
    def test_show_str(self):
        person=Person('A','a',1)
        self.assertEqual("姓:A 名:a 编号:1",person.__str__())

class TestJosephusCircle(unittest.TestCase):
    def setUp(self):
        people_list = get_people_list(CORRECT_LIST)
        self.josephus_circle_eg = JosephusCircle(people_list, 3, 3)

    def test_eg_iterable(self):
        if isinstance(self.josephus_circle_eg,Iterable):
            correct_id = [6,9,1,4,8,2,7,3,11,5,10]
            for i in range(len(correct_id)):
                for person in self.josephus_circle_eg:
                    self.assertEqual(correct_id[i], person.id)
                    break
        else:
            print("JosephusCircle类不能正确生成可迭代的约瑟夫环对象")

class TestExcelReader(unittest.TestCase):
    def test_excel_reader(self):
        read_list = ExcelReader("resources\lastname&firstname&id.xls").read()
        self.assertEqual(CORRECT_LIST,read_list)

class TestCsvReader(unittest.TestCase):
    def test_csv_reader(self):
        read_list = CsvReader("resources\lastname&firstname&id.csv").read()
        self.assertEqual(CORRECT_LIST,read_list)

class TestZipReader(unittest.TestCase):
    def test_zip_reader(self):
        read_list = ZipReader("resources\lastname&firstname&id.zip","lastname&firstname&id.csv").read()
        self.assertEqual(CORRECT_LIST,read_list)

if __name__ == '__main__':
    unittest.main()
