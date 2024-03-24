class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("Katie", "Sweet", 32, "KSweet@gmail.com", "New York")
user2 = User("Elrond", "Peredhel", 23000, "Coolguy@gmail.com", "Rivendell")
user3 = User("Peregrin", "Took", 50, "partyguy@gmail.com", "The Shire")

user1.describe_user()
user1.greet_user()

print("\n")

user2.describe_user()
user2.greet_user()

print("\n")

user3.describe_user()
user3.greet_user()