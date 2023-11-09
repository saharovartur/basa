from datetime import datetime
import time
import random

#Создаем список из чисел
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
            21, 23, 25, 27, 29, 31, 33, 35, 37,
            39, 41, 43, 45, 47, 49, 51, 53, 55,
          57, 59]
#С помощью цикла выводим if/else заданное количество раз через range
for i in range(5):
    right_this_minute = datetime.today().minute #Задаем точечную нотацию(секунды)
    if right_this_minute in odds:
        print("четное число")
        
    else:
        print('нечетное число минут')
##    
##    wait_time = random.randint(1, 60) #Получаем рандомное число в диапозоне()
##    time.sleep(wait_time) #Приказываем остановить программу на рандомное количество сек.





