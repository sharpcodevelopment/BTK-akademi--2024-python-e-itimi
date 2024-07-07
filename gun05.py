"""print("slav u rez")

class Ogrenci():
      bolum = "Bilişim"
      kurs = "Btk Akademi"

      def __init__(self, ad, soyad, tc):
        print("Ogrenci oluşturuldu")
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc

      def tamAd(self):
        return self.ad + self.soyad

      def kafHarf(self):
        return len(self.ad)

      def __str__(self):
        return f"{self.ad} - {self.soyad} - adında bir öğrenci"
ogr1 = Ogrenci("kerim","can",123)

print(ogr1)

print(ogr1.bolum)
print(ogr1.kurs)
print(vars(ogr1))
print(ogr1.tamAd())
harf_sayisi = ogr1.kafHarf()
print(harf_sayisi)
# print(Ogrenci.tamAd())



#
class Kedi():
   ayak=4
   kuyruk=True

   def __init__(self,ad,adim) :
      self.ad=ad
      self.adim=adim

   def yurume():
      print(self.ad,self.adim,"adım attı")

   def miyav(cls):
      print("miyav dedi")


tekir=Kedi("tekir",5)
print(tekir.ad)
print(tekir.adim)
tekir.yurume()
tekir.miyav()



class Araba():
    teker=4
    kapi=True

    def __init__(self,marka,model,renk,calismaDurumu):
        self.marka=marka
        self.model=model
        self.renk=renk
        self.calismaDurumu=calismaDurumu
    def __str__(self):
        return f"{self.marka} marka{self.model} renk{self.renk} çalışmaDurumu{self.calismaDurumu}"
    def calistir(self):
        if self.calismaDurumu==True:
            self.calismaDurumu=True
            print("araba çalıştırıldı")
            self.hiz=0
        else:
            print("araba zaten çalışıyor")

    def durdur(self):
        if self.calismaDurumu==True:
            self.calismaDurumu==False
            print("araba durduruldu")
        else:
            print("araba zaten duruyor")
    def hizArttir(self):
        if self.calismaDurumu==True:
            self.hiz+=10
            print(self.hiz)
        else:
            print("önce arabayı çalıştır")

    def hizAzalt(self):
        if self.calismaDurumu==True and self.hiz>=10:
            self.hiz-=10
            print(self.hiz)
        elif self.calismaDurumu==True and self.hiz==0:
            print("araç çalışıyor ama  zaten duruyor hız azaltılamaz")
        else:
            print("arabayı öncelikle çalıştırınız")

    def hizGoster(self):
        if self.calismaDurumu==False:
            self.hiz=0
            print("aracın hızı",self.hiz)
            return self.hiz
        
    
oto1=Araba(marka="tofaş",model="kartal",renk="kırmızı",calismaDurumu="True")
print(oto1)
oto1.calistir()
oto1.durdur()
oto1.hizArttir()
oto1.hizGoster()
oto1.hizAzalt()
oto1.hizGoster()

class Fatura():
    baslik="Halil Pazarlama"
    odeme=True
    icerik={}

    def __init__(self,mAdi,vNo,tarih):
        self.mAdi=mAdi
        self.vNo=vNo
        self.tarih=tarih
        self.tutar=0
        self.icerik={}

    def __str__(self) :
        return self.mAdi+" adlı müşterinin faturası"
    
    def urunEkle(self):
        urunAd=input("ürün bilgisi giriniz")
        urunFiyati= int(input(f"{urunAd} fiyatını giriniz"))
        urunAdet=int(input(f"{urunAd} adet bilgisi"))
        urunTutar=urunAdet*urunFiyati
        self.tutar +=urunTutar
        self.icerik[urunAd]=[urunAd,urunFiyati,urunTutar,urunAdet]
        print(self.icerik[urunAd],"ürünü sepete eklendi")
        return self.tutar

    def urunCikar(self):
        urunAd=input("ürün bilgisi giriniz")
        urunFiyati= int(input(f"{urunAd} fiyatını giriniz"))
        urunAdet=int(input(f"{urunAd} adet bilgisi"))
        urunTutar=self.icerik[urunAd][3]
        self.tutar -=urunTutar
        print(self.icerik[urunAd],"ürünü sepetten çıkarıldı")
        self.icerik.pop(urunAd)
        return self.tutar
    def faturaTutari(self):
        print("güncel fatura tutari",self.tutar)
        return self.tutar
    

musteri=Fatura("hamza","1452","bugün")
print(musteri)
musteri.urunEkle()
musteri.urunCikar()





kitap_listesi = []
kitaplar = []
class Kitap():
    def __init__(self,ad,yazar,sayfa,basim):
        self.ad=ad
        self.yazar=yazar
        self.sayfa=sayfa
        self.basim=basim
    def __str__(self):
        return self.ad

def kitapListesineEkle():
    kitap_adi = input("Kitap adı")
    kitap_yazar = input("yazar")
    kitap_sayfa = int(input("sayfa"))
    kitap_yili = int(input("yili"))
    kitap = Kitap(kitap_adi,kitap_yazar, kitap_sayfa, kitap_yili)
    degerler = vars(kitap)
    kitap_listesi.append(degerler)
    kitaplar.append(kitap)

def kitapListesiKaydet():
    try:
        with open("kitap.json","r") as file:
            kitap_listesi2 = list(json.loads(file.read()))
    except:
        kitap_listesi2 = []
    if len(kitap_listesi2) == 0:
        if len(kitap_listesi) > 0:
            y = json.dumps(kitap_listesi)
            with open("kitap.json","w") as file:
                file.write(y)
            kitap_listesi.clear()
            kitaplar.clear()
        else:
            print("Kaydedilecek Kitap Yok")
    else:
        if len(kitap_listesi) > 0:
            kitap_listesi2.extend(kitap_listesi)
            y = json.dumps(kitap_listesi2)
            with open("kitap.json","w") as file:
                file.write(y)
            kitap_listesi.clear()
            kitaplar.clear()
            del kitap_listesi2
        else:
            print("Kaydetmeyi Bekleyen Kitap Yok")

def kitapListele():
    if len(kitaplar)>0:
        for kitap in kitaplar:
            print(kitap)
    else:
        print("Kaydedilmeyi bekleyen kitap yok")

def kayitlikitapListele():
    try:
        with open("kitap.json", "r") as file:
            kitap_listesi2 = list(json.loads(file.read()))
    except:
        kitap_listesi2 = []
    if len(kitap_listesi2)>0:
        for kitap_bilgisi in kitap_listesi2:
            kitap_adi = kitap_bilgisi["ad"]
            kitap_yazar = kitap_bilgisi["yazar"]
            kitap_sayfa = kitap_bilgisi["sayfa"]
            kitap_yili = kitap_bilgisi["basim"]
            kitap = Kitap(kitap_adi, kitap_yazar, kitap_sayfa, kitap_yili)
            kitaplar.append(kitap)
        for kitap in kitaplar:
            print(kitap)
        kitaplar.clear()
    else:
        print("Kayıtlı kitap yok")
def menu():
    k_giris = input("Kaydet, Ekle, Çıkart, Listele, Dosya listele, Q")
    return k_giris
while True:
    cevap = menu()
    if cevap == "e":
        kitapListesineEkle()
    elif cevap == "k":
        kitapListesiKaydet()
    elif cevap == "q":
        print("programdan çıkıldı")
        exit()
    elif cevap == "l":
        kitapListele()
    elif cevap == "d":
        kayitlikitapListele()
    else:
        print("hatalı işlem girişi")

# kitap = Kitap("Python","Sinan Hoca",30, 2024)
#
# kitap_ekleme = kitapekle(kitap)
# if kitap_ekleme:
#     print("Kitap Ekleme Başarılı")
# else:
#     print("Kitap ekleme Başarısız")
"""

