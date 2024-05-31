import random

class PasswordGenerator:
  def __init__(self, length=12):
    self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    self.length = length
    
  def generate(self):
    return ''.join(random.choice(self.characters) for i in range(self.length))

class PasswordChecker:
  def __init__(self, password):
    self.password = password
    self.criteria = Criteria(password)

  def calculate_strength(self):
    return sum(self.criteria.criterium_list)

class Criteria:
  def __init__(self, password):
    self.length = len(password) >= 8
    self.lowercase = any(char.islower() for char in password)
    self.uppercase = any(char.isupper() for char in password)
    self.digit = any(char.isdigit() for char in password)
    self.special = any(char in "!@#$%^&*()" for char in password)
    self.criterium_list = (self.length, 
                     self.lowercase, 
                     self.uppercase, 
                     self.digit, 
                     self.special)

password_generator = PasswordGenerator(length=12)
password = password_generator.generate()
print("Generated password:", password)

password_checker = PasswordChecker(password=password)
password_strength = password_checker.calculate_strength()
print("Password strength:", password_strength)