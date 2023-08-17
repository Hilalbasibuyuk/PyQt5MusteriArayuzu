import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from musteriKaydolmasi_main import kaydet
from MusteriKaydetme import Ui_form_kampanya
from yönetici_girisi_main import Yonetici_giris
class App(QtWidgets.QMainWindow):
    def __init__(self)-> None:
        super().__init__()
        self.ui = Ui_form_kampanya()
        self.ui.setupUi(self)
        self.kaydetme= kaydet()
        self.yonetme = Yonetici_giris()
        self.ui.btn_musteri.clicked.connect(self.musteriler)
        self.ui.btn_yonetici.clicked.connect(self.yonetici)


    def musteriler(self):
        self.hide()
        self.kaydetme.show()
        

    def yonetici(self):
        self.hide()
        self.yonetme.show()
        
        
def app():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        win = App()
        win.show()
        sys.exit(app.exec_())
app()


