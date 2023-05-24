import datetime
import json

from PySide6 import QtWidgets

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
        self.ui.pushButton_2.clicked.connect(self.showAllNotes)


    def newNote(self):
        self.ui.noteHead.clear()
        self.ui.note_Text.clear()
        self.ui.dateTimeEdit.setDateTime(datetime.datetime.today())
        self.ui.saveButton.setEnabled(True)

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
        for note in list(self.file['notes'].keys()):
            if note == title:
                self.file['notes'].pop(note)
                self.ui.note_Text.setPlainText('Заметка удалена!')

        with open('data.json', 'w', encoding='utf8') as file:
            self.file = {
                'notes': self.notes,
            }
            json.dump(self.file, file, indent=4)

    def showNote(self):
        date = self.ui.dateTimeEdit_2.text()
        flag = False
        for note, values in self.file["notes"].items():
            if values["deadline"] == date:
                self.ui.plainTextEdit.appendPlainText(f'Заметки на эту дату: {values["content"]}')
                flag = True
        if not flag:
            self.ui.plainTextEdit.setPlainText(f'Заметок на эту дату нет!')
            raise ValueError()

    def showAllNotes(self):
        for note, values in self.file["notes"].items():
            if values["content"]:
                self.ui.plainTextEdit.appendPlainText(f'Нужно сделать: {values["content"]}')


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

