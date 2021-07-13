import pandas as pd
import zipfile


class Reader(object):
    def read_excel(filename):
        assert filename != ''
        person_data = pd.read_excel(filename)
        list = person_data.values.tolist()
        return list

    def read_csv(filename):
        assert filename != ''
        person_data = pd.read_csv(filename)
        list = person_data.values.tolist()
        return list

    def read_zip(filename, inner_filename):
        assert filename != ''
        assert inner_filename != ''
        with zipfile.ZipFile(filename, 'r')as z:
            inner_file = z.open(inner_filename)
            person_data = pd.read_csv(inner_file)
            list = person_data.values.tolist()
            inner_file.close()
            z.close()
        return list


class Person(object):
    def __init__(self, last_name, first_name, person_id):
        self.last_name = last_name
        self.first_name = first_name
        self.person_id = person_id


def get_people_list(people_nums, filename, inner_filename=''):
    assert people_nums > 0
    assert filename != ''
    people_list = []

    file_type = filename[-3:]
    if((file_type == "xls") or (file_type == "lsx")):  # excel文件后缀xls或xlsx的倒三位
        read_list = Reader.read_excel(filename)
    elif(file_type == "csv"):
        read_list = Reader.read_csv(filename)
    elif(file_type == "zip"):
        read_list = Reader.read_zip(filename, inner_filename)

    for i in range(people_nums):
        people_list.append(
            Person(read_list[i][0], read_list[i][1], read_list[i][2]))

    return people_list


def josephus_circle(people_list, interval, start_people_id):
    assert people_list != []
    assert interval > 0
    assert 0 < start_people_id <= len(people_list)

    list = []

    for i in range(len(people_list)):  # 根据开始报数人的编号找开始报数人的位置索引
        if(start_people_id == people_list[i].person_id):
            people_index = i
            break

    while(len(people_list)):
        people_index = (people_index+interval-1) % len(people_list)
        list.append(people_list.pop(people_index))

    return list


if __name__ == '__main__':
    people_list = get_people_list(11, "lastname&firstname&id.csv")
    josephus_circle_list = josephus_circle(people_list, 3, 4)

    for people in josephus_circle_list:
        print(people.last_name, people.first_name, people.person_id)
