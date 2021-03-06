import datetime
import threading
import webbrowser

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
    ccursor = cnx.cursor(buffered=True)

except BaseException as e:
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    msgbox = QtWidgets.QMessageBox()
    msgbox.setWindowTitle("Ошибка соединения с базой данных")
    msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
    msgbox.setText('Проверьте подключение к Базе Данных')
    msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
    msgbox.setDetailedText(str(e))
    msgbox.exec()


menu_items = []
order_items = []
order_totals = []
order_no = []

order_number = 0

items = []

isopen = False  # подгружать из базы

guest_number = 1488
id_user = 0


class MainWindow(QtWidgets.QWidget):

    def setupUi(self):
        Main.setObjectName("Main")
        Main.setWindowTitle("Доброе место")
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
        self.clientcashbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientcashbutton.sizePolicy().hasHeightForWidth())
        self.clientcashbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clientcashbutton.setFont(font)
        self.clientcashbutton.setObjectName("clientcashbutton")
        self.gridLayout.addWidget(self.clientcashbutton, 3, 3, 1, 1)
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

        self.newclient = QtWidgets.QPushButton()
        self.gridLayout.addWidget(self.newclient, 5, 3, 1, 1)

        self.screenlockbutton = QtWidgets.QPushButton(self.centralwidget)
        self.screenlockbutton.setObjectName("screenlockbutton")
        self.gridLayout.addWidget(self.screenlockbutton, 6, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        Main.showMaximized()

        Main.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/favicon.ico')))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Main)

    def openAdmin(self):
        w = AdminWindow()
        my_thread = threading.Thread(target=w.exec_())
        my_thread.start()
        self.draw_orders()

    def openNewOrder(self):
        w = NewOrderWindow()
        w.exec_()

        OrderTotalThread()
        # self.draw_orders()

    def openReserve(self):
        webbrowser.open("vk.com")

    def openNotifications(self):
        w = NotificationsWindow()
        my_thread = threading.Thread(target=w.exec_())
        my_thread.start()
        self.draw_orders()

    def openclientcash(self):
        client = QtWidgets.QInputDialog.getText(self, "Сканируйте карту гостя", "Карта")

        try:
            if client != "" and client != " ":
                amount = QtWidgets.QInputDialog.getText(self, "Введите сумму оплаты", "Сумма")
                if amount != "" and amount != " ":
                    query = "insert into orders values(default,now(),now(),%s,228,'account',%s,null);"
                    data = (str(amount[0]), str(client[0]))
                    cursor.execute(query, data)
                    cnx.commit()
                    query = "select No_Orders from orders order by NO_Orders desc limit 1"
                    cursor.execute(query)
                    for item in cursor:
                        for value in item:
                            value = str(value)
                    query = "insert into order_content values(%s,'Пополнение',default,now(),'Yes','account',%s);"
                    data = (value, str(client[0]))
                    cursor.execute(query, data)
                    cnx.commit()
                    Message.show(Message, "Информация", "Счет пополнен")
        except BaseException:
            return 0

    def addclient(self):
        client = QtWidgets.QInputDialog.getText(self, "Сканируйте новую карту", "Карта")

        try:
            if client != "" and client != " ":
                amount = QtWidgets.QInputDialog.getText(self, "Введите имя", "Имя")
                if amount != "" and amount != " ":
                    query = "insert into clients (id_client, Name, Card_Num_client) values (default, %s, %s);"
                    data = (str(amount[0]), str(client[0]))
                    cursor.execute(query, data)
                    cnx.commit()
                    Message.show(Message, "Гость добавлен",
                                 "Для добавления остальных данных из анкеты, передайте анкету менеджеру")
        except BaseException as e:
            print(e)
            return 0

    def closeday(self):

        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Чековый принтер не подключен")
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
        msgbox.setText('Проверьте подключение к чековому принтеру')
        msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        # msgbox.setDetailedText(str(e))
        msgbox.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.clientcashbutton.setText(_translate("Main", "Пополнение счета"))
        self.groupBox_2.setTitle(_translate("Main", "Информация"))
        self.groupBox.setTitle(_translate("Main", "Гости"))
        self.orderbutton.setText(_translate("Main", "Новый посетитель"))
        self.reservebutton.setText(_translate("Main", "Бронирование"))
        self.closedaybutton.setText(_translate("Main", "Закрытие смены"))
        self.adminbutton.setText(_translate("Main", "Редактирование Базы"))
        self.notificationbutton.setText(_translate("Main", "Уведомления"))
        self.xbutton.setText(_translate("Main", "Промежуточный отчет"))
        self.screenlockbutton.setText(_translate("Main", "Выйти из аккаунта"))

        self.newclient.setText("Регистрация гостя")

        # BackgroundThread()


        self.adminbutton.clicked.connect(self.openAdmin)
        self.orderbutton.clicked.connect(self.openNewOrder)
        self.notificationbutton.clicked.connect(self.openNotifications)
        self.reservebutton.clicked.connect(self.openReserve)
        self.clientcashbutton.clicked.connect(self.openclientcash)
        self.newclient.clicked.connect(self.addclient)
        self.closedaybutton.clicked.connect(self.closeday)
        self.xbutton.clicked.connect(self.printX)

        self.adminbutton.setEnabled(False)
        self.xbutton.setEnabled(False)
        self.closedaybutton.setEnabled(False)

        self.screenlockbutton.clicked.connect(self.setupLoginUi)

        self.draw_orders()

        global id_user

        query = "select User_lvl from users where idUsers = %s"
        cursor.execute(query, (id_user,))

        for item in cursor:
            for value in item:
                if int(value) == 1:
                    pass
                if int(value) == 2:
                    self.adminbutton.setEnabled(True)
                if int(value) == 3:
                    self.adminbutton.setEnabled(True)
                    self.xbutton.setEnabled(True)
                    self.closedaybutton.setEnabled(True)

    def draw_orders(self):

        def create_icon(path):
            item_label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(path)
            item_label.setPixmap(pixmap)
            return item_label

        for i in reversed(range(self.orderslayout.count())):
            if isinstance(self.orderslayout.itemAt(i).widget(), QtWidgets.QGroupBox):
                self.orderslayout.itemAt(i).widget().deleteLater()

        query = "select name,open_date,total,No_orders, comments from orders,clients " \
                "where id_visitor=id_client && isnull(close_date);"
        cursor.execute(query)

        i = 1

        order_totals.clear()
        order_no.clear()

        j = 0

        for item in cursor:
            item_group = QtWidgets.QGroupBox("Клиент: " + str(item[0]))
            categorieslayout = QtWidgets.QGridLayout(item_group)
            self.orderslayout.addWidget(item_group)
            item_group.clicked.connect(lambda: print(1))
            for value in item:
                value = str(value)
                if i == 2:
                    item_label = QtWidgets.QLabel("Клиент пришел: " + value)
                    categorieslayout.addWidget(item_label, 0, j, 1, 1)
                    j += 1
                if i == 3:
                    item_label = QtWidgets.QLabel("К оплате: " + value + "₽")
                    categorieslayout.addWidget(item_label, 0, j, 1, 1)
                    order_totals.append(item_label)
                    j += 1
                if i == 4:
                    order_number = value
                    j = 0
                    item_button = QtWidgets.QPushButton("Просмотреть")
                    categorieslayout.addWidget(item_button, 1, j, 1, 1)
                    j += 1
                    item_button.clicked.connect(lambda state, order=value: open_order(order))
                    order_no.append(value)
                    item_button = QtWidgets.QPushButton("Рассчитать")
                    categorieslayout.addWidget(item_button, 1, j, 1, 1)
                    j += 1
                    item_button.clicked.connect(lambda state, order=value: open_payments(order))
                if i == 5:
                    add_item = QtWidgets.QGroupBox()
                    layout = QtWidgets.QGridLayout(add_item)
                    query = "select content from order_content where id_order=%s and paid = 'No';"
                    data = (order_number,)
                    ccursor.execute(query, data)
                    k = 0
                    for citem in ccursor:
                        for cvalue in citem:
                            if cvalue == "Nintendo Switch":
                                layout.addWidget(create_icon('icons/switch'), 1, k, 1, 1)
                                k += 1
                            if cvalue == "Геймпад PS":
                                layout.addWidget(create_icon('icons/playstation'), 1, k, 1, 1)
                                k += 1
                            if cvalue == "Геймпад XBOX":
                                layout.addWidget(create_icon('icons/xbox'), 1, k, 1, 1)
                                k += 1
                            if cvalue == "Паспорт":
                                layout.addWidget(create_icon('icons/passport'), 1, k, 1, 1)
                                k += 1
                            if cvalue == "Права":
                                layout.addWidget(create_icon('icons/driver'), 1, k, 1, 1)
                                k += 1
                            if cvalue == "Настольная игра":
                                layout.addWidget(create_icon('icons/board'), 1, k, 1, 1)
                                k += 1
                    item_label = QtWidgets.QLabel("Комментарий: " + value)
                    if value != "None" and value != "" and value != " ":
                        layout.addWidget(item_label, 0, 0, 1, 1)

                    if layout.count() > 0:
                        categorieslayout.addWidget(add_item, 2, 0, 2, 2)

                    j += 1
                    i = 0
                i += 1
            j = 0

        def open_payments(order):
            global order_number
            order_number = int(order)

            w = PaymentWindow()
            my_thread = threading.Thread(target=w.exec_())
            my_thread.start()

            self.draw_orders()

        def open_order(order):
            global order_number
            order_number = int(order)

            w = OrderWindow()
            my_thread = threading.Thread(target=w.exec_())
            my_thread.start()
            self.draw_orders()

    def printX(self):

        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Чековый принтер не подключен")
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
        msgbox.setText('Проверьте подключение к чековому принтеру')
        msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        # msgbox.setDetailedText(str(e))
        msgbox.exec()

        '''
        query = "select sum(total) from orders;"
        cursor.execute(query)

        query = "select sum(total) from orders where type = %s;"
        data = ("Cash",)
        cursor.execute(query, data)
        data = ("Card",)
        cursor.execute(query, data)
        '''

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
                value = str(value)
                item_label = QtWidgets.QLabel(value)
                orderslayout.addWidget(item_label)

    def setupLoginUi(self):
        Main.setObjectName("Main")
        Main.resize(679, 357)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
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
        self.label_2.setText(_translate("Main", "Номер карты"))
        self.label_3.setText(_translate("Main", "Пароль"))
        self.pushButton.setText(_translate("Main", "Войти"))
        self.label.setText(_translate("Main", "Вход"))

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton.clicked.connect(self.login)

    def login(self):
        if self.lineEdit.text() != " " and self.lineEdit_2.text() != " " and self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
            card = self.lineEdit.text()
            password = self.lineEdit_2.text()

            query = "select pass from users where Card_num = %s;"
            data = (card,)
            cursor.execute(query, data)

            if cursor.rowcount == 0:
                Message.show(Message, "Ошибка", "Проверьте правильность введеных данных")

            for item in cursor:
                for value in item:
                    value = str(value)
                    if value == password:
                        self.openshift(card)
                    else:
                        Message.show(Message, "Ошибка", "Проверьте правильность введеных данных")
        else:
            Message.show(Message, "Ошибка", "Проверьте правильность введеных данных")

    def openshift(self, card):
        query = "select idshifts from shifts where shift_close_time is null && shift_open_time is not null into @l;"
        cursor.execute(query)

        query = "select if(@l is null,0,1);"
        cursor.execute(query)

        for item in cursor:
            for value in item:
                value = str(value)
                if value == "0":

                    query = "select idUsers from users where Card_num = %s;"
                    data = (card,)
                    cursor.execute(query, data)

                    for item in cursor:
                        for value in item:
                            value = str(value)
                            global id_user
                            id_user = value

                    query = "insert into shifts values (default, now(), null, %s, null, null, null, default);"
                    data = (value,)
                    cursor.execute(query, data)
                    cnx.commit()
                    self.setupUi()
                if value == "1":
                    self.setupUi()


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
            "Категория",
            "Код"
        ]

        draw_labels(labels, self.gridLayout_3, 1)

        query = "select * from products;"
        cursor.execute(query)
        j = 4
        k = 1
        for item in cursor:
            for value in item:
                value = str(value)
                if k == 1:
                    line_item = QtWidgets.QLineEdit(value)
                    self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                    id = value
                    line_item.textChanged.connect(
                        lambda state, line=[line_item, value, id, k]: modify(line, "product"))
                    k += 1
                    continue
                line_item = QtWidgets.QLineEdit(value)
                self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(
                    lambda state, line=[line_item, value, id, k]: modify(line, "product"))

                but_item = QtWidgets.QPushButton("Удалить")
                self.gridLayout_3.addWidget(but_item, j, 6, 1, 1)
                but_item.clicked.connect(lambda state, name=id: delete(name, "product"))

                k += 1
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
                value = str(value)
                if k == 0:
                    id = value
                    k += 1
                    continue
                if k != 3:
                    line_item = QtWidgets.QLineEdit(value)
                    self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                    line_item.textChanged.connect(
                        lambda state, line=[line_item, value, id, k]: modify(line, "client"))
                if k == 3:
                    line_item = QtWidgets.QLabel(value)
                    self.gridLayout_3.addWidget(line_item, j, k, 1, 1)

                k += 1
            but_item = QtWidgets.QPushButton("Удалить")
            self.gridLayout_3.addWidget(but_item, j, 7, 1, 1)
            but_item.clicked.connect(lambda state, row=id: delete(row, "client"))
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
                value = str(value)
                if k == 0:
                    k += 1
                    but_item = QtWidgets.QPushButton("Удалить")
                    self.gridLayout_3.addWidget(but_item, j, 5, 1, 1)
                    id = value
                    but_item.clicked.connect(lambda state, row=value: delete(row, "user"))
                    continue
                line_item = QtWidgets.QLineEdit(value)
                self.gridLayout_3.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=[line_item, value, id, k]: modify(line, "user"))

                k += 1
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
                query = "delete from clients where id_client=%s;"
                cursor.execute(query, (data,))
                cnx.commit()
            if type == "product":
                query = "delete from products where products =%s;"
                cursor.execute(query, (data,))
                cnx.commit()
            Message.show(Message, "Инфо", "Удалено успешно")
            self.retranslateAdminUi()

    def setupproductUi(self):
        w = AddItemWindow()
        my_thread = threading.Thread(target=w.exec_())
        my_thread.start()

        self.retranslateAdminUi()

    def setupworkUi(self):
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

    # noinspection PyShadowingNames,PyShadowingNames,PyShadowingNames,PyShadowingNames
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


class AddItemWindowUi(object):
    def setupUi(self, AddItemWindowUi):
        AddItemWindowUi.setObjectName("AddItemWindowUi")
        AddItemWindowUi.resize(570, 105)
        self.gridLayout = QtWidgets.QGridLayout(AddItemWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.barcodeedit = QtWidgets.QLineEdit(AddItemWindowUi)
        self.barcodeedit.setObjectName("barcodeedit")
        self.gridLayout.addWidget(self.barcodeedit, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(AddItemWindowUi)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.addbutton = QtWidgets.QPushButton(AddItemWindowUi)
        self.addbutton.setObjectName("addbutton")
        self.gridLayout.addWidget(self.addbutton, 2, 0, 1, 5)
        self.label = QtWidgets.QLabel(AddItemWindowUi)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.costedit = QtWidgets.QLineEdit(AddItemWindowUi)
        self.costedit.setObjectName("costedit")
        self.gridLayout.addWidget(self.costedit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddItemWindowUi)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.productedit = QtWidgets.QLineEdit(AddItemWindowUi)
        self.productedit.setObjectName("productedit")
        self.gridLayout.addWidget(self.productedit, 1, 0, 1, 1)
        self.amountedit = QtWidgets.QLineEdit(AddItemWindowUi)
        self.amountedit.setObjectName("amountedit")
        self.gridLayout.addWidget(self.amountedit, 1, 2, 1, 1)
        self.categoryedit = QtWidgets.QLineEdit(AddItemWindowUi)
        self.categoryedit.setObjectName("categoryedit")
        self.gridLayout.addWidget(self.categoryedit, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(AddItemWindowUi)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(AddItemWindowUi)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.retranslateUi(AddItemWindowUi)
        QtCore.QMetaObject.connectSlotsByName(AddItemWindowUi)

    def retranslateUi(self, AddItemWindowUi):
        _translate = QtCore.QCoreApplication.translate
        AddItemWindowUi.setWindowTitle(_translate("AddItemWindowUi", "Добавление товара"))
        self.label_5.setText(_translate("AddItemWindowUi", "Штрихкод"))
        self.addbutton.setText(_translate("AddItemWindowUi", "Добавить"))
        self.label.setText(_translate("AddItemWindowUi", "Название позиции"))
        self.label_2.setText(_translate("AddItemWindowUi", "Цена"))
        self.label_4.setText(_translate("AddItemWindowUi", "Категория"))
        self.label_3.setText(_translate("AddItemWindowUi", "Количество"))

        self.addbutton.clicked.connect(self.writeproduct)

    def writeproduct(self):
        query = "insert into products values(%s, %s, %s, %s, %s);"
        data = (self.productedit.text(), self.costedit.text(), self.amountedit.text(), self.categoryedit.text(),
                self.barcodeedit.text())
        cursor.execute(query, data)
        cnx.commit()
        # AddItemWindow.accept()


class AddItemWindow(QtWidgets.QDialog, AddItemWindowUi):
    def __init__(self, parent=None):
        super(AddItemWindow, self).__init__(parent)
        self.setupUi(self)


class NewOrderWindowUi(object):
    def setupUi(self, NewOrderWindowUi):
        NewOrderWindowUi.setObjectName("NewOrderWindowUi")
        NewOrderWindowUi.resize(700, 700)
        self.gridLayout = QtWidgets.QGridLayout(NewOrderWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(NewOrderWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.scanitembutton = QtWidgets.QPushButton(NewOrderWindowUi)
        self.scanitembutton.setObjectName("scanitembutton")
        self.gridLayout.addWidget(self.scanitembutton, 4, 0, 1, 2)
        self.OrderBox = QtWidgets.QGroupBox(NewOrderWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.OrderBox.sizePolicy().hasHeightForWidth())
        self.OrderBox.setSizePolicy(sizePolicy)
        self.OrderBox.setObjectName("OrderBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.OrderBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.OrderBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 166, 130))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.OrderBox, 1, 1, 1, 1)
        self.createbutton = QtWidgets.QPushButton(NewOrderWindowUi)
        self.createbutton.setObjectName("createbutton")
        self.gridLayout.addWidget(self.createbutton, 6, 0, 1, 2)
        self.scanbutton = QtWidgets.QPushButton(NewOrderWindowUi)
        self.scanbutton.setObjectName("scanbutton")
        self.gridLayout.addWidget(self.scanbutton, 3, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(NewOrderWindowUi)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(NewOrderWindowUi)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.retranslateUi(NewOrderWindowUi)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NewOrderWindowUi)

    def retranslateUi(self, NewOrderWindowUi):
        _translate = QtCore.QCoreApplication.translate
        NewOrderWindowUi.setWindowTitle(_translate("NewOrderWindowUi", "Новый заказ"))
        self.scanitembutton.setText(_translate("NewOrderWindowUi", "Сканировать товар"))
        self.OrderBox.setTitle(_translate("NewOrderWindowUi", "Заказ"))
        self.createbutton.setText(_translate("NewOrderWindowUi", "Создать "))
        self.scanbutton.setText(_translate("NewOrderWindowUi", "Сканировать карту гостя"))
        self.scanbutton.clicked.connect(self.scanGuest)
        self.label.setText(_translate("NewOrderWindowUi", "Комментарий"))
        order = []

        query = "select distinct product_category from products"
        cursor.execute(query)
        for item in cursor:
            for value in item:
                value = str(value)
                tab = QtWidgets.QWidget()
                tab.setObjectName("tab")
                self.tabWidget.addTab(tab, value)
                tab_layout = QtWidgets.QVBoxLayout()
                tab.setLayout(tab_layout)
                query = "select products from products where product_category=%s;"
                data = (value,)
                bcursor.execute(query, data)
                for response in bcursor:
                    for result in response:
                        result = str(result)
                        item_button = QtWidgets.QPushButton(result)
                        item_button.setObjectName("item_button")
                        tab_layout.addWidget(item_button)
                        item_button.clicked.connect(lambda state, button=item_button: select_item(button))

        def select_item(button):
            try:
                order.append(button.text())
            except AttributeError:
                order.append(button)
            draw_order()

        def draw_order():

            total = 0

            for i in reversed(range(self.gridLayout_3.count())):
                self.gridLayout_3.itemAt(i).widget().deleteLater()

            i = 0
            for pos in order:
                item_button = QtWidgets.QPushButton(pos)
                item_button.setObjectName("order_item")
                self.gridLayout_3.addWidget(item_button, i, 0, 1, 1)
                delete_button = QtWidgets.QPushButton()
                delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
                delete_button.setIconSize(QtCore.QSize(24, 24))
                self.gridLayout_3.addWidget(delete_button, i, 2, 1, 1)
                delete_button.clicked.connect(lambda state, data=pos: pop_item(data))

                percent = 0

                query = "select Client_lvl from clients where id_client=%s;"
                global guest_number
                cursor.execute(query, (guest_number,))
                for item in cursor:
                    for value in item:
                        value = int(value)
                        if value == 1:
                            percent = 5
                        if value == 2:
                            percent = 10
                        if value == 3:
                            percent = 15

                query = "select Product_cost from products where products=%s;"
                cdata = (pos,)
                ccursor.execute(query, cdata)
                for citem in ccursor:
                    for cvalue in citem:
                        label = QtWidgets.QLabel(str(int(int(cvalue) - (int(cvalue) / 100 * percent))) + "₽")
                        label.setObjectName("cost")
                        self.gridLayout_3.addWidget(label, i, 1, 1, 1)
                        total += cvalue
                        font = QtGui.QFont()
                        font.setPointSize(20)
                        total_item = QtWidgets.QLabel("Итог " + str(total) + "₽")
                        total_item.setObjectName("total_label")
                        total_item.setFont(font)
                        self.gridLayout_3.addWidget(total_item, i + 1, 0, 1, 1)
                i += 1

        def create_order():
            if len(order) == 0:
                pass
            else:
                global guest_number

                data = (guest_number,)

                query = "insert into orders values (default,now(),null,null,228,null,%s,null);"
                cursor.execute(query, data)
                cnx.commit()
                query = "select no_orders from orders order by no_orders desc limit 1;"
                cursor.execute(query)
                for result in cursor:
                    for value in result:
                        value = str(value)
                        number = value
                for item in order:
                    query = '''
                    insert into order_content values(%s,%s, default,curtime(), 'no', default,
                    (select round(product_cost/100*(100-(select if(client_lvl=3,15,if(client_lvl=2,10,if(client_lvl=1,5,0)))
                    from clients,orders 
                    where id_client=id_visitor && no_orders=%s))) from products where products=%s));
                    '''
                    data = (number, item, number, item)
                    cursor.execute(query, data)
                    cnx.commit()
                query = "update orders set comments=%s where no_orders=%s;"
                data = (self.lineEdit.text(), number)
                cursor.execute(query, data)
                cnx.commit()
                Message.show(Message, "Инфо", "Заказ добавлен")
                guest_number = 123

                OrderTotalThread()

                NewOrderWindowUi.accept()

        def pop_item(item):
            order.pop(order.index(item))
            draw_order()

        def scanItem():

            text, ok = QtWidgets.QInputDialog.getText(self, 'Сканируйте товар',
                                                      'Код:')

            if ok and text != "" and text != " ":
                query = "select Products from products where Code = %s"
                data = (text,)
                cursor.execute(query, data)
                for item in cursor:
                    for value in item:
                        value = str(value)
                        select_item(value)

        self.createbutton.clicked.connect(create_order)
        self.scanitembutton.clicked.connect(scanItem)


    def scanGuest(self):

        text, ok = QtWidgets.QInputDialog.getText(self, 'Сканируйте карту пользователя',
                                                  'Номер карты:')

        if ok and text != "" and text != " ":
            global guest_number
            guest_number = text
            w = GuestWindow()
            w.exec_()
            guest_number = guest_number


class NewOrderWindow(QtWidgets.QDialog, NewOrderWindowUi):
    def __init__(self, parent=None):
        super(NewOrderWindow, self).__init__(parent)
        self.setupUi(self)


class PaymentWindowUi(object):
    def setupUi(self, PaymentWindowUi):
        PaymentWindowUi.setObjectName("PaymentWindowUi")
        PaymentWindowUi.resize(665, 405)
        self.gridLayout = QtWidgets.QGridLayout(PaymentWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.precheckbutton = QtWidgets.QPushButton(PaymentWindowUi)
        self.precheckbutton.setObjectName("precheckbutton")
        self.gridLayout.addWidget(self.precheckbutton, 10, 0, 1, 3)
        self.couponsbutton = QtWidgets.QPushButton(PaymentWindowUi)
        self.couponsbutton.setObjectName("couponsbutton")
        self.gridLayout.addWidget(self.couponsbutton, 7, 2, 1, 1)
        self.paymentbutton = QtWidgets.QPushButton(PaymentWindowUi)
        self.paymentbutton.setObjectName("paymentbutton")
        self.gridLayout.addWidget(self.paymentbutton, 9, 0, 1, 3)
        self.inputlabel = QtWidgets.QLabel(PaymentWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputlabel.sizePolicy().hasHeightForWidth())
        self.inputlabel.setSizePolicy(sizePolicy)
        self.inputlabel.setObjectName("inputlabel")
        self.gridLayout.addWidget(self.inputlabel, 5, 0, 1, 1)
        self.paymentbox = QtWidgets.QComboBox(PaymentWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paymentbox.sizePolicy().hasHeightForWidth())
        self.paymentbox.setSizePolicy(sizePolicy)
        self.paymentbox.setObjectName("paymentbox")
        self.paymentbox.addItem("")
        self.paymentbox.addItem("")
        self.paymentbox.addItem("")
        self.paymentbox.addItem("")
        self.gridLayout.addWidget(self.paymentbox, 4, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(PaymentWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(PaymentWindowUi)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 460, 263))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.groupBox, 3, 2, 4, 1)
        self.clientcashlabel = QtWidgets.QLabel(PaymentWindowUi)
        self.clientcashlabel.setObjectName("clientcashlabel")
        self.gridLayout.addWidget(self.clientcashlabel, 3, 0, 1, 2)
        self.refundlabel = QtWidgets.QLabel(PaymentWindowUi)
        self.refundlabel.setObjectName("refundlabel")
        self.gridLayout.addWidget(self.refundlabel, 6, 0, 1, 2)

        self.retranslateUi(PaymentWindowUi)
        QtCore.QMetaObject.connectSlotsByName(PaymentWindowUi)

    def retranslateUi(self, PaymentWindowUi):

        global order_number

        self.part = []
        self.no_s = []

        _translate = QtCore.QCoreApplication.translate
        PaymentWindowUi.setWindowTitle(_translate("PaymentWindowUi", "Оплата"))
        self.precheckbutton.setText(_translate("PaymentWindowUi", "Пречек"))
        self.couponsbutton.setText(_translate("PaymentWindowUi", "Купоны"))
        self.paymentbutton.setText(_translate("PaymentWindowUi", "Оплата"))
        self.inputlabel.setText(_translate("PaymentWindowUi", "Внесено"))
        self.paymentbox.setItemText(0, _translate("PaymentWindowUi", "Тип оплаты"))
        self.paymentbox.setItemText(1, _translate("PaymentWindowUi", "Счет"))
        self.paymentbox.setItemText(2, _translate("PaymentWindowUi", "Наличные"))
        self.paymentbox.setItemText(3, _translate("PaymentWindowUi", "Безналичные"))
        self.groupBox.setTitle(_translate("PaymentWindowUi", "Заказ"))
        self.clientcashlabel.setText(_translate("PaymentWindowUi", "На счете клиента"))
        self.refundlabel.setText(_translate("PaymentWindowUi", "Сдача"))

        self.paymentbox.currentIndexChanged.connect(self.updatechange)

        query = "select client_cash from clients,orders where id_visitor=id_client && no_orders=%s;"
        data = (order_number,)
        cursor.execute(query, data)

        for item in cursor:
            for value in item:
                value = str(value)
                self.client_cash = value
                self.clientcashlabel.setText(_translate("PaymentWindowUi", "На счете клиента " + value))

        self.refundlabel.setText(_translate("PaymentWindowUi", "Сдача"))

        self.paymentbutton.clicked.connect(self.pay)
        self.lineEdit.textChanged.connect(self.updatechange)

        self.paymentbutton.setEnabled(False)

        query = "select no, content from order_content where id_order=%s and paid = 'No';"
        data = (order_number,)
        cursor.execute(query, data)

        i = 0
        for item in cursor:
            for value in item:
                if isinstance(value, int):
                    no = str(value)
                    continue
                value = str(value)
                order_item = QtWidgets.QCheckBox(value)
                self.gridLayout_2.addWidget(order_item, i, 0, 1, 1)
                query = "select price from order_content where no=%s;"
                cdata = (no,)
                ccursor.execute(query, cdata)
                for citem in ccursor:
                    for cvalue in citem:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel(str(cvalue) + '₽'), i, 1, 1, 1)
                order_item.stateChanged.connect(
                    lambda state, line=[value, order_item, cvalue, no]: part_pay(line))
            i += 1

        def part_pay(item):
            self.value = 0
            if item[1].isChecked():
                if (item[3]) not in self.no_s:
                    self.part.append(item[0])
                    self.no_s.append(item[3])
                value = 0
                for item in self.no_s:
                    query = "select price from order_content where no=%s;"
                    cdata = (item,)
                    ccursor.execute(query, cdata)
                    for citem in ccursor:
                        for cvalue in citem:
                            value += int(cvalue)

                total_item.setText("К оплате " + str(value) + "₽")
                self.value = value

            self.updatechange()

        query = "SELECT total FROM orders WHERE No_orders = %s;"
        data = (order_number,)
        cursor.execute(query, data)

        for item in cursor:
            for value in item:
                value = str(value)
                font = QtGui.QFont()
                font.setPointSize(20)
                total_item = QtWidgets.QLabel("К оплате " + value + "₽")
                total_item.setFont(font)
                self.gridLayout_2.addWidget(total_item, i, 0, 1, 1)
                self.value = value

    def updatechange(self):
        try:
            if self.lineEdit.text() != "" and self.lineEdit.text() != " " and (
                    int(self.lineEdit.text()) - int(self.value)) > 0:
                self.refundlabel.setText("Cдача " + str(int(self.lineEdit.text()) - int(self.value)) + "₽")
            else:
                self.refundlabel.setText("Cдача 0₽")
        except ValueError:
            self.refundlabel.setText("Некорректный ввод")
        try:
            if float(self.lineEdit.text()) - int(self.value) >= 0 and self.paymentbox.currentIndex() != 0:
                self.paymentbutton.setEnabled(True)
            else:
                self.paymentbutton.setEnabled(False)
        except ValueError:
            self.paymentbutton.setEnabled(False)
            self.refundlabel.setText("Cдача 0₽")

    def pay(self):
        if len(self.part) == 0:
            global order_number
            if float(self.value) <= float(self.lineEdit.text()) and self.paymentbox.currentIndex() != 0:
                if self.paymentbox.currentIndex() == 1:
                    if int(self.client_cash) >= int(self.value):
                        query = "update orders set close_date=now(),Type='Account' where no_orders=%s;"

                    else:
                        Message.show(Message, "Информация", "На счете клиента недостаточно средств")
                        return 0
                if self.paymentbox.currentIndex() == 2:
                    query = "update orders set close_date=now(),Type='Cash' where no_orders=%s;"
                if self.paymentbox.currentIndex() == 3:
                    query = "update orders set close_date=now(),Type='Card' where no_orders=%s;"

                data = (order_number,)
                cursor.execute(query, data)
                cnx.commit()
                query = "update order_content set paid='Yes' where id_order=%s;"
                cursor.execute(query, data)
                cnx.commit()

                if self.paymentbox.currentIndex() == 1:
                    if int(self.client_cash) >= int(self.value):
                        query = "update clients set client_cash=client_cash-%s where id_client=(select id_client from orders where no_orders=%s);"
                        data = (self.value, order_number)
                        cursor.execute(query, data)

                Message.show(Message, "Инфо", "Оплата внесена \n" + self.refundlabel.text())

                def close():
                    PaymentWindow.accept()

                # close()

                # TODO: Закрытие окна после вывода инфо
        else:
            for no in self.no_s:
                if float(self.value) <= float(self.lineEdit.text()) and self.paymentbox.currentIndex() != 0:
                    if self.paymentbox.currentIndex() == 1:
                        if int(self.client_cash) >= int(self.value):
                            query = "update order_content set paid='Yes',type='Account' where no=%s;"
                        else:
                            Message.show(Message, "Информация", "На счете клиента недостаточно средств")
                            return 0
                    if self.paymentbox.currentIndex() == 2:
                        query = "update order_content set paid='Yes',type = 'Cash' where no=%s;"
                    if self.paymentbox.currentIndex() == 3:
                        query = "update order_content set paid='Yes',type = 'Card' where no=%s;"
                    data = (no,)
                    cursor.execute(query, data)
                    cnx.commit()

                    if self.paymentbox.currentIndex() == 1:
                        if int(self.client_cash) >= int(self.value):
                            query = "update clients set client_cash=client_cash-%s where id_client=(select id_client from orders where no_orders=%s);"
                            data = (self.value, order_number)
                            cursor.execute(query, data)

                    Message.show(Message, "Инфо", "Оплата внесена \n" + self.refundlabel.text())


class PaymentWindow(QtWidgets.QDialog, PaymentWindowUi):
    def __init__(self, parent=None):
        super(PaymentWindow, self).__init__(parent)
        self.setupUi(self)


class OrderWindowUi(object):
    def setupUi(self, OrderWindowUi):
        OrderWindowUi.setObjectName("OrderWindowUi")
        OrderWindowUi.resize(700, 700)
        self.gridLayout = QtWidgets.QGridLayout(OrderWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(OrderWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.scanitembutton = QtWidgets.QPushButton(OrderWindowUi)
        self.scanitembutton.setObjectName("scanitembutton")
        self.gridLayout.addWidget(self.scanitembutton, 3, 0, 1, 2)
        self.OrderBox = QtWidgets.QGroupBox(OrderWindowUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.OrderBox.sizePolicy().hasHeightForWidth())
        self.OrderBox.setSizePolicy(sizePolicy)
        self.OrderBox.setObjectName("OrderBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.OrderBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.OrderBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 166, 130))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.OrderBox, 1, 1, 1, 1)
        self.createbutton = QtWidgets.QPushButton(OrderWindowUi)
        self.createbutton.setObjectName("createbutton")
        self.gridLayout.addWidget(self.createbutton, 5, 0, 1, 2)
        self.openguestbutton = QtWidgets.QPushButton(OrderWindowUi)
        self.openguestbutton.setObjectName("openguestbutton")
        self.gridLayout.addWidget(self.openguestbutton, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(OrderWindowUi)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(OrderWindowUi)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.guestlabel = QtWidgets.QLabel(OrderWindowUi)
        self.guestlabel.setObjectName("guestlabel")
        self.gridLayout.addWidget(self.guestlabel, 0, 0, 1, 1)

        self.retranslateUi(OrderWindowUi)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OrderWindowUi)

    def retranslateUi(self, OrderWindowUi):
        global order_number

        order = []
        new_items = []

        _translate = QtCore.QCoreApplication.translate
        OrderWindowUi.setWindowTitle(_translate("OrderWindowUi", "Заказ " + str(order_number)))
        self.scanitembutton.setText(_translate("OrderWindowUi", "Сканировать товар"))
        self.OrderBox.setTitle(_translate("OrderWindowUi", "Заказ"))
        self.createbutton.setText(_translate("OrderWindowUi", "Сохранить"))
        self.openguestbutton.setText(_translate("OrderWindowUi", "Открыть карту гостя"))
        self.label.setText(_translate("OrderWindowUi", "Комментарий"))

        # TODO Получение имени клиента
        self.guestlabel.setText(_translate("OrderWindowUi", "Гость"))

        def update_comment():
            global order_number

            comment = self.lineEdit.text()
            data = (comment, order_number)
            query = "update orders set comments=%s where no_orders=%s;"
            cursor.execute(query, data)
            cnx.commit()

        def update_order():
            for item in new_items:
                query = '''
                                    insert into order_content values(%s,%s, default,curtime(), 'no', default,
                                    (select round(product_cost/100*(100-(select if(client_lvl=3,15,if(client_lvl=2,10,if(client_lvl=1,5,0)))
                                    from clients,orders 
                                    where id_client=id_visitor && no_orders=%s))) from products where products=%s));
                        '''
                data = (order_number, item, order_number, item)
                cursor.execute(query, data)
                cnx.commit()

            try:
                special_cursor = ccursor

                special_cursor.execute(
                    "select no from order_content,products where paid='No' && content=products && product_category='Тарифы';")

                data = []

                for item in special_cursor:
                    for value in item:
                        data.append(value)

                for value in data:
                    data = (str(value),)
                    query = "select round((price/60) * (UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(times))/60) from order_content where no=%s into @j;"
                    special_cursor.execute(query, data)
                    query = "select stop_check from products,order_content where products=content && no=%s into @f;"
                    special_cursor.execute(query, data)
                    query = "update order_content set price=(if(@j<price,price,if(@j>@f,@f,@j))) where no=%s;"
                    special_cursor.execute(query, data)
                    cnx.commit()

            except EnvironmentError as e:
                print(e)
                pass

            try:

                special_cursor = bcursor

                for no in order_no:
                    data = (no, no)
                    query = 'update orders set total=(select sum(price) from order_content where id_order=%s && paid="no") where no_orders=%s ;'
                    special_cursor.execute(query, data)

                    cnx.commit()

                ui.draw_orders()

            except BaseException as e:
                print(str(e))
                pass

            OrderWindowUi.accept()

        self.createbutton.setEnabled(False)
        self.createbutton.clicked.connect(update_order)
        self.lineEdit.textChanged.connect(update_comment)

        query = "select comments from orders where no_orders = %s;"
        data = (order_number,)
        bcursor.execute(query, data)
        for item in bcursor:
            for value in item:
                self.lineEdit.setText(str(value))

        query = "select distinct product_category from products;"
        cursor.execute(query)
        for item in cursor:
            for value in item:
                value = str(value)
                tab = QtWidgets.QWidget()
                self.tabWidget.addTab(tab, value)
                tab_layout = QtWidgets.QVBoxLayout()
                tab.setLayout(tab_layout)
                query = "select products from products where product_category=%s;"
                data = (value,)
                bcursor.execute(query, data)
                for response in bcursor:
                    for result in response:
                        result = str(result)
                        item_button = QtWidgets.QPushButton(result)
                        tab_layout.addWidget(item_button)
                        item_button.clicked.connect(lambda state, button=item_button: select_item(button))

        query = "select content from order_content where id_order=%s;"
        data = (order_number,)
        cursor.execute(query, data)

        i = 0
        for item in cursor:
            for value in item:
                value = str(value)
                order_item = QtWidgets.QPushButton(value)
                self.gridLayout_3.addWidget(order_item, i, 0, 1, 1)
                order.append(value)
                query = "select Product_cost from products where products=%s;"
                cdata = (value,)
                ccursor.execute(query, cdata)
                for citem in ccursor:
                    for cvalue in citem:
                        self.gridLayout_3.addWidget(QtWidgets.QLabel(str(cvalue) + "₽"), i, 1, 1, 1)
            i += 1

        query = "SELECT total FROM orders WHERE No_orders = %s;"
        data = (order_number,)
        cursor.execute(query, data)

        for item in cursor:
            for value in item:
                value = str(value)
                font = QtGui.QFont()
                font.setPointSize(20)
                total_item = QtWidgets.QLabel("Итог " + value + "₽")
                total_item.setFont(font)
                self.gridLayout_3.addWidget(total_item, i, 0, 1, 1)

        def select_item(button):
            try:
                new_items.append(button.text())
            except AttributeError:
                new_items.append(button)

            draw_order()

            self.createbutton.setEnabled(True)

        def draw_order():
            total = 0

            for i in reversed(range(self.gridLayout_3.count())):
                self.gridLayout_3.itemAt(i).widget().deleteLater()

            i = 0

            for item in new_items:
                item_button = QtWidgets.QPushButton(item)
                self.gridLayout_3.addWidget(item_button, i, 0, 1, 1)
                delete_button = QtWidgets.QPushButton()
                delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
                delete_button.setIconSize(QtCore.QSize(24, 24))
                self.gridLayout_3.addWidget(delete_button, i, 2, 1, 1)
                delete_button.clicked.connect(lambda state, data=item: pop_item(data))
                query = "select Product_cost from products where products=%s;"
                cdata = (item,)
                ccursor.execute(query, cdata)
                for citem in ccursor:
                    for cvalue in citem:
                        total += cvalue
                        self.gridLayout_3.addWidget(QtWidgets.QLabel(str(cvalue) + "₽"), i, 1, 1, 1)
                i += 1

            for item in order:
                item_button = QtWidgets.QPushButton(item)
                self.gridLayout_3.addWidget(item_button, i, 0, 1, 1)
                query = "select Product_cost from products where products=%s;"
                cdata = (item,)
                ccursor.execute(query, cdata)
                for citem in ccursor:
                    for cvalue in citem:
                        self.gridLayout_3.addWidget(QtWidgets.QLabel(str(cvalue) + "₽"), i, 1, 1, 1)
                        total += cvalue
                        font = QtGui.QFont()
                        font.setPointSize(20)
                        total_item = QtWidgets.QLabel("Итог " + str(total) + "₽")
                        total_item.setFont(font)
                        self.gridLayout_3.addWidget(total_item, i + 1, 0, 1, 1)
                i += 1

        def pop_item(item):
            try:
                new_items.pop(new_items.index(item))
            except ValueError:
                Message.show(Message, "Инфо", "Невозможно удалить позицию внесенную ранее")
            draw_order()

        def scanItem(self):
            text, ok = QtWidgets.QInputDialog.getText(self, 'Сканируйте товар',
                                                      'Код:')
            if ok and text != "" and text != " ":
                query = "select Products from products where Code = %s"
                data = (text,)
                cursor.execute(query, data)
                for item in cursor:
                    for value in item:
                        value = str(value)
                        select_item(value)

        self.scanitembutton.clicked.connect(scanItem)


class OrderWindow(QtWidgets.QDialog, OrderWindowUi):
    def __init__(self, parent=None):
        super(OrderWindow, self).__init__(parent)
        self.setupUi(self)


class GuestWindowUi(object):
    def setupUi(self, GuestWindowUi):
        GuestWindowUi.setObjectName("GuestWindowUi")
        GuestWindowUi.resize(408, 300)
        self.gridLayout = QtWidgets.QGridLayout(GuestWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(GuestWindowUi)
        self.tabWidget.setObjectName("tabWidget")
        self.profiletab = QtWidgets.QWidget()
        self.profiletab.setObjectName("profiletab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.profiletab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget.addTab(self.profiletab, "")

        self.historytab = QtWidgets.QWidget()
        self.historytab.setObjectName("historytab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.historytab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget.addTab(self.historytab, "")

        self.scrollArea = QtWidgets.QScrollArea(self.historytab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 460, 263))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea)


        self.recomendationtab = QtWidgets.QWidget()
        self.recomendationtab.setObjectName("recomendationtab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.recomendationtab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget.addTab(self.recomendationtab, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.guestlabel = QtWidgets.QLabel(GuestWindowUi)
        self.guestlabel.setObjectName("guestlabel")
        self.gridLayout.addWidget(self.guestlabel, 0, 0, 1, 1)
        self.acceptbutton = QtWidgets.QPushButton(GuestWindowUi)
        self.acceptbutton.setObjectName("acceptbutton")
        self.gridLayout.addWidget(self.acceptbutton, 2, 0, 1, 1)

        self.retranslateUi(GuestWindowUi)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GuestWindowUi)

    def retranslateUi(self, GuestWindowUi):
        _translate = QtCore.QCoreApplication.translate
        GuestWindowUi.setWindowTitle(_translate("GuestWindowUi", "Карточка гостя"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profiletab),
                                  _translate("GuestWindowUi", "Карточка Гостя"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.historytab),
                                  _translate("GuestWindowUi", "История заказов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recomendationtab),
                                  _translate("GuestWindowUi", "Рекомендации"))

        def acceptance():

            global guest_number

            query = "select id_client from clients where Card_Num_client = %s"
            data = (guest_number,)
            cursor.execute(query, data)
            for item in cursor:
                for value in item:
                    value = str(value)
                    guest_number = value

            GuestWindowUi.done(1)

        self.acceptbutton.setText(_translate("GuestWindowUi", "Подтвердить"))
        self.acceptbutton.clicked.connect(acceptance)

        global guest_number

        self.guestlabel.setText(_translate("GuestWindowUi", "Гость " + str(guest_number)))

        query = "select * from clients where Card_Num_client  = %s"
        data = (guest_number,)
        cursor.execute(query, data)

        i = 0

        for item in cursor:
            for value in item:
                value = str(value)
                if value == "None":
                    value = "Не указано"
                if i == 0:
                    i += 1
                    continue
                if i == 1:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Имя " + value), i, 1, 1, 1)
                if i == 2:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Номер карты " + value), i, 1, 1, 1)
                if i == 3:
                    i += 1
                    continue
                if i == 4:
                    i += 1
                    continue
                    # TODO отображение фото
                if i == 5:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Уровень привелегий " + value), i, 1, 1, 1)
                if i == 6:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Телефон " + value), i, 1, 1, 1)
                if i == 7:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Сумма на счете " + value), i, 1, 1, 1)
                if i == 8:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("День Рождения " + value), i, 1, 1, 1)
                if i == 9:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Соцсети " + value), i, 1, 1, 1)
                if i == 10:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Дополнительно " + value), i, 1, 1, 1)

                i += 1

        def draw_history():

            for i in reversed(range(self.scrollLayout.count())):
                self.scrollLayout.itemAt(i).widget().deleteLater()

            i = 0
            query = "select NO_Orders, Open_date, Owner, Type, Comments from orders where Id_visitor in (select id_client from clients where Card_Num_client = %s)"
            data = (guest_number,)
            cursor.execute(query, data)

            j = 0

            for item in cursor:
                for value in item:
                    value = str(value)
                    if value == "None":
                        continue
                    else:
                        if j == 0:
                            self.scrollLayout.addWidget(QtWidgets.QLabel("Номер заказа " + value), i, 1, 1, 1)
                            order = value
                        if j == 1:
                            self.scrollLayout.addWidget(QtWidgets.QLabel("Дата и время открытия " + value), i, 1, 1, 1)
                        if j == 2:
                            self.scrollLayout.addWidget(QtWidgets.QLabel("Администратор " + value), i, 1, 1, 1)
                        if j == 3:
                            self.scrollLayout.addWidget(QtWidgets.QLabel("Тип оплаты " + value), i, 1, 1, 1)
                        if j == 4:
                            self.scrollLayout.addWidget(QtWidgets.QLabel("Комментарий" + value), i, 1, 1, 1)
                        j += 1
                        i += 1
                button = QtWidgets.QPushButton("Просмотреть")
                button.clicked.connect(lambda state, order_no=order: draw_order(order_no))
                self.scrollLayout.addWidget(button, i - 1, 2, 1, 1)
                j = 0

        draw_history()

        def draw_order(id):

            for i in reversed(range(self.scrollLayout.count())):
                self.scrollLayout.itemAt(i).widget().deleteLater()

            query = "select Content from order_content where id_Order = %s"
            data = ((id),)
            cursor.execute(query, data)

            i = 0

            for item in cursor:
                for value in item:
                    self.scrollLayout.addWidget(QtWidgets.QLabel(value), i, 1, 1, 1)
                    i += 1

                button = QtWidgets.QPushButton("Вернуться")
                button.clicked.connect(draw_history)
                self.scrollLayout.addWidget(button, i + 1, 1, 1, 1)


class GuestWindow(QtWidgets.QDialog, GuestWindowUi):
    def __init__(self, parent=None):
        super(GuestWindow, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        global guest_number
        guest_number = 1488
        event.accept()


class NotificationsWindowUi(object):
    def setupUi(self, NotificationsWindowUi):
        NotificationsWindowUi.setObjectName("NotificationsWindowUi")
        NotificationsWindowUi.resize(700, 300)
        self.gridLayout = QtWidgets.QGridLayout(NotificationsWindowUi)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(NotificationsWindowUi)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 251))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.createactionbutton = QtWidgets.QPushButton(NotificationsWindowUi)
        self.createactionbutton.setObjectName("createactionbutton")
        self.gridLayout.addWidget(self.createactionbutton, 1, 0, 1, 1)

        self.retranslateUi(NotificationsWindowUi)
        QtCore.QMetaObject.connectSlotsByName(NotificationsWindowUi)

    def retranslateUi(self, NotificationsWindowUi):
        _translate = QtCore.QCoreApplication.translate
        NotificationsWindowUi.setWindowTitle(_translate("NotificationsWindowUi", "Уведомления"))
        self.createactionbutton.setText(_translate("NotificationsWindowUi", "Создать напоминание"))

        def draw_notifications():

            for i in reversed(range(self.gridLayout_2.count())):
                self.gridLayout_2.itemAt(i).widget().deleteLater()

            i = 0
            j = 0

            labels = ['Cодержимое', 'Приоритет', 'Дата и Время активации', 'Статус']
            for label in labels:
                self.gridLayout_2.addWidget(QtWidgets.QLabel(label), i, j, 1, 1)
                j += 1

            i += 1
            j = 0

            query = "select * from notifications order by not_stat,importance ,dates;"
            cursor.execute(query)
            for item in cursor:
                for value in item:
                    if j == 0:
                        j += 1
                        id = value
                        continue
                    if j == 4:
                        value = str(list(value)[0])
                        self.gridLayout_2.addWidget(QtWidgets.QLabel(value), i, j - 1, 1, 1)
                        j += 1
                        continue
                    value = str(value)
                    self.gridLayout_2.addWidget(QtWidgets.QLabel(value), i, j - 1, 1, 1)
                    j += 1
                button = QtWidgets.QPushButton("Закрыть")
                self.gridLayout_2.addWidget(button, i, j, 1, 1)
                button.clicked.connect(lambda state, row=id: close(row))
                i += 1
                j = 0

            def close(id):
                query = "update notifications set not_stat='Закрыт' where id_not=%s"
                data = (id,)
                cursor.execute(query, data)
                cnx.commit()
                draw_notifications()

        draw_notifications()


class NotificationsWindow(QtWidgets.QDialog, NotificationsWindowUi):
    def __init__(self, parent=None):
        super(NotificationsWindow, self).__init__(parent)
        self.setupUi(self)


class Message(object):
    def show(self, Title, Text):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(Title)
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/i.png')))
        msgbox.setText(Text)
        msgbox.exec()

    def notify(self, no):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Уведомление")
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/remind.png')))
        query = "select content from notifications where id_not = %s"
        data = (no,)
        ccursor.execute(query, data)
        for item in ccursor:
            for value in item:
                msgbox.setText(str(value))
        query = "update notifications set not_stat='Закрыт' where id_not=%s"
        ccursor.execute(query, data)
        cnx.commit()
        msgbox.exec()


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


    def OrderTotalThread():

        try:
            special_cursor = ccursor

            special_cursor.execute(
                "select no from order_content,products where paid='No' && content=products && product_category='Тарифы';")

            data = []

            for item in special_cursor:
                for value in item:
                    data.append(value)

            for value in data:
                data = (str(value),)
                query = "select round((price/60) * (UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(times))/60) from order_content where no=%s into @j;"
                special_cursor.execute(query, data)
                query = "select stop_check from products,order_content where products=content && no=%s into @f;"
                special_cursor.execute(query, data)
                query = "update order_content set price=(if(@j<price,price,if(@j>@f,@f,@j))) where no=%s;"
                special_cursor.execute(query, data)
                cnx.commit()

        except EnvironmentError as e:
            print(e)
            pass

        try:

            special_cursor = bcursor

            for no in order_no:
                data = (no, no)
                query = 'update orders set total=(select sum(price) from order_content where id_order=%s && paid="no") where no_orders=%s ;'
                special_cursor.execute(query, data)

                cnx.commit()

            ui.draw_orders()

        except BaseException as e:
            print(str(e))
            pass


    BackgroundThread()
    timer = QTimer()
    timer.timeout.connect(BackgroundThread)
    timer.start(60000)

    OrderTotalThread()
    total_timer = QTimer()
    total_timer.timeout.connect(OrderTotalThread)
    total_timer.start(10000)

    def CheckNotificationsThread():
        pass
        # TODO Хранение уведомлений в базе
        query = "select id_not from notifications where not_stat='Открыт' && timestampdiff( second,dates, now())>=0;"
        bcursor.execute(query)
        for item in bcursor:
            Message.notify(Message, item[0])


    reminder = QTimer()
    reminder.timeout.connect(CheckNotificationsThread)
    reminder.start(100)

    sys.exit(app.exec_())
