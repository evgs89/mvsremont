# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/es89/Dropbox/Projects/Python/MBC PEMOHT/ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.operator = QtWidgets.QWidget()
        self.operator.setObjectName("operator")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.operator)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.operatorTable = QtWidgets.QTableView(self.operator)
        self.operatorTable.setObjectName("operatorTable")
        self.verticalLayout.addWidget(self.operatorTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.operatorDeviceTypeFilter = QtWidgets.QComboBox(self.operator)
        self.operatorDeviceTypeFilter.setObjectName("operatorDeviceTypeFilter")
        self.operatorDeviceTypeFilter.addItem("")
        self.operatorDeviceTypeFilter.addItem("")
        self.operatorDeviceTypeFilter.addItem("")
        self.horizontalLayout.addWidget(self.operatorDeviceTypeFilter)
        self.operatorDateAfter = QtWidgets.QDateEdit(self.operator)
        self.operatorDateAfter.setObjectName("operatorDateAfter")
        self.horizontalLayout.addWidget(self.operatorDateAfter)
        self.operatorDateBefore = QtWidgets.QDateEdit(self.operator)
        self.operatorDateBefore.setObjectName("operatorDateBefore")
        self.horizontalLayout.addWidget(self.operatorDateBefore)
        self.operatorState = QtWidgets.QComboBox(self.operator)
        self.operatorState.setObjectName("operatorState")
        self.horizontalLayout.addWidget(self.operatorState)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.operatorRefreshButton = QtWidgets.QPushButton(self.operator)
        self.operatorRefreshButton.setObjectName("operatorRefreshButton")
        self.horizontalLayout.addWidget(self.operatorRefreshButton)
        self.operatorAddIncidentButton = QtWidgets.QPushButton(self.operator)
        self.operatorAddIncidentButton.setObjectName("operatorAddIncidentButton")
        self.horizontalLayout.addWidget(self.operatorAddIncidentButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.operator, "")
        self.arena = QtWidgets.QWidget()
        self.arena.setObjectName("arena")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.arena)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.arenaTable = QtWidgets.QTableView(self.arena)
        self.arenaTable.setObjectName("arenaTable")
        self.verticalLayout_4.addWidget(self.arenaTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.arenaDateAfter = QtWidgets.QDateEdit(self.arena)
        self.arenaDateAfter.setObjectName("arenaDateAfter")
        self.horizontalLayout_2.addWidget(self.arenaDateAfter)
        self.arenaDateBefore = QtWidgets.QDateEdit(self.arena)
        self.arenaDateBefore.setObjectName("arenaDateBefore")
        self.horizontalLayout_2.addWidget(self.arenaDateBefore)
        self.arenaState = QtWidgets.QComboBox(self.arena)
        self.arenaState.setObjectName("arenaState")
        self.horizontalLayout_2.addWidget(self.arenaState)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.arenaRefresh = QtWidgets.QPushButton(self.arena)
        self.arenaRefresh.setObjectName("arenaRefresh")
        self.horizontalLayout_2.addWidget(self.arenaRefresh)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.arena, "")
        self.uragan = QtWidgets.QWidget()
        self.uragan.setObjectName("uragan")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.uragan)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.uraganTable = QtWidgets.QTableView(self.uragan)
        self.uraganTable.setObjectName("uraganTable")
        self.verticalLayout_6.addWidget(self.uraganTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uraganDateAfter = QtWidgets.QDateEdit(self.uragan)
        self.uraganDateAfter.setObjectName("uraganDateAfter")
        self.horizontalLayout_3.addWidget(self.uraganDateAfter)
        self.uraganDateBefore = QtWidgets.QDateEdit(self.uragan)
        self.uraganDateBefore.setObjectName("uraganDateBefore")
        self.horizontalLayout_3.addWidget(self.uraganDateBefore)
        self.uraganState = QtWidgets.QComboBox(self.uragan)
        self.uraganState.setObjectName("uraganState")
        self.horizontalLayout_3.addWidget(self.uraganState)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.uraganRefresh = QtWidgets.QPushButton(self.uragan)
        self.uraganRefresh.setObjectName("uraganRefresh")
        self.horizontalLayout_3.addWidget(self.uraganRefresh)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.uragan, "")
        self.usermanagement = QtWidgets.QWidget()
        self.usermanagement.setObjectName("usermanagement")
        self.tabWidget.addTab(self.usermanagement, "")
        self.more = QtWidgets.QWidget()
        self.more.setObjectName("more")
        self.tabWidget.addTab(self.more, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 729, 27))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.connectToDB = QtWidgets.QAction(MainWindow)
        self.connectToDB.setObjectName("connectToDB")
        self.settings = QtWidgets.QAction(MainWindow)
        self.settings.setObjectName("settings")
        self.menu.addAction(self.connectToDB)
        self.menu.addAction(self.settings)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.operatorDeviceTypeFilter.setItemText(0, _translate("MainWindow", "Все"))
        self.operatorDeviceTypeFilter.setItemText(1, _translate("MainWindow", "Арена"))
        self.operatorDeviceTypeFilter.setItemText(2, _translate("MainWindow", "Ураган"))
        self.operatorRefreshButton.setText(_translate("MainWindow", "Обновить"))
        self.operatorAddIncidentButton.setText(_translate("MainWindow", "Добавить!!!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.operator), _translate("MainWindow", "Оператор"))
        self.arenaRefresh.setText(_translate("MainWindow", "Обновить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.arena), _translate("MainWindow", "Ремонт арен"))
        self.uraganRefresh.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uragan), _translate("MainWindow", "Ремонт Ураган-ЮГ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usermanagement), _translate("MainWindow", "Управление пользователями"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.more), _translate("MainWindow", "Дополнительно"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.connectToDB.setText(_translate("MainWindow", "Соединиться с БД"))
        self.settings.setText(_translate("MainWindow", "Настройки программы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
