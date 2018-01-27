class Animal(object):
	def run(self):
		print('Animal is runing...')
	
class Dog(Animal):
	def run(self):
		print ('Dog is running...')
class Cat(Animal):
	#def run(self):
	#	print ('Cat is running...')
	pass
def run_twice(a):
	a.run()
	a.run()
	
def test():
	pass
	

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
