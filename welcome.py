import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import loginn
import lpp

class WelcomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laptop Price Prediction Program")
        self.setFixedSize(800, 600)

        # Add background image
        background_image = QtGui.QPixmap("background.jpg")
        background_label = QtWidgets.QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 800, 600)

        # Add title label
        title_label = QtWidgets.QLabel(self)
        title_label.setText("Welcome to\n Laptop Price Prediction Program")
        title_label.setGeometry(50, 50, 700, 100)
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_font = QtGui.QFont()
        title_font.setPointSize(30)
        title_font.setBold(True)
        title_label.setFont(title_font)

        # Add description label
        description_label = QtWidgets.QLabel(self)
        description_label.setText("This program helps you predict the price of a laptop based on its specifications.")
        description_label.setGeometry(50, 200, 700, 50)
        description_label.setAlignment(QtCore.Qt.AlignCenter)
        description_font = QtGui.QFont()
        description_font.setPointSize(14)
        description_label.setFont(description_font)

        # Add start button
        start_button = QtWidgets.QPushButton(self)
        start_button.setText("Start")
        start_button.setGeometry(300, 350, 200, 50)
        start_button.setFont(description_font)
        start_button.setStyleSheet("background-color: #008080; color: white; border-radius: 10px;")
        start_button.clicked.connect(self.open_main_window)
        # self.open_main_window()

    def open_main_window(self):
        # self.log = lpp.QtWidgets.QStackedWidget()
        # self.loginwindow = lpp.loginApp()
        # self.regwindow = lpp.regApp()
        # self.predwindow = lpp.predApp()
        # self.log.addWidget(self.loginwindow)
        # self.log.addWidget(self.regwindow)
        # self.log.addWidget(self.predwindow)
        # self.log.setCurrentIndex(0)
        # self.log.setFixedSize(650,500)
        # self.log.setWindowTitle('Laptop Price Predictor')
        # self.log.setWindowIcon(QIcon('icon.png'))
        self.log = loginn.LoginPage()
        self.log.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    welcome = WelcomeWindow()
    welcome.show()
    sys.exit(app.exec_())

