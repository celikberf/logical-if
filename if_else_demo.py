#1- Kullanıcıdan isim , yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
#   Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

"""
name = input('isim : ')
age = int(input('yaş : '))
egitimBilgisi = input('eğitim bilgisi : ')

if (age >= 18) and (egitimBilgisi == 'lise' or egitimBilgisi == 'üniversite'):
    print('Ehliyet için uygundur')
else : 
    print('Ehliyet için uygun değildir')

    """

#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#   0-24 => 0 
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5

"""
yazili1 = int(input('yazili1 : '))
yazili2 = int(input('yazili2 : '))
sozlu = int(input('sözlü : '))

ortalama = (yazili1 + yazili2 + sozlu) / 3
print('Ortalamanız : ' , ortalama)

if (ortalama > 0 ) and (ortalama <= 24):
    print('0')
elif(ortalama > 24) and (ortalama <= 44):
    print('1')
elif(ortalama > 44) and (ortalama <= 54):
    print('2')
elif(ortalama > 54) and (ortalama <= 69):
    print('3')
elif(ortalama > 69) and (ortalama <= 84):
    print('4')
elif(ortalama > 84) and (ortalama <= 100):
    print('5')
else: 
    print('Yanlış not aralığında not girdiniz')

"""
#3- Trafiğe çıkış tarihi alınan aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#   1. Bakım => 1.yıl
#   2. Bakım => 2.yıl
#   3. Bakım => 3.yıl
#   Süre hesabını alınan gün , ay , yıl bilgisine göre gün bazılı hesaplayınız. (datetime)
#   (simdi) - (2013/8/1) => gün

"""

import datetime

tarih = (input('aracınız hangi tarihte trafiğe çıktı (2024/12/17) : '))
tarih = tarih.split('/')

# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

trafigeCikis =  datetime.datetime(int(tarih[0]) , int(tarih[1]) , int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days


if days <= 365 :
    print('1.servis aralığı')
elif days > 365 and days <= 365*2:
    print('2.servis aralığı')
elif days > 365*2 and days <= 365*2:
    print('3. servis aralığı')
else :
    print('Servis aralığında değildir')
"""