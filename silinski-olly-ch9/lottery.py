import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_numbers = random.sample(lottery_pool[:10], 4) + random.sample(lottery_pool[10:], 1)

user_input = input("Enter your lottery number (four numbers and one letter): ")

user_numbers = [int(num) for num in user_input[:-1]]
user_letter = user_input[-1]

if user_numbers == [2, 2, 2, 2] and user_letter == 'b':
    print("WOOO YOU WON!!!")
else:
    print("Boooo, you didn't win ):")