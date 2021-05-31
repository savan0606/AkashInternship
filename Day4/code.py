def fun1():
    name = "Mr. Sam"
    contact = 98162543728
    return(name,contact)

name,contact = fun1()
print("Name: ",name)
print("Contact No: ",contact)

print("")

print("Parameter not passed")
def fun2(a=23,b=28):
    print(a+b)

fun2()

print("")

print("default arguments")
fun2(10,20)

print("")

print("keywordargument")
fun2(b=30,a=45)

print("")

print("variable length arguments")
print("Non keyworded")
def sum_fun1(*argu):
    sum=0
    for i in argu:
        sum = sum + i
    return sum

print("Sum: ",sum_fun1(10,20,30,40,50))

print("")

print("Keyworded")
def fun3(**arg):
    for i,j in arg.items():
        print(i,j)

fun3(Name="Savan" , Surname="Shekhada")

print("")

def fun4():
    x=100
    print("x inside the function : ",x)

x=215
fun4()
print("x outside the function : ",x)

print("")

print("Arithmetic operaters")
x=10
y=20
print("y+x is",y+x)
print("y-x is",y-x)
print("y*x is",y*x)
print("y/x is",y/x)
print("y//x is",y//x)
print("y**x is",y**x)

print("")

print("Relational operaters")
x=10
y=20
print("y>x is",y>x)
print("y<x is",y<x)
print("y<=x is",y<=x)
print("y>=x is",y>=x)
print("y==x is",y==x)
print("y!=x is",y!=x)

print("")

print("Logical operaters")
a,b,c = int(input("Enter three numbers: ")),int(input()),int(input())
if a>b and a>c:
    print(a," is greatest")
elif b>c and b>a:
    print(b," is greatest")
else:
    print(c," is greatest")

print("")

print("Membership operaters")
list = [1,3,5,7,9]
print(list)
print("2 in list",2 in list)
print("5 in list",5 in list)

print("")

print("Indentity operaters")
x = 200
y = 200
print("x is",x,"y is",y)
print("x is y : ",x is y)
print("x is not y",x is not y)