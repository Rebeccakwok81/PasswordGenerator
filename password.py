#Create a random password generator
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(()_-=+"


pwd_length = int(input("What length would you like your password to be: "))
password = ""

for x in range(0,pwd_length):
    password_char = random.choice(chars)
    password = password + password_char
print("Here is your password: ", password)