# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\wpython\QtUi_one\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(40, 130, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 130, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 10, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(76, 10, 71, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuThis_is_my_baseline = QtWidgets.QMenu(self.menuBar)
        self.menuThis_is_my_baseline.setObjectName("menuThis_is_my_baseline")
        self.menuSomeThing_New = QtWidgets.QMenu(self.menuBar)
        self.menuSomeThing_New.setObjectName("menuSomeThing_New")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionHelio = QtWidgets.QAction(MainWindow)
        self.actionHelio.setObjectName("actionHelio")
        self.actionHolie = QtWidgets.QAction(MainWindow)
        self.actionHolie.setObjectName("actionHolie")
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuThis_is_my_baseline.addAction(self.actionFile)
        self.menuThis_is_my_baseline.addSeparator()
        self.menuThis_is_my_baseline.addAction(self.actionExit)
        self.menuSomeThing_New.addSeparator()
        self.menuSomeThing_New.addAction(self.actionHelio)
        self.menuSomeThing_New.addSeparator()
        self.menuSomeThing_New.addAction(self.actionHolie)
        self.menuBar.addAction(self.menuThis_is_my_baseline.menuAction())
        self.menuBar.addAction(self.menuSomeThing_New.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "One"))
        self.radioButton_2.setText(_translate("MainWindow", "Two"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))
        self.label.setText(_translate("MainWindow", "Your Name"))
        self.menuThis_is_my_baseline.setTitle(_translate("MainWindow", "This is my baseline"))
        self.menuSomeThing_New.setTitle(_translate("MainWindow", "SomeThing New"))
        self.actionHelio.setText(_translate("MainWindow", "Helio"))
        self.actionHolie.setText(_translate("MainWindow", "Holie"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
