#Identity Operator  : is

"""
x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y) #true
print(x == z) #true
print(x is y) #true
print(x is z) #false => Obejeler aynı mı değil mi sorguladık. Aynı adresi mi tutuyorlar.

"""

x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse() #ters cevirdik

print(x == y) #True => Elemanlar aynı
print (x is y) #False => Aynı objeyı (adresi) göstermez
print (x is not y) # True

#Membership Operator : in

list = ['apple', 'banana']
print('banana' in list) #True => 'banana' listin içinde mi 

name = 'berf'
print('e' in name) #True => e harfi name içinde var mı
print('e' not in name) #False => e harfi name içerisinde yok mu 