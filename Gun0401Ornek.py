"""import Gun04
from math import *
import random
import datetime
from datetime import datetime
import time
import os
import time
karekok = sqrt
yazdir = print
yazdir(karekok(16))



# print(help(random))
print(random.random())
print(random.randint(0,100))
print(random.randrange(0,100))




# print("merhaba dünya")
# time.sleep(5)
# print("sana da merhaba")
a = input("birinci giris")
giris = datetime.now()
print(giris)
b = input("ikinci giris")
giris2 = datetime.now()
fark = giris2 - giris
print(fark)
print(fark.total_seconds())


dosya = open("deneme.txt")
# print(dosya.read())
# print(dosya.read(10))
# print(dosya.readline())
# print(dosya.readline())
# satirlar = dosya.readlines()
# print(satirlar)
# for satir in satirlar:
#     print(satir, end="")
okuma1 = dosya.read()
print(okuma1)
okuma2 = dosya.read()
print(okuma2)
dosya.close()





dosya_adi = "deneme.txt"
with open(dosya_adi, "a") as dosya:
    dosya.write("esma")
with open(dosya_adi, "r") as dosya:
    print(dosya.read())

dosya_adi2 = "deneme2.txt"
if not(os.path.isfile(dosya_adi2)):
    dosya = open(dosya_adi2, "x")
    print("dosya oluşturuldu")
    dosya.close()
else:
    print("oluşturmak istediğiniz dosya mevcut")
time.sleep(5)
if os.path.exists(dosya_adi2):
  os.remove(dosya_adi2)
  print("dosya silindi")
else:
  print("The file does not exist")

  dosya_adi = "oyun.txt"
if not (os.path.exists(dosya_adi)):
    dosya = open(dosya_adi, "x")
    dosya.close()

while True:
    cevap = int(input("oyun için 1,\tİstatistik için 2,\tÇıkış için 3"))
    if cevap == 1:
        dosya = open(dosya_adi, "a")
        rastgele = random.randrange(1,100)
        dosya.write(str(rastgele) + " + ")
        tahminSayisi = 10
        taban = 0
        tavan = 100
        while tahminSayisi >=1:
            tahmin = int(input("Bir Sayı Giriniz"))
            dosya.write(str(tahmin) + ",")
            if tahmin == rastgele:
                dosya.write("+ kazandınız \n")
                print("Tebrikler Kazandınız")
                dosya.close()
                break
            elif tahmin > rastgele:
                print("daha küçük bir değer giriniz")
                tavan = tahmin
            elif tahmin < rastgele:
                print("daha büyük bir sayı giriniz")
                taban = tahmin
            tahminSayisi -= 1
            print("kalan tahmin sayınız", tahminSayisi)
            if tahminSayisi == 0:
                dosya.write("Kaybettiniz \n")
                dosya.close()
    elif cevap == 2:
        dosya = open(dosya_adi)
        print(dosya.read())
        print(dosya.readlines())
        dosya.close()
    else: # elif cevap == 3:
        print("Sistemden Çıkış Yapıldı")
        break



ortalamam=Gun04.sinifOrtalama(70,75,80)
print(ortalamam)


from .Gun04 import sinifOrtalama ##Buraya bak
print(sinifOrtalama(5,55,100))

def kisiselBilgiKarti(**kwargs):
    print(kwargs["ad"],kwargs["soyad"])
    if "bolum" in kwargs.keys
    
    

def factorial(num):
    if num<0:
        print("hatalı sayı girişi")
    if num>0:
        return num*factorial(num-1)
    else:
        return 1
    
print(factorial(5))


def forDongusu(baslangic,bitis=0,artis=1):
    forListesi=[]
    def sirala(baslangic,bitis,artis):
        if baslangic<=bitis:
            forListesi.append(baslangic)
            baslangic+=artis    
            return sirala(baslangic,bitis)
        return forListesi
    if baslangic>bitis:
        return sirala(bitis,baslangic)
    else:
        return sirala(baslangic,bitis)
    
print(forDongusu(5,10,2))




a=1
def ustFonksiyon():
    print(a)
    b=2
    def altFonksiyon():
        print(a)
        print(b)
        c=3

ustFonksiyon()
altFonksiyon()
    """


#oop Giriş


class Ogrenci():
    kurs="Btk Python"
    fakulte=""

print(Ogrenci.kurs)
print(Ogrenci.fakulte)
ogr1=Ogrenci()
print(Ogrenci.kurs)


class Kitaplar():
    ad=""
    yazar=""
    yayinEvi=""
    kitapTuru=""
    sayfa=""
    basimYili=""

kitap1=Kitaplar()
kitap1.ad="Bugünün Yarını"
kitap1.yazar="Sergen Aladağ"
kitap1.yayinEvi=""


class Kitap():
    ad=""
    yazar=""
    basim=""


kitapListesi=[]


