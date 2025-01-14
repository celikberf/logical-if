#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
"""
sayi = int(input('sayı : '))

if (sayi >= 0) and (sayi <= 100):
    print('Bu sayı 0 ile 100 arasındadır.')
else: 
    print('Bu sayı 0 ile 100 arasında değildir.')
    
"""

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz. 

"""
sayi = int(input('sayı : '))
if (sayi > 0) and (sayi % 2 == 0):
    print('Sayı pozitif ve çifttir')
elif (sayi < 0) and (sayi % 2 != 0):
    print('Sayı negatif ve tektir.')
elif (sayi > 0) and (sayi % 2 != 0):
    print('Sayı pozitif ve tektir.')
elif (sayi < 0) and (sayi % 2 == 0):
    print('Sayı negatif ve çifttir.')
else:
    print('Sayı sıfırdır.')
"""

#3- Email ve parola bilgileri ile giriş kontrolü yapınız.
#   email = berfincelik
#   pass = abc123

"""
girilenEmail = input('email : ')
girilenpassw = input('pass : ')

email = 'berfin@hotmal.com'
passw = 'abc123'

if (girilenEmail == email) and (girilenpassw == passw):
    print('Giriş başarılı ')
elif (girilenEmail != email) and (girilenpassw == passw):
    print('Yanlış email ')
if (girilenEmail == email) and (girilenpassw != passw):
    print('Yanlış pass ')
else : 
    print('email ve pass yanlış')

"""

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız. 

"""
sayi1 = int(input('sayi1 : '))
sayi2 = int(input('sayi2 : '))
sayi3 = int(input('sayi3 : '))

if (sayi1 > sayi2) and (sayi1 > sayi3) :
    print('sayi1 en büyüktür')
elif (sayi2 > sayi3) and (sayi2 > sayi3) :
    print('sayi2 en büyüktür')
if (sayi3 > sayi2) and (sayi3 > sayi1) :
    print('sayi3 en büyüktür')
else : 
    ('Sayılar eşittir.')
"""
#5- Kullanıcıdan 2vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
#   Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdırın.
#   ortalama 50 olsa bile final notu en az 50 olmalıdır
#   finalden 70 alındığı taktirde ortalamanın önemi olmasın. 

"""

vize1 = float(input('vize1 : '))
vize2 = float(input('vize2 : '))
final = float(input('final : '))

ortalama = ((vize1 + vize2) / 2) * 0.6 + (final * 0.4)

# result = (ortalama >= 50) and (final >= 50)
# result = (ortalama >= 50) or (final >= 70)

if (ortalama >= 50):
    if (final >= 50):
        print(f"Öğrencilerin ortalaması : {ortalama} ve geçme durumu : başarılı")
    else:
        print(f"Öğrencilerin ortalaması : {ortalama} ve geçme durumu : başarısız . Finalden min 50 almanız gerek")
else: 
    print(f"Öğrencilerin ortalaması : {ortalama} ve geçme durumu : başarısız")


"""

#   Kişinin ad, kilo ve boy bilgilerini alıp indexlerini hesaplayınız. Formül : kilo / boy uzunlugunun karesi
#   0 - 18.4 => Zayıf
#   18.5 - 24.9 => Normal
#   25.0 - 29.9 => Fazla Kilolu
#   30.0 - 34.9 => Şişman (Obez)

ad = str(input('ad : '))
kilo = float(input('kilo : '))
boy = float(input('boy : '))


indeks = kilo / (boy**2)

print('Boy kilo indeksiniz : ' , indeks)

if (indeks >0) and (indeks <= 18.4):
    print('Zayıf')
elif (indeks >18.4) and (indeks <= 24.9):
    print('Normal')
elif (indeks >24.9) and (indeks <= 29.9):
    print('Kilolu')
elif (indeks >29.9) and (indeks <= 34.9):
    print('Obez')
else:
    print('İndeks aralıgında değer girilmedi')