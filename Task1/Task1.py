# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



str1='/Users/denisblohin/Desktop/Обучение/Python/HWork/HW5_1/Task1/Text1.txt'
with open(str1, 'r', encoding='UTF-8') as file:
    str1=file.readline()
   
str1=str1.split()
f=lambda elem: 'абв' not in elem.lower()
str2=''
str2=' '.join(list(filter(f, str1)))
print(str1)
print(str2)
name='/Users/denisblohin/Desktop/Обучение/Python/HWork/HW5_1/Task1/Text2.txt'

with open(name, 'w', encoding='UTF-8') as file2:
    file2.write(str2)

