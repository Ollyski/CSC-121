class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 3

    def describe_user(self):
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Gandalf", "Greyhame", 0, "john.doe@example.com", "Middle Earth")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login Attempts: {user1.login_attempts}")

user1.reset_login_attempts()

print(f"Login Attempts after reset: {user1.login_attempts}")