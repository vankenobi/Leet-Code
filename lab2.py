from itertools import count
from math import remainder


a = [0,1,5,10,50,100,500,1000]

# 7'yi bulmak için liste içerisindeki hangi iki sayıyı toplamalıyım.
result = ""
remainder = 2856
counter = 0

while(remainder !=0):
    if(counter == len(a)-1):
        print(a[counter]," Eklendi.")
        remainder = remainder - a[counter]
        counter = 0
    elif(remainder >= a[counter] and remainder < a[counter+1]):
        print(a[counter]," Eklendi.")
        remainder = remainder - a[counter]
    counter += 1

        