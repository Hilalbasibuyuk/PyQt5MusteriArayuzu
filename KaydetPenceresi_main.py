from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from KaydetPenceresi import Ui_Kaydet_penceresi
class kayit_et(QWidget):
    def __init__(self)-> None:
        super().__init__()
        self.kayitEt= Ui_Kaydet_penceresi()
        self.kayitEt.setupUi(self)
        self.kayitEt.pushButton.clicked.connect(self.bilgilerimiKaydet)
        self.kayitEt.pushButton_2.clicked.connect(self.cikisYap)


    def bilgilerimiKaydet(self):
        isim = self.kayitEt.lineEdit.text()
        soyadi = self.kayitEt.lineEdit_2.text()
        telefon_no = self.kayitEt.lineEdit_3.text()
        mail = self.kayitEt.lineEdit_4.text()
        cinsiyet = self.kayitEt.lineEdit_5.text()
        tc = self.kayitEt.lineEdit_6.text()


        if len(telefon_no) != 10:
            print("Telefon numarası 10 hane olmalı.")

        elif len(tc) != 11:
            print("TC kimlik numarası 11 hane olmalı.")

        elif not all([isim, soyadi, telefon_no, mail, cinsiyet, tc]):
            print("Lütfen tüm alanları doldurun.")
            return
        else:
            with open("Musteri_kayit.txt","a",encoding="utf-8") as file:
                file.write("\nİsim: {} , Soyadı: {} , Telefon No: {} , Mail: {} , Cinsiyet: {} , TC: {}".format(isim, soyadi , telefon_no , mail , cinsiyet,tc))
            print("Başarıyla kaydedildi ")
            file.close()


    def cikisYap(self):
        quit()


