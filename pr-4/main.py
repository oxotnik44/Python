import multiprocessing
from multiprocessing import Process
from datetime import datetime

def exponentiation(queue):
    while True:
        if queue.empty():
            continue
        number, pow = queue.get()
        exponent = number ** pow
        dateTime = datetime.now()
        summanumbers = sum(range(exponent + 1))
        with open("file.txt", "a", encoding='utf8') as file:
            file.write(str(dateTime) + " >> " + str(number) + " ^ " + str(pow) + " = " + str(exponent) + ": Сумма числа от ноля до полученного результата возведения в степени = " + str(summanumbers) + "\n")

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = Process(target=exponentiation, args=(queue,))
    process.start()
    while True:
        try:
            str = input("Через пробел введите число, после чего степень, в которую нужно возвести данное число: ")
            number, pow = (str.split(' '))
            numbercel: int = int(number)
            powcel: int = int(pow)
            datatuple = [numbercel, powcel]
            queue.put(datatuple)
        except:
            print("Возникла ошибка при в вводе данных")