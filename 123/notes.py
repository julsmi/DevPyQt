import datetime
import json

from PySide6 import QtWidgets, QtGui

from design import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.notes = {}
        self.file = {
            'notes': self.notes
        }

        try:
            with open('data.json', 'r', encoding='utf8') as file:
                self.file = json.load(file)
                self.notes = self.file['notes']

        except:
            with open('data.json', 'w', encoding='utf8') as file:
                self.file = {
                    'notes': self.notes,
                }
                json.dump(self.file, file, indent=4)


    def initSignals(self):
        self.ui.saveButton.clicked.connect(self.saveNote)
        self.ui.delete_Button.clicked.connect(self.deleteNote)
        self.ui.newNoteButton.clicked.connect(self.newNote)
        self.ui.pushButton.clicked.connect(self.showNote)


    def newNote(self):
        self.ui.noteHead.clear()
        self.ui.note_Text.clear()
        self.ui.dateTimeEdit.setDateTime(datetime.datetime.now())

    def saveNote(self):
        self.notes[self.get_note_title()] = {
            "title": self.get_note_title(),
            "date": str(datetime.datetime.now()),
            "content": self.get_note_text(),
            "deadline": self.getDeadline()
            }

        self.ui.saveButton.setEnabled(False)
        self.ui.delete_Button.setEnabled(True)

        with open('data.json', 'w', encoding='utf8') as file:
            self.file = {
                'notes': self.notes,
            }
            json.dump(self.file, file, indent=4)

    def deleteNote(self, title):
        title = self.get_note_title()
        for note in self.file['notes']:
            pass



    def showNote(self):
        date = self.ui.dateTimeEdit_2.text()
        for note in self.file["notes"]:
            if note["deadline"] == date:
                self.ui.plainTextEdit.setPlainText(f'Заметки на эту дату:{self.notes["content"]}')


    def get_note_title(self):
        return self.ui.noteHead.toPlainText()

    def get_note_text(self):
        return self.ui.note_Text.toPlainText()

    def getDeadline(self):
        return self.ui.dateTimeEdit.text()



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

