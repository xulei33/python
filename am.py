#!/bin/Python
while True:
    num=input("please input a digital\n")
    if not num.isdigit():
        print("%s is not digital"%num)
        continue
    ##
    intnum=int(num)
    #print(intnum)
    lenth=len(num)
    #print(lenth)
    sum=0
    w=0
    while intnum>=10:
        w+=1
        v=intnum%10
        sum+=v**lenth
        intnum=intnum//10
        print(w," ",v," ",sum," ",intnum)
    else:
        sum+=intnum**lenth
        print("sum is %d"%sum)
    if sum==int(num):
        print("ok")
        break
        