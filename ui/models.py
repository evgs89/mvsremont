from PyQt5 import QtSql
#from PyQt5.QtCore import pyqtSlot, Qt, QVariant, QPoint, QDate, QSortFilterProxyModel
#from PyQt5.QtWidgets import QMainWindow, QMenu, QMessageBox, QHeaderView, QFileDialog
#from PyQt5.QtGui import QBrush, QColor, QIcon, QPixmap

class operatorModel(QtSql.QSqlQueryModel):
    def __init__(self, parent, db):
        QtSql.QSqlQueryModel.__init__(self)
        self.gui = parent
        self.db = db
        self.columns = {0:'idIncident', 1:'serialNumber',  2:'type', 3:'takeoffDate', 4:'textProblems', 
                                    5:'brigadeEngineer', 6:'desiredFinishDate', 7:'toEngeneerDate', 8:'toStockDate'}
        self.columnsRus = {0:"№", 1:'Сер. №', 2:"тип", 3:"Демонтаж:", 4:"Причина демонтажа", 
                                        5:"Бригада", 6:"Нужна на:", 7:"В цеху с:", 8:"Готова с:"}
    
    def data(self, index, role):
        pass
    
    def setData(self, index, value, role):
        pass
    
    
