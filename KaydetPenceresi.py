from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kaydet_penceresi(object):
    def setupUi(self, Kaydet_penceresi):
        Kaydet_penceresi.setObjectName("Kaydet_penceresi")
        Kaydet_penceresi.resize(575, 667)
        self.label_6 = QtWidgets.QLabel(Kaydet_penceresi)
        self.label_6.setGeometry(QtCore.QRect(130, 20, 311, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Kaydet_penceresi)
        self.label_7.setGeometry(QtCore.QRect(40, 70, 361, 61))
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(Kaydet_penceresi)
        self.layoutWidget.setGeometry(QtCore.QRect(44, 150, 80, 451))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.layoutWidget1 = QtWidgets.QWidget(Kaydet_penceresi)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 120, 139, 521))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.pushButton = QtWidgets.QPushButton(Kaydet_penceresi)
        self.pushButton.setGeometry(QtCore.QRect(380, 160, 141, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Kaydet_penceresi)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 400, 141, 121))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Kaydet_penceresi)
        QtCore.QMetaObject.connectSlotsByName(Kaydet_penceresi)

    def retranslateUi(self, Kaydet_penceresi):
        _translate = QtCore.QCoreApplication.translate
        Kaydet_penceresi.setWindowTitle(_translate("Kaydet_penceresi", "Kaydet Penceresi"))
        self.label_6.setText(_translate("Kaydet_penceresi", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">MÜŞTERİ KAYDETME FORMU</span></p></body></html>"))
        self.label_7.setText(_translate("Kaydet_penceresi", "<html><head/><body><p><span style=\" font-size:9pt;\">LÜTFEN AŞAĞIYA BİLGİLERİNİZİ GİRİNİZ:</span></p></body></html>"))
        self.label.setText(_translate("Kaydet_penceresi", "İSİM:"))
        self.label_2.setText(_translate("Kaydet_penceresi", "SOYADI:"))
        self.label_3.setText(_translate("Kaydet_penceresi", "TELEFON NO:"))
        self.label_4.setText(_translate("Kaydet_penceresi", "MAİL:"))
        self.label_5.setText(_translate("Kaydet_penceresi", "CİNSİYET:"))
        self.label_8.setText(_translate("Kaydet_penceresi", "TC:"))
        self.pushButton.setText(_translate("Kaydet_penceresi", "Bilgilerimi Kaydet"))
        self.pushButton_2.setText(_translate("Kaydet_penceresi", "Vazgeç ve Çıkış Yap"))
