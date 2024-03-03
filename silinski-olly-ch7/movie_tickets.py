age = input("How old are you?")
age = int(age)

if age <= 3:
  print(f"{age} - your ticket is complementary.")

elif age >= 4 and age <13:
  print(f"{age} - your ticket is $10")

elif age >= 13:
  print(f"{age} - your ticket is $15")
