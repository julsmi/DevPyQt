"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""
import time

from PySide6 import QtWidgets
from PySide6 import QtCore


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

    def event(self, event: QtCore.QEvent) -> bool:
        print(time.ctime(), event)
        return super().event(event)

    def initSignal(self):
        self.pushButtonMirror.clicked.connect(self.invertData)
        # self.lineEditInput.textChanged.connect(lambda x: self.lineEditMirror.setText(x[::-1]))

    def invertData(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
