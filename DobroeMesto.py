import datetime

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

d = datetime.datetime.today()  # время получается один раз при запуске программы, требует обновления перед записью

try:
    cnx = mysql.connector.connect(user='root', password='i130813',
                                  host='127.0.0.1',
                                  database='dobroe_mesto')

    cursor = cnx.cursor(buffered=True)
    bcursor = cnx.cursor(buffered=True)

except BaseException as e:
    # TODO: Доделать
    pass
    # QtWidgets.QMessageBox.about(, "Title", "Message")

menu_items = []
order_items = []
order_totals = []
order_no = []

items = []

is_ex = False

is_n = False

is_cash = False
is_card = False

money = ""

isopen = False  # подгружать из базы


class MainWindow(object):

    def setupUi(self):
        Main.setObjectName("Main")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        Main.setFont(font)
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
        self.gridLayout.addWidget(self.cashbox, 3, 3, 1, 1)
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.ordersview = QtWidgets.QWidget()
        self.ordersview.setGeometry(QtCore.QRect(0, 0, 474, 422))
        self.ordersview.setObjectName("ordersview")
        self.orderslayout = QtWidgets.QVBoxLayout(self.ordersview)
        self.orderslayout.setObjectName("orderslayout")
        self.scrollArea.setWidget(self.ordersview)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 10, 3)
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
        self.gridLayout.addWidget(self.orderbutton, 1, 3, 1, 1)
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
        self.gridLayout.addWidget(self.reservebutton, 2, 3, 1, 1)
        self.closedaybutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closedaybutton.sizePolicy().hasHeightForWidth())
        self.closedaybutton.setSizePolicy(sizePolicy)
        self.closedaybutton.setObjectName("closedaybutton")
        self.gridLayout.addWidget(self.closedaybutton, 9, 3, 1, 1)
        self.adminbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adminbutton.sizePolicy().hasHeightForWidth())
        self.adminbutton.setSizePolicy(sizePolicy)
        self.adminbutton.setObjectName("adminbutton")
        self.gridLayout.addWidget(self.adminbutton, 10, 3, 1, 1)
        self.notificationbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notificationbutton.sizePolicy().hasHeightForWidth())
        self.notificationbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.notificationbutton.setFont(font)
        self.notificationbutton.setObjectName("notificationbutton")
        self.gridLayout.addWidget(self.notificationbutton, 7, 3, 1, 1)
        self.xbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xbutton.sizePolicy().hasHeightForWidth())
        self.xbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.xbutton.setFont(font)
        self.xbutton.setObjectName("xbutton")
        self.gridLayout.addWidget(self.xbutton, 4, 3, 1, 1)
        self.screenlockbutton = QtWidgets.QPushButton(self.centralwidget)
        self.screenlockbutton.setObjectName("screenlockbutton")
        self.gridLayout.addWidget(self.screenlockbutton, 6, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        Main.showMaximized()

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def test(self):
        w = AdminWindow()
        w.exec_()

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.cashbox.setText(_translate("Main", "Рассчет"))
        self.groupBox_2.setTitle(_translate("Main", "Информация"))
        self.infolabel.setText(_translate("Main", "Время + дата"))
        self.groupBox.setTitle(_translate("Main", "Гости"))
        self.orderbutton.setText(_translate("Main", "Новый гость"))
        self.reservebutton.setText(_translate("Main", "Бронирование"))
        self.closedaybutton.setText(_translate("Main", "Закрытие смены"))
        self.adminbutton.setText(_translate("Main", "Редактирование Базы"))
        self.notificationbutton.setText(_translate("Main", "Уведомления"))
        self.xbutton.setText(_translate("Main", "Промежуточный отчет"))
        self.screenlockbutton.setText(_translate("Main", "Блокировка"))

        self.adminbutton.clicked.connect(self.test)

        '''
        query = "select User_lvl from users where idUsers = %s"
        cursor.execute(query, (iduser, ))

        for item in cursor:
            for value in item:
                if int(value) == 1:
                    pass
                if int(value) == 2:
                    pass
                if int(value) == 3:
                    self.closedordersbutton.setEnabled(True)
                    self.modifydatabutton.setEnabled(True)
        '''

        query = "select name,open_date,total,No_orders from orders,clients " \
                "where id_visitor=id_client && isnull(close_date);"
        cursor.execute(query)

        i = 1
        j = 1
        k = 0

        order_totals.clear()
        order_no.clear()

        j = 0

        for item in cursor:
            item_group = QtWidgets.QGroupBox("Клиент: " + str(item[0]))
            categorieslayout = QtWidgets.QGridLayout(item_group)
            self.orderslayout.addWidget(item_group)
            item_group.clicked.connect(lambda: print(1))
            for value in item:
                if i == 2:
                    item_label = QtWidgets.QLabel("Гость пришел: " + str(value))
                    categorieslayout.addWidget(item_label, 0, j, 1, 1)
                    j += 1
                if i == 3:
                    item_label = QtWidgets.QLabel("К оплате: " + str(value))
                    categorieslayout.addWidget(item_label, 0, j, 1, 1)
                    order_totals.append(item_label)
                    j += 1
                if i == 4:
                    j = 0
                    item_button = QtWidgets.QPushButton("Просмотреть")
                    categorieslayout.addWidget(item_button, 1, j, 1, 1)
                    j += 1
                    # item_button.clicked.connect(lambda state, order=value: open_order(order))
                    order_no.append(value)
                    item_button = QtWidgets.QPushButton("Рассчитать")
                    categorieslayout.addWidget(item_button, 1, j, 1, 1)
                    j += 1
                    # item_button.clicked.connect(lambda state, order=value: open_order(order))
                    # TODO: Добавить комментарии и иконки
                    i = 0
                i += 1
            j = 0

    def printX(self):
        query = "select sum(total) from orders;"
        cursor.execute(query)

        query = "select sum(total) from orders where type = %s;"
        data = ("Cash",)
        cursor.execute(query, data)
        data = ("Card",)
        cursor.execute(query, data)

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

        query = "select no_orders,name,total,Open_date from orders,clients " \
                "where id_visitor=id_client && close_date is not null;"
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
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 559))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
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
        self.pushButton.setText(_translate("Main", "Вход"))
        self.label.setText(_translate("Main", "Сканируйте карту"))
        self.pushButton_3.setText(_translate("Main", "Повторное сканирование"))
        self.pushButton_2.setText(_translate("Main", "Настройки"))

    def login(self):
        password = self.lineEdit.text()
        login = self.label.text()

        query = "set @k=null;"
        cursor.execute(query)
        data = (password, login)
        query = "select if(pass=%s,1,0) from users where card_num=%s into @k;"
        cursor.execute(query, data)
        query = "select if(isnull(@k),0,if(@k=1,1,2));"
        cursor.execute(query)

        for item in cursor:
            for value in item:
                if str(value) == "1":
                    global isopen
                    if isopen:
                        pass
                    else:
                        query = "select idUsers from users where card_num = %s;"
                        cursor.execute(query, data)
                        for item in cursor:
                            for value in item:
                                query = "insert into shifts values(default,now(),null,%s,null,null,null,default);"
                                data = (str(value),)
                                cursor.execute(query, data)
                if str(value) == "2":
                    self.lineEdit.setText("Пароль неверный")
                if str(value) == "0":
                    self.label.setText("Не валидная карта")

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
        self.orderslayout = QtWidgets.QGridLayout(self.orderlayout)
        self.orderslayout.setObjectName("orderslayout")
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
        Main.setWindowTitle(_translate("Main", "Main"))
        self.backbutton.setText(_translate("Main", "Назад"))
        self.savebutton.setText(_translate("Main", "Сохранить"))
        self.cancelbutton.setText(_translate("Main", "Отмена"))
        self.cashbutton.setText(_translate("Main", "Чек"))

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

            font = QtGui.QFont()
            font.setPointSize(20)

            query = "select products from products where product_category=%s;"
            data = (button,)
            cursor.execute(query, data)

            for item in cursor:
                for value in item:
                    query = "select if(product_amount<>0,1,0) from products where products=%s;"
                    data = (value,)
                    bcursor.execute(query, data)
                    for response in bcursor:
                        for result in response:
                            if int(result) == 1:
                                item_button = QtWidgets.QPushButton(str(value))
                                self.categorieslayout.addWidget(item_button)
                                item_button.clicked.connect(lambda state, button=item_button: select_item(button))
                                item_button.setStyleSheet("background-color: orange")
                                item_button.setFont(font)
                                menu_items.append(item_button)
                                item_button.setEnabled(True)
                            if int(result) == 0:
                                item_button = QtWidgets.QPushButton(str(value))
                                self.categorieslayout.addWidget(item_button)
                                item_button.clicked.connect(lambda state, button=item_button: select_item(button))
                                item_button.setStyleSheet("background-color: orange")
                                item_button.setFont(font)
                                menu_items.append(item_button)
                                item_button.setEnabled(False)

        def select_item(button):
            global order_number

            query = "insert into order_content values(%s,%s, default,curtime());"

            try:
                data = (order_number, button.text())
            except NameError:
                order_number = 1
                data = (order_number, button.text())
            cursor.execute(query, data)

            query = "update products set product_amount=product_amount-1 where products=%s && product_amount>0;"
            data = (button.text(),)
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
                    self.orderslayout.addWidget(item_label, i, 0, 1, 1)
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
                bcursor.execute(query, data)
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
        self.orderslayout = QtWidgets.QGridLayout(self.groupBox)
        self.orderslayout.setObjectName("orderslayout")
        self.button9 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        self.button9.setObjectName("button9")
        self.orderslayout.addWidget(self.button9, 2, 2, 1, 1)
        self.button8 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        self.button8.setObjectName("button8")
        self.orderslayout.addWidget(self.button8, 2, 1, 1, 1)
        self.button7 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setObjectName("button7")
        self.orderslayout.addWidget(self.button7, 2, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setObjectName("button2")
        self.orderslayout.addWidget(self.button2, 0, 1, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        self.button5.setObjectName("button5")
        self.orderslayout.addWidget(self.button5, 1, 1, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setObjectName("button1")
        self.orderslayout.addWidget(self.button1, 0, 0, 1, 1)
        self.button3 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setObjectName("button3")
        self.orderslayout.addWidget(self.button3, 0, 2, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setObjectName("button4")
        self.orderslayout.addWidget(self.button4, 1, 0, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setObjectName("button6")
        self.orderslayout.addWidget(self.button6, 1, 2, 1, 1)
        self.buttonC = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonC.sizePolicy().hasHeightForWidth())
        self.buttonC.setSizePolicy(sizePolicy)
        self.buttonC.setObjectName("buttonC")
        self.orderslayout.addWidget(self.buttonC, 3, 0, 1, 1)
        self.button0 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy)
        self.button0.setObjectName("button0")
        self.orderslayout.addWidget(self.button0, 3, 1, 1, 1)
        self.buttonCA = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCA.sizePolicy().hasHeightForWidth())
        self.buttonCA.setSizePolicy(sizePolicy)
        self.buttonCA.setObjectName("buttonCA")
        self.orderslayout.addWidget(self.buttonCA, 3, 2, 1, 1)
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


class AdminWindowUi(object):
    def setupAdminUi(self, AdminWindowUi):
        AdminWindowUi.setObjectName("AdminWindowUi")
        AdminWindowUi.showNormal()
        AdminWindowUi.setWindowTitle("Редактирование Базы Данных")
        self.gridLayout = QtWidgets.QGridLayout(AdminWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.savebutton = QtWidgets.QPushButton(AdminWindowUi)
        self.savebutton.setObjectName("savebutton")
        self.gridLayout.addWidget(self.savebutton, 0, 3, 1, 1)
        self.addclientbutton = QtWidgets.QPushButton(AdminWindowUi)
        self.addclientbutton.setObjectName("addclientbutton")
        self.gridLayout.addWidget(self.addclientbutton, 0, 1, 1, 1)
        self.addworkerbutton = QtWidgets.QPushButton(AdminWindowUi)
        self.addworkerbutton.setObjectName("addworkerbutton")
        self.gridLayout.addWidget(self.addworkerbutton, 0, 2, 1, 1)
        self.addproductbutton = QtWidgets.QPushButton(AdminWindowUi)
        self.addproductbutton.setObjectName("addproductbutton")
        self.gridLayout.addWidget(self.addproductbutton, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(AdminWindowUi)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 231))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 4)

        self.retranslateAdminUi()
        QtCore.QMetaObject.connectSlotsByName(AdminWindowUi)

    def retranslateAdminUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.savebutton.setText(_translate("AdminWindowUi", "Применить"))
        self.addclientbutton.setText(_translate("AdminWindowUi", "Добавить клиента"))
        self.addworkerbutton.setText(_translate("AdminWindowUi", "Добавить сотрудника"))
        self.addproductbutton.setText(_translate("AdminWindowUi", "Добавить товар"))
        self.addproductbutton.clicked.connect(self.setupproductUi)
        self.addworkerbutton.clicked.connect(self.setupworkUi)

        for i in reversed(range(self.gridLayout_3.count())):
            if isinstance(self.gridLayout_3.itemAt(i).widget(), QtWidgets.QLabel):
                self.gridLayout_3.itemAt(i).widget().deleteLater()

        def draw_labels(labels, widget, line):
            for label in labels:
                line_item = QtWidgets.QLabel(label)
                widget.addWidget(line_item, line, labels.index(label) + 1, 1, 1)

        line_item = QtWidgets.QLabel("Товары")
        self.gridLayout_3.addWidget(line_item, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(18)
        line_item.setFont(font)

        labels = [
            "Название",
            "Cтоимость",
            "Количество",
            "Категория"
        ]

        draw_labels(labels, self.gridLayout_3, 1)

        query = "select * from products;"
        cursor.execute(query)
        i = 1
        j = 4
        k = 1
        for item in cursor:
            for value in item:
                if k == 1:
                    line_item = QtWidgets.QLineEdit(str(value))
                    self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                    id = str(value)
                    line_item.textChanged.connect(
                        lambda state, line=[line_item, str(value), id, k]: modify(line, "product"))
                    k += 1
                    continue
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(
                    lambda state, line=[line_item, str(value), id, k]: modify(line, "product"))

                but_item = QtWidgets.QPushButton("Удалить")
                self.gridLayout_3.addWidget(but_item, j, 5, 1, 1)
                but_item.clicked.connect(lambda state, name=id: delete(name, "product"))

                k += 1
                if k % 5 == 0:
                    j += 1
                    k = 1

        query = "select * from clients;"
        cursor.execute(query)
        k = 0
        j += 2
        i = 0
        line_item = QtWidgets.QLabel("Клиенты")
        self.gridLayout_3.addWidget(line_item, j, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(18)
        line_item.setFont(font)

        labels = [
            "Имя",
            "Номер карты",
            "Пароль",
            "ID Фото",
            "Уровень скидки",
            "Номер телефона",
            "Контакт",
            "Личный счет"
        ]
        draw_labels(labels, self.gridLayout_3, j)

        j += 1
        for item in cursor:
            for value in item:
                if k == 0:
                    id = str(value)
                    k += 1
                    continue
                if k != 3:
                    line_item = QtWidgets.QLineEdit(str(value))
                    self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                    line_item.textChanged.connect(
                        lambda state, line=[line_item, str(value), id, k]: modify(line, "client"))
                if k == 3:
                    line_item = QtWidgets.QLabel(str(value))
                    self.gridLayout_3.addWidget(line_item, j, k, 1, 1)

                but_item = QtWidgets.QPushButton("Удалить")
                self.gridLayout_3.addWidget(but_item, j, 7, 1, 1)
                but_item.clicked.connect(lambda state, row=id: delete(row, "client"))

                k += 1
                if k % 7 == 0:
                    j += 1
                    i += 1
                    k = 0

        line_item = QtWidgets.QLabel("Работники")
        self.gridLayout_3.addWidget(line_item, j, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(18)
        line_item.setFont(font)

        labels = [
            "Имя",
            "Номер карты",
            "Пароль",
            "Уровень доступа",
            "Номер телефона",
            "Контакт",
        ]
        draw_labels(labels, self.gridLayout_3, j)

        j += 1
        i = 0
        query = "select * from users;"
        cursor.execute(query)
        k = 0
        for item in cursor:
            for value in item:
                if k == 0:
                    k += 1
                    but_item = QtWidgets.QPushButton("Удалить")
                    self.gridLayout_3.addWidget(but_item, j, 5, 1, 1)
                    id = str(value)
                    but_item.clicked.connect(lambda state, row=str(value): delete(row, "user"))
                    continue
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=[line_item, str(value), id, k]: modify(line, "user"))

                k += 1
                if k % 5 == 0:
                    j += 1
                    i += 1
                    k = 0

        def modify(data, type):
            self.savebutton.clicked.connect(lambda: save(data, type))
            self.savebutton.setEnabled(True)

        def save(list, type):
            data = (list[0].text(), list[1], list[2])
            k = list[3]
            if type == "user":
                if k == 1:
                    query = "update users set Name_users = %s where Name_users = %s;"
                if k == 2:
                    query = "update users set Card_num = %s where Card_num = %s;"
                if k == 3:
                    query = "update users set pass = %s where pass = %s;"
                if k == 4:
                    query = "update users set User_lvl = %s where User_lvl = %s;"
                cursor.execute(query, data)
                cnx.commit()
            if type == "client":
                if k == 1:
                    query = "update clients set Name = %s where Name = %s;"
                if k == 2:
                    query = "update clients set Card_Num_client = %s where Card_Num_client = %s;"
                if k == 3:
                    query = "update clients set id_photo = %s where id_photo = %s;"
                if k == 4:
                    query = "update clients set Client_lvl = %s where Client_lvl = %s;"
                cursor.execute(query, data)
                cnx.commit()
            if type == "product":
                if k == 1:
                    query = "update products set Products = %s where Products = %s;"
                if k == 2:
                    query = "update products set Product_cost = %s where Product_cost = %s && Products = %s;"
                if k == 3:
                    query = "update products set Product_Amount = %s where Product_Amount = %s && Products = %s;"
                if k == 4:
                    query = "update products set Product_category = %s where Product_category = %s && Products = %s;"
                cursor.execute(query, data)
                cnx.commit()
            self.savebutton.setEnabled(False)
            self.retranslateAdminUi()

        def delete(id, type):
            data = id
            if type == "user":
                query = "delete from users where idUsers=%s;"
                cursor.execute(query, (data,))
                cnx.commit()
            if type == "client":
                query = "delete from passenger where idPassenger=%s;"
                cursor.execute(query, (data,))
                cnx.commit()
            if type == "product":
                query = "delete from users where idUsers=%s;"
                cursor.execute(query, (data,))
                cnx.commit()
            QtWidgets.QMessageBox.about(self, "Инфо", "Удалено успешно")
            self.retranslateAdminUi()

    def setupproductUi(self):
        AdminWindowUi.setObjectName("AdminWindowUi")
        self.centralwidget = QtWidgets.QWidget(AdminWindowUi)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 11, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 10, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        AdminWindowUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindowUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        AdminWindowUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindowUi)
        self.statusbar.setObjectName("statusbar")
        AdminWindowUi.setStatusBar(self.statusbar)

        self.retranslateproductUi(AdminWindowUi)
        QtCore.QMetaObject.connectSlotsByName(AdminWindowUi)

    def retranslateproductUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("AdminWindowUi", "AdminWindowUi"))
        self.pushButton.setText(_translate("AdminWindowUi", "Сохранить"))
        self.pushButton_2.setText(_translate("AdminWindowUi", "Назад"))
        self.label_4.setText(_translate("AdminWindowUi", "Категория"))
        self.label.setText(_translate("AdminWindowUi", "Название"))
        self.label_2.setText(_translate("AdminWindowUi", "Стоимость"))
        self.label_3.setText(_translate("AdminWindowUi", "Количество"))

        self.pushButton_2.clicked.connect(self.setupAdminUi)
        self.pushButton.clicked.connect(self.writeproduct)

    def writeproduct(self):
        query = "insert into products(Products, Product_cost, Product_Amount, Product_category)values(%s, %s, %s, %s);"
        data = (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        cursor.execute(query, data)
        cnx.commit()
        self.setupAdminUi()

    def setupworkUi(self):
        AdminWindowUi.setObjectName("AdminWindowUi")
        self.centralwidget = QtWidgets.QWidget(AdminWindowUi)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 11, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 10, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        AdminWindowUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindowUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        AdminWindowUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindowUi)
        self.statusbar.setObjectName("statusbar")
        AdminWindowUi.setStatusBar(self.statusbar)

        self.retranslateworkUi(AdminWindowUi)
        QtCore.QMetaObject.connectSlotsByName(AdminWindowUi)

    def retranslateworkUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("AdminWindowUi", "AdminWindowUi"))
        self.pushButton.setText(_translate("AdminWindowUi", "Сохранить"))
        self.pushButton_2.setText(_translate("AdminWindowUi", "Назад"))
        self.label_4.setText(_translate("AdminWindowUi", "Уровень пользователя"))
        self.label.setText(_translate("AdminWindowUi", "Имя"))
        self.label_2.setText(_translate("AdminWindowUi", "Номер карты"))
        self.label_3.setText(_translate("AdminWindowUi", "Пароль"))

        self.pushButton_2.clicked.connect(self.setupAdminUi)
        self.pushButton.clicked.connect(self.writeworker)

    def writeworker(self):
        query = "insert into users(Name_users, Card_num, pass, User_lvl)values(%s, %s, %s, %s);"
        data = (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),)
        cursor.execute(query, data)
        cnx.commit()
        self.setupAdminUi()


class AdminWindow(QtWidgets.QDialog, AdminWindowUi):
    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.setupAdminUi(self)


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
        except BaseException:
            pass

        try:
            for total, no in zip(order_totals, order_no):
                data = (no,)
                query = "select if(client_lvl=3,15,if(client_lvl=2,10,if(client_lvl=1,5,0))) as 'discount' " \
                        "from clients,orders " \
                        "where id_client=id_visitor && no_orders=%s into @c;"
                bcursor.execute(query, data)
                query = "select sum(product_cost) from order_content,products where " \
                        "content=products && id_order=%s && product_category<>'Время' into @a; "
                bcursor.execute(query, data)
                query = "select if(@a is null,0,@a) into @a;"
                bcursor.execute(query)
                query = "select round(sum((Product_cost/60) * ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(times))/60)))" \
                        "from order_content, products " \
                        "where id_order = %s && content = products && product_category = 'Время' into @b;"
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

        except BaseException:
            pass


    timer = QTimer()
    timer.timeout.connect(BackgroundThread)
    timer.start(100)

    sys.exit(app.exec_())
