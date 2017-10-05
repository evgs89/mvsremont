# -*- coding: utf-8 -*-

"""
Module implementing userAuth.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import configparser
import mysql.connector
from ui.Ui_userAuth import Ui_userAuth


class userAuth(QMainWindow, Ui_userAuth):
    userAuthorized = pyqtSignal(str, str)
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(userAuth, self).__init__(parent)
        self.setupUi(self)
        config = configparser.ConfigParser()
        config.read('./config/dbsettings.ini')
        self.dbHost.setText(config['db']['host'])
        self.dbLogin.setText(config['db']['login'])
        self.dbPassword.setText(config['db']['password'])
        self.dbName.setText(config['db']['dbname'])
        self.userName.setText(config['user']['name'])    
        self.userPassword.setText(config['user']['password'])    
        
    
    @pyqtSlot()
    def on_okButton_released(self):
        """
        Slot documentation goes here.
        """
        config = configparser.ConfigParser()
        config.read('./config/dbsettings.ini')
        config.set('db', 'host', self.dbHost.text())
        config.set('db', 'login', self.dbLogin.text())
        config.set('db', 'password', self.dbPassword.text())
        config.set('db', 'dbname', self.dbName.text())
        config.set('user', 'name', self.userName.text())
        config.set('user', 'password', self.userPassword.text())
        configfile = open('./config/dbsettings.ini', 'w')
        config.write(configfile)
        configfile.close()
        try:
            self.mysqlconn = mysql.connector.connect(host = self.dbHost.text(), database = self.dbName.text(), user = self.dbLogin.text(), password = self.dbPassword.text())
        except:
            self.msgbox = QMessageBox()
            self.msgbox.setText('Невозможно подключиться к серверу')
            self.msgbox.show()
            print(mysql.connector.Error())
        else:
            if self.mysqlconn.is_connected():
                cursor = self.mysqlconn.cursor()
                cursor.execute("SELECT * FROM user WHERE username = '%s'" % self.userName.text())
                row = cursor.fetchone()
                if row[1] == self.userPassword.text():
                    self.userAuthorized.emit(self.userName.text(), row[4])
                    self.close()
                else: 
                    self.msgbox = QMessageBox()
                    self.msgbox.setText('Ошибка аутентификации пользователя')
                    self.msgbox.show()
            
    def closeEvent(self, event):
        self.mysqlconn.close()
        event.accept()
