print("------------------------------------------------------")
print("Problem: 1")
class cal1:
    def setdata(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c
        print("x: ",self.x)
        print("y: ",self.y)
        print("z: ",self.z)
    
    def display(self):
        print("Sum: ",self.x+self.y+self.z)

pro1 = cal1()
pro1.setdata(2,4,6)
pro1.display()

print("------------------------------------------------------")

print("Problem: 2")
class cal2:
    def setdata(self):
        self.r=int(input("Enter radius of circle: "))
    
    def area(self):
        self.Area = 3.14*self.r*self.r
    
    def display(self):
        print("Area of the circle:",self.Area)

pro2 = cal2()
pro2.setdata()
pro2.area()
pro2.display()

print("------------------------------------------------------")

print("Problem: 3")
class cal3:
    def __init__(self,p,r,n):
        self.p=p
        self.r=r
        self.n=n
   
    def calintrest(self):
        self.intrest=(self.p*self.r*self.n)/100
    
    def display(self):
        print("Total intrest:",self.intrest)

p=int(input("Enter amount: "))
r=int(input("Enter rate per annum: "))
n=int(input("Enter number of duration in years: "))
pro3 = cal3(p,r,n)
pro3.calintrest()
pro3.display()

print("------------------------------------------------------")

print("Problem: 4")
class cal4:
    def setdata(self,n):
        self.n=n

    def display(self):
        self.sqr = pow(self.n,2)
        return self.sqr

pro4 = cal4()
pro4.setdata(int(input("Enter number: ")))
print("Square of the number:",pro4.display())

print("------------------------------------------------------")

print("Problem: 5")
class employee:
    name="Richard"
    designation="Python Developer"

class personal(employee):
    salary=100000
    def __init__(self):
        print("From parent class -> Name :",self.name,"\tDesignation :",self.designation)
        print("From child class -> Salary :",self.salary)

pro5 = personal()

print("------------------------------------------------------")

print("Problem: 6")
class cal6:
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def calarea(self):
        self.area = self.l*self.w
    
    def display(self):
        print("Area of the rectangle:",self.area)

l = int(input("Enter length: "))
w = int(input("Enter width: "))
pro6 = cal6(l,w)
pro6.calarea()
pro6.display()

print("------------------------------------------------------")

print("Problem: 7")
class cal7:
    def setdata(self):
        self.l = int(input("Enter length of square: "))

    def area(self):
        self.Area=pow(self.l,2)
    
    def display(self):
        print("Area of the Square:",self.Area)

pro7=cal7()
pro7.setdata()
pro7.area()
pro7.display()

print("------------------------------------------------------")

print("Problem: 8")
class publisher:
    def gettitle(self):
        self.title=input("Enter Book title: ")

    def printtitle(self):
        print("Title of the book is '"+self.title+"'")

class book(publisher):
    def __init__(self):
        print("Book class inherits publisher ")
    
    def getpageno(self):
        self.page_no=int(input("Enter page no of book: "))

    def printpageno(self):
        print("Page:",self.page_no)

class tape(publisher):
    def __init__(self):
        print("Tape class inherits publisher ")
    
    def gettime(self):
        self.time_for_playing=int(input("Enter tape playing time: "))

    def printtime(self):
        print("Tape playing time:",self.time_for_playing)

print("Functionalities of BOOK class")
pro8_1 = book()
pro8_1.gettitle()
pro8_1.getpageno()
pro8_1.printtitle()
pro8_1.printpageno()

print("")

print("Functionalities of TAPE class")
pro8_2 = tape()
pro8_2.gettitle()
pro8_2.gettime()
pro8_2.printtitle()
pro8_2.printtime()

print("------------------------------------------------------")

print("Problem: 9")
class Scheme:
    def getScheme(self):
        self.scheme_id=input("Enter scheme id: ")
        self.scheme_name=input("Enter scheme name: ")
        self.outgoing_rate=int(input("Enter outgoing rate: "))
        self.message_charge=int(input("Enter message charge: "))

    def printScheme(self):
        print("Printing Scheme details...")
        print("Scheme id:",self.scheme_id)
        print("Scheme name:",self.scheme_name)
        print("Outgoing rate:",self.outgoing_rate)
        print("Message charge:",self.message_charge)

class customer(Scheme):
    def getcust(self):
        self.cust_id=input("Enter customer id: ")
        self.name=input("Enter your name: ")
        self.mobile_no=int(input("Enter your mobile no: "))

    def printcust(self):
        print("Printing customer details...")
        print("Customer id:",self.cust_id)
        print("Name:",self.name)
        print("Mobile no:",self.mobile_no)

pro9 = customer()
pro9.getScheme()
pro9.getcust()
print("")
pro9.printScheme()
pro9.printcust()

print("------------------------------------------------------")

print("Problem: 10")
class arith:
    a=b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a*self.b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
pro10 =arith(a,b)
print("Addition :",pro10.add())
print("Substraction :",pro10.sub())
print("Multiplication :",pro10.mul())