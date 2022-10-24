
try:
    while True:
        word = input()
        if word.isalpha() and len(word) >= 3:
            for i in word:
                if word == "А" or word == "О" or word == "У" or word == "Ы" or word == "Э" or word == "Е" or word == "Ё" or word == "И" or word == "Ю" or word == "Я" or word == "а" or word == "о" or word == "у" or word == "ы" or word == "э" or word == "е" or word == "ё" or word == "и" or word == "ю" or word == "я":
                    i.lower()
                else:
                    i.upper()
            break
        else:
            print("Коректно введите данные")
        file = open("./files/"+word+".txt", "w")

except:
    print("Произошла ошибка")
