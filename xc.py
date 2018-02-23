#!/bin/python
class Animal(object):
	def run(self):
		print('Animal is runing...')
		self.__jump()

	def __jump(self):
		print('Private jumping....')

class Dog(Animal):
	def eat(self):
		print('dog is eating...')

	def run(self):
		print('dog is runing....')
		pass


class Cat(Animal):
	def eat(self):
		print('cat is eating...')


dog=Dog()
cat=Cat()

dog.run()
dog.eat()

cat.run()
cat.eat()




def alrun(cc):
	cc.eat()

print('##########################')

alrun(dog)
alrun(cat)

print(dir(dog)) 

print(dir(dog))


