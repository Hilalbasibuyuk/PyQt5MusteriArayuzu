from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from Musteri_sil import Ui_Musteri_sil
class musteriSil (QWidget):
    def __init__(self):
        super().__init__() 
        self.sil = Ui_Musteri_sil()
        self.sil.setupUi(self)
        self.sil.btn_sil.clicked.connect(self.musteri_sil)
        self.sil.btn_vazgec.clicked.connect(self.vazgec)

    def musteri_sil(self):
        tc = self.sil.lineEdit_sil.text()
        satirlar = []

        if len(tc) != 11:
            print("Geçerli bir TC kimlik numarası girmelisiniz (11 hane).")
        else:
            with open("Musteri_kayit.txt", "r",encoding="utf-8") as file:
                satirlar=file.readlines()

        found = False
        with open("Musteri_kayit.txt", "w",encoding="utf-8") as file:
            for satir in satirlar:
                if "TC: {}".format(tc) not in satir:
                    found=True
                else:
                     file.write(satir)

        if found:
            print("Musteri bilgileri başarıyla silindi.")
        else:
            print("Belirtilen TC kimlik numarası kayıtlı listede bulunamadı.")




                
         

    def vazgec(self):
        quit()



def app():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        win = musteriSil()
        win.show()
        sys.exit(app.exec_())
app()



