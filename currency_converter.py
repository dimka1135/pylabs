import json
import sys
from urllib.request import urlopen

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)


Qt.Key_Enter    #Enter на цифровой(дополнительной) клавиатуре
Qt.Key_Return   #Enter на основной клавиатуре


class Course(QObject):
    CBR_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def get(self):
        with urlopen(self.CBR_URL) as r:
            courses = json.load(r)
            return courses['Valute']['USD']['Value']


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()
        self._initLayouts()

    def _initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)
        self.srcAmount.setDecimals(3)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        self.resultAmount.setDecimals(3)

        self.convertBtn = QPushButton('Перевести', self)
        self.resetBtn = QPushButton('Сброс', self)
        self.convertBtn.setEnabled(False)

    def _initSignals(self):
        self.convertBtn.clicked.connect(self.convert)
        self.resetBtn.clicked.connect(self.reset)
        self.srcAmount.valueChanged.connect(self.valuechange)
        self.resultAmount.valueChanged.connect(self.valuechange)

    def _initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.resetBtn)

        self.setCentralWidget(w)

    def convert(self):
        # value = self.srcAmount.value()

        # if value:
        #     self.resultAmount.setValue(value / Course().get())

        valueRUB = self.srcAmount.value()
        valueUSD = self.resultAmount.value()

        if valueRUB and not valueUSD:
            self.resultAmount.setValue(valueRUB / Course().get())
        elif valueUSD and not valueRUB:
            self.srcAmount.setValue(valueUSD * Course().get())

    def reset(self):
        self.srcAmount.setValue(0)
        self.resultAmount.setValue(0)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.convert()

    def valuechange(self):
        if (self.srcAmount.value()) and (self.resultAmount.value()):
            self.convertBtn.setEnabled(False)
        elif (self.srcAmount.value()) or (self.resultAmount.value()):
            self.convertBtn.setEnabled(True)
        else:
            self.convertBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = MainWindow()
    converter.show()
    sys.exit(app.exec_())