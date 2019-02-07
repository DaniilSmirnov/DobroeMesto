import datetime

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

d = datetime.datetime.today()  # время получается один раз при запуске программы, требует обновления перед записью

cnx = mysql.connector.connect(user='root', password='i130813',
                              host='127.0.0.1',
                              database='dobroe_mesto2')
cursor = cnx.cursor(buffered=True)
bcursor = cnx.cursor(buffered=True)

menu_items = []
order_items = []
order_totals = []
order_no = []

is_ex = False

is_n = False

is_cash = False
is_card = False

money = ""

isopen = False  # подгружать из базы


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
        self.clientsbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientsbutton.sizePolicy().hasHeightForWidth())
        self.clientsbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clientsbutton.setFont(font)
        self.clientsbutton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.clientsbutton, 1, 1, 2, 1)
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
        self.adminboxlayout = QtWidgets.QVBoxLayout(self.groupBox)

        self.closedordersbutton = QtWidgets.QPushButton(self.centralwidget)
        self.adminboxlayout.addWidget(self.closedordersbutton)
        self.closedordersbutton.setText("Закрытые заказы")

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
        self.orderbutton.setText(_translate("Main", "Новый клиент"))
        self.clientsbutton.setText(_translate("Main", "Текущие клиенты"))
        self.cashbox.setText(_translate("Main", "Расчет"))
        self.groupBox.setTitle(_translate("Main", "Администрирование"))

        self.exitbutton.setStyleSheet("background-color: red")
        self.printXbutton.setStyleSheet("background-color: blue")
        self.closebutton.setStyleSheet("background-color: blue")
        self.opencashboxbuttton.setStyleSheet("background-color: blue")
        self.clientsbutton.setStyleSheet("background-color: grey")
        self.orderbutton.setStyleSheet("background-color: grey")
        self.reservebutton.setStyleSheet("background-color: grey")
        self.cashbox.setStyleSheet("background-color: grey")

        self.clientsbutton.clicked.connect(self.setupClientsUi)
        self.orderbutton.clicked.connect(self.setupOrderUi)
        self.closebutton.clicked.connect(self.setupLoginUi)
        self.cashbox.clicked.connect(self.setupCashboxUi)
        self.exitbutton.clicked.connect(self.exittowindows)
        self.closedordersbutton.clicked.connect(self.setupClosedOrdersUi)

    def setupClosedOrdersUi(self):
        Main.setObjectName("Main")
        Main.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.closedorderslayour = QtWidgets.QVBoxLayout(self.centralwidget)
        self.closedorderslayour.setContentsMargins(0, 0, 0, 0)
        self.closedorderslayour.setObjectName("closedorderslayour")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setObjectName("pushButton")
        self.closedorderslayour.addWidget(self.loginbutton)
        Main.setCentralWidget(self.centralwidget)

        item_group = QtWidgets.QGroupBox("Закрытые заказы")
        self.orderslayout = QtWidgets.QVBoxLayout(item_group)
        self.closedorderslayour.addWidget(item_group)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(item_group)
        self.closedorderslayour.addWidget(self.scrollArea)

        self.retranslateClosedOrdersUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateClosedOrdersUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.loginbutton.setText(_translate("Main", "Закрыть"))
        self.loginbutton.clicked.connect(self.setupUi)

        query = "select no_orders,name,total,Open_date from orders,clients where id_visitor=id_client && close_date is not null;"
        cursor.execute(query)

        for item in cursor:
            item_group = QtWidgets.QGroupBox("Заказ: " + str(item[0]))
            self.orderslayout.addWidget(item_group)
            orderslayout = QtWidgets.QVBoxLayout(item_group)
            for value in item:
                item_label = QtWidgets.QLabel(str(value))
                orderslayout.addWidget(item_label)

    @staticmethod
    def exittowindows():
        if isopen:
            print(1)
        else:
            import sys
            sys.exit()

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
        Main.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.categorieswidget = QtWidgets.QWidget()
        self.categorieswidget.setGeometry(QtCore.QRect(0, 0, 377, 372))
        self.categorieswidget.setObjectName("categorieslayout")
        self.categorieslayout = QtWidgets.QVBoxLayout(self.categorieswidget)
        self.categorieslayout.setObjectName("verticalLayout_2")
        self.backbutton = QtWidgets.QPushButton(self.categorieswidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backbutton.setFont(font)
        self.backbutton.setObjectName("backbutton")
        self.categorieslayout.addWidget(self.backbutton)
        self.scrollArea.setWidget(self.categorieswidget)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.orderlayout = QtWidgets.QWidget()
        self.orderlayout.setGeometry(QtCore.QRect(0, 0, 376, 372))
        self.orderlayout.setObjectName("orderlayout")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.orderlayout)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2.setWidget(self.orderlayout)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savebutton.sizePolicy().hasHeightForWidth())
        self.savebutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.savebutton.setFont(font)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.cancelbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbutton.sizePolicy().hasHeightForWidth())
        self.cancelbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancelbutton.setFont(font)
        self.cancelbutton.setObjectName("cancelbutton")
        self.verticalLayout.addWidget(self.cancelbutton)

        self.cashbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cashbutton.sizePolicy().hasHeightForWidth())
        self.cashbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cashbutton.setFont(font)
        self.cashbutton.setObjectName("cashbutton")
        self.verticalLayout.addWidget(self.cashbutton)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 21))
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
        self.cashbutton.setText(_translate("MainWindow", "Чек"))

        self.cashbutton.clicked.connect(lambda: opencashbox())
        self.cancelbutton.clicked.connect(self.cancel_order)
        self.savebutton.clicked.connect(self.save_order)

        def opencashbox():
            global is_n, is_ex

            if not is_ex:
                is_n = True
            if is_n:
                is_n = False

            self.setupCashboxUi()

        def create():
            global order_number

            draw_main()

            if not is_ex:
                # query = "insert into orders values(%s,now(),null,null,*id сотрудника*,null,*id посетителя*);"
                query = "insert into orders values (default,now(),null,null,228,null,228);"
                cursor.execute(query)
                cnx.commit()

                query = "select no_orders from orders order by no_orders desc limit 1 ;"
                cursor.execute(query)
                for item in cursor:
                    for value in item:
                        order_number = int(value)
            else:
                self.cancelbutton.hide()
                pass  # добавить работу с номером заказа при переходе из окна заказов

        def draw_main():
            font = QtGui.QFont()
            font.setPointSize(20)
            self.backbutton.setEnabled(False)
            query = "select distinct product_category from products"
            cursor.execute(query)

            for item in cursor:
                for value in item:
                    item_button = QtWidgets.QPushButton(str(value))
                    self.categorieslayout.addWidget(item_button)
                    item_button.clicked.connect(lambda state, button=item_button: select_sub(button))
                    item_button.setStyleSheet("background-color: orange")
                    item_button.setFont(font)
                    menu_items.append(item_button)

            if is_ex:
                draw_order()

        def select_sub(button):

            for item in menu_items:
                try:
                    item.deleteLater()
                except BaseException:
                    pass
            menu_items.clear()

            button = button.text()
            self.backbutton.setEnabled(True)
            self.backbutton.clicked.connect(select_back_item)

            query = "select Products from products where product_category = %s;"
            data = (button,)

            cursor.execute(query, data)

            font = QtGui.QFont()
            font.setPointSize(20)

            for item in cursor:
                for value in item:
                    item_button = QtWidgets.QPushButton(str(value))
                    self.categorieslayout.addWidget(item_button)
                    item_button.clicked.connect(lambda state, button=item_button: select_item(button))
                    item_button.setStyleSheet("background-color: orange")
                    item_button.setFont(font)
                    menu_items.append(item_button)

        def select_item(button):
            global order_number

            query = "insert into order_content values(%s,%s, default,curtime());"

            try:
                data = (order_number, button.text())
            except NameError:
                order_number = 1
                data = (order_number, button.text())
            cursor.execute(query, data)

            cnx.commit()

            draw_order()

        def draw_order():
            global order_number

            query = "select no, content from order_content where id_order=%s;"
            data = (order_number,)
            cursor.execute(query, data)

            for item in order_items:
                try:
                    item.deleteLater()
                except BaseException:
                    pass
            order_items.clear()

            i = 1
            j = 1
            for item in cursor:
                for value in item:
                    if j % 2 != 0:
                        j += 1
                        no = int(value)
                        continue
                    item_label = QtWidgets.QPushButton(str(value))
                    self.gridLayout_2.addWidget(item_label, i, 0, 1, 1)
                    item_label.clicked.connect(lambda state, id=no: delete_item(id))
                    item_label.setStyleSheet("background-color: red")
                    order_items.append(item_label)
                    i += 1
                    j += 1

        def delete_item(id):

            query = "delete from order_content where no =%s;"
            data = (id,)
            cursor.execute(query, data)

            query = "UPDATE order_content SET no = no-1 WHERE no > %s;"
            data = (id,)
            cursor.execute(query, data)

            cnx.commit()

            draw_order()

        def select_back_item():
            for item in menu_items:
                item.deleteLater()
            menu_items.clear()
            draw_main()

        create()

    def save_order(self):
        global order_number

        query = "select no from order_content where id_order=%s limit 1 into @nuller;"
        data = (order_number,)
        cursor.execute(query, data)
        query = "select isnull(@nuller);"
        cursor.execute(query)

        for item in cursor:
            if int(item[0]) == 1:
                query = "delete from orders where no_orders= %s;"
                data = (order_number,)
                cursor.execute(query, data)
                cnx.commit()

        global is_ex
        if is_ex:
            is_ex = False
        self.setupUi()

    def cancel_order(self):
        if not is_ex:
            global order_number
            query = "delete from orders where no_orders= %s;"
            data = (order_number,)
            cursor.execute(query, data)
            query = "delete from order_content where id_order= %s;"
            data = (order_number,)
            cursor.execute(query, data)
            cnx.commit()

        query = "select no from order_content where id_order=%s limit 1 into @nuller;"
        data = (order_number,)
        cursor.execute(query, data)
        query = "select isnull(@nuller);"
        cursor.execute(query)

        for item in cursor:
            if int(item[0]) == 1:
                query = "delete from orders where no_orders= %s;"
                data = (order_number,)
                cursor.execute(query, data)
                cnx.commit()

        self.setupUi()

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

        self.inlabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inlabel.sizePolicy().hasHeightForWidth())
        self.inlabel.setSizePolicy(sizePolicy)
        self.inlabel.setObjectName("inlabel")
        self.gridLayout_3.addWidget(self.inlabel, 2, 0, 1, 3)

        self.finalbutton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finalbutton.sizePolicy().hasHeightForWidth())
        self.finalbutton.setSizePolicy(sizePolicy)
        self.finalbutton.setObjectName("finalbutto")
        self.finalbutton.setText("Рассчет")
        self.gridLayout_3.addWidget(self.finalbutton, 3, 0, 1, 1)

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
        self.categorieswidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.categorieswidget.setContentsMargins(0, 0, 0, 0)
        self.categorieswidget.setObjectName("verticalLayout_2")
        self.backbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.backbutton.setObjectName("backbutton")
        self.categorieswidget.addWidget(self.backbutton)
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
        Main.setCentralWidget(self.gridLayoutWidget)
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

        self.finalbutton.clicked.connect(lambda: closeorder())
        self.cashbutton.clicked.connect(lambda: cash())
        self.noncashbutton.clicked.connect(lambda: card())

        self.finalbutton.setEnabled(False)

        def cash():
            global is_cash
            is_cash = True
            self.noncashbutton.setEnabled(False)

        def card():
            global is_card
            is_card = True
            self.cashbutton.setEnabled(False)

        def closeorder():

            global order_number, is_cash, is_card

            query = "SELECT total FROM orders WHERE No_orders = %s;"
            data = (order_number,)
            cursor.execute(query, data)

            for item in cursor:
                if int(money) >= int(item[0]):
                    if is_cash:
                        query = "update orders set close_date=now(),Type='Cash' where no_orders=%s;"
                        data = (order_number,)
                    if is_card:
                        query = "update orders set close_date=now(),Type='Card' where no_orders=%s;"
                        data = (order_number,)
                    if is_card or is_cash:
                        cursor.execute(query, data)
                        cnx.commit()
                        is_card = False
                        # добавить печать чека
                        self.setupUi()

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
            global money
            self.inlabel.setText("Внесено " + money)

            try:
                global order_number
                query = "SELECT total FROM orders WHERE No_orders = %s;"
                data = (order_number,)
                cursor.execute(query, data)
                for item in cursor:
                    if int(money) >= int(item[0]):
                        self.finalbutton.setEnabled(True)
                        if int(money) > int(item[0]):
                            self.inlabel.setText("Внесено: " + money + "\nCдача: " + str(int(money) - int(item[0])))
                    else:
                        self.finalbutton.setEnabled(False)
            except BaseException:
                pass

        global is_ex, is_n

        if is_ex or is_n:
            global order_number

            query = "select content from order_content where id_order=%s;"
            data = (order_number,)
            cursor.execute(query, data)

            for item in order_items:
                try:
                    item.deleteLater()
                except BaseException:
                    pass
            order_items.clear()

            for item in cursor:
                for value in item:
                    item_label = QtWidgets.QPushButton(str(value))
                    self.verticalLayout.addWidget(item_label)
                    # item_label.setStyleSheet("background-color: ")
                    order_items.append(item_label)

            query = "SELECT total FROM orders WHERE No_orders = %s;"
            data = (order_number,)
            cursor.execute(query, data)
            for item in cursor:
                self.summlabel.setText("К Оплате: " + str(item[0]))

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

    def setupClientsUi(self):
        Main.setObjectName("Main")
        Main.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 621, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.newbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.newbutton.setFont(font)
        self.newbutton.setObjectName("newbutton")
        self.gridLayout.addWidget(self.newbutton, 3, 2, 1, 2)
        self.infolabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infolabel.sizePolicy().hasHeightForWidth())
        self.infolabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.infolabel.setFont(font)
        self.infolabel.setObjectName("label")
        self.gridLayout.addWidget(self.infolabel, 0, 0, 1, 4)
        self.mainbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mainbutton.setFont(font)
        self.mainbutton.setObjectName("mainbutton")
        self.gridLayout.addWidget(self.mainbutton, 3, 0, 1, 2)
        Main.setCentralWidget(self.gridLayoutWidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        item_group = QtWidgets.QGroupBox("Заказы")
        self.orderslayout = QtWidgets.QGridLayout(item_group)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(item_group)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 4)

        self.retranslateClientsUi(Main)

    def retranslateClientsUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.newbutton.setText(_translate("Main", "Новый клиент"))
        self.infolabel.setText(_translate("Main", "Дата + Время"))
        self.mainbutton.setText(_translate("Main", "На главную"))
        self.mainbutton.clicked.connect(self.setupUi)
        self.newbutton.clicked.connect(self.setupOrderUi)

        query = "select name,open_date,total,No_orders from orders,clients where id_visitor=id_client && isnull(close_date);"
        cursor.execute(query)

        i = 1
        j = 1
        k = 0

        order_totals.clear()
        order_no.clear()

        for item in cursor:
            item_group = QtWidgets.QGroupBox("Клиент: " + str(item[0]))
            categorieslayout = QtWidgets.QVBoxLayout(item_group)
            self.orderslayout.addWidget(item_group, j, k, 1, 1)

            k += 1
            if k % 3 == 0:
                k = 0
                j += 1
            for value in item:
                if i == 2:
                    item_label = QtWidgets.QLabel("Заказ открыт: " + str(value))
                    categorieslayout.addWidget(item_label)
                if i == 3:
                    item_label = QtWidgets.QLabel("К оплате: " + str(value))
                    categorieslayout.addWidget(item_label)
                    order_totals.append(item_label)
                if i == 4:
                    item_button = QtWidgets.QPushButton("Просмотреть")
                    categorieslayout.addWidget(item_button)
                    item_button.clicked.connect(lambda state, order=value: open_order(order))
                    order_no.append(value)
                    item_button = QtWidgets.QPushButton("Рассчитать")
                    categorieslayout.addWidget(item_button)
                    item_button.clicked.connect(lambda state, order=value: open_order(order))
                    i = 0
                i += 1

        def open_order(value):
            global order_number, is_ex
            order_number = int(value)
            is_ex = True
            self.setupOrderUi()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi()
    Main.show()

    def BackgroundThread():
        date = datetime.datetime.today()
        months = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября",
                  'Ноября', "Декабря"]
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        day = date.weekday()
        month = date.month
        if date.minute < 10:
            time = str(
                "{0} {1} {2} {3}:0{4}".format(str(date.day), months[month - 1], weekdays[day], str(date.hour),
                                              str(date.minute)))
        else:
            time = str(
                "{0} {1} {2} {3}:{4}".format(str(date.day), months[month - 1], weekdays[day], str(date.hour),
                                             str(date.minute)))
        try:
            ui.infolabel.setText(time)
        except RuntimeError:
            pass

        try:
            for total, no in zip(order_totals, order_no):
                data = (no,)
                query = "select if(client_lvl=3,15,if(client_lvl=2,10,if(client_lvl=1,5,0))) as 'discount' from clients,orders where id_client=id_visitor && no_orders=%s into @c;"
                bcursor.execute(query, data)
                query = "select sum(product_cost) from order_content,products where content=products && id_order=%s && product_category<>'Время' into @a;  "
                bcursor.execute(query, data)
                query = "select if(@a is null,0,@a) into @a;"
                bcursor.execute(query)
                query = "select sum(round(Product_cost/60) * round(time_to_sec(timediff(curtime(),times))/60)) from order_content,products where id_order=%s && content=products && product_category='Время' into @b;"
                bcursor.execute(query, data)
                query = "select if(@b is null,0,@b) into @b;"
                bcursor.execute(query)
                query = "update orders set total=(@a+@b)/100*(100-@c) where no_orders=%s;"
                bcursor.execute(query, data)
                cnx.commit()

                query = "SELECT total FROM orders WHERE No_orders = %s;"
                data = (no,)
                bcursor.execute(query, data)
                for item in cursor:
                    total.setText("К Оплате: " + str(item[0]))

        except RuntimeError:
            pass


    timer = QTimer()
    timer.timeout.connect(BackgroundThread)
    timer.start(1000)

    sys.exit(app.exec_())
