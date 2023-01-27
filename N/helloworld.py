print("Hello world")


if 7>2:
	print("a je vece od b")
else:
	print("a je manje od b")

#Uvek mora tab da se metne posle if-a
"""Komentar se moze pisati i ovako"""


x=4
#Navodjenje varijabli nije neophodno
y= int(3)
print(x, y)
z='Ognjen'

print(type(x))
print(type(z))


#camelCase     Sve reci krecu sa velikim slovom osim prve
myNameIs = "Ognjen"
#PascalCase   Sve reci krecu sa velikim slovom
MyNameIS = "Ognjen"
#snake_case    Izmedju svake reci ide _
my_name_is = "Ognjen"



my_name_is,myMidnameIs,MySurnameIs= "Ognjen","Vladimir","Grgur"
print(my_name_is, myMidnameIs, MySurnameIs)

Ime=["Danijela","Dusan","Grgur"]
my_name_is,myMidnameIs,MySurnameIs=Ime
print(my_name_is, myMidnameIs, MySurnameIs)


x=7
y=5
print(x+y)

x=" Python je"
y=" super"
print(x+y, y+x)


#definisanje funkcija na lokalnom nivou varijable
x="Super"

def Funkcija1():
	x="Odlican"
	print("Pythonje " +x)

Funkcija1()
print(x)


#def fje na globalnom nivou
x="Ognjne"
print(x, " Grgur")
def Ime():
	global x
	x="Danijela"

Ime()
print(x, " Grgur")

Funkcija1() #kada se fj-a samo pozove ona samo odradi sta je u njoj

x = 20.5
print(type(x))


#kovertovanje int to float and complex

x=6
y=7.8
z=5j

a= float(x)
b= int(y)
c= complex(x)

print(a,b,c)
print(type(a))

import random
print(random.randrange(1,9))

#prvi karakter
a= "Ognjen"
print(a[1])

#slovo po slovo
for x in "Ognjen":
	print(x)

#duzina
a="Banana"
print(len(a))

#da bi pronasli neku rec u tekstu in
txt ="Ognjen ima kompijuter"
print("ima" in txt)

#sa if
if "ima" in txt:
	print("rec ima je u tekstu")

#provera da li rec nije u tekstu
print("nema" not in txt)

#sa if
if "nema" not in txt:
	print("rec nema nije u tekstu")


#ispisi karaktere od do
print(txt[0:5])
print(txt[:5])
print(txt[2:])





