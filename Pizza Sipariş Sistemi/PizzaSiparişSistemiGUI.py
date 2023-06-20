#Gerekli kitaplıkları içe aktaralım.
import csv
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#GUI Uygulamasındaki 2. penceremiz için SiparisDiyalog sınıfını yazalım.
class SiparisDiyalog (QDialog):
    def __init__(self, parent = None):
        super (SiparisDiyalog,self).__init__(parent)
        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        # Izgarayı oluşturalım.
        izgara = QGridLayout()
        
        
        #Kullanıcıdan bilgilerini yazdıracağımız pencereyi oluşturmaya başlayalım.
        #Kullanıcı bilgileri için widgetlarımızı ızgaraya ekleyelim.
        izgara.addWidget(QLabel("Ad Soyad:"),0,0,1,1) 
        self.isim=""
        self.isimKutu = QLineEdit(self.isim)
        izgara.addWidget(self.isimKutu,0,1,1,1)
        
        izgara.addWidget(QLabel("TC Kimlik No:"), 1,0,1,1)
        self.tc=""
        self.tcKutu = QLineEdit(self.tc)
        izgara.addWidget(self.tcKutu,1,1,1,1)
        
        izgara.addWidget(QLabel("Kredi Kartı No:"), 2,0,1,1)
        self.no=""
        self.noKutu = QLineEdit(self.no)
        izgara.addWidget(self.noKutu,2,1,1,1)
        
        izgara.addWidget(QLabel("Kredi Kartı Şifresi:"), 3,0,1,1)
        self.sifre=""
        self.sifreKutu = QLineEdit(self.sifre)
        izgara.addWidget(self.sifreKutu,3,1,1,1)
        
        
        #Sipariş tamamlama ve vazgeçme butonlarını ızgaramıza ekleyelim.
        dugmeKutusu = QDialogButtonBox(QDialogButtonBox.Ok|
                                       QDialogButtonBox.Cancel)
        
        dugmeKutusu.button(QDialogButtonBox.Ok).setText("Sipariş Tamamla")
        dugmeKutusu.button(QDialogButtonBox.Cancel).setText("Siparişten Vazgeç")
    
        dugmeKutusu.button(QDialogButtonBox.Ok).clicked.connect(self.siparisTamamla)
        dugmeKutusu.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        izgara.addWidget(dugmeKutusu,4,0,1,2)
        
        
        #Izgarayı penceremize ekleyelim.
        self.setLayout(izgara)
        self.setWindowTitle("Sipariş Tamamla")
        self.setWindowIcon(QIcon('credit-card.ico'))
        
        
        
    #Sipariş tamamlama butonunu aktifleştirelim.
    def siparisTamamla(self):
        #Eksik bilgi olma durumunda Hata Mesajı penceresini açtıralım.
        self.isim = self.isimKutu.text()
        self.tc = self.tcKutu.text()
        self.no = self.noKutu.text()
        self.sifre = self.sifreKutu.text()
        
        if self.isim=="" or self.no=="" or self.sifre=="" or self.tc=="":
            QMessageBox.warning(self, "Hatalı Giriş","Eksik bilgi girdiniz! Yeniden deneyiniz.")
            return  
        
        #Sipariş kayıtlarını veritabanına kaydedelim.        
        order_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("Orderss_Database.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([AnaUygulamaAkilliDiyalog.__class__.__name__,self.parent.pizza, self.parent.sos,self.isim, self.tc, self.no, self.sifre, order_time])
            print("Sipariş bilgileriniz kaydedilmiştir.")
        
        #Sipariş durumunu gösteren etiketi set edelim.
        self.parent.etiket.setText('< font color ="blue", size = "+6" >Siparişiniz Alınmıştır! </font>')
        QDialog.accept(self)
        
        
        
        
#GUI Uygulamasındaki 1. penceremiz için  AnaUygulamaAkilliDiyalog sınıfını yazalım.
class AnaUygulamaAkilliDiyalog(QDialog):
    def __init__(self, parent = None):
        super (AnaUygulamaAkilliDiyalog,self).__init__(parent)
        
        # Izgarayı oluşturalım.
        izgara = QGridLayout()
        
        
        # Kullanıcının sipariş tercihlerini yazdıracağımız pencereyi oluşturalım.
        #Kullanıcının pizza tercihleri için widgetlarımızı ızgaraya ekleyelim.
        izgara.addWidget(QLabel("Pizza Seçiminiz:"), 0,0,1,1) 
        self.pizzaListe = QComboBox()
        
        self.pl = {0:'Klasik Pizza', 1:'Margarita Pizza', 2:'Türk Pizza', 3:'Sade Pizza'}
        self.pizza = self.pl[0]
        
        self.pizzaListe.addItem('Klasik Pizza')
        self.pizzaListe.addItem('Margarita Pizza')
        self.pizzaListe.addItem('Türk Pizza')
        self.pizzaListe.addItem('Sade Pizza')
        
        self.pizzaListeIndisi = self.pizzaListe.findText(self.pizza)
        self.pizzaListe.setCurrentIndex(self.pizzaListeIndisi)
        self.pizzaListe.activated.connect(self.pizzaDegistir)
        izgara.addWidget(self.pizzaListe,0,1,1,1)   
       
        
       #Kullanıcının sos tercihleri için widgetlarımızı ızgaraya ekleyelim.
        izgara.addWidget(QLabel("Sos Seçiminiz:"), 1,0,1,1) 
        self.sosListe = QComboBox()
        
        self.sl = {0:'Zeytin', 1:'Mantar', 2:'Keçi Peyniri', 3:'Et', 4:'Soğan', 5:'Mısır'}
        self.sos = self.sl[0]
        
        self.sosListe.addItem('Zeytin')
        self.sosListe.addItem('Mantar')
        self.sosListe.addItem('Keçi Peyniri')
        self.sosListe.addItem('Et')
        self.sosListe.addItem('Soğan')
        self.sosListe.addItem('Mısır')
        
        self.sosListeIndisi = self.sosListe.findText(self.sos)
        self.sosListe.setCurrentIndex(self.sosListeIndisi)
        self.sosListe.activated.connect(self.sosDegistir)
        izgara.addWidget(self.sosListe,1,1,1,1)   
        
        
        #Kullanıcı sipariş tercihlerine göre toplam tutarın görüleceği widgetı ekleyelim.
        izgara.addWidget(QLabel ("Toplam Tutar:" ),2,0,1,1)
        self.tutar = (QLabel('<i> Toplam Tutar</i>')) 
        izgara.addWidget(self.tutar,2,1,1,1)
        
        
        #Tutar hesaplama butonunu oluştalım.
        self.hesaplaDugmesi = QPushButton("Tutar Hesapla")
        self.hesaplaDugmesi.clicked.connect(self.tutarHesapla)
        izgara.addWidget(self.hesaplaDugmesi,3,0,1,1)
        
        
        #Sipariş etme butonunu oluşturalım.
        self.siparisDugmesi = QPushButton("Sipariş Et")
        self.siparisDugmesi.clicked.connect(self.siparisEt)
        izgara.addWidget(self.siparisDugmesi,3,1,1,1)
        
        
        #Sipariş durumunu gösteren etiketi oluşturup ızgaramıza ekleyelim.
        self.etiket = QLabel('< font color ="red", size = "+3" > Siparişiniz Tamamlanmadı! </font>' )
        izgara.addWidget(self.etiket,4,0,1,2)
        
        
        #Izgarayı penceremize ekleyelim.
        self.setLayout(izgara)
        self.setWindowTitle('Pizza Sipariş Sistemi')
        self.setWindowIcon(QIcon('pizza.ico'))
    
    
    
    #Seçilen pizza ve sosları değişkenlerimize atayalım. 
    def pizzaDegistir(self,tip1):
        self.pizza = self.pl[tip1]
     
        
     
    def sosDegistir(self,tip2):
        self.sos = self.sl[tip2]
        
        
        
    #Tutar Hesapla butonunu aktifleştirelim.
    def tutarHesapla (self):
        
        #Kullanıcının sipariş tercihlerine göre fiyatlandırma yapalım.
        if self.sos == self.sl[0]:
            sos_cost=5.0
        if self.sos == self.sl[1]:
            sos_cost=6.0
        if self.sos == self.sl[2]:
            sos_cost=7.5
        if self.sos == self.sl[3]:
            sos_cost=10.0
        if self.sos == self.sl[4]:
            sos_cost=4.0
        if self.sos == self.sl[5]:
            sos_cost=3.5
            
            
        if self.pizza == self.pl[0]:
            pizza_cost=25.0
        if self.pizza == self.pl[1]:
            pizza_cost=30.0
        if self.pizza == self.pl[2]:
            pizza_cost=35.0
        if self.pizza == self.pl[3]:
            pizza_cost=20.0
        
        
        tutar = sos_cost + pizza_cost
        self.tutar.setText('<font color ="black"><b>%0.2f</b></font>' % tutar)
        
        
        
    #Sipariş Et butonunu aktifleştirelim.
    def siparisEt(self):
        diyalog = SiparisDiyalog(self)
        diyalog.exec_()               
        
        
#GUI uygulaması olay döngüsünü başlatalım.
uyg = QApplication([]) 
pencere = AnaUygulamaAkilliDiyalog()   
pencere.show()
uyg.exec_()