print("Hello World")

a,b = "studies in GEC ", "Gandhinagar, sector-"
c = 28
print("Sam "+a+b,c)
print(type(a),type(b),type(c))

print("")

'''Type of
            Variable'''
a = 1 + 2j
print("a =", a, "is of ", type(a))
print('Is "a" Complex number ? ',isinstance(a, complex))

print("")

#String
name = "Mr. Sam"
print(name[5])       # letter printing
print(name[:5])      # Start (By Default) : END
print(name[3:])      # Start : END (By Default)
print(name[3:6])    # Start : END
print(name * 2)

print("")
print("")

#LIST Datatype
print("List DataType")
print("")
list = [10, 5.5 ,"Cricket", 10, "Chess", 10]
print(list)
print(list[2],"This variable \"list\" is of type",type(list))
print(list[1:3], list[2:], list[:2])
list.append("Anand")
print(list)
print("\"10\" is available in list ", list.count(10), "times")

print("")
print("")

#Tuple
print("Tuple DataType")
print("")
tuple = (10, 5.5 ,"Kotyark","Store")
print(tuple)
print(tuple[2],"This variable \"tuple\" is of type",type(tuple))
print(tuple[1:3], tuple[2:], tuple[:2])

print("")
print("")

print("Dictionary Data Type")
print("")
dict = {1:"15", 2:"Days", 3:"Internship" ,"ak":'in', 5:"Akash Technolabs", 6:[1,2,3,4,5]}
print(dict)
print(dict.keys())
print(dict.values())
print(dict["ak"])
print("list in Dictionary",dict[6])