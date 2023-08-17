from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 434)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.txt_edt_yazi = QtWidgets.QTextEdit(Form)
        self.txt_edt_yazi.setGeometry(QtCore.QRect(20, 30, 481, 261))
        self.txt_edt_yazi.setStyleSheet("")
        self.txt_edt_yazi.setObjectName("txt_edt_yazi")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 350, 481, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txt_edt_yazi.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Merhaba.Teknolojik aletler mağazamıza hoş geldiniz. Mağazamızda bilgisayar , telefon ,tablet, kulaklık ,mouse , şarj aletleri ve dijital saatler bulunmaktadır. Web sitemize üye olursanız , belirli zamanlarda sadece üyelere özel olarak yapılan kampanyalardan yararlanabilirsiniz. İlk üye olma gününüze özel tüm ürünlere %15 indirim uygulanacaktır (Üye olduğunuz ilk gün satın alırsanız geçerlidir sadece).Üye olmak istiyorsanız evet , istemiyorsanız hayır seçeneğine tıklayınız. Üye olmak istiyor musunuz?</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "EVET"))
        self.pushButton_2.setText(_translate("Form", "HAYIR"))