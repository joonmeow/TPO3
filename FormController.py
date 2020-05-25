import sys
from PyQt5 import QtCore, QtWidgets
from ProdactionCode import form, FilePathTester


class FormController(QtWidgets.QWidget, form.Ui_Form):
    def __init__(self, parent=None):
        super(FormController, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.filePathTester = FilePathTester.FilePathTester()
        self.errorMessage = None

        self.addPathBtn.clicked.connect(self.addPath)
        self.delValBtn.clicked.connect(self.removePath)
        self.delInvalBtn.clicked.connect(self.removeIncorrectPath)
        self.moveValBtn.clicked.connect(self.moveCorrectPath)
        self.takeInvalBtn.clicked.connect(self.takeIncorrectPath)

    def addPath(self):
        try:
            result = self.filePathTester.addPath(self.pathText.text())
        except ValueError as error:
            self.showErrorMessage('Error', str(error))
            return

        if result:
            self.valList.addItem(self.pathText.text())
        else:
            self.invalList.addItem(self.pathText.text())
        self.pathText.setText('')

    def removePath(self):
        if self.valList.currentItem() == None or \
                self.filePathTester.removeCorrectPath(self.valList.currentItem().text()) == False:
            return
        self.valList.takeItem(self.valList.currentRow())

    def removeIncorrectPath(self):
        if self.invalList.currentItem() == None or \
                self.filePathTester.removeIncorrectPath(self.invalList.currentItem().text()) == False:
            return
        self.invalList.takeItem(self.invalList.currentRow())

    def moveCorrectPath(self):
        if self.valList.currentItem() == None or \
                self.filePathTester.moveCorrectPathToIncorrect(self.valList.currentItem().text()) == False:
            return
        self.invalList.addItem(self.valList.currentItem().text())
        self.valList.takeItem(self.valList.currentRow())

    def takeIncorrectPath(self):
        if self.invalList.currentItem() == None:
            currentItem = ''
        else:
            currentItem = self.invalList.currentItem().text()
        try:
            result = self.filePathTester.takeIncorrectPath(currentItem)
        except ValueError as error:
            self.showErrorMessage('Error', str(error))
            return
        if result == False:
            return
        self.pathText.setText(result)
        self.invalList.takeItem(self.invalList.currentRow())

    def showErrorMessage(self, head, message):
        self.errorMessage = QtWidgets.QMessageBox()
        self.errorMessage.setIcon(QtWidgets.QMessageBox.Warning)
        self.errorMessage.setWindowTitle(head)
        self.errorMessage.setText(message)
        self.errorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.errorMessage.show()


def showWindow():
    app = QtWidgets.QApplication(sys.argv)
    window = FormController()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    showWindow()
