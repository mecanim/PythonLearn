from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')



def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="")

def edit_data():
    fileNumToEdit = int(input("Файл для изменения (1 или 2): \n"))
    fileName = "data_first_variant.csv"
    if fileNumToEdit == 2:
        fileName = "data_second_variant.csv"
    incr = 5 if fileNumToEdit == 1 else 2

    with open(fileName, "r+", encoding="utf-8") as file:
        data = file.readlines()
        print("Данные для изменения: ")
        for i in range(0, len(data), incr):                
            print(data[i][:-1] + ": " + str(i))
        
        lineNumToEdit = int(input("Введите индекс данных для изменения: \n"))
        if(0 <= lineNumToEdit < len(data)):
            name, surname, phone, adress = input_user_data()

            file.truncate(0)
            if fileNumToEdit == 1:
                data[lineNumToEdit] = name
                data[lineNumToEdit + 1] = surname
                data[lineNumToEdit + 2] = phone
                data[lineNumToEdit + 3] = adress

                for i in range(0, len(data), incr):
                    file.write( f'{data[i]}\n'
                        f'{data[i + 1]}\n'
                        f'{data[i + 2]}\n'
                        f'{data[i + 3]}\n\n')
            else:
                data[lineNumToEdit] = name + ';' + surname + ';' + phone + ';' + adress
                for i in range(0, len(data)):
                    file.write(f'{data[i]}\n\n')