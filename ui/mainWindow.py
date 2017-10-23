# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QAbstractTableModel, QDate, Qt, QSortFilterProxyModel, QPoint
from PyQt5.QtWidgets import QMainWindow,QHeaderView#, QMessageBox

from .Ui_mainWindow import Ui_MainWindow
from .addIncident import addIncident
from .models import operatorModel as Model

import configparser
import datetime # , date, timedelta


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    reconnectDB = pyqtSignal()
    def __init__(self, user, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        Today = QDate.currentDate()
        self.dateBefore.setDate(Today)
        self.currentUser = user
        self.readSettings()
        self.dateAfter.setDate(Today.addDays(0-int(self.progConfig['interface']['defaultDaysToView'])))
        query = """SELECT * FROM operatorView WHERE
                    `takeoffDate` >= DATE('%s') AND `takeoffDate` <= DATE('%s');""" % (
                    self.dateAfter.date().toString("yyyy-MM-dd"), self.dateBefore.date().toString("yyyy-MM-dd"))
        self.connectDB(query)
        devicesListQuery = QtSql.QSqlQuery()
        self.devtypeBox.addItem("Все")
        ok = devicesListQuery.exec("SELECT * FROM MBC_PEMOHT.typesOfDevices;")
        if ok:
            while devicesListQuery.next(): self.devtypeBox.addItem(devicesListQuery.value(0))

    def readSettings(self):
        self.config = configparser.ConfigParser(allow_no_value = True)
        self.config.read('./config/dbsettings.ini')
        self.progConfig = configparser.ConfigParser()
        self.progConfig.read('./config/programsettings.ini')
    
    def connectDB(self, initQuery):
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName(self.config['db']['host'])
        self.db.setUserName(self.config['db']['login'])
        self.db.setPassword(self.config['db']['password'])
        self.db.setDatabaseName(self.config['db']['dbname'])
        tabmodel = Model(self, self.db, initQuery)
        orderedTabmodel = QSortFilterProxyModel(self)
        orderedTabmodel.setSourceModel(tabmodel)
        orderedTabmodel.setDynamicSortFilter(True)
        self.tableView.setModel(orderedTabmodel)
#        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
#        self.tableView.customContextMenuRequested[QPoint].connect(self.contextMenuRequested)
        self.tableView.show()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    
    @pyqtSlot()
    def on_addIncidentButton_released(self):
        self.addIncidentDialog = addIncident(self.db)
        self.addIncidentDialog.accepted.connect(self.on_refreshButton_released)
        self.addIncidentDialog.show()
    
    @pyqtSlot()
    def on_refreshButton_released(self):
        if self.devtypeBox.currentText() != "Все": addQuery1 = " AND `type` = '%s'" % self.devtypeBox.currentText()
        else: addQuery1 = ''
        if self.stateBox.currentText() == "все": addQuery2 = ''
        elif self.stateBox.currentText() == "снятые": addQuery2 = " AND `setupDate` IS NULL"
        elif self.stateBox.currentText() == "в цеху": addQuery2 = " AND `toEngeneerDate` IS NOT NULL"
        elif self.stateBox.currentText() == "на складе": addQuery2 = " AND `toStockDate` IS NOT NULL"
        if self.serialNumberEdit.text() != '': addQuery3 = " AND `serialNumber` = '%s'" % self.serialNumberEdit.text()
        else: addQuery3 = ''
        query = "SELECT * FROM operatorView WHERE `takeoffDate` >= DATE('%s') AND `takeoffDate` <= DATE('%s')%s%s%s;" % (
        self.dateAfter.date().toString("yyyy-MM-dd"), self.dateBefore.date().toString("yyyy-MM-dd"), addQuery1, addQuery2, addQuery3)
        print(query)
        self.tableView.model().sourceModel().refresh(query)
    
    @pyqtSlot()
    def on_connectToDbAction_triggered(self):
        self.reconnectDB.emit()
        self.close()

    
    @pyqtSlot()
    def on_exitAction_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
