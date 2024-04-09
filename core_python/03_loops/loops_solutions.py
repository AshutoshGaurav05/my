# Answer 1
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print("Final count of Positive number is: ",positive_number_count)

# Answer 2
# n = int(input("Enter the number: "))
# sum_even = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += i   
# print("Sum of even numbers is: ",sum_even)

# Answer 3
# number = int(input("Enter the number: "))
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(f"{number} x {i} = {number*i}")

# Answer 4
# input_string = input("Enter the string: ")
# reversed_string = ""
# for char in input_string:
#     reversed_string = char + reversed_string
# print("Reversed string is:",reversed_string)

# Answer 5
# input_string = input("Enter the string: ")
# for char in input_string:
#     if input_string.count(char) == 1:
#         print(f"First non-repeating character is: {char}")
#         break
    
# Answer 6
# number = int(input("Enter the number: "))
# factorial = 1
# while number > 0:
#     # factorial = factorial*number
#     # number = number - 1
#     factorial *= number
#     number -= 1
# print("Factorial of the number is: ",factorial)

# Answer 7
# while True:
#     number = int(input("Enter value b/w 1 to 10: "))
#     if 1 <= number <= 10:
#         break
#     else:
#         print("Invalid input, please try again")

# Answer 8
# number = int(input("Enter the number: "))
# is_prime = True
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             print(f"{number} is not a prime number")
#             break
# if is_prime:
#     print(f"{number} is a prime number")

# Answer 9
# items = ["Apple", "Banana", "Orange", "Grapes", "Pineapple","Apple"]
# unique_items = set()
# for item in items:
#     if item in unique_items:
#         print("Duplicate: ", item)
#         break
#     unique_items.add(item)


# Answer 10
import time

wait_time = 1
max_retries = 5 
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts+1} - Waiting for {wait_time} seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1