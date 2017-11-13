from PyQt5 import QtSql, QtCore
#from PyQt5.QtCore import pyqtSlot, Qt, QVariant, QPoint, QDate, QSortFilterProxyModel
#from PyQt5.QtWidgets import QMainWindow, QMenu, QMessageBox, QHeaderView, QFileDialog
#from PyQt5.QtGui import QBrush, QColor, QIcon, QPixmap

class operatorModel(QtSql.QSqlQueryModel):
    def __init__(self, parent, db, initQuery):
        QtSql.QSqlQueryModel.__init__(self)
        self.gui = parent
        self.db = db
        self.columns = {0:'idIncident', 1:'serialNumber',  2:'type', 3:'location', 4:'takeoffDate', 5:'textProblems', 
                                    6:'brigadeEngineer', 7:'desiredFinishDate', 8:'toEngeneerDate', 9:'engineer',  10:'toStockDate', 11:'setupDate'}
        self.columnsRus = {0:"№", 1:'Сер. №', 2:"тип", 3:"Место", 4:"Демонтаж:", 5:"Причина демонтажа", 
                                        6:"Бригада", 7:"Нужна на:", 8:"В цеху с:", 9:"Инженер", 10:"Готова с:", 11:'Установлена'}
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
    

    
    
