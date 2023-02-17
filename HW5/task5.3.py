# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import random

def random_numb():
    a = str(random.randint(100,1000))
    return a

def make_file():
    f = open('abvwords.txt','w+')
    for i in range(1, 10):
        f.write("абв" + f"{str(i)} \n")
    f.close()
    print
    
def read_file():
    f = open('abvwords.txt','r')
    print(f.read())
    f.close()
    
def edit_file():
    f = open('abvwords.txt','r+')
    f.readline
    f.writelines
    print

make_file()
read_file()
edit_file()
read_file()