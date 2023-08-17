from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
import sys

class musterileriGoster(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.text_edit = QTextEdit(self)
        self.setGeometry(300, 300, 800, 400)
        layout.addWidget(self.text_edit)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.load_customer_info()

    def load_customer_info(self):
        try:
            with open("musteri_kayit.txt", "r", encoding="utf-8") as file:
                customer_info = file.read()
                self.text_edit.setPlainText(customer_info)
        except FileNotFoundError:
            self.text_edit.setPlainText("Dosya bulunamadı.")


