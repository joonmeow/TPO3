import behave
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QTimer


@behave.given('a user on main form')
def step_impl(context):
    context.window.pathText.setText('')
    # context.window.valList.clearSelection()
    # context.window.invalList.clearSelection()
    context.window.paths = context.window.valList.count()
    context.window.incorrectPaths = context.window.invalList.count()


@behave.given('path "{path}" is in the list of paths')
def step_impl(context, path):
    QTest.keyClicks(context.window.pathText, path)
    QTest.mouseClick(context.window.addPathBtn, Qt.LeftButton)
    context.window.paths = context.window.valList.count()


@behave.when('they type "{path}" in the input bar')
def step_impl(context, path):
    QTest.keyClicks(context.window.pathText, path)


@behave.when('they push the button "Добавить"')
def step_impl(context):
    QTest.mouseClick(context.window.addPathBtn, Qt.LeftButton)


@behave.when('they push the button "Добавить" on empty the input bar')
def step_impl(context):
    def closeErrorMessage():
        context.window.errorMessage.close()
    QTimer.singleShot(0, closeErrorMessage)
    QTest.mouseClick(context.window.addPathBtn, Qt.LeftButton)


@behave.when('they push the button "Удалить" below the list of paths')
def step_impl(context):
    QTest.mouseClick(context.window.delValBtn, Qt.LeftButton)


@behave.when('they select "{path}" in the list of paths')
def step_impl(context, path):
    item = context.window.valList.item(context.window.valList.count() - 1)
    context.window.valList.setCurrentItem(item)


@behave.when('they push the button "Удалить" below the list of incorrect paths')
def step_impl(context):
    QTest.mouseClick(context.window.delInvalBtn, Qt.LeftButton)


@behave.when('they select "{incorrectPath}" in the list of incorrect paths')
def step_impl(context, incorrectPath):
    item = context.window.invalList.item(context.window.invalList.count() - 1)
    context.window.invalList.setCurrentItem(item)


@behave.when('they push the button "Переместить" below the list of paths')
def step_impl(context):
    QTest.mouseClick(context.window.moveValBtn, Qt.LeftButton)


@behave.when('they push the button "Вернуть" below the list of incorrect paths')
def step_impl(context):
    QTest.mouseClick(context.window.takeInvalBtn, Qt.LeftButton)


@behave.then('they will see "{path}" in the list of paths')
def step_impl(context, path):
    assert context.window.valList.item(context.window.valList.count() - 1).text() == path


@behave.then('they will see "{incorrectPath}" in the list of incorrect paths')
def step_impl(context, incorrectPath):
    assert context.window.invalList.item(context.window.invalList.count() - 1).text() == incorrectPath


@behave.then('they will see warning "{textMessage}"')
def step_impl(context, textMessage):
    assert context.window.errorMessage.text() == textMessage


@behave.then('they will see the list of paths remained unchanged')
def step_impl(context):
    assert context.window.valList.count() is context.window.paths


@behave.then('they will see "{path}" has been deleted from list of paths')
def step_impl(context, path):
    assert context.window.valList.item(context.window.valList.count() - 1) is None


@behave.then('they will see the list of incorrect paths remained unchanged')
def step_impl(context):
    assert context.window.invalList.count() is context.window.incorrectPaths


@behave.then('they will see "{incorrectPath}" has been deleted from list of incorrect paths')
def step_impl(context, incorrectPath):
    assert context.window.invalList.item(context.window.invalList.count() - 1) is None


@behave.then('they will see "{incorrectPath}" in the input bar')
def step_impl(context, incorrectPath):
    assert context.window.pathText.text() == incorrectPath

