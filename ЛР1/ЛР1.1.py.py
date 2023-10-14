numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0  ## Не знаю, как можно заменить, не считая руками
unique_numbers = set(numbers)
sum_of_numbers = sum(unique_numbers)
count_of_numbers = len(unique_numbers)
new_number = sum_of_numbers / count_of_numbers
numbers[4] = new_number

print("Измененный список:", numbers)
