#Яна Шурпик, Минск, AQA, python


for i in range(11):
    ask = int(input("Введите число больше 7: "))
    if ask > 7:
        print("Привет")
        break
    else:
        print("Error. Повторите попытку")