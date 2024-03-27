class Dog: 

	# class attribute 
	attr1 = "mammal"

	# Instance attribute 
	def __init__(self, name): 
		self.name = name 

# Driver code 
# Object instantiation 
Rodger = Dog("Rodger") 
Tommy = Dog("Tommy") 

# Accessing class attributes 
print("Rodger is a {}".format(Rodger.__class__.attr1)) 
print("Tommy is also a {}".format(Tommy.__class__.attr1)) 

# Accessing instance attributes 
print("My name is {}".format(Rodger.name)) 
print("My name is {}".format(Tommy.name))


# classes and objects with methods
# __init__ is a special method (constructor) that initializes an instance of the Dog class. It takes two parameters: self (referring to the instance being created) and name (representing the name of the dog). The name parameter is used to assign a name attribute to each instance of Dog.
# The speak method is defined within the Dog class. This method prints a string that includes the name of the dog instance.

class Dog: 

	# class attribute 
	attr1 = "mammal"

	# Instance attribute 
	def __init__(self, name): 
		self.name = name 
		
	def speak(self): 
		print("My name is {}".format(self.name)) 

# Driver code 
# Object instantiation 
Rodger = Dog("Rodger") 
Tommy = Dog("Tommy") 

# Accessing class methods 
Rodger.speak() 
Tommy.speak()
