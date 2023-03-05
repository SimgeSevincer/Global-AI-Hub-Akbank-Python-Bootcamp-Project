#Gerekli kitaplıkları içe aktaralım.
import csv
from datetime import datetime


#Üst sınıfımız olan Pizza sınıfımızı oluşturalım.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
    
    
#Pizza sınıfının alt sınıfları olan Klasik, Margarita, Türk Pizzası, Dominos Pizza vb. pizza sınıflarını oluşturalım.
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 25.0)
        
class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 30.0)
        
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 35.0)
        
class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 20.0)       
        

#Bir Decorator sınıfı oluşturalım. Decorator, burada tüm sos sınıflarının süper sınıfı olarak adlandırılır.
class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()
    
    
#Sos olarak Zeytin, Mantar, Keçi Peyniri, Et, Soğan ve Mısır'ı belirleyelim ve belirlediğimiz sosların her birini bir sınıf olarak tanımlayalım.
class ZeytinSos(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 5.0

    def get_description(self):
        return self.pizza.get_description() + ", Zeytin"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class MantarSos(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 5.0

    def get_description(self):
        return self.pizza.get_description() + ", Mantar"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class KeciPeyniriSos(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 7.5

    def get_description(self):
        return self.pizza.get_description() + ", Keçi Peyniri"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class EtSos(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 10.0

    def get_description(self):
        return self.pizza.get_description() + ", Et"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class SoganSos(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 4.0

    def get_description(self):
        return self.pizza.get_description() + ", Soğan"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class MisirSos(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 3.5

    def get_description(self):
        return self.pizza.get_description() + ", Mısır"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost


#Bir main fonksiyonu oluşturalım. Bu fonksiyon içerisinde sipariş işlemleri yapılcaktır.
def main():
    #menu.txt dosyasından menuyü ekrana yazdıralım.
    s = open("menu.txt", encoding="utf-8").read()
    print(s)
    
    # Kullanıcının seçim yapmasını isteyelim.
    pizza_choice = int(input("Pizza seçiminiz (1-4): "))
    while pizza_choice not in [1, 2, 3, 4]:
        pizza_choice = int(input("Geçersiz giriş. Lütfen tekrar deneyin: "))

    # Seçilen pizza nesnesini oluşturalım.
    if pizza_choice == 1:
        pizza = KlasikPizza()
    elif pizza_choice == 2:
        pizza = MargaritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    else:
        pizza = SadePizza()

    # Kullanıcının seçim yapmasını iste ve seçilen sos nesnesini oluştur
    durum=1
    while durum:
        sos_choice = int(input("Sos seçiminiz (5-10): "))
        while sos_choice not in [5,6,7,8,9,10]:
            sos_choice = int(input("Geçersiz giriş. Lütfen tekrar deneyin: "))
        if sos_choice == 5:
            pizza = ZeytinSos(pizza)
        if sos_choice == 6:
            pizza = MantarSos(pizza)
        if sos_choice == 7:
            pizza = KeciPeyniriSos(pizza)
        if sos_choice == 8:
            pizza = EtSos(pizza)
        if sos_choice == 9:
            pizza = SoganSos(pizza)
        if sos_choice == 10:
            pizza = MisirSos(pizza)
        durum=int(input("Eklemek istediğiniz ek sos var ise '1' yok ise '0' butonuna basınız."))

    # Sipariş özetimizi ekrana yazdıralım.
    print("Sipariş özeti:")
    print(pizza.get_description())
    print("Toplam fiyat: ", pizza.get_cost())

    # Kullanıcı bilgilerini isteyelim ve kaydedelim.
    name = input("Adınız: ")
    id_no = input("TC kimlik numaranız: ")
    card_no = input("Kredi kartı numaranız: ")
    sifre = input("Kredi kartı şifresi: ")
    order_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Siparişi veritabanına kaydedelim.
    with open("Orders_Database.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([pizza.__class__.__name__, name, id_no, card_no, sifre, pizza.get_description(), order_time])
        print("Sipariş bilgileriniz kaydedilmiştir.")
#main fonksiyonumuzu çalıştıralım.
if __name__ == '__main__':
    main()