#brushing python concepts for soc
a = [6,9,   69, 420  ]
b = a[3]
print(type(a))
a[3]= 69
print (a)
kotawale= ["atishay","gungun","harsh","yash","chumtiya"]
print(kotawale[0:4])
limst = [1,6,4,8,856,8678,364]
limst.insert(6,69)
limst.insert(6,69)
print(limst)
limst.pop(3)
print(limst)
limst.remove(69)
# print(limst)
# limst.remove(669)
# print(limst)
# t = (1, )
# print(t)
# from tkinter import E










# a=input("insert your number ")
# b=input("insert your number ")
# c=input("insert your number ")
# d=input("insert your number ")
# list = [37,69,68,69,78,69,57]
# print(list.count(69))







mydic = {
"yash": "nibba",
"vinayak": "bhandnayak",
"yuvraj": "gymkachomda",
"batra": "bewda",
"sanket": "simppp",
65: ["pavan","shrey","harry"],
"simran": "simp"}

mydic[65] = "bich"
print(mydic.keys())
print(list(mydic.values()))
f = {
    "disha" : "babli"
}
mydic.update(f)

print(mydic.get(65))












f = {1,3,4,1,1,(1,5,7)}
# print(f)
f.add(69)
print(f)
# # f = set()
# f.remove(1)
# print(f)
# f.pop()
# print(f)
print(f.union({69,57}))

s={69,69.0,"69"}
print(s)












import nntplib


lang={}

a = input( "what's your name dude?" )
al = input( "what's your fav lang dude?")
b = input( "what's your name dude?" )
bl = input( "what's your fav lang dude?")
c = input( "what's your name dude?" )
cl = input( "what's your fav lang dude?")
d = input( "what's your name dude?" )
dl = input( "what's your fav lang dude?")

amdd = {
a:"a1",
b: "b1",
c:"c1",
d:"d1"

}

print( amdd)










she= input("what type is she :")
if(she =="cute"):
    print("Kiss her")
elif(she =="hot"):
    print("take her to a club")
elif(she =="funny"):
    print("Take her on a date")
elif(she =="sexy"):
    print("Date her")















 age = input("what's your age dude :")
 age = int(age1)
 if(age >= 17):
     print("adultr")

 elif( age >= 14): print("teen")














a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))
fff= [a,b,c,d]
fff.sort()
ln= fff[0]
tn = sum(fff)
if(ln>33 and tn>160): print("PASS")
else: print("FAIL")














a = input('type your text')
if ("shruti" in a):
    print("yupp present")
else :
    print("not present")












# i= 1
# while i < 51 :
#     print (i)
#     i += 1

hge = ["Jahnvi","Khushi","Nandini","Srushti","Srishti","Annie","Sanika","Aakanksha","Preethi","Bhagyashree"]
i= 0
while i < len(hge)-1 :
    i += 1
    
    

# # for item in hge:
# #       print(item + " likes Atishay")
# #  else: 
# #       print("dudees were satisfied.")
# for item in  hge:
#     print(item)
    if(i== 6):
        continue
    print(hge[i]+ " likes Atishay")
    
else:
     print("karma is a bitch")

n = int(input("insert your number dude:"))














print("here's your table dude:")
i=10
while i>0 :
    print(n*i)
    i = i - 1


for i in range(2, a):
    if(a%i == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime") 














a=1
for i in range(1,n+1):
    a = a * i
print(a)


for i in range(1,n+1):
    if(i%2 ==1) : print("***")
    else: print("* *")















def spi(marks):
    return(sum(marks))/6

yash =[8,7,6,8,8,8] 
atishay =[8,8,7,6,8,8]
yuvraj=[9,8,7,8,8,7]
vinayak=[6,4,6,8,7,6]

print(spi(yash))
print(spi(atishay))
print(spi(yuvraj))
print(spi(vinayak))















def sum (n):
    if n== 0 : 
        return 0
    return n+sum(n-1)

print(sum(10))














def greatest(set):
    a = set[0]
    if(set[1]> set[0]):
        a= set[1]
    if (set[2]>a):
        a= set[2]
    return a
semt =[167,69,99]
print(greatest(semt))

def convert(f):
     return f*(9/5) + 32

print(convert(10))     

def table(n):
      for i in range(1,11):
          print(n*i)
table(5)

def designm(n):
    i=n
    while i > 0:
        print("*"*i)
        i=i-1
designm (10)














string = "       India is my country all indians are my brothers and their sisters    "
def removal(word):
    a= string.replace(word,"")
    a = a.strip()
    print (a)
    
print (string)    
removal(" country")