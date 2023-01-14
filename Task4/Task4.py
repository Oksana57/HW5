# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def coding_zip(str1):
    zip_str = ''
    count=1
    i=0
    while i<len(str1):
        while i+1< len(str1) and str1[i]==str1[i+1]:
            count+=1
            i+=1
        zip_str+=str(count)+str1[i]  
        i+=1
        count=1  
    return zip_str 
str1 = input('Введите строку для кодировки: ')
str2=coding_zip(str1)
print(str2)

def decoding_zip(str1):
    dezip_str=''
    i=0
    while i<len(str1):
        dezip_str+=int(str1[i])*str1[i+1]
        i+=2
    return dezip_str

print(decoding_zip(str2))