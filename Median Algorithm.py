import datetime
import time
from random import randrange

def find_mode(list):
    count_dict = {}
    for num in list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        
    max_count = max(count_dict.values())
    mode = [key for key, value in count_dict.items() if value == max_count]

    return mode, max_count
     
def dominant(list):
    if len(list)/count == len(mode):
        print (list)
        print("Brak wartości modalnej")
    else:
        print (list)
        print("wartość modalna:", ', '.join(map(str, mode)), "występuje", count, "razy") 


listSize = (int)(input("ilość elementów tablicy: "))
listGen = (str)(input("czy liczby mają zostać wygenerowane losowo?(1 - tak, 0 - nie):  "))
list = []
if (listGen == "1"): 
    a = (int)(input("Z jakiego przedziału?\nOd: "))
    b = (int)(input("Do: "))
while (listSize > 0):
    if (listGen == "1"):  
        c = randrange(a,b)
    else:
        c = (int)(input("podaj liczbe: "))
    list.append(c)
    listSize -= 1

list.sort()
list.reverse() 

startTime = datetime.datetime.now()  
mode, count = find_mode(list)    
time.sleep(0)
endtime = datetime.datetime.now()
timeElapsed = endtime - startTime
seconds = timeElapsed.seconds
microsec = timeElapsed.microseconds
dominant(list)
print (f"{seconds} sekund , {microsec} milisekund")
