# python class

# class Worker

# (_init_) means initialization
# self means 自己，本身 or instance本身
class Worker:
	def __init__(self, name, pay):
		self.name = name #self is the new object
		self.pay = pay
	def firstName(self):
		return self.name.split()[0]
	def lastName(self):
		return self.name.split()[-1]#split string on blanks
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent) #Update pay in-place
		
bob = Worker(input(), 20000)
print(bob.lastName())
print(bob.firstName())
bob.giveRaise(.20)
print(bob.pay)