#variables = values

a = 5
b = 1.1
c = "chargebee"
d = 4+2j
e = True
print(a,b,c,d,e)
print(type(a),type(b),type(c),type(d),type(e))

#collection datatypes
list   a = [ item1, item2, ...] 
tuple  b = ( item1, item2, ... )
set    c = { item1, item2, ...}
dict   d = {key:value,key:value,key:value,...}

#string operations

a = "Jay"

print(a)
print(a[0]) 
print(a[4]) 
print(a[-1]) 
print(a[-3]) 

print(a[4:8]) 

print(a[::2]) 
print(a[::-1]) 

b = "Bavani"
print(b[9:6:-1]) 
print(b[-5:-8:-1]) 
print(b[9:-8:-1]) 
print(b[-5:6:-1]) 

b = "    Manideep    "
print(b.strip())
print(b.lstrip())
print(b.rstrip())


a = ["nethra", "ram", "suma"]
print(a)
print(type(a))

b = ("nethra", "ram", "suma")
print(b)
print(type(b))

a[0] = "Baradwaj"
print(a)


c = {1,1.1,"i"}
print(c)

d= {1:"ravi", 2:"raj"}
print(d)
print(d[1])


d= {"veg":{"tomato":5,"brinjal":10}, "fruits":{"apple":5,"banana":10}}
print(d)
print(d["veg"]) 



password= "admin@123"
limit =0
while (limit<3):
    entry = input("Enter the password")
    if (password == entry):
        print("password match")
        break
    else:
        print("check your password")
        limit = limit+1
else:
    print("attempt limit reached")

#funtions

def abc():
    print("hello world")
    print("123")

abc()

def add(a,b):
    print(a+b)

add(2,3)

#classes, object

class First:
    a = 78

    def method1(self):
        print("Method1")

o1 = First()
print(o1.a)
o1.a = 80
print(o1.a)
o1.method1()

#inheritance concept 

class Second(First):
    b = 45

    def Method2(self):
        print("Method2")

s1 = Second()
print(s1.b)
print(s1.a)


















    















