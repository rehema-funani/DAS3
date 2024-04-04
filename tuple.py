my_tuple = (1,2,4,5)
print(my_tuple)
y = list(my_tuple)#converting the list to a tupple
y.remove(1)#Remove item in my_tuple
print(y)
my_tuple =tuple(y)#converting the list back to tupple
print(my_tuple)


mytuple = (11,12,13,14,15)
print(mytuple)
z = list(mytuple)#converting mytuple to a list
print(z)

print(z.append(20))
mytuple = tuple(z)#converting mytuple back to tuple
print(mytuple)


print(mytuple[1])#Accessing the element z