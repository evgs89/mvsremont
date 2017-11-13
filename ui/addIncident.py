# -*- coding: utf-8 -*-

"""
Module implementing addIncident.
"""

from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtWidgets import QDialog, QRadioButton, QPushButton
from PyQt5 import QtSql
import netaddr

from .Ui_addIncident import Ui_Dialog


class addIncident(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, db, user, id=None, parent=None):
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
        self.operator = user
        self.id = id
        self.dateCreationEdit.setDate(QDate.currentDate())
        self.getTypesOfDevices()
        if id == None: pass
        else:
            # first get ID of device from incidents
            incidentQryTxt = "SELECT * FROM incidents WHERE idIncident = %d;" % self.id
            incidentQry = QtSql.QSqlQuery()
            ok = incidentQry.exec(incidentQryTxt)
            if ok:
                # get serial number and type of device in this incident
                incidentQry.first()
                getBasicInfoQryTxt = "SELECT serialNumber, type FROM allDevices WHERE id = %d" % incidentQry.value(1)
                getBasicInfoQry = QtSql.QSqlQuery()
                ok = getBasicInfoQry.exec(getBasicInfoQryTxt)
            if ok:    
                getBasicInfoQry.first()
                self.type = getBasicInfoQry.value(1)
                self.serNum = getBasicInfoQry.value(0)
                self.serialNumberEdit.setText(self.serNum)
                # fill other fields
                self.getInfo()
                self.dateCreationEdit.setDate(incidentQry.value(5))
                self.desiredFinishDateCalendar.setSelectedDate(incidentQry.value(8))
                for i in range(0, self.typeDevicesLayout.count()):
                    if self.typeDevicesLayout.itemAt(i).widget().text() == self.type: self.typeDevicesLayout.itemAt(i).widget().setChecked(True)
                for i in range(0, self.brigadeLayout.count()):
                    if self.brigadeLayout.itemAt(i).widget().text() == incidentQry.value(3): self.brigadeLayout.itemAt(i).widget().setChecked(True)
                # set problems, described in incident
                problems = []
                otherProblems = ""
                getProblemsTxt = "SELECT typicalProblem FROM problems WHERE incident = %d;" % self.id
                getProblemsQry = QtSql.QSqlQuery()
                ok = getProblemsQry.exec(getProblemsTxt)
                if ok: 
                    while getProblemsQry.next(): problems.append(getProblemsQry.value(0))
                    getProblemsTxt = "SELECT otherProblem FROM problems WHERE incident = %d;" % self.id
                    ok = getProblemsQry.exec(getProblemsTxt)
                    while getProblemsQry.next():
                        if getProblemsQry.value(0) != "": otherProblems = getProblemsQry.value(0)
                    for i in range(0, self.typicalProblemsLayout.count()):
                        if self.typicalProblemsLayout.itemAt(i).widget().text() in problems:
                            self.typicalProblemsLayout.itemAt(i).widget().setChecked(True)
                    if otherProblems != "":
                        self.moreButton.setChecked(True)
                        self.commentEnabledToggle(True)
                        self.commentEdit.setPlainText(otherProblems)
        self.buttonBox.accepted.disconnect(self.accept)
        self.buttonBox.accepted.connect(self.on_buttonBox_accepted_clicked)
        self.buttonBox.rejected.disconnect(self.reject)
        self.buttonBox.rejected.connect(self.on_buttonBox_rejected_clicked)
        
        
    
    def connectDB(self):
        try:
            self.db.open()
        except:
            self.dbState = False
        else:
            self.dbState = True
    
    def getTypesOfDevices(self):
        #dynamically fill types of devices, brigades and locations lists
        devicesListQuery = QtSql.QSqlQuery()
        if self.dbState:
            ok = devicesListQuery.exec("SELECT * FROM typesOfDevices;")
            if ok:
                prevItem = self.dateCreationEdit
                while devicesListQuery.next(): 
                    but = QRadioButton(devicesListQuery.value(0))
                    but.toggled.connect(self.selectedTypeOfDevice)
                    self.typeDevicesLayout.addWidget(but)
                    self.setTabOrder(prevItem, but)
                    prevItem = but
                self.setTabOrder(prevItem, self.ipEdit)
            locationsQryTxt = "SELECT * FROM locations"
            locationsQry = QtSql.QSqlQuery()
            ok2 = locationsQry.exec(locationsQryTxt)
            if ok2:
                while locationsQry.next():
                    self.locationComboBox.addItem(locationsQry.value(0))
            brigadeQryTxt = "SELECT * FROM brigadeEngineer;"
            brigadeQry = QtSql.QSqlQuery()
            ok3 = brigadeQry.exec(brigadeQryTxt)
            if ok3:
                prevItem = self.commentEdit
                while self.brigadeLayout.count():
                    item = self.brigadeLayout.takeAt(0)
                    widget = item.widget()
                    if widget is not None: widget.deleteLater()
                while brigadeQry.next(): 
                    but = QRadioButton(brigadeQry.value(0))
                    self.brigadeLayout.addWidget(but)
                    but.toggled.connect(self.selectedBrigade)
                    self.setTabOrder(prevItem, but)
                    prevItem = but
                self.setTabOrder(prevItem, self.desiredFinishDateCalendar)
    
    def selectedTypeOfDevice(self):
        self.type = self.sender().text()
        self.getInfo()
        
    def selectedBrigade(self):
        self.brigade = self.sender().text()
        
    def getInfo(self, id = None):
        # if serial is wrote and type is selected, try to fill other fields
        if self.serNum != '' and self.type != '':
            qryInfo = "SELECT * FROM allDevices WHERE `serialNumber` = '%s' AND `type` = '%s';" % (self.serNum, self.type)
            infoQry = QtSql.QSqlQuery()
            ok = infoQry.exec(qryInfo)
            infoQry.first()
            for i in [self.ipEdit, self.netmaskEdit, self.gatewayEdit, self.comEdit]: i.setEnabled(True)
            if ok: 
                self.ipEdit.setText(infoQry.value(7))
                self.netmaskEdit.setText(infoQry.value(9))
                self.gatewayEdit.setText(infoQry.value(8))
                try: com = int(infoQry.value(10))
                except: com = 0
                self.comEdit.setValue(com)
                if infoQry.value(11) != '': self.locationComboBox.setCurrentIndex(self.locationComboBox.findText(infoQry.value(11)))
            # when selected type, get typical problems and add them as checkable buttons to second tab
#            moreButton = QPushButton('Дополнительно')
#            moreButton.setCheckable(True)
            self.moreButton.toggled.connect(self.commentEnabledToggle)
            while self.typicalProblemsLayout.count():
                item = self.typicalProblemsLayout.takeAt(0)
                widget = item.widget()
                if widget is not None: widget.deleteLater()
            qryProblems = "SELECT typicalProblem from typicalProblemsByDevices WHERE `typeDevice` = '%s';" % self.type
            problemsQry = QtSql.QSqlQuery()
            ok2 = problemsQry.exec(qryProblems)
            if ok2:
                prevItem = self.locationComboBox
                while problemsQry.next():
                    button = QPushButton()
                    button.setText(problemsQry.value(0))
                    button.setCheckable(True)
                    self.typicalProblemsLayout.addWidget(button)
                    self.setTabOrder(button, prevItem)
#                self.typicalProblemsLayout.addWidget(moreButton)
                self.setTabOrder(prevItem, self.moreButton)
            
    
    @pyqtSlot()
    def on_ipEdit_editingFinished(self):
        # if there is no info in database, try to calculate netmask and gateway by ip
        try: ip = netaddr.IPNetwork(self.ipEdit.text())
        except: pass #if ip is not valid, do nothing
        else:
            if ip.ip.words[0] == 192: ip.prefixlen = 24
            elif ip.ip.words[0] == 10: ip.prefixlen = 27
            self.netmaskEdit.setText(str(ip.netmask))
            if ip.prefixlen == 24: gateway = '%s.%s.%s.1' % (str(ip.ip.words[0]), str(ip.ip.words[1]), str(ip.ip.words[2]))
            elif ip.prefixlen == 27: gateway = str(ip.broadcast - 1)
            self.gatewayEdit.setText(gateway)
            
    
    @pyqtSlot()
    def on_serialNumberEdit_editingFinished(self):
        self.serNum = self.serialNumberEdit.text()
        self.getInfo()
    
    def on_buttonBox_accepted_clicked(self):
        index = self.toolBox.currentIndex()
        if index < 2: 
            self.toolBox.setCurrentIndex(index + 1)
        else: 
            self.editingFinished()
    
    def editingFinished(self):
        # first try to update info about device
        if self.serNum != '' and self.type != '':
            qryInfo = "SELECT * FROM allDevices WHERE `serialNumber` = '%s' AND `type` = '%s';" % (self.serNum, self.type)
            infoQry = QtSql.QSqlQuery()
            updateQry = QtSql.QSqlQuery()
            ok = infoQry.exec(qryInfo)
            #if there is no such device, add it
            if not infoQry.first():
                qryAddDevice = "INSERT INTO allDevices(serialNumber,type) VALUES (%s,'%s');" % (self.serNum, self.type)
                ok = updateQry.exec(qryAddDevice)
                ok = infoQry.exec(qryInfo)
                ok = infoQry.first()
            if ok:
                if infoQry.value(7) != self.ipEdit.text():
                    qryIP = "UPDATE allDevices SET ipAddress = '%s' WHERE `serialNumber` = '%s' AND `type` = '%s';" % (
                                self.ipEdit.text(), self.serNum, self.type)
                    ok = updateQry.exec(qryIP)
                if infoQry.value(8) != self.gatewayEdit.text():
                    qryIP = "UPDATE allDevices SET ipGateway = '%s' WHERE `serialNumber` = '%s' AND `type` = '%s';" % (
                                self.gatewayEdit.text(), self.serNum, self.type)
                    ok = updateQry.exec(qryIP)
                if infoQry.value(9) != self.netmaskEdit.text():
                    qryIP = "UPDATE allDevices SET ipNetmask = '%s' WHERE `serialNumber` = '%s' AND `type` = '%s';" % (
                                self.netmaskEdit.text(), self.serNum, self.type)
                    ok = updateQry.exec(qryIP)
                try: comSet = int(infoQry.value(10))
                except: comSet = 0
                if comSet != self.comEdit.value():
                        qryIP = "UPDATE allDevices SET COM = '%s' WHERE `serialNumber` = '%s' AND `type` = '%s';" % (
                                    str(self.comEdit.value()), self.serNum, self.type)
                        ok = updateQry.exec(qryIP)
                if infoQry.value(11) != self.locationComboBox.currentText():
                    qryLoc = "UPDATE allDevices SET location = '%s' WHERE `serialNumber` = '%s' AND `type` = '%s';" % (
                                    self.locationComboBox.currentText(), self.serNum, self.type)
                    ok = updateQry.exec(qryLoc)
            # adding info to incidents
            # get id of device
            idGet = "SELECT id FROM allDevices WHERE `serialNumber` = '%s' AND `type` = '%s';" % (self.serNum, self.type)
            idQry = QtSql.QSqlQuery()
            ok = idQry.exec(idGet)
            idQry.first()
            # TODO: disable adding similar incidents (for same id and date), instead of it edit existing incident
            # insert basic info about incident
            # if it's new incident
            if ok and self.id == None:
                id = idQry.value(0)
                values = [str(id), self.operator, self.brigade, self.dateCreationEdit.date().toString("yyyy-MM-dd"), self.desiredFinishDateCalendar.selectedDate().toString("yyyy-MM-dd")]
                addIncidentQryTxt = "INSERT INTO incidents(idDevice,operator,brigadeEngineer,takeoffDate,desiredFinishDate) VALUES(%s,'%s','%s','%s','%s');" % (str(id), self.operator, self.brigade, 
                                                                                                                                                                                                                                                                        self.dateCreationEdit.date().toString("yyyy-MM-dd"), 
                                                                                                                                                                                                                                                                        self.desiredFinishDateCalendar.selectedDate().toString("yyyy-MM-dd"))
                addIncidentQry = QtSql.QSqlQuery()
                ok = addIncidentQry.exec(addIncidentQryTxt)
                if ok:
                    idIncident = QtSql.QSqlQuery()
                    ok = idIncident.exec("SELECT LAST_INSERT_ID();")
                    idIncident.first()
                    self.id = idIncident.value(0)
            #or if incident already exists
            elif ok:
                id = idQry.value(0)
                values = [str(id), self.brigade, self.dateCreationEdit.date().toString("yyyy-MM-dd"), self.desiredFinishDateCalendar.selectedDate().toString("yyyy-MM-dd"), self.id]
                updateQryTxt = "UPDATE incidents SET `idDevice`='{}', `brigadeEngineer`='{}', `takeoffDate`='{}', `desiredFinishDate`='{}' WHERE `idIncident`='{}';".format(values[0], values[1], values[2], values[3], values[4])
                ok = updateQry.exec(updateQryTxt)
            #get problems if exists in db
            getProblemsQryTxt = "SELECT typicalProblem FROM problems WHERE incident=%d;" % self.id
            ok = idQry.exec(getProblemsQryTxt)
            #get selected problems
            problems = []
            problemsToRemove = []
            textProblems = ""
            if ok:
                while self.typicalProblemsLayout.count():
                        item = self.typicalProblemsLayout.takeAt(0)
                        widget = item.widget()
                        if widget is not None: 
                            if widget.isChecked(): 
                                problems.append(widget.text())
                                textProblems += "%s, " % widget.text()
                addProblemQry = QtSql.QSqlQuery()
                #write problems to base
                #first check if some removed
                while idQry.next():
                    if idQry.value(0) not in problems: problemsToRemove.append(idQry.value(0))
                    #if already in db, excluding from list to add
                    else: problems.remove(idQry.value(0))
                for i in problemsToRemove:
                    removeProblemQryTxt = "DELETE FROM problems WHERE id=%d AND typicalProblem='%s';" % (self.id, i)
                    ok = addProblemQry.exec(removeProblemQryTxt)
                for i in problems:
                    addProblemQryTxt = "INSERT INTO problems(typicalProblem,incident) VALUES('%s',%d);" % (i, self.id)
                    ok = addProblemQry.exec(addProblemQryTxt)
                if self.moreButton.isChecked():
                    addOtherProblemQryTxt = "INSERT INTO problems(incident,otherProblem) VALUES(%d,'%s');" % (self.id, self.moreButton.text())
                    ok = addProblemQry.exec(addOtherProblemQryTxt)
                if textProblems != "": ok = addProblemQry.exec("UPDATE incidents SET textProblems='%s' WHERE idIncident='%s';" % (textProblems, self.id))
            self.accept()
        
    def on_buttonBox_rejected_clicked(self):
        index = self.toolBox.currentIndex()
        if index > 0: 
            self.toolBox.setCurrentIndex(index - 1)
        else: self.reject()
    
    def commentEnabledToggle(self, state):
        self.commentEdit.setEnabled(state)
        self.commentEdit.setReadOnly(not state)
