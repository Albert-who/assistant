import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Voice Assistant')
        self.lbl = QLabel('Привет, как я могу Вам помочь?', self)
        self.lbl.move(50, 50)
        self.btn = QPushButton('Нажми меня', self)
        self.btn.setToolTip('Это кнопка для обработки вашего запроса')
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.buttonClicked)        
        self.show()
        
    def buttonClicked(self):
        self.lbl.setText('Я обработал ваш запрос')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# на это можете не обращать внимания