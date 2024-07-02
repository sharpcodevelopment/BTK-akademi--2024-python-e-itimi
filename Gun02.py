ad=input("adınızı giriniz")
if ad=="sergen" or ad=="ahmet":
    print("adaşız")


yas=int(input("yaşınız kaç \t:"))
if yas>=18:
    print("ehliyet alabilir")
else:
    print(f"ehliyet alamazsınız{yas} yasındasınız")


yol= 150
zaman=1
hız=yol/zaman
if hız>132:
    print(f"{hız-132} kadar aştın")
else:
    print(f"{hız}kurallara uyduğun için teşekkür ederiz")   
 

#yemek sipariş uygulaması

yemek=input("yemek bilgisi giriniz")
icecek=input("içecek bilgisi giriniz")
if yemek=="pide" and icecek=="ayran":
    print("sipariş alındı")
else:
    print("bu menü uygun değildir")

puan=int(input("ortalamanızı giriniz"))
if puan<=70:
    print("belge alamazsınız")
else:
    if puan<85:
        print("teşekkür alabilirsiniz")
    else:
        if puan<=100:
            print("takdir alabilirsiniz")
        else:
            print("geçerli bir not girmedin")

#kısa if yapısı

a=5
c="büyüktür" if a>4 else "küçüktür"
print(c)

gun=input("gün değerini giriniz")
match gun:
    case"pazartesi":
        print("haftanın ilk gün")
    case "salı":
        print("haftanın ikinci günü")
    case _:
        print("tanımsız gün")

ad="besteakıllılar"
print(len(ad))
print(ad[0])
print(ad[-1])
print(ad[0:5])
print(ad[:5])
print(ad[-9:])
print(ad[::2])#baştan sona ikişer atlayarak yazdırır
print(ad[::-1])#sondanbaşa birer birer yazdırır
print(ad[3:8:2])#üçüncü indeksten sekizinci indekse kadar ikişer ikişer atlayarak yazar
print ("b" in ad) #ad değişkeninde b varmı


print("ali","veli","can",sep=="*")
print("ali","veli","can",end=888)


#Döngüler
print(list(range(5)))
for dd in range(0,5):
    print(dd,"merhaba")

isim="zuhal"
for dd in "zuhal":
    print(dd)


for dilim in range(1,6,2):
    print(dilim,"pizzanız")

isim=input("adınızı giriniz")
yas=int(input("yaşınızı giriniz"))
for i in range(yas):
    print(isim)


toplam=0
for ii in range(10):
    toplam +=ii
    print(ii,toplam)

baslangic=2
bitis=10
artis=2
for ii in range(baslangic,bitis,artis):
    print(ii)


aralik1=int(input("değeri gir"))
aralik2=int(input("değer girin"))
artis=int(input("değeri gir"))
toplam=0
carpim=1
for ii in range (aralik1,aralik2,artis):
    toplam +=ii
    carpim*=ii

    print("normal değer",ii)
    print("toplam",toplam)
    print("carpim",carpim)



i=0
while i<10:
    print(i,"dilim pizza")
    i+=1

print(i)


sayac=0
while sayac<15:
  
    print(sayac)  
    sayac+=1




for dd in range(15):
    ad=input("adınızı girin")
    if ad=="hatice":
        print("hatice bulundu")
        break
print(dd)




carpim=1
sayac=0
while sayac<10:
    girilen=int(input("deger gir"))
    if girilen==0:
        continue
    carpim*=girilen
    sayac+=1
    print(carpim)


#Listeler

ogrenciAdı="hatice"
ogrenciSoyadi="akıncı"
ogrenciYas=21
ogrenciBoy=1.63
ogrenciCinsiyet=True

ogrenciBilgisi=[ogrenciAdı,ogrenciSoyadi,ogrenciYas,ogrenciBoy,ogrenciCinsiyet]




ad=input("adınız nedir")
soyad=input("soyadınızı girin")



#list() yapısı
ad="YarenOzankarali"
ad_list=list(ad)
print(ad_list)
orjinalAd=str(ad_list)
print(orjinalAd) 

pazar=["elma","armut","erik","çilek","karpuz"]
meyve = ["elma","armut","üzüm","erik","çilek","karpuz"]

meyve.append("üzüm")
print(meyve)
print(meyve.count("üzüm"))
print(meyve.index("armut"))
meyve.insert(1,"kavun")
print(meyve)
meyve[3] = "kara üzüm"
print(meyve)
meyve.sort()
print(meyve)
meyve.reverse()
print(meyve)
liste2 = ["şeftali","muz"]
meyve.extend(liste2)
print(meyve)
liste3 = ["canerik","muşmula"]
meyve.append(liste3)
print(meyve)
meyve.pop()
print(meyve)
meyve.pop(2)
print(meyve)
meyve.remove("erik")
print(meyve)
meyve.clear()
print(meyve)
del meyve
print(meyve)
    

  


