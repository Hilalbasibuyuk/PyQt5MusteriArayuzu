import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Ekranı")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.username_edit = QLineEdit(self)
        self.username_edit.setPlaceholderText("Kullanıcı Adı")
        layout.addWidget(self.username_edit)

        self.password_edit = QLineEdit(self)
        self.password_edit.setPlaceholderText("Parola")
        self.password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_edit)

        self.login_button = QPushButton("Giriş", self)
        layout.addWidget(self.login_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.login_button.clicked.connect(self.check_login)

    def check_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if username == "kullanici" and password == "parola":
            self.close()
            self.open_next_window()
        else:
            self.show_login_error()

    def open_next_window(self):
        self.next_window = NextWindow()
        self.next_window.show()

    def show_login_error(self):
        error_label = QLabel("Hatalı kullanıcı adı veya parola. Tekrar deneyin.", self)
        layout = self.layout()
        layout.addWidget(error_label)

class NextWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bir Sonraki Sayfa")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        message_label = QLabel("Başarılı giriş! Hoş geldiniz.", self)
        layout.addWidget(message_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

