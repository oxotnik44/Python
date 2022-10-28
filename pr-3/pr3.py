import multiprocessing
from multiprocessing import Process
from random import randint
from typing import List
from RandomWordGenerator import RandomWord
import os

def create(num: int, quantity: int):
    Random = RandomWord()
    Random.constant_word_size = False
    d: int = os.getpid()
    named: str = f'./files/Process-{num}-{d}.txt'
    file = open(named, 'a')
    for w in range(quantity):
        file.write(f'{Random.generate()}\n')
    file.close() 
    analytica(named)

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    list_process: List[Process] = []
    for i in range(multiprocessing.cpu_count()):
        s: str = f"m{i}"
        quant: int = randint(100000, 5000000)
        m: Process = Process(target=create, args = (i+1, quant), name=s)
        list_process.append(m)
        m.start()
    for i in range(multiprocessing.cpu_count()):
        list_process[i].join()

def length(named):
    file = open(named, 'r')
    k = 0
    for line in file:
        k += 1
    file.close()
    return k

def total(named: str):
    file = open(named, 'r')
    t = 0
    for line in file:
        for word in line:
            if word != '\n':
                t += len(word)
    file.close()
    return t

def maxlength(named: str):
    file = open(named, 'r')
    maxlenth: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if maxlenth == -1:
                maxlenth = len(line)
            else:
                if maxlenth < len(line):
                    maxlenth = len(line)
    file.close()
    return maxlenth

def minlength(named: str):
    file = open(named, 'r')
    minlenth: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if minlenth == -1:
                minlenth = len(line)
            else:
                if minlenth > len(line):
                    minlenth = len(line)
    file.close()
    return minlenth

def middlelength(named: str):
    middlelenth: int = total(named) / length(named)
    return middlelenth

def consonant(named: str):
    file = open(named, 'r')
    consonant: int = 0
    for line in file:
        for p in line:
            if p in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y', '\n', ' ']:
                pass
            else:
                consonant += 1
    file.close()
    return consonant

def vowel(named: str):
    file = open(named, 'r')
    vow: int = 0
    for line in file:
        for p in line:
            if p in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
                vow += 1
            else:
                pass
    file.close()
    return vow

def repetitions(named: str):
    file = open(named, 'r')
    list_file: List[str] = file.read().split()
    diction: dict = dict()

    for word in list_file:
        if len(word) in diction:
            diction[len(word)] += 1
        else:
            diction[len(word)] = 1

    sorted_dict = {}
    sorted_keys = sorted(diction.keys())

    for w in sorted_keys:
        sorted_dict[w] = diction[w]
    rep_dict = sorted_dict.copy()

    rep: str = ""
    for key in diction:
        rep += f"   * {key} симв. >> {diction[key]} повторений.\n"
    file.close()
    return rep

def analytica(named: str):
    e:str = ""
    for b in range(55):
        e += '*'

    print(e + f"\n" + f"Аналитика для файла {named}" + f"\n" + e + f"\n" +
          f"1. Всего символов --> {total(named)}\n" +
          f"2. Максимальная длина слова --> {maxlength(named)}\n" +
          f"3. Минимальная длина слова --> {minlength(named)}\n" +
          f"4. Средняя длина слова --> {middlelength(named)}\n" +
          f"5. Количество гласных --> {vowel(named)}\n" +
          f"6. Количество согласных --> {consonant(named)}\n" +
          "7. Количество повторений слов с одинаковой длиной:\n"+
          f"{repetitions(named)} \n")