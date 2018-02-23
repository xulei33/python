print("hello word")
a=[1,2,3]
for x in a:
	print(x)


def hello():
	print("hello words")

hello()

def hello(name):
	print("hello %s"%name)
	return "xulei"

a=hello("xulei")
print(a)

def person(name,*pars):
	print(name)
	for x in pars:
		print(x)

person('xulei','man',26,'guangzhou')


def defultpars(name,age=21,sex='man'):
	print(name)
	print(age)
	print(sex)

defultpars('xulei',20,'man')
defultpars('yanping',sex='woman')


def fact(n):
	if(n==1):
		return 1
	return n*fact(n-1)


print(fact(3))



class xclass(object):
	i=123
	def f(self):
		return 'hello words'


a=xclass()
print(a.f())
print(a.i)


class person(object):
	"""docstring for person"""
	#name=''

	def __init__(self, name,age):
		super(person, self).__init__()
		self.name=name
		self.__age = age
		print('name is:',self.name,' age is:',self.__age)

	def pname(self):
		print('name is:',self.name,' age is:',self.__age)


	def set__age(self,age):
		print(self.__age)
		self.__add(age)


	def __add(self,age):
		self.__age+=age
		print('add age:',age,' new age:',self.__age)


p=person('xulei',34)
p.pname()

print('After change ')
p.name='kkkk'
p.__age=12
p.pname()

p.set__age(22)
p.pname()




class student(person):
	"""docstring for student"""
	def __init__(self, arg):
		super(student, self).__init__()
		self.arg = arg
		











		




