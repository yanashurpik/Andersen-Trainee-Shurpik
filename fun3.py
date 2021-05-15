#Яна Шурпик, Минск, AQA, python


def collecting_data():
    num = int(input("Введите количество цифр в массиве: "))
    third_data = []
    for i in range(num):
        n = int(input("Введите цифру: "))
        third_data.append(n)
    return third_data


def third_function(third_data):
    m = []
    for i in third_data:
        if i % 3 == 0:
            m.append(i)
    return m

#print(third_function(collecting_data()))