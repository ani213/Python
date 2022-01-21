# Examples of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b

# Subtraction of numbers
sub = a - b

# Multiplication of number
mul = a * b

# Division(float) of number
div1 = a / b

# Division(floor) of number
div2 = a // b

# Modulo of both number
mod = a % b

# Power
p = a ** b

# print results

# print(add,"Add")
# print(sub,"Substract")
# print(mul,"multiple")
# print(div1,"division")
# print(div2,"double divison")
# print(mod,"modulas")
# print(p,"power")


# A Python program to demonstrate the use of
# "//" for integers
# print (5//2)
# print (-5//2)

# Python program to show use of
# + operator for different purposes.

# print(1 + 2)

# concatenate two strings
# print("Geeks"+"For")

# Product two numbers
# print(3 * 4)

# Repeat the String
# print("Geeks"*4)

repeated="Aniket"*4
# print(repeated)

# Python Program illustrate how
# to overload an binary + operator

class A:
	def __init__(self, a):
		self.a = a

	# adding two objects
	def __add__(self, o):
		return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Aniket")
ob4 = A("_Verma")
print(ob1)
print(ob2)
print(ob3)
print(ob4)
print(ob1 + ob2)
print(ob3 + ob4)
