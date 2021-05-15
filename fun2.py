#Яна Шурпик, Минск, AQA, python

def collecting_data():
    second_data = input("Введите имя: ")
    return second_data


def second_function(second_data):
    if second_data == 'Вячеслав':
        print('Привет, Вячеслав')
        return True
    else:
        print("Нет такого имени")
        return False

#second_function(collecting_data())