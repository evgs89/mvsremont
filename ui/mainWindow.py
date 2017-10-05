# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QAbstractTableModel, QDate, Qt, QSortFilterProxyModel, QPoint
from PyQt5.QtWidgets import QMainWindow,QHeaderView#, QMessageBox

from .Ui_mainWindow import Ui_MainWindow
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
        self.dateAfter.setDate(Today.addDays(-214))
        self.currentUser = user
        self.readSettings()
        query = """SELECT * FROM operatorView WHERE
                    `takeoffDate` >= DATE('%s') AND `takeoffDate` <= DATE('%s');""" % (self.dateAfter.date().toString("yyyy-MM-dd"), 
                                                                                                                                self.dateBefore.date().toString("yyyy-MM-dd"))
        self.connectDB(query)
        devicesListQuery = QtSql.QSqlQuery()
        self.devtypeBox.addItem("Все")
        ok = devicesListQuery.exec("SELECT * FROM MBC_PEMOHT.typesOfDevices;")
        if ok:
            while devicesListQuery.next(): self.devtypeBox.addItem(devicesListQuery.value(0))

    def readSettings(self):
        self.config = configparser.ConfigParser(allow_no_value = True)
        self.config.read('./config/dbsettings.ini')
    
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
    
    @pyqtSlot(str)
    def on_stateBox_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSlot()
    def on_addIncidentButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_refreshButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
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
