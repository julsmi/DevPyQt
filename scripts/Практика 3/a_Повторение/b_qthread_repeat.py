"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets, QtCore
import requests


class CheckSiteThread(QtCore.QThread):
    started_signal = QtCore.Signal()
    finished_signal = QtCore.Signal()
    status_code_signal = QtCore.Signal(int)

    def __init__(self, parent=None, url=''):
        super().__init__(parent)
        self.url = url

    def run(self):
        self.started_signal.emit()
        try:
            response = requests.get(self.url)
            status_code = response.status_code
        except requests.exceptions.RequestException:
            status_code = None
        self.status_code_signal.emit(status_code)
        self.finished_signal.emit()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.urlLineEdit = QtWidgets.QLineEdit()
        self.checkButton = QtWidgets.QPushButton('Проверить')
        self.statusLabel = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel('URL'))
        layout.addWidget(self.urlLineEdit)
        layout.addWidget(self.checkButton)
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

        self.thread_1 = CheckSiteThread()
        self.thread_1.started_signal.connect(self.onThreadStart)
        self.thread_1.finished_signal.connect(self.onThreadFinish)
        self.thread_1.status_code_signal.connect(self.onThreadStatus)

        self.checkButton.clicked.connect(self.onClicked)

    def onThreadStart(self):
        self.checkButton.setEnabled(False)
        self.statusLabel.setText('Начали расчет')

    def onThreadFinish(self):
        self.checkButton.setEnabled(True)
        #self.statusLabel.setText('Закончили расчет')

    def onThreadStatus(self, value):
        if value is None:
            self.statusLabel.setText('Сайт недоступен')
        elif value == 200:
            self.statusLabel.setText('Сайт доступен')
        else:
            self.statusLabel.setText(f'Что-то не так, код {value}')

    def onClicked(self):
        url = self.urlLineEdit.text()
        self.thread_1.url = url
        self.thread_1.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
