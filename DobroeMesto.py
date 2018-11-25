from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from PyQt5.QtCore import QTimer, QTime

d = datetime.datetime.today() #время получается один раз при запуске программы, требует обновления перед записью

con = sqlite3.connect('data.db')

menu_items = []
order_items = []

order_number = 0 #подгружать из базы

money = ""

isopen = False #подгружать из базы


class MainWindow(object):

    def setupUi(self):
        Main.setObjectName("Main")
        Main.showFullScreen()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.managementgroup = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.managementgroup.setFont(font)
        self.managementgroup.setObjectName("managementgroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.managementgroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.opencashboxbuttton = QtWidgets.QPushButton(self.managementgroup)
        self.opencashboxbuttton.setObjectName("opencashboxbuttton")
        self.gridLayout_3.addWidget(self.opencashboxbuttton, 0, 0, 1, 1)
        self.closebutton = QtWidgets.QPushButton(self.managementgroup)
        self.closebutton.setObjectName("closebutton")
        self.gridLayout_3.addWidget(self.closebutton, 2, 0, 1, 1)
        self.printXbutton = QtWidgets.QPushButton(self.managementgroup)
        self.printXbutton.setObjectName("printXbutton")
        self.gridLayout_3.addWidget(self.printXbutton, 1, 0, 1, 1)
        self.exitbutton = QtWidgets.QPushButton(self.managementgroup)
        self.exitbutton.setObjectName("exitbutton")
        self.gridLayout_3.addWidget(self.exitbutton, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.managementgroup, 3, 3, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.reservebutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reservebutton.sizePolicy().hasHeightForWidth())
        self.reservebutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reservebutton.setFont(font)
        self.reservebutton.setObjectName("reservebutton")
        self.gridLayout.addWidget(self.reservebutton, 1, 2, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infolabel = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.infolabel.setFont(font)
        self.infolabel.setObjectName("infolabel")
        self.horizontalLayout.addWidget(self.infolabel)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 4)
        self.orderbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderbutton.sizePolicy().hasHeightForWidth())
        self.orderbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.orderbutton.setFont(font)
        self.orderbutton.setObjectName("orderbutton")
        self.gridLayout.addWidget(self.orderbutton, 1, 0, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 2, 1)
        self.cashbox = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cashbox.sizePolicy().hasHeightForWidth())
        self.cashbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cashbox.setFont(font)
        self.cashbox.setObjectName("cashbox")
        self.gridLayout.addWidget(self.cashbox, 1, 3, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 3, 0, 2, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.managementgroup.setTitle(_translate("Main", "Управление"))
        self.opencashboxbuttton.setText(_translate("Main", "Открыть кассу"))
        self.closebutton.setText(_translate("Main", "Закрыть смену"))
        self.printXbutton.setText(_translate("Main", "Печать X отчета"))
        self.exitbutton.setText(_translate("Main", "Выход в Windows"))
        self.reservebutton.setText(_translate("Main", "Бронирование"))
        self.groupBox_2.setTitle(_translate("Main", "Информация"))
        self.infolabel.setText(_translate("Main", "Время + дата"))
        self.orderbutton.setText(_translate("Main", "Заказ"))
        self.pushButton.setText(_translate("Main", "Просмотр"))
        self.cashbox.setText(_translate("Main", "Касса"))
        self.groupBox.setTitle(_translate("Main", "Администрирование"))

        self.orderbutton.clicked.connect(self.setupOrderUi)
        self.closebutton.clicked.connect(self.setupLoginUi)
        self.cashbox.clicked.connect(self.setupCashboxUi)
        self.exitbutton.clicked.connect(self.exittowindows)

    def exittowindows(self):
        if isopen:
            print(1)
        else:
            import sys
            sys.exit()
		
    def onCountChanged(self, value):
        self.infolabel.setText(value)

    def setupLoginUi(self):
        Main.setObjectName("Main")
        Main.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 230, 601, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passwordedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordedit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.passwordedit)
        self.loginbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.loginbutton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.loginbutton)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateLoginUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateLoginUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.loginbutton.setText(_translate("Main", "Вход"))

    def setupOrderUi(self):
        Main.showFullScreen()
        Main.setObjectName("Main")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 351, 337))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 351, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.categorieslayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.categorieslayout.setContentsMargins(0, 0, 0, 0)
        self.categorieslayout.setObjectName("verticalLayout_2")
        self.backbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.backbutton.setObjectName("backbutton")
        self.categorieslayout.addWidget(self.backbutton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 351, 337))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 351, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.cancelbutton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbutton.setObjectName("cancelbutton")
        self.verticalLayout.addWidget(self.cancelbutton)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateOrderUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateOrderUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backbutton.setText(_translate("MainWindow", "Назад"))
        self.savebutton.setText(_translate("MainWindow", "Сохранить"))
        self.cancelbutton.setText(_translate("MainWindow", "Отмена"))
        self.cancelbutton.clicked.connect(self.setupUi)

        def create():

            draw_main()

        def draw_main():
            self.backbutton.setEnabled(False)
            with con:
                cur = con.cursor()
                cur.execute("SELECT name FROM range")
                rows = cur.fetchall()

                for row in rows:
                    item_button = QtWidgets.QPushButton(str(row)[2:-3])
                    self.categorieslayout.addWidget(item_button)
                    item_button.clicked.connect(lambda state, button=item_button: select_sub(button))
                    menu_items.append(item_button)

        def select_sub(button):

            for item in menu_items:
                try:
                    item.deleteLater()
                except BaseException:
                    print(1)
            menu_items.clear()

            button = str(button.text())
            self.backbutton.setEnabled(True)
            self.backbutton.clicked.connect(select_back_item)
            with con:
                cur = con.cursor()
                cur.execute("SELECT  FROM  WHERE  " + button)
                rows = cur.fetchall()

            for row in rows:
                    print(row)
                    item_button = QtWidgets.QPushButton(str(row)[2:-3])
                    self.itemslayout.addWidget(item_button)
                    item_button.clicked.connect(lambda state, button=item_button: select_item(button))
                    menu_items.append(item_button)

        def select_item(button):
            global order_number
            #with con:
             #   cur = con.cursor()
              #  cur.execute("SELECT * FROM под пункт WHERE имя категории=?", (str(button.text()),))
               # rows = cur.fetchall()
            cur = con.cursor()
            cur.execute("insert into orders (order_num, item, cost, act_time) values (?, ?, ?, ?)",
                        (order_number, str(button.text()), 100, str(d.hour()+":"+d.minute())))
            draw_order()

        def redraw():
            for item in menu_items:
                try:
                    item.deleteLater()
                except BaseException:
                    print(1)
            menu_items.clear()

        def draw_order():
            global order_number

            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM orders WHERE order_num=?", (order_number,))
                rows = cur.fetchall()

            for item in order_items:
                try:
                    item.deleteLater()
                except BaseException:
                    print(1)
            order_items.clear()

            for row in rows:
                    print(row)
                    item_label = QtWidgets.QLabel(str(row)[2:-1])
                    self.orderlayout.addWidget(item_label)
                    order_items.append(item_label)

        def select_back_item():
            for item in menu_items:
                item.deleteLater()
            menu_items.clear()
            draw_main()

        def save_order():
            order_number += 1


        create()

    def setupCashboxUi(self):
        Main.setObjectName("Main")
        Main.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 10, 961, 721))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button9 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        self.button9.setObjectName("button9")
        self.gridLayout_2.addWidget(self.button9, 2, 2, 1, 1)
        self.button8 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        self.button8.setObjectName("button8")
        self.gridLayout_2.addWidget(self.button8, 2, 1, 1, 1)
        self.button7 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setObjectName("button7")
        self.gridLayout_2.addWidget(self.button7, 2, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setObjectName("button2")
        self.gridLayout_2.addWidget(self.button2, 0, 1, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        self.button5.setObjectName("button5")
        self.gridLayout_2.addWidget(self.button5, 1, 1, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setObjectName("button1")
        self.gridLayout_2.addWidget(self.button1, 0, 0, 1, 1)
        self.button3 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setObjectName("button3")
        self.gridLayout_2.addWidget(self.button3, 0, 2, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setObjectName("button4")
        self.gridLayout_2.addWidget(self.button4, 1, 0, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setObjectName("button6")
        self.gridLayout_2.addWidget(self.button6, 1, 2, 1, 1)
        self.buttonC = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonC.sizePolicy().hasHeightForWidth())
        self.buttonC.setSizePolicy(sizePolicy)
        self.buttonC.setObjectName("buttonC")
        self.gridLayout_2.addWidget(self.buttonC, 3, 0, 1, 1)
        self.button0 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy)
        self.button0.setObjectName("button0")
        self.gridLayout_2.addWidget(self.button0, 3, 1, 1, 1)
        self.buttonCA = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCA.sizePolicy().hasHeightForWidth())
        self.buttonCA.setSizePolicy(sizePolicy)
        self.buttonCA.setObjectName("buttonCA")
        self.gridLayout_2.addWidget(self.buttonCA, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.summlabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summlabel.sizePolicy().hasHeightForWidth())
        self.summlabel.setSizePolicy(sizePolicy)
        self.summlabel.setObjectName("summlabel")
        self.gridLayout_3.addWidget(self.summlabel, 1, 0, 1, 3)
        self.noncashbutton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noncashbutton.sizePolicy().hasHeightForWidth())
        self.noncashbutton.setSizePolicy(sizePolicy)
        self.noncashbutton.setObjectName("noncashbutton")
        self.gridLayout_3.addWidget(self.noncashbutton, 0, 2, 1, 1)
        self.cashbutton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cashbutton.sizePolicy().hasHeightForWidth())
        self.cashbutton.setSizePolicy(sizePolicy)
        self.cashbutton.setObjectName("cashbutton")
        self.gridLayout_3.addWidget(self.cashbutton, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.orderarea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.orderarea.setWidgetResizable(True)
        self.orderarea.setObjectName("orderarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 475, 325))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 471, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.backbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.backbutton.setObjectName("backbutton")
        self.verticalLayout_2.addWidget(self.backbutton)
        self.orderarea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.orderarea, 1, 0, 1, 1)
        self.modbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.modbutton.setObjectName("modbutton")
        self.gridLayout.addWidget(self.modbutton, 2, 0, 1, 1)
        self.itemsarea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.itemsarea.setWidgetResizable(True)
        self.itemsarea.setObjectName("itemsarea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 475, 326))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 481, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.itemsarea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.itemsarea, 0, 0, 1, 1)
        self.cancelbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cancelbutton.setObjectName("cancelbutton")
        self.gridLayout.addWidget(self.cancelbutton, 3, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateCashboxUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateCashboxUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.groupBox.setTitle(_translate("Main", "Ввод"))
        self.button9.setText(_translate("Main", "9"))
        self.button8.setText(_translate("Main", "8"))
        self.button7.setText(_translate("Main", "7"))
        self.button2.setText(_translate("Main", "2"))
        self.button5.setText(_translate("Main", "5"))
        self.button1.setText(_translate("Main", "1"))
        self.button3.setText(_translate("Main", "3"))
        self.button4.setText(_translate("Main", "4"))
        self.button6.setText(_translate("Main", "6"))
        self.buttonC.setText(_translate("Main", "C"))
        self.button0.setText(_translate("Main", "0"))
        self.buttonCA.setText(_translate("Main", "CA"))
        self.groupBox_2.setTitle(_translate("Main", "Оплата"))
        self.summlabel.setText(_translate("Main", "Сумма к оплате"))
        self.noncashbutton.setText(_translate("Main", "Банковская карта"))
        self.cashbutton.setText(_translate("Main", "Наличные"))
        self.backbutton.setText(_translate("Main", "Назад"))
        self.modbutton.setText(_translate("Main", "Особые модификаторы"))
        self.cancelbutton.setText(_translate("Main", "Отмена"))

        def adder(number):
            global money
            money += number
            updateui()

        def clean():
            global money
            money = ""
            updateui()

        def delete():
            global money
            money = money[:-1]
            updateui()

        def updateui():
            self.summlabel.setText("Сумма к оплате " + "\nВнесено " + money)

        self.button0.clicked.connect(lambda state, number="0": adder(number))
        self.button1.clicked.connect(lambda state, number="1": adder(number))
        self.button2.clicked.connect(lambda state, number="2": adder(number))
        self.button3.clicked.connect(lambda state, number="3": adder(number))
        self.button4.clicked.connect(lambda state, number="4": adder(number))
        self.button5.clicked.connect(lambda state, number="5": adder(number))
        self.button6.clicked.connect(lambda state, number="6": adder(number))
        self.button7.clicked.connect(lambda state, number="7": adder(number))
        self.button8.clicked.connect(lambda state, number="8": adder(number))
        self.button9.clicked.connect(lambda state, number="9": adder(number))
        self.buttonCA.clicked.connect(clean)
        self.buttonC.clicked.connect(delete)
        self.cancelbutton.clicked.connect(self.setupUi)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi()
    Main.show()

    def showTime():
        d = datetime.datetime.today()
        months = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        day = d.weekday()
        month = d.month
        if d.minute < 10:
            time = str(str(d.day) + " " + months[month - 1] + " " + weekdays[day] + " " + str(d.hour) + ":0" + str(d.minute))
        else:
            time = str(str(d.day) + " " + months[month - 1] + " " + weekdays[day] + " " + str(d.hour)+":"+str(d.minute))
        try:
            ui.infolabel.setText(time)
        except BaseException:
        		return 0
				
    timer = QTimer()
    timer.timeout.connect(showTime)
    timer.start(1000)

    sys.exit(app.exec_())

