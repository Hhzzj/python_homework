from .entity.person import Person

def get_people_list(read_list):
    assert type(read_list)==list

    people_list=[]
    for i in range(len(read_list)):
        people_list.append(Person(read_list[i][0], read_list[i][1], read_list[i][2]))
    return people_list