# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QAbstractTableModel, QDate, QVariant, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from .Ui_mainWindow import Ui_MainWindow

import mysql.connector, configparser
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
        self.dateAfter.setDate(Today.addDays(-14))
    
    @pyqtSlot(QDate)
    def on_dateAfter_userDateChanged(self, date):
        """
        Slot documentation goes here.
        
        @param date DESCRIPTION
        @type QDate
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSlot(QDate)
    def on_dateBefore_userDateChanged(self, date):
        """
        Slot documentation goes here.
        
        @param date DESCRIPTION
        @type QDate
        """
        # TODO: not implemented yet
        pass
    
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
