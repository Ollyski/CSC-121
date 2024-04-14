class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        self.annual_salary += raise_amount

import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee("John", "Doe", 60000)
        self.employee2 = Employee("Jane", "Smith", 70000)

    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, 65000)

    def test_give_custom_raise(self):
        self.employee2.give_raise(10000)
        self.assertEqual(self.employee2.annual_salary, 80000)

if __name__ == '__main__':
    unittest.main()