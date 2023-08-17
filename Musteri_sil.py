from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Musteri_sil(object):
    def setupUi(self, Musteri_sil):
        Musteri_sil.setObjectName("Musteri_sil")
        Musteri_sil.resize(489, 220)
        self.label = QtWidgets.QLabel(Musteri_sil)
        self.label.setGeometry(QtCore.QRect(20, 20, 461, 31))
        self.label.setObjectName("label")
        self.lineEdit_sil = QtWidgets.QLineEdit(Musteri_sil)
        self.lineEdit_sil.setGeometry(QtCore.QRect(40, 80, 391, 22))
        self.lineEdit_sil.setObjectName("lineEdit_sil")
        self.widget = QtWidgets.QWidget(Musteri_sil)
        self.widget.setGeometry(QtCore.QRect(50, 140, 381, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_vazgec = QtWidgets.QPushButton(self.widget)
        self.btn_vazgec.setObjectName("btn_vazgec")
        self.horizontalLayout.addWidget(self.btn_vazgec)
        self.btn_sil = QtWidgets.QPushButton(self.widget)
        self.btn_sil.setObjectName("btn_sil")
        self.horizontalLayout.addWidget(self.btn_sil)

        self.retranslateUi(Musteri_sil)
        QtCore.QMetaObject.connectSlotsByName(Musteri_sil)

    def retranslateUi(self, Musteri_sil):
        _translate = QtCore.QCoreApplication.translate
        Musteri_sil.setWindowTitle(_translate("Musteri_sil", "Müşteri Silme Sayfası"))
        self.label.setText(_translate("Musteri_sil", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Silmek istediğiniz müşterinin TC kimlik numarasını giriniz:</span></p></body></html>"))
        self.btn_vazgec.setText(_translate("Musteri_sil", "Vazgeç"))
        self.btn_sil.setText(_translate("Musteri_sil", "Müşteriyi Sil"))
