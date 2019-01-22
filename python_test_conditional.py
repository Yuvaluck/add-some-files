x=10

if x<0:
	print("X is smaller than 0.")
elif x>10:
	print("X is bigger than 10.")
else:
	print("X isbetween 0 and 10.")

###
y=10
if y<10:
	print("y is small.")
elif y>=0:
	print("y is big.")	
else:
	print("error")	
##
y=int(input("enter value of y:"))
if y<10:
	print("y is small.")
elif y>=0:
	print("y is big.")	
else:
	print("error")	
##

animal = ['cat','dog','turtle','bird']
print (animal)

for x in animal:
	print(x)
	print(len(x))

number=[1,2,3,4,5,6,7,8,9,10]

for i in number:
	print(i**2)

number= range(10)
for i in number:
	print(i**2)

number= range(11)
for i in number:
	print(i**2)