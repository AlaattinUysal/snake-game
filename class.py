#CLASS İNHERİTANCE [MİRAS ALMA YÖNTEMİ]
class Calisan:
    zam_oranı = 1.1
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email= isim + soyisim + "@gmail.com"

    def bilgiler(self):
        return "Ad = {} , Soyad: {} , Maas: {} , Email: {}".format(self.isim,self.soyisim,self.maas,self.email)


class Yazilimci(Calisan):
    zam_oranı = 1.4
    def __init__(self,isim,soyisim,maas,dil):
        super().__init__(isim,soyisim,maas)
        self.dil = dil

    def bilgiler(self):
        return super().bilgiler() +  " , bildigi dil: {}".format(self.dil)



calisan1 = Calisan("Enes","Kaya","40k")

yazilimci1 = Yazilimci("Tuna","Karali","60k","Java")

class Yönetici(Calisan):
    def __init__(self,isim,soyisim,maas,calisanlar = None):
        super().__init__(isim,soyisim,maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_cikar(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisan_bilgileri(self):
        for calisan in self.calisanlar:
           print(calisan.bilgiler())



yönetici2 = Yönetici("Feyyaz","Altın","80.000",[calisan1,yazilimci1])
yönetici2.calisan_bilgileri()

print(issubclass(Yönetici,Calisan))