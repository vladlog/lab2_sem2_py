import pickle
from Structs import *



def Enter_Name():
    name = input("Введите название файла: ")
    return name


def is_in_base(Prog_now : TeleProg, base: list):
    flag = False
    if flag == False:
        for prog_old in base:
            prog = TeleProg(prog_old)
            startTime = Prog_now.h_start * 60 + Prog_now.m_start
            startTime1 = prog.h_start * 60 + prog.m_start
            endTime = Prog_now.h_end * 60 + Prog_now.m_end
            endTime1 = prog.h_end * 60 + prog.m_end
            if Prog_now.nameOfProg == prog.nameOfProg:
                flag = True
                break
            elif startTime < startTime1 and endTime > endTime1:
                flag = True
                break
            elif endTime1 > endTime > startTime1:
                flag = True
                break
            elif startTime1 < startTime < endTime1:
                flag = True
                break
            else:
                flag = False
    return flag


def get_input(name):
    list = []
    mode = input("Хотите добавить свой вклад? Если да, введите a. В противном случае введите w: ")
    while True:
        if mode == 'a':
            with open(name, 'rb') as file:
                pickle.load(file)
                break
        if mode == 'w':
            with open(name, 'wb') as file:
                file.truncate()
                break
        while mode != 'a' and mode != 'w':
            mode = input("Enter correct letter (a or w): ")
    with open(name, 'wb') as file:
        print(
            "Введите информация [имя ч:м ч:м]\n Чтобы закончить строчку | press ---> ENTER\n Закончить ввод | press ---> ENTER twice\n")
        line = input()
        while line:
            prog = TeleProg(line)
            if not is_in_base(prog, list):
                list.append(line)
            else:
                print("Введите новое имя программы или корректное время:")
            line = input()
        pickle.dump(list, file)


def lenght_of_prog(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        for i in range(len(temp)):
            prog = TeleProg(temp[i])
            startTime = prog.h_start * 60 + prog.m_start
            endTime = prog.h_end * 60 + prog.m_end
            length = endTime - startTime
            print("Имя программы: ", prog.nameOfProg, "| в эфире: ", str(int(length / 60)), "часов ", str(length % 60), "минут\n")


def new_list(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        str = []
        for i in range(len(temp)):
            prog = TeleProg(temp[i])
            if prog.h_start >= 9 and (prog.h_end < 18 or prog.h_end  == 18 and prog.m_end  == 0):
                str.append(temp[i])
        with open("output_file.txt", 'wb') as fileof:
            pickle.dump(str, fileof)


def get_format(Tele):
    prog = TeleProg(Tele)
    str_h_start = str(prog.h_start)
    str_m_start = str(prog.m_start)
    str_h_end = str(prog.h_end)
    str_m_end = str(prog.m_end)
    if prog.h_start < 10:
        str_h_start = '0' + str_h_start
    if prog.m_start < 10:
        str_m_start = '0' + str_m_start
    if prog.h_end < 10:
        str_h_end = '0' + str_h_end
    if prog.m_end < 10:
        str_m_end = '0' + str_m_end
    return str_h_start + ':' + str_m_start + ' ' + str_h_end + ':' + str_m_end


def print_TeleProg(Tele):
    prog = TeleProg(Tele)
    print("Имя:", prog.nameOfProg, " ", get_format(Tele))


def output(name):
    with open(name, 'rb') as fileif:
        temp = pickle.load(fileif)
        for i in range(len(temp)):
            print_TeleProg(temp[i])