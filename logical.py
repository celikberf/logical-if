x = 6
hak = 0
devam = 'e'
result = 5 < x < 10

#and

result = (x > 5) and (x < 10) 
# True + True => True
result = (x > 6) and (x < 10) 
# False + True => False
result = (hak > 0) and (devam == 'e') # False

#or

result = (x > 0) or (x % 2 == 0)  #True

#True + False => True
#True + True => False
#False + False => False


#not

result = not(x > 0)  #False


# x , 5-10 arasındaa bir çift sayı mı ? 

result = ((x > 5 ) and (x < 10)) and (x %2 == 0)

print(result)