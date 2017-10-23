from PyQt5 import QtSql, QtCore
#from PyQt5.QtCore import pyqtSlot, Qt, QVariant, QPoint, QDate, QSortFilterProxyModel
#from PyQt5.QtWidgets import QMainWindow, QMenu, QMessageBox, QHeaderView, QFileDialog
#from PyQt5.QtGui import QBrush, QColor, QIcon, QPixmap

class operatorModel(QtSql.QSqlQueryModel):
    def __init__(self, parent, db, initQuery):
        QtSql.QSqlQueryModel.__init__(self)
        self.gui = parent
        self.db = db
        self.columns = {0:'idIncident', 1:'serialNumber',  2:'type', 3:'takeoffDate', 4:'textProblems', 
                                    5:'brigadeEngineer', 6:'desiredFinishDate', 7:'toEngeneerDate', 8:'engineer',  9:'toStockDate', 10:'setupDate'}
        self.columnsRus = {0:"№", 1:'Сер. №', 2:"тип", 3:"Демонтаж:", 4:"Причина демонтажа", 
                                        5:"Бригада", 6:"Нужна на:", 7:"В цеху с:", 8:"Инженер", 9:"Готова с:", 10:'Установлена'}
        self.query = initQuery
        self.refresh(self.query)
    
    def refresh(self, query):
        if not self.db.isOpen():
            try:
                self.db.open()
            except:
                print("Can't connect")
        self.setQuery(query)
        for i in self.columnsRus.keys(): self.setHeaderData(i, QtCore.Qt.Horizontal, self.columnsRus[i])
        self.cached = {}
        self.layoutChanged.emit()
    
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if index in self.cached.keys(): return self.cached[index]
            else: return super(operatorModel, self).data(index, role)
        else: return QtCore.QVariant()
    

    
    
