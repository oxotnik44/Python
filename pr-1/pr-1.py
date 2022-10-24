def first():
    print("Введите фамилию, имя, отчество и год рождения:")
    text = input()
    if text == '0': return text
    text = text.split()
    
    if len(text) >=5: raise Exception("Вы ввели неправильное количество данных")
    try: int(text[3])
    except: raise Exception("Год запишите как число")
    k = 0
    for i in range(3):
        try: 
            float(text[i])
            break
        except:
            k+=1
            continue
    if(k == 3):
        with open('file.txt', 'a') as con:
            con.write(text[0] +" "+ text[1] +" "+ text[2] +" "+ text[3] +"\n")
    else:
        print("ФИО запишите не как число")

def second():
    try:
        with open('file.txt', 'r', encoding='utf-8') as conn:
            print('Фамилия Имя Отчество Год рождения')
            for line in conn:
                line=line.strip()
                print(line)
    except Exception as e:
        print(e)
while True:
    try:
        if first() == '0': break
    except Exception as e:
        print(e)
second()