# int type data

Rezwan = 420 

print(type(Rezwan)) 

# floating type data 

Rizvy = 40.2

print(type(Rizvy)) 

# Complex type data

Anizone = 420j

print(type(Anizone)) 

# str type data 

Pika = 'lika'

zard = "lizard"

print(Pika + ' ' +zard) 



# bool type data

AZB1 = False
print(type(AZB1)) 

x = 10
y = 10

print(x==y)


#binary type data

RezwanList = [1,2,3,4,5,6,7,255]

b = bytes(RezwanList)
print(type(b))

#binary type data bytearray

RezwanList1 = [1,2,3,4,5,6,7,255]

b1 = bytearray(RezwanList1)

b1[1] = 100
print(b1[1])


#none type data


x = None

print(type(x))


#list type data

li = ['eshan','rezwan','radvin','rayan','rayid']

li[0] = "rezwan"
print(li)


#tuple type data 

tup = (5,10,15,20,25)


print(type(tup))


#range type data

ran = range(7);

for i in ran:
    print(i)