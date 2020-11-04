
import nltk
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QTableWidget,QTableWidgetItem
from preprocessing import *
from userend import *
import sys

class Ui_RunWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(140, 640, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 180, 821, 411))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(len(result)//3)
        self.tableWidget.setObjectName("tableWidget")
        
        
        
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(40, 30, 981, 141))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(24)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultLabel.setWordWrap(True)
        self.ResultLabel.setObjectName("ResultLabel")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(570, 640, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                
        
        for i in range(len(result)//3):
            self.tableWidget.setItem(i,0, QTableWidgetItem(result["Aword"+str(i)]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(result["Sense"+str(i)])))
            self.tableWidget.setItem(i,2, QTableWidgetItem(result["Def"+str(i)]))
        
        
        self.return_button.clicked.connect(self.return_click)
        self.exit_button.clicked.connect(self.exit_click)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_button.setText(_translate("MainWindow", "RETURN"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Word"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sense"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Definition"))
        self.ResultLabel.setText(_translate("MainWindow", "Resulting Senses of Ambiguous Words"))
        self.exit_button.setText(_translate("MainWindow", "EXIT"))
        header = self.tableWidget.horizontalHeader()       
       #header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
       
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,100) 
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        
    def return_click(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        
    def exit_click(self):
        sys.exit()

     
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(40, 20, 981, 141))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(24)
        self.titlelabel.setFont(font)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setWordWrap(True)
        self.titlelabel.setObjectName("titlelabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 180, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.user_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.user_ip.setGeometry(QtCore.QRect(400, 170, 581, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.user_ip.setFont(font)
        self.user_ip.setObjectName("user_ip")
        self.preproc_button = QtWidgets.QPushButton(self.centralwidget)
        self.preproc_button.setGeometry(QtCore.QRect(400, 320, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.preproc_button.setFont(font)
        self.preproc_button.setObjectName("preproc_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 410, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.preprocess_op = QtWidgets.QLabel(self.centralwidget)
        self.preprocess_op.setGeometry(QtCore.QRect(400, 390, 581, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.preprocess_op.setFont(font)
        self.preprocess_op.setFrameShape(QtWidgets.QFrame.Box)
        self.preprocess_op.setText("")
        self.preprocess_op.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.preprocess_op.setWordWrap(True)
        self.preprocess_op.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.preprocess_op.setObjectName("preprocess_op")
        self.preprocess_op_2 = QtWidgets.QLabel(self.centralwidget)
        self.preprocess_op_2.setGeometry(QtCore.QRect(400, 540, 581, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.preprocess_op_2.setFont(font)
        self.preprocess_op_2.setFrameShape(QtWidgets.QFrame.Box)
        self.preprocess_op_2.setText("")
        self.preprocess_op_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.preprocess_op_2.setWordWrap(True)
        self.preprocess_op_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.preprocess_op_2.setObjectName("preprocess_op_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 560, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.run_class_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_class_button.setGeometry(QtCore.QRect(400, 700, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.run_class_button.setFont(font)
        self.run_class_button.setObjectName("run_class_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.preproc_button.clicked.connect(self.preproc_click)
        self.run_class_button.clicked.connect(self.run_click)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titlelabel.setText(_translate("MainWindow", "Word Sense Disambiguation using Neural Networks"))
        self.label_2.setText(_translate("MainWindow", "Enter Input Text:"))
        self.preproc_button.setText(_translate("MainWindow", "PREPROCESS"))
        self.label_3.setText(_translate("MainWindow", "Preprocessed Word List:"))
        self.label_4.setText(_translate("MainWindow", "Ambiguous Word List:"))
        self.run_class_button.setText(_translate("MainWindow", "RUN CLASSIFIER ON WORDS"))

    def run_click(self):
        if self.user_ip.toPlainText()=="":
            self.showpopup1()
        elif self.preprocess_op.text()=="":
            self.showpopup2() 
        elif self.preprocess_op_2.text()=="":
            self.showpopup3()         
        else:
            
            global result
            result=run_user_end(wordlist,awords)
            self.ui = Ui_RunWindow()
            self.ui.setupUi(MainWindow)
            MainWindow.show()
            
            #print("\n",wordlist,"\n")
            #print("\n",awords,"\n")
        
    def preproc_click(self):
        if self.user_ip.toPlainText()=="":
            self.showpopup1()
        else:
            
            ipsent=self.user_ip.toPlainText()
            global wordlist
            wordlist=preprocess(ipsent)
            wlist=""
            for i in wordlist:
                wlist=wlist+i+", "
            self.preprocess_op.setText(wlist)
            global awords
            awords=findambiwords(wordlist)
            alist=""
            for i in awords:
                alist=alist+i+", "
            self.preprocess_op_2.setText(alist)
    
    def showpopup1(self):
        msg=QMessageBox()
        msg.setWindowTitle("Invalid Entry")
        msg.setText("Please Give Input Text")
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_()
    
    def showpopup2(self):
        msg=QMessageBox()
        msg.setWindowTitle("Invalid Entry")
        msg.setText("Please Preprocess your statement first")
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_()
        
    def showpopup3(self):
        msg=QMessageBox()
        msg.setWindowTitle("Invalid Entry")
        msg.setText("Sorry no ambiguous words were found in your text")
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_()
        
        
if __name__ == "__main__":
    import sys
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


