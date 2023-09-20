import random

name = input('What is your name? ')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
password = ''
for ch in range(16):
    password += random.choice(chars)
print(f'Hi {name}, your password is: {password}')