import random
CHARS1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHARS2 = "abcdefghijklmnopqrstuvwxyz"


class people:
    def __init__(self, last_name, first_name, people_id):
        self.last_name = last_name
        self.first_name = first_name
        self.people_id = people_id


def get_name(CHARS):  # 随机两个大写/小写字母作为姓/名
    assert CHARS != ''
    name = ''
    for i in range(2):
        name += random.choice(CHARS)
    return name


def get_people_list(people_nums):
    assert people_nums > 0
    people_list = []
    for i in range(people_nums):
        last_name = get_name(CHARS1)  # 随机两个大写字母作为姓
        first_name = get_name(CHARS2)  # 随机两个小写字母作为名
        people_id = i+1  # 从1开始给每个人编号
        people_list.append(people(last_name, first_name, people_id))
    return people_list


def josephus_circle(people_nums, interval, start_people_id):
    assert people_nums > 0
    assert interval > 0
    assert 0 < start_people_id <= people_nums

    people_list = get_people_list(people_nums)
    josephus_circle_list = []

    for i in range(len(people_list)):  # 根据开始报数人的编号找开始报数人的位置索引
        if(start_people_id == people_list[i].people_id):
            people_index = i
            break

    while(len(people_list)):
        people_index = (people_index+interval-1) % len(people_list)
        josephus_circle_list.append(people_list.pop(people_index))

    return josephus_circle_list


if __name__ == '__main__':
    josephus_circle_list = josephus_circle(11, 3, 4)

    for people in josephus_circle_list:
        print(people.last_name, people.first_name, people.people_id)
