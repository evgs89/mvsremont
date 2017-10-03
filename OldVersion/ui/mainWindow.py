# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QAbstractTableModel, QDate, QVariant, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.Ui_mainWindow import Ui_MainWindow
import mysql.connector, configparser
from datetime import datetime, date, timedelta

class operatorViewModel(QAbstractTableModel):
    def __init__(self, parent):
        QAbstractTableModel.__init__(self)
        self.gui = parent
        self.__delta = timedelta(days = 14)
        self.type = 'Все'
        self.state = 'Все'
        self.colLabels = ['ID', 'Сер. №', 'Тип', 'Снято', 'План. установка', 'Причина', 'В цеху', 'Работы', 'На складе']
        self.filterDateChange()
        self.refreshTimeoutChange()
        self.updated = self.refreshData()
    def filterDateChange(self, dateBefore = date.today(), dateAfter = date.today()):
        self.dateBefore = dateBefore
        if dateAfter != dateBefore: self.dateAfter = dateAfter
        else: self.dateAfter = dateAfter - self.__delta
    def refreshTimeoutChange(self, timeout = 5):
        self.refreshDataTimeout = timeout
        self.__refreshDataTimeoutDelta = timedelta(minutes = timeout)
    def checkLastUpdate(self):
        updated = False
        try:
            config = configparser.ConfigParser()
            config.read('./config/dbsettings.ini')
            mysqlconn = mysql.connector.connect(host = config['db']['host'], database = config['db']['dbname'], user = config['db']['login'], password = config['db']['password'])
            if mysqlconn.is_connected():
                cursor = mysqlconn.cursor()
                command = "SELECT * FROM updates WHERE view = 'operatorView'"
                cursor.execute(command)
                row = cursor.fetchone()
                if row[3] != config['user']['name']: 
        except: 
            pass
    def refreshData(self):
        try:
            config = configparser.ConfigParser()
            config.read('./config/dbsettings.ini')
            mysqlconn = mysql.connector.connect(host = config['db']['host'], database = config['db']['dbname'], user = config['db']['login'], password = config['db']['password'])
            if mysqlconn.is_connected():
                cursor = mysqlconn.cursor()
                command = "SELECT * FROM operatorView WHERE takeoffDate > '%s' AND takeoffDate <= '%s'" % str(self.dateBefore), str(self.dateAfter)
                if self.type != 'Все': command += ' AND type = ' + self.type
                if self.state != 'Все':
                    if self.state == 'Снятые': command += ' AND toEngineerDate == NULL'
                    if self.state == 'В работе': command += ' AND toStockDate == NULL'
                    if self.state == 'Готовые': command += ' AND toStockDate != NULL'
                cursor.execute(command)
                k = 0
                aa = True
                self.order = {}
                while aa:
                    row = cursor.fetchone()
                    if not row: 
                        aa = False
                        break
                    self.dataCached[row[0]] = row
                    self.order[k] = row[0]
                    k += 1
                return datetime.now()
            mysqlconn.close()
        except:
            self.msgbox = QMessageBox()
            self.msgbox.setText('Невозможно подключиться к серверу')
            self.msgbox.show()
            self.on_connectToDB_triggered()
            print(mysql.connector.Error())
    def data(self, index, role):
        if self.__refreshDataTimeoutDelta != 0:
            currentDelta = datetime.now() - self.updated
            if currentDelta > self.__refreshDataTimeoutDelta: 
                self.updated = self.refreshData()
        if not index.isValid(): return QVariant()
        elif role != Qt.DisplayRole: return QVariant()# and role != Qt.EditRole and role != Qt.BaclgroundRole: return QVariant()
        value = ''
        row = index.row()
        column = index.column()
        if role == Qt.DisplayRole:
            value = str(self.dataCached[self.order[row]][column]) ##Потом расписать отдельно форматирование по колонкам
            return QVariant(value)
    def rowCount(self, parent):
        return len(self.dataCached)
    def columnCount(self, parent):
        if len(self.dataCached[0]) > 0:
            return len(self.dataCached[0])
        else: return 0
    def headerSettings(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole: return QVariant(self.colLabels[section])
        return QVariant()
        
class MainWindow(QMainWindow, Ui_MainWindow):
    reconnectDB = pyqtSignal()
    def __init__(self, user, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.user = user
        config = configparser.ConfigParser()
        config.read('./config/dbsettings.ini')
        try:
            mysqlconn = mysql.connector.connect(host = config['db']['host'], database = config['db']['dbname'], user = config['db']['login'], password = config['db']['password'])
            if mysqlconn.is_connected():
                cursor = mysqlconn.cursor()
                cursor.execute("SELECT * FROM userRights WHERE user = '%s'" % self.user)
                row = cursor.fetchone()
                for i in range(2, 7):
                    self.tabWidget.setTabEnabled(i-2, row[i])
            mysqlconn.close()
        except:
            self.msgbox = QMessageBox()
            self.msgbox.setText('Невозможно подключиться к серверу')
            self.msgbox.show()
            self.on_connectToDB_triggered()
            print(mysql.connector.Error())
        
    def showOperatorTab(self):
        Today = QDate.currentDate()
        self.operatorDateBefore.setDate(Today)
        self.operatorDateAfter.setDate(Today.addDays(-14))
        
    
    
    
    @pyqtSlot()
    def on_connectToDB_triggered(self):
        self.reconnectDB.emit()
        self.close()
