class Person(object):
    def __init__(self, last_name, first_name, id):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id

    def __str__(self):
        return "姓:%s 名:%s 编号:%s" %(self.last_name, self.first_name, self.id)

