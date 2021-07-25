from usecase.read_different_types_files import ZipReader
from usecase.read_different_types_files import CsvReader
from usecase.read_different_types_files import ExcelReader
from usecase.get_people_list import get_people_list
from usecase.entity.josephus import JosephusCircle
from usecase.entity.person import Person

class JosephusCircleSys():
    def __init__(self):
        self.people_list = []

    def add_person_to_people_list_by_hand(self):
        last_name = input("请输入人员的姓：")
        first_name = input("请输入人员的名：")
        id = input("请输入人员编号：")

        self.people_list.append(Person(last_name, first_name, id))
        print("人员信息录入成功")
        return self.people_list

    def get_people_list_by_excel(self):
        reader = ExcelReader(r"src\usecase\entity\peopledata\lastname&firstname&id.xls")
        read_list = reader.read()
        self.people_list = get_people_list(read_list)
        print("人员信息录入成功")
        return self.people_list

    def get_people_list_by_csv(self):
        reader = CsvReader(r"src\usecase\entity\peopledata\lastname&firstname&id.csv")
        read_list = reader.read()
        self.people_list = get_people_list(read_list)
        print("人员信息录入成功")
        return self.people_list

    def get_people_list_by_zip(self):
        reader = ZipReader(r"src\usecase\entity\peopledata\lastname&firstname&id.zip",
                           "lastname&firstname&id.csv")
        read_list = reader.read()
        self.people_list = get_people_list(read_list)
        print("人员信息录入成功")
        return self.people_list

    def show_josephus_circle(self):
        self.josephus_circle = JosephusCircle(self.people_list, 3, 3)
        for person in self.josephus_circle:
            print(person.__str__())
        return self.josephus_circle


def run():
    manager = JosephusCircleSys()
    while True:
        menu = """
                约瑟夫环管理系统
            1. 手动录入人员信息列表
            2. 通过excel文件录入人员信息列表
            3. 通过csv文件录入人员信息列表
            4. 通过zip文件录入人员信息列表
            5. 查看约瑟夫环信息
            6. 退出
                请输入正确的选择:"""

        choice = input(menu)
        if choice == '1':
            manager.add_person_to_people_list_by_hand()
        elif choice == '2':
            manager.get_people_list_by_excel()
        elif choice == '3':
            manager.get_people_list_by_csv()
        elif choice == '4':
            manager.get_people_list_by_zip()
        elif choice == '5':
            manager.show_josephus_circle()
        elif choice == '6':
            exit(0)
        else:
            print("请输入正确的选择!")