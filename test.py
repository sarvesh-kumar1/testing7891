############################conditional statements###############################
"""
a = 12

if a%3 ==0:
	print("the value is divisible by 3")

elif a%5 ==0:
	print("the value is divisible by 5")

else:
	print("the value is not divisible by 3")

"""

#/////////////////////////////for loop for prime numbers/////////////////////////

"""
a =1

if a>1:
	for x in range(2,a):
		if (a%x)==0:
			print("Not prime")
			break

	else:
		print("prime")

else:
	print("the value is less than or eqaul to 1")

"""


#///////////////////////////// my list, my string ////////////////////////

"""
my_list  = [1,2,3,4,5]

for x in my_list[0:3]:
	print(x)

print("below state print value from index 3 to till end")

for x in my_list[3:]:
	print(x)

"""

#//////////////////////////////nested for loop/////////////////

"""
for x in range(1,10):
	for y in range(x):
		print(x,end=" ")

"""

#//////////////////////////////nested while loop/////////////

"""
a = [1,2,3,4,5]

while a:
	print(a.pop(-1))
	b=["------","_______"]
	while b:
		print(b.pop(0))

"""


#/////////////////////////////////lambda functions/////////////
"""
a =lambda x:x*x
print(a(3))

a =lambda x,y:x*y
print(a(3,4))

"""

#///////////////////////////////////user defined fuctions//////////////
"""
def add(a,b):
	return a+b
print(add(3,4))

def lamb(x):
	return (lambda y:x*y)

t=lamb(3)

print(t(5))

"""

#///////////////////////////////////list///////////////////////////////////////////////
"""
new_list = [1,2,3,4,5]

print(new_list)

new_list.append(8)
print(new_list)
new_list.extend([11,12])
print(new_list)
new_list.pop(2)
print(new_list)

print("using for loop")

for x in new_list:
	print(x)

new_list.insert(2, "sarvesh")
print(new_list)
"""

#//////////////////////////////////////dictionary////////////////////////////
#hold keypair values and dict are mutable
"""
a =dict({1:"sarvesh",2:"ajay",3:"amit"})

print(a)
print(a[2])
print(a.get(3))

a[2]="mangal"
print(a)

"""

#///////////////////////////////////tuples/////////////////////////
#same as list but faster that list and also not mutable
"""
a =(1,2,3,4,5)
b=()

c =tuple((2,3,4,5))

print(a)
print(b)
print(c)

"""

#////////////////////////////////sets//////////////////////
#unordered collections of unique elements and mutable
"""
a ={2,3,4,4,5}
print(a)
b={7,8,9}
print(b)

c=a|b
print(c)

"""


#/////////////////////////////////////////////classes and objects//////////////////////////////////
"""

class myclass:
	def myfunc(self):
		return "hello my class"


obj = myclass()
print(obj.myfunc())

class myclass1:
	def myfunc(self,a,b):
		return a+b


obj = myclass1()
print(obj.myfunc(3,4))


"""

#   the __inti__ method like constructors in c++

"""
class myclass:
	def __init__(self,name):
		self.name=name

	def funct(self):
		print(self.name)


p = myclass("sarvesh")
p.funct()

"""

#//////////////////////////////////////////////////inheritance/////////////////////////////
"""
class myclass:
	def first(self):
		print("parent function")


class child(myclass):
	def second(self):
		print("child function")


p = child()
p.second()
p.first()
"""


#////////////////////////////////////////////encapsulation///////////////

class myclass:
	def __init__(self):
		self.__hi()

	def funct(self):
		print("hi how are you")

	def __hi(self):
		print("sab mast")


obj = myclass()
obj.funct();

class myclass:
	def funct(self):
		print("hi how are you")

	def __hi(self):
		print("sab mast")


obj = myclass()
obj.funct()
obj._myclass__hi()
