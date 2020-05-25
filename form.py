# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S\C#\TPO\GL3\form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(433, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pathText = QtWidgets.QLineEdit(Form)
        self.pathText.setObjectName("pathText")
        self.gridLayout.addWidget(self.pathText, 0, 0, 1, 3)
        self.addPathBtn = QtWidgets.QPushButton(Form)
        self.addPathBtn.setObjectName("addPathBtn")
        self.gridLayout.addWidget(self.addPathBtn, 0, 3, 1, 1)
        self.valList = QtWidgets.QListWidget(Form)
        self.valList.setObjectName("valList")
        self.gridLayout.addWidget(self.valList, 1, 0, 1, 2)
        self.invalList = QtWidgets.QListWidget(Form)
        self.invalList.setObjectName("invalList")
        self.gridLayout.addWidget(self.invalList, 1, 2, 1, 2)
        self.delValBtn = QtWidgets.QPushButton(Form)
        self.delValBtn.setObjectName("delValBtn")
        self.gridLayout.addWidget(self.delValBtn, 2, 0, 1, 1)
        self.moveValBtn = QtWidgets.QPushButton(Form)
        self.moveValBtn.setObjectName("moveValBtn")
        self.gridLayout.addWidget(self.moveValBtn, 2, 1, 1, 1)
        self.delInvalBtn = QtWidgets.QPushButton(Form)
        self.delInvalBtn.setObjectName("delInvalBtn")
        self.gridLayout.addWidget(self.delInvalBtn, 2, 2, 1, 1)
        self.takeInvalBtn = QtWidgets.QPushButton(Form)
        self.takeInvalBtn.setObjectName("takeInvalBtn")
        self.gridLayout.addWidget(self.takeInvalBtn, 2, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FilePathTester"))
        self.addPathBtn.setText(_translate("Form", "Добавить"))
        self.delValBtn.setText(_translate("Form", "Удалить"))
        self.moveValBtn.setText(_translate("Form", "Переместить"))
        self.delInvalBtn.setText(_translate("Form", "Удалить"))
        self.takeInvalBtn.setText(_translate("Form", "Вернуть"))
