"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignal()
    def initUi(self):

        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.pushButtonMirror = QtWidgets.QPushButton("Развернуть")

        layout_1 = QtWidgets.QHBoxLayout()
        layout_2 = QtWidgets.QVBoxLayout()

        layout_1.addWidget(self.lineEditInput)
        layout_1.addWidget(self.lineEditMirror)

        layout_2.addLayout(layout_1)
        layout_2.addWidget(self.pushButtonMirror)

        self.setLayout(layout_2)

    def initSignal(self):
        self.pushButtonMirror.clicked.connect(self.invertData)
        #self.lineEditInput.textChanged.connect(lambda x: self.lineEditMirror.setText(x[::-1]))

    def invertData(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
