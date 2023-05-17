"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from b_systeminfo_widget import SystemInfoWindow
from c_weatherapi_widget import WeatherInfoWindow

class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.app_1 = SystemInfoWindow(self.centralwidget)
        self.app_2 = WeatherInfoWindow(self.centralwidget)
        self.horizontalLayout.addWidget(self.app_1)
        self.horizontalLayout.addWidget(self.app_2)
        self.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
