from PyQt5 import QtWidgets
from ProdactionCode.FormController import FormController
import behave
from selenium import webdriver
import sys
import os


@behave.fixture
def browserChrome(context):
    context.browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
    yield context.browser
    context.browser.quit()


@behave.fixture
def qtFilePathTester(context):
    app = QtWidgets.QApplication(sys.argv)
    window = FormController()
    window.show()
    context.window = window
    yield context.window


def before_tag(context, tag):
    if tag == 'chrome':
        behave.use_fixture(browserChrome, context)
    if tag == 'qt':
        behave.use_fixture(qtFilePathTester, context)
