#Яна Шурпик, Минск, AQA, python


def collecting_data():
    first_data = int(input("Введите число больше 7: "))
    return first_data


def first_function(first_data):
    if first_data > 7:
        print("Привет")
        return True
    else:
        print("Error. Повторите попытку")
        return False

#first_function(collecting_data())
