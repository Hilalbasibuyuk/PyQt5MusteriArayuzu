from PyQt5.QtWidgets import *
from musteriKaydolmasi import Ui_Form
from KaydetPenceresi_main import kayit_et
class kaydet(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kaydetme = Ui_Form()
        self.kaydetme.setupUi(self)
        self.kayıt_et = kayit_et()
        self.kaydetme.pushButton.clicked.connect(self.musteri_islemleri)
        self.kaydetme.pushButton_2.clicked.connect(self.cikis)
        

    def musteri_islemleri(self):
        self.hide()
        self.kayıt_et.show()

    def cikis(self):
        quit()


