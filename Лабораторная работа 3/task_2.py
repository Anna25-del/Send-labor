# TODO Напишите функцию find_common_participants
def find_common_participants (group_1, group_2, sep=','):
    first_group = set(group_1.split(sep))
    second_group = group_2.split(sep)
    common_set = first_group.intersection(second_group)
    common_list = []
    for i in common_set:
        common_list.append(i)
    common_list = list(common_list)
    common_list.sort()
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, sep="|")
print("Общие участники:", common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
