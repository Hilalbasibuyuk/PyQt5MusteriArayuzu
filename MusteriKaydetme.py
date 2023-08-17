from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_kampanya(object):
    def setupUi(self, form_kampanya):
        form_kampanya.setObjectName("form_kampanya")
        form_kampanya.resize(447, 496)
        self.btn_yonetici = QtWidgets.QPushButton(form_kampanya)
        self.btn_yonetici.setGeometry(QtCore.QRect(140, 100, 141, 81))
        self.btn_yonetici.setObjectName("btn_yonetici")
        self.btn_musteri = QtWidgets.QPushButton(form_kampanya)
        self.btn_musteri.setGeometry(QtCore.QRect(140, 260, 141, 81))
        self.btn_musteri.setObjectName("btn_musteri")

        self.retranslateUi(form_kampanya)
        QtCore.QMetaObject.connectSlotsByName(form_kampanya)

    def retranslateUi(self, form_kampanya):
        _translate = QtCore.QCoreApplication.translate
        form_kampanya.setWindowTitle(_translate("form_kampanya", "Kampanya"))
        self.btn_yonetici.setText(_translate("form_kampanya", "Yönetici İşlemleri"))
        self.btn_musteri.setText(_translate("form_kampanya", "Müşteri İşlemleri"))
