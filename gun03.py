"""print("hello world")
adet=int(input("kaç farklı eşya alacaksınız"))
pazarList=[]
for i in range(1,adet+1):
    urun=input(f"{i}. urun bilgisini giriniz:")
    pazarList.append(urun)


for urun in pazarList:
    print(urun,sep="*" ,end="\t")


mesaj="pazar listesi oluşturma programına hoşgeldiniz programdan çıkmak için X'e basınız"
print(mesaj)
urunList=[]

while True:
    urun=input( "ürün girişi yapınız")
    if urun.lower()=="x":
        print("pazar listeniz",urunList)
        break
    elif urun==" ":
        continue
    else:
        urunList.append(urun)



sebze=["domates,biber"]
meyve=["çilek","kivi","karpuz"]
yesillik=["roka","maydanoz","tere"]
pazarList=sebze+meyve+yesillik
print(pazarList)
print(len(pazarList))


pazarList=[sebze,meyve,yesillik,"baklava"]
print(pazarList)
print(pazarList[0][0])
for kategori in pazarList:
    print (kategori)
    if type (kategori)!=list:
        continue
    for urun in kategori:
        print(urun)  


        print()

for x in range(len(pazarList)):
    print(x+1,"kategorisinde:",pazarList[x])
    for y in range(len(pazarList[x])):
        print(x+1,y+1,"ürünü\t",pazarList[x][y])

for indew,urun in enumerate(pazarList[x]):
    print(x+1,urun)


kizlar=["ayşe","fatma","hayriye"]
erkekler=["ali","veli","can"]
liste1=[erkekler,kizlar]

for dd in liste1:
    for kisi in dd:
        print(dd,kisi)

for kiz,erkek in zip(kizlar,erkekler):
    print(kiz,erkek)



degiskenBuyuk=0
degiskenKucuk=0
sira=0
sayiList=[]

for aa in range(10):
    sayi=int(input("sayı giriniz"))
 
    if sayi>degiskenBuyuk:
        degiskenBuyuk=sayi
        sira+=1
      
    if sayi<degiskenKucuk:
        degiskenKucuk=sayi
        sira+=1 
    sayiList.append(sayi)


print(sayiList) 
print("büyük sayı:",degiskenBuyuk,sira)
print("kücük sayı",degiskenKucuk,sira)




#tuple
demet=24,8,2.5,True
print(demet)
print(type(demet))
dlist=[demet]
print(dlist)
dlist[0]="sergen"
demet=tuple(dlist)
print(demet)
print(dlist)



#set yapısı

ogrenciler={"ali","veli","can","kadir","kaan"}
print(ogrenciler)
print(ogrenciler.pop())
for ogrenci in ogrenciler:
    print(ogrenci)

if "can" in ogrenciler:
    ogrenciler.remove("can")
    print(ogrenciler)



degiskenBuyuk=0
degiskenKucuk=0
sira=0
varmi=False
sayiset={}

for aa in range(10):
    sayi=int(input("sayı giriniz"))

    
    if sayiset==varmi:
        continue
        if sayi>degiskenBuyuk:
            degiskenBuyuk=sayi
            sira+=1     #BİR DAHA BAK
      
        if sayi<degiskenKucuk:
            degiskenKucuk=sayi
            sira+=1 
        varmi=False
    
        sayiset.append(sayi)


print(sayiset) 
print("büyük sayı:",degiskenBuyuk,sira)
print("kücük sayı",degiskenKucuk,sira)



kume1={"a","b","c",2}
kume2={1,2,3}
kume3=kume1|kume2
print(kume2,kume1,kume3)
kume4={"8",9,45}
kume3=kume4.union(kume2,kume1)
print(kume3)




#dictionary 

treng={"araba":"car","kalem":"pen"}

yemekler = {"çorbalar":{"etli": ["işkembe", "kelle paça", "tavuk suyu"],
                         "etsiz": ["mercimek", "ezo gelin"],
                         "sebze": ["domates", "brokoli"]},
           "Kebaplar": {"acılı": ["adana", "beyti"],
                        "acısız": ["urfa","mardin"],
                        "dürümler":["ciger","adana"]},
            "icecek":"çay"
            }
print(yemekler["çorbalar"]["etli"][0])
yemekler["çorbalar"]["etli"].append("bayma çorbası")
sutlu_tatlilar = ["sütlaç"]
yemekler["tatlilar"] = {"sütlü":sutlu_tatlilar}
for menubasligi in yemekler:
    print(menubasligi)
    if type(yemekler[menubasligi]) is dict:
        for altmenu in yemekler[menubasligi]:
            print("\t",altmenu)
            for yemek in yemekler[menubasligi][altmenu]:
                print("\t\t",yemek)
    else:
        print(yemekler[menubasligi])



#basit sayı tahmin oyunu
sayi=35 
tahmin=int(input("bir sayı giriniz"))
if tahmin==sayi:
    print("tahmin başarılı")

#versiyon 2
sayi=35
tahmin=int(input("bir sayı giriniz"))
if tahmin==sayi:
    print("tahmin başarılı")
elif tahmin>sayi:
    print("tahmin sayıdan büyük")
elif tahmin<sayi:
    print("tahmin sayıdan küçük")



#versiyon3
sayi = 35
taban = 0
tavan = 100
basarili=0
basarisiz=0
yanlisT=0
print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
tahmin = int(input("Bir sayı giriniz"))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıkta")
        basarili+=1
        break
        
    else:
        print(f"Tahmin aralığı dışında geçersiz tahmin")
        basarisiz+=1
        print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
        tahmin = int(input("Bir sayı giriniz"))
while tahmin != sayi:
    if tahmin > sayi:
        print("Tahmin Başarısız Keşke küçük bir sayı söyleseydin")
        tavan = tahmin
        yanlisT+=1
    elif tahmin < sayi:
        print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")
        taban = tahmin

    while True:
        if taban < tahmin < tavan:
            print(f"Tahmin geçerli aralıkta")
            break
        else:
            print(f"Tahmin aralığı dışında geçersiz tahmin")
            print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
            tahmin = int(input("Bir sayı giriniz"))
else:
    print("Tahmin Başarılı tebrikler")

i=100
birler=0
onlar=0
yüzler=0

while i<=1000:
    birler=i%10
    birler*birler*birler
    onlar 
   
import random

sayi =random.randint(0,100)
taban = 0
tavan = 100

print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
tahmin = int(input("Bir sayı giriniz"))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıkta")
        break
        
    else:
        print(f"Tahmin aralığı dışında geçersiz tahmin")

        print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
        tahmin = int(input("Bir sayı giriniz"))
while tahmin != sayi:
    if tahmin > sayi:
        print("Tahmin Başarısız Keşke küçük bir sayı söyleseydin")
        tavan = tahmin

    elif tahmin < sayi:
        print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")
        taban = tahmin

    while True:
        if taban < tahmin < tavan:
            print(f"Tahmin geçerli aralıkta")
            break
        else:
            print(f"Tahmin aralığı dışında geçersiz tahmin")
            print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
            tahmin = int(input("Bir sayı giriniz"))
else:
    print("Tahmin Başarılı tebrikler")



dosya=open("Deneme.txt")
print(dosya.readline(10))
dosyaAdi="Deneme.txt"
with open(dosyaAdi) as dosyam:
    print(dosyam.readline())

dosyaAdi="Deneme.txt"
with open(dosyaAdi,"w") as dosya:
    dosya.write("esma")
  
with open(dosyaAdi) as dosya2:
    print(dosya2.read())


dosyaAdi2="sergen.txt"
with open(dosyaAdi2,"x") as dosya3:
    dosya.write("esma")
with open(dosyaAdi2) as okuma:
    print(okuma)


# #versiyon 1
# sayi = int(input("bir sayı giriniz"))
# ssayi = str(sayi)
# toplam = 0
# for rakam in ssayi:
#     kup= int(rakam)**len(ssayi)
#     toplam += kup
#     print(rakam, kup, toplam)
# if toplam == sayi:
#     print(sayi,"sayisi bir armstrong sayısıdır")
#versiyon 2
for i in range(100000):
    sayi = i
    ssayi = str(sayi)
    toplam = 0
    for rakam in ssayi:
        kup= int(rakam)**len(ssayi)
        toplam += kup
        # print(rakam, kup, toplam)
    if toplam == sayi:
        print(sayi,"sayisi bir armstrong sayısıdır")
 """
