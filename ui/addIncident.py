# -*- coding: utf-8 -*-

"""
Module implementing addIncident.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QRadioButton, QAbstractButton
from PyQt5 import QtSql

from .Ui_addIncident import Ui_Dialog


class addIncident(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, db, id=None, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(addIncident, self).__init__(parent)
        self.setupUi(self)
        self.dbState = False
        self.db = db
        self.connectDB()
        self.type = ''
        self.serNumber = ''
        if id == None:
            self.getTypesOfDevices()
        self.buttonBox.accepted.disconnect(self.accept)
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted_clicked)
        self.buttonBox.rejected.disconnect(self.reject)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected_clicked)       
        
    
    def connectDB(self):
        try:
            self.db.open()
        except:
            print("Can't connect")
            self.dbState = False
        else:
            self.dbState = True
    
    def getTypesOfDevices(self):
        devicesListQuery = QtSql.QSqlQuery()
        if self.dbState:
            ok = devicesListQuery.exec("SELECT * FROM MBC_PEMOHT.typesOfDevices;")
            if ok:
                prevItem = self.dateCreationEdit
                while devicesListQuery.next(): 
                    but = QRadioButton(devicesListQuery.value(0))
                    but.toggled.connect(self.selectedTypeOfDevice)
                    self.typeDevicesLayout.addWidget(but)
                    self.setTabOrder(prevItem, but)
                    prevItem = but
                self.setTabOrder(prevItem, self.ipEdit)
    
    def selectedTypeOfDevice(self):
        self.type = self.sender().text()
        self.getInfo()
        
    def getInfo(self):
        # if serial is wrote and type is selected, try to fill other fields
        if self.serNum != '' and self.type != '':
            qryInfo = "SELECT * FROM MBC_PEMOHT.allDevices WHERE `serialNumber` = '%s' AND `type` = '%s';" % (self.serNum, self.type)
            print(qryInfo)
            infoQry = QtSql.QSqlQuery()
            ok = infoQry.exec(qryInfo)
            infoQry.first()
            for i in [self.ipEdit, self.netmaskEdit, self.gatewayEdit, self.comEdit]: i.setEnabled(True)
            if ok: ##7.8.9.10
                self.ipEdit.setText(infoQry.value(7))
                self.netmaskEdit.setText(infoQry.value(8))
                self.gatewayEdit.setText(infoQry.value(9))
                try: com = int(infoQry.value(10))
                except: com = 0
                self.comEdit.setValue(com)
            # when selected type, get typical problems and add them as checkable buttons to second tab
            while self.typicalProblemsLayout.count():
                item = self.typicalProblemsLayout.takeAt(0)
                widget = item.widget()
                if widget is not None: widget.deleteLater()
            qryProblems = "SELECT typicalProblem from typicalProblemsByDevices WHERE `typeDevice` = '%s';" % self.type
            problemsQry = QtSql.QSqlQuery()
            ok2 = problemsQry.exec(qryProblems)
            if ok2:
                while problemsQry.next():
                    pass
                    
            
    
    @pyqtSlot()
    def on_ipEdit_editingFinished(self):
        """
        automatically calculate netmask and gateway
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSlot()
    def on_serialNumberEdit_editingFinished(self):
        self.serNum = self.serialNumberEdit.text()
        self.getInfo()
    
    def on_buttonBox_accepted_clicked(self):
        index = self.toolBox.currentIndex()
        if index < 3: 
            self.toolBox.setCurrentIndex(index + 1)
        else: self.accept()
        
    def on_buttonBox_rejected_clicked(self):
        index = self.toolBox.currentIndex()
        if index > 0: 
            self.toolBox.setCurrentIndex(index - 1)
        else: self.reject()
