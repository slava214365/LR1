users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

total_sum = len(users)
unique_numbers = set(users)
unique_sum = len(unique_numbers)

statist = {
    'Общее количество': total_sum,
    'Уникальные посещения': unique_sum,
}

print(statist)
