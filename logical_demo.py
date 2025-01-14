#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz 

"""
sayi = int(input('sayı : '))
result = (0 < sayi < 100)
print(f"bu sayı -100 arasındadır : {result}")

"""

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""
sayi = int(input('sayi : '))
pozcift = (sayi > 0) and (sayi %2 == 0)
print(f"Girilen sayı pozitif ve çifttir : {pozcift}")

"""

#3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
"""
girilenEmail = str(input('email : '))
girilenPassword = str(input('password : '))

email = 'berfincelik@hotmail.com'
password = '1234'

print(f"Girilen email : {email == girilenEmail} . Girilen password :  {password == girilenPassword}")

"""

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız. 

"""
sayi1 = int(input('sayı1 : '))
sayi2 = int(input('sayı2 : '))
sayi3 = int(input('sayı3 : '))

oran = (sayi1 > sayi2) and (sayi1 > sayi3)
print(f"sayi1 en büyük sayıdır : {oran} ")

oran = (sayi2 > sayi1) and (sayi2 > sayi3)
print(f"sayi2 en büyük sayıdır : {oran} ")

oran = (sayi3 > sayi1) and (sayi3 > sayi2)
print(f"sayi3 en büyük sayıdır : {oran} ")

"""

#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse 
#   geçti değilse kaldı yazdırın . 
#   a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b) Finalde 70 alındığında ortalamanın bir önemi olmasın. 


"""
vize1 = float(input('vize1 : '))
vize2 = float(input('vize2 : '))
final = float(input('final : '))

ortalama = ((vize1 + vize2)/2 * 0.6 ) + (final * 0.4)
# sartlar = (ortalama >= 50) and (final >= 50) 
sartlar = (ortalama >= 50 ) or (final >= 70)


print(f"Ortalamanız : {ortalama} Dersten geçtiniz : {sartlar} ")
"""

#6- Kişinin ad, kilo ve boy bilgilerini alıp indexlerini hesaplayınız. Formül : kilo / boy uzunlugunun karesi
#   0 - 18.4 => Zayıf
#   18.5 - 24.9 => Normal
#   25.0 - 29.9 => Fazla Kilolu
#   30.0 - 34.9 => Şişman (Obez)

ad = str(input('ad : '))
kilo = float(input('kilo : '))
boy = float(input('boy : '))

index = (kilo) / (boy ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
kilolu = (index >= 24.9) and (index <= 29.9)
obez = (index >= 30) and (index <= 34.9)

print(f"{ad} kilo indexin : {index} ve kilo değerlendirmen zayıf {zayif}")
print(f"{ad} kilo indexin : {index} ve kilo değerlendirmen normal {normal}")
print(f"{ad} kilo indexin : {index} ve kilo değerlendirmen kilolu {kilolu}")
print(f"{ad} kilo indexin : {index} ve kilo değerlendirmen obez {obez}")