from PyQt5 import QtWidgets
from ui.userAuth import userAuth
from ui.mainWindow import MainWindow
import sys

class windowMaker:
    def showMainWindow(self, user):
        self.mainWindow = MainWindow(user)
        self.mainWindow.reconnectDB.connect(self.showAuthWindow)
        self.mainWindow.show()

        
    def showAuthWindow(self):
        self.ui = userAuth()
        self.ui.userAuthorized.connect(self.showMainWindow)
        self.ui.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = windowMaker()
    w.showAuthWindow()
    sys.exit(app.exec_())
    

