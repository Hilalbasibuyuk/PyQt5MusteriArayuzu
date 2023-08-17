import sys
from PyQt5 import QtCore,QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from yonetici_islemleri import Ui_Yonetici_islemleri
from KaydetPenceresi_main import kayit_et
from KaydetPenceresi import Ui_Kaydet_penceresi
from Musteri_sil_main import musteriSil
from Musterileri_goruntule_main import musterileriGoster
class yonetici(QWidget):
    def __init__(self):
        super().__init__()
        self.yonetmek = Ui_Yonetici_islemleri()
        self.yonetmek.setupUi(self)
        self.kayitEt=kayit_et()
        self.silme=musteriSil()
        self.goster = musterileriGoster()
        self.yonetmek.musterileri_goruntule.clicked.connect(self.musteri_goruntuleme)
        self.yonetmek.musteri_sil.clicked.connect(self.musterileri_sil)
        self.yonetmek.cikis.clicked.connect(self.cikisYap)

        

    def musteri_goruntuleme(self):
        self.hide()
        self.goster.show()

    def musterileri_sil(self):
        self.hide()
        self.silme.show()

    def cikisYap(self):
        quit()


"""class NextWindow(QMainWindow):
    def __init__(self) ->None:
        super.__init__() 
        self.kayitEt = Ui_Kaydet_penceresi()
        self.kayitEt=kayit_et()
        self.kayitEt.setupUi(self)
        self.setWindowTitle("Müşteri Listesi")
        self.setGeometry(100, 100, 400, 200)
        tc =self.kayitEt.lineEdit_6.text()

        with open("Musteri_kayit.txt","r",encoding="utf-8") as file:
            satirlar=file.readlines()

        with open("Musteri_kayit.txt","w",encoding="utf-8") as file:
            for satir in satirlar:
                if"TC: ".format(tc) not in satir:
                    file.write(satir)"""


def app():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        win = yonetici()
        win.show()
        sys.exit(app.exec_())
app()


"""
    def add_window(self):
        yonetici.count=yonetici.count+1
        sub = QMdiSubWindow()
        self.mdi.addSubWindow(sub)
        sub.show()

     uic.loadUi("yonetici_islemleri.ui",self)
        self.mdi = self.findChild( QMdiArea,"mdiArea")
        self.button = self.findChild(QPushButton ,"musterileri_goruntule")
        self.button.clicked.connect(self.add_window)
"""

"""scroll_area = QScrollArea(self)
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)
        self.musteri_goruntuleme(scroll_area)

        layout = QVBoxLayout(content_widget)

        try:
            with open("Musteri.kayit.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    label = QLabel(line)
                    layout.addWidget(label)
        except FileNotFoundError:
            label = QLabel("Dosya bulunamadı.")
            layout.addWidget(label)"""








