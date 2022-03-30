
import sys
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox, 
    QApplication, QVBoxLayout)


class Example(QWidget):

    def __init__(self,data):
        super().__init__()
        self.data = data
        self.initUI()
        

    def initUI(self):
        
        vbox = QVBoxLayout(self)

        listWidget = QListWidget()
        for i in self.data:
            listWidget.addItem(i) 
        listWidget.itemDoubleClicked.connect(self.onClicked)
        
        vbox.addWidget(listWidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Tokens')
        self.show()

    def onClicked(self, item):

        QMessageBox.information(self, "Info", item.text())


def mains():

    app = QApplication(sys.argv)
    ex = Example(['Daniel','ramiro'])
    sys.exit(app.exec_())


if __name__ == '__main__':
    mains()