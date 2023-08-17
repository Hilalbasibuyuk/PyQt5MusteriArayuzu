from PyQt5.QtWidgets import *
from yönetici_girisi import Ui_yonetici_giris
from yonetici_islemleri_main import yonetici
class Yonetici_giris(QWidget):
    def __init__(self)-> None:
        super().__init__()
        self.yonetici=Ui_yonetici_giris()
        self.yonetici.setupUi(self)
        self.yonetmek = yonetici()
        self.yonetici.lineEdit.setPlaceholderText("Kullanıcı Adı")
        self.yonetici.lineEdit_2.setPlaceholderText("Şifre")
        self.yonetici.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.yonetici.btn_giris.clicked.connect(self.girisYap)

    def girisYap(self):
        kullanici_adi= self.yonetici.lineEdit.text()
        sifre = self.yonetici.lineEdit_2.text()

        if kullanici_adi=="Hilalbasibuyuk" and sifre=="ataaitteam.0001":
            self.close()
            self.yonetmek.show()
        else:
            print("Lütfen eksiksiz girdiğinize emin olun!")
