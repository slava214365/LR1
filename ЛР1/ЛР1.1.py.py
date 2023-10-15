numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = 4
numbers[missing_index] = 0
sum_of_numbers = sum(numbers)
count_of_numbers = len(numbers)
new_number = sum_of_numbers / count_of_numbers
numbers[missing_index] = new_number

print("Измененный список:", numbers)
