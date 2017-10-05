from PyQt5 import QtWidgets
from ui.userAuth import userAuth
from ui.mainWindow import MainWindow
import sys

class windowMaker:
    def showWindow(self, user, role):
        if role == "operator":
            self.mainWindow = MainWindow(user)
            self.mainWindow.reconnectDB.connect(self.showAuthWindow)
            self.mainWindow.show()
        elif role == "admin":
            self.msgbox = QtWidgets.QMessageBox()
            self.msgbox.setText('Админку пока не сделал')
            self.msgbox.show()
        elif role == "ingeneer":
            self.msgbox = QtWidgets.QMessageBox()
            self.msgbox.setText('Инженерка пока не сделана')
            self.msgbox.show()
        else:
            self.msgbox = QtWidgets.QMessageBox()
            self.msgbox.setText('Пользователь неверно настроен, обратитесь к администратору')
            self.msgbox.show()
            self.showAuthWindow()

        
    def showAuthWindow(self):
        self.ui = userAuth()
        self.ui.userAuthorized.connect(self.showWindow)
        self.ui.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = windowMaker()
    w.showAuthWindow()
    sys.exit(app.exec_())
    

