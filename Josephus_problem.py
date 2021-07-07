def Josephus_problem(people_nums, death_gap):
    death_gap=death_gap%people_nums
    people_list = list(range(1, people_nums+1))
    death_list = []
    death_index = 0

    if people_nums==1 or death_gap==1:
        death_list = people_list

    while(len(people_list)>1):
        death_index = (death_index+death_gap-1) % len(people_list)
        death_list.append(people_list.pop(death_index))
    print(death_list)

    return death_list


if __name__ == '__main__':
    Josephus_problem(41, 3)
