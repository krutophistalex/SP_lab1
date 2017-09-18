# Program Search_Number
import random

r_number = random.randint(1,100)
print('Добро пожаловать в игру "Угадай число"')
print('Число загадано')

while True :
      user_in = int(input())
      if user_in == r_number:
            print("Вы угадали число", user_in, "Загаданое число = ", r_number)
            break
      elif user_in < r_number:
            print("Ваше число меньше")
      elif user_in > r_number:
            print("Ваше число больше")
            
            

