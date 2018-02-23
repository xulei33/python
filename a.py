#!/usr/bin/python3
#_*_ coding:UTF-8 _*_
import random
number=random.randint(1,100)
print('value is %d' %number)
guess=0
while True:
	num_input=input("输入一个0到100的数字：输入q退出\n")
	guess+=1
	if not num_input.isdigit():
		if num_input=='q':
			break
		else:
			print("输入的必须是数字")
	elif int(num_input)<0 or int(num_input)>100:
		print("输入的数字必须0到100")
	else:
		if number==int(num_input):
			print("恭喜你，答案正确，你共猜了%d次"%guess)
			break
		elif number<int(num_input):
			print("输入的值太大")
		elif number>int(num_input):
			print("输入的值太小")
		


