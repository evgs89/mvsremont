# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/es89/Dropbox/Projects/Python/MBC PEMOHT/ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serialNumberEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.serialNumberEdit.setObjectName("serialNumberEdit")
        self.horizontalLayout.addWidget(self.serialNumberEdit)
        self.devtypeBox = QtWidgets.QComboBox(self.centralWidget)
        self.devtypeBox.setObjectName("devtypeBox")
        self.horizontalLayout.addWidget(self.devtypeBox)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateAfter = QtWidgets.QDateEdit(self.centralWidget)
        self.dateAfter.setObjectName("dateAfter")
        self.horizontalLayout.addWidget(self.dateAfter)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateBefore = QtWidgets.QDateEdit(self.centralWidget)
        self.dateBefore.setObjectName("dateBefore")
        self.horizontalLayout.addWidget(self.dateBefore)
        self.stateBox = QtWidgets.QComboBox(self.centralWidget)
        self.stateBox.setObjectName("stateBox")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.horizontalLayout.addWidget(self.stateBox)
        self.refreshButton = QtWidgets.QPushButton(self.centralWidget)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout.addWidget(self.refreshButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.addIncidentButton = QtWidgets.QPushButton(self.centralWidget)
        self.addIncidentButton.setObjectName("addIncidentButton")
        self.horizontalLayout.addWidget(self.addIncidentButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.connectToDbAction = QtWidgets.QAction(MainWindow)
        self.connectToDbAction.setObjectName("connectToDbAction")
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.menu.addAction(self.connectToDbAction)
        self.menu.addSeparator()
        self.menu.addAction(self.exitAction)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "с"))
        self.label_2.setText(_translate("MainWindow", "до"))
        self.stateBox.setItemText(0, _translate("MainWindow", "все"))
        self.stateBox.setItemText(1, _translate("MainWindow", "снятые"))
        self.stateBox.setItemText(2, _translate("MainWindow", "в цеху"))
        self.stateBox.setItemText(3, _translate("MainWindow", "на складе"))
        self.refreshButton.setText(_translate("MainWindow", "Обновить"))
        self.addIncidentButton.setText(_translate("MainWindow", "Добавить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.connectToDbAction.setText(_translate("MainWindow", "Соединиться с БД"))
        self.exitAction.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

