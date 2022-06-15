import string
import random

def password_generator():
  how_many = int(input("how many letters/numbers do you want in your password? "))
  
  for i in range(how_many):
    letter = random.choice(string.ascii_letters)
    print(letter.lower(), end="")
    num = str(random.randint(0, 9))
    print(num, end="")
password_generator()