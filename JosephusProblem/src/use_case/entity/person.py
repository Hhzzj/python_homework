class Person(object):
    def __init__(self, last_name, first_name, id):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id

    def __str__(self):
        return "姓:%s 名:%s 编号:%s" %(self.last_name, self.first_name, self.id)

def get_people_list(read_list):
    assert type(read_list)==list

    people_list=[]
    for i in range(len(read_list)):
        people_list.append(Person(read_list[i][0], read_list[i][1], read_list[i][2]))
    return people_list