import modules # импорт модуля
import modules as md # импорт модуля с алеасом 
from modules import f2, f3 # импорт конкретных функций
from modules import * 

# from modules import *  если импортируем так, то функции можно вызывать без обращения к пакету
# f1()
modules.f1()
md.f2()