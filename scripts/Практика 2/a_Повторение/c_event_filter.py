"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

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
        self.label = QtWidgets.QLabel("До наведения")
        self.pushButtonMirror.installEventFilter(self)
        self.lineEditMirror.installEventFilter(self)
        self.lineEditInput.installEventFilter(self)
        self.label.installEventFilter(self)
        self.label.setTextFormat(QtCore.Qt.RichText)


        layout_1 = QtWidgets.QHBoxLayout()
        layout_2 = QtWidgets.QVBoxLayout()

        layout_1.addWidget(self.lineEditInput)
        layout_1.addWidget(self.lineEditMirror)

        layout_2.addLayout(layout_1)
        layout_2.addWidget(self.pushButtonMirror)

        self.setLayout(layout_2)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.lineEditInput and event.type() == event.type() == QtCore.QEvent.Type.Wheel:
            self.lineEditMirror.setText("Попали на 1 форму")

        return super().eventFilter(watched, event)

    def initSignal(self):
        self.pushButtonMirror.clicked.connect(self.invertData)


    def invertData(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
