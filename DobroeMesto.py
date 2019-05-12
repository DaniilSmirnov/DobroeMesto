import datetime
import threading

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


query = "select no, content from order_content where id_order=%s;"

query = "delete from order_content where no =%s;"

query = "UPDATE order_content SET no = no-1 WHERE no > %s;"

menu_items = []
order_items = []
order_totals = []
order_no = []
order_number = 0
guest_number = 0

items = []

is_cash = False
is_card = False

isopen = False  # подгружать из базы


class MainWindow(object):

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
        my_thread = threading.Thread(target=w.exec_())
        my_thread.start()
        self.draw_orders()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
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

        self.adminbutton.clicked.connect(self.openAdmin)
        self.orderbutton.clicked.connect(self.openNewOrder)
        self.draw_orders()

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

    def draw_orders(self):

        def create_icon(path):
            item_label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(path)
            pixmap = pixmap.scaled(32, 32, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
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
                    item_label = QtWidgets.QLabel("Гость пришел: " + value)
                    categorieslayout.addWidget(item_label, 0, j, 1, 1)
                    j += 1
                if i == 3:
                    item_label = QtWidgets.QLabel("К оплате: " + value)
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
                    query = "select content from order_content where id_order=%s;"
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
                self.gridLayout_3.addWidget(but_item, j, 6, 1, 1)
                but_item.clicked.connect(lambda state, name=id: delete(name, "product"))

                k += 1
                if k % 6 == 0:
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
                query = "delete from clients where id_client=%s;"
                cursor.execute(query, (data,))
                cnx.commit()
            if type == "product":
                query = "delete from products where products =%s;"
                cursor.execute(query, (data,))
                cnx.commit()
            Message.create(Message, "Инфо", "Удалено успешно")
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
        NewOrderWindowUi.resize(640, 480)
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
        self.scanitembutton.clicked.connect(self.scanItem)
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
                tab = QtWidgets.QWidget()
                self.tabWidget.addTab(tab, str(value))
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

        def select_item(button):
            order.append(button.text())
            draw_order()

        def draw_order():

            total = 0

            for i in reversed(range(self.gridLayout_3.count())):
                self.gridLayout_3.itemAt(i).widget().deleteLater()

            i = 0
            for item in order:
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
                        self.gridLayout_3.addWidget(QtWidgets.QLabel(str(cvalue) + "₽"), i, 1, 1, 1)
                        total += cvalue
                        font = QtGui.QFont()
                        font.setPointSize(20)
                        total_item = QtWidgets.QLabel("Итог " + str(total) + "₽")
                        total_item.setFont(font)
                        self.gridLayout_3.addWidget(total_item, i + 1, 0, 1, 1)
                i += 1

        def create_order():
            if len(order) == 0:
                pass
            else:
                query = "insert into orders values (default,now(),null,null,228,null,228,null);"
                cursor.execute(query)
                cnx.commit()
                query = "select no_orders from orders order by no_orders desc limit 1;"
                cursor.execute(query)
                for result in cursor:
                    for value in result:
                        number = str(value)
                for item in order:
                    query = "insert into order_content values(%s,%s, default,curtime(), 'no');"
                    data = (number, item)
                    cursor.execute(query, data)
                    cnx.commit()
                query = "update orders set comments=%s where no_orders=%s;"
                data = (self.lineEdit.text(), number)
                cursor.execute(query, data)
                cnx.commit()
                Message.create(Message, "Инфо", "Заказ добавлен")
                NewOrderWindowUi.accept()

        def pop_item(item):
            order.pop(order.index(item))
            draw_order()

        self.createbutton.clicked.connect(create_order)

    def scanGuest(self):

        text, ok = QtWidgets.QInputDialog.getText(self, 'Сканируйте карту пользователя',
                                                  'Номер карты:')

        if ok and text != "" and text != " ":
            global guest_number
            guest_number = text
            w = GuestWindow()
            w.exec_()

    def scanItem(self):

        text, ok = QtWidgets.QInputDialog.getText(self, 'Сканируйте товар',
                                                  'Код:')

        if ok and text != "" and text != " ":
            pass


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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        _translate = QtCore.QCoreApplication.translate
        PaymentWindowUi.setWindowTitle(_translate("PaymentWindowUi", "Оплата заказа"))
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

        self.paymentbutton.clicked.connect(self.pay)
        self.lineEdit.textChanged.connect(self.updatechange)

        self.paymentbutton.setEnabled(False)

        global order_number

        query = "select content from order_content where id_order=%s;"
        data = (order_number,)
        cursor.execute(query, data)

        i = 0
        for item in cursor:
            for value in item:
                order_item = QtWidgets.QPushButton(str(value))
                self.gridLayout_2.addWidget(order_item, i, 0, 1, 1)
                query = "select Product_cost from products where products=%s;"
                cdata = (value,)
                ccursor.execute(query, cdata)
                for citem in ccursor:
                    for cvalue in citem:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel(str(cvalue) + "₽"), i, 1, 1, 1)

            i += 1

        query = "SELECT total FROM orders WHERE No_orders = %s;"
        data = (order_number,)
        cursor.execute(query, data)

        for item in cursor:
            for value in item:
                font = QtGui.QFont()
                font.setPointSize(20)
                total_item = QtWidgets.QLabel("К оплате " + str(value) + "₽")
                total_item.setFont(font)
                self.gridLayout_2.addWidget(total_item, i, 0, 1, 1)
                self.value = value

    def updatechange(self):
        try:
            if self.lineEdit.text() != "" and self.lineEdit.text() != " " and (
                    float(self.lineEdit.text()) - self.value) > 0:
                self.refundlabel.setText("Cдача " + str(float(self.lineEdit.text()) - self.value) + "₽")
            else:
                self.refundlabel.setText("Cдача 0₽")
        except ValueError:
            self.refundlabel.setText("Некорректный ввод")
        try:
            if float(self.lineEdit.text()) - self.value >= 0 and self.paymentbox.currentIndex() != 0:
                self.paymentbutton.setEnabled(True)
            else:
                self.paymentbutton.setEnabled(False)
        except ValueError:
            self.paymentbutton.setEnabled(False)
            self.refundlabel.setText("Cдача 0₽")

    def pay(self):
        global order_number
        if float(self.value) <= float(self.lineEdit.text()) and self.paymentbox.currentIndex() != 0:
            if self.paymentbox.currentIndex() == 1:
                query = "update orders set close_date=now(),Type='Account' where no_orders=%s;"
            if self.paymentbox.currentIndex() == 2:
                query = "update orders set close_date=now(),Type='Cash' where no_orders=%s;"
            if self.paymentbox.currentIndex() == 3:
                query = "update orders set close_date=now(),Type='Card' where no_orders=%s;"

            data = (order_number,)
            cursor.execute(query, data)
            cnx.commit()

            Message.create(Message, "Инфо", "Оплата внесена \n" + self.refundlabel.text())

            # PaymentWindow.closeEvent(PaymentWindowUi)
            # TODO: Закрытие окна после вывода инфо
            # TODO: Добавить тип оплаты Account в БД
            # TODO: отображение Client_cash


class PaymentWindow(QtWidgets.QDialog, PaymentWindowUi):
    def __init__(self, parent=None):
        super(PaymentWindow, self).__init__(parent)
        self.setupUi(self)


class OrderWindowUi(object):
    def setupUi(self, OrderWindowUi):
        OrderWindowUi.setObjectName("OrderWindowUi")
        OrderWindowUi.resize(640, 480)
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

        def update_order():
            for item in new_items:
                query = "insert into order_content values(%s,%s, default,curtime(), 'no');"
                data = (order_number, item)
                cursor.execute(query, data)
                cnx.commit()

            OrderWindowUi.accept()

        self.createbutton.setEnabled(False)
        self.createbutton.clicked.connect(update_order)

        query = "select distinct product_category from products"
        cursor.execute(query)
        for item in cursor:
            for value in item:
                tab = QtWidgets.QWidget()
                self.tabWidget.addTab(tab, str(value))
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
                order_item = QtWidgets.QPushButton(str(value))
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
                font = QtGui.QFont()
                font.setPointSize(20)
                total_item = QtWidgets.QLabel("Итог " + str(value) + "₽")
                total_item.setFont(font)
                self.gridLayout_3.addWidget(total_item, i, 0, 1, 1)

        def select_item(button):
            new_items.append(button.text())

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
                Message.create(Message, "Инфо", "Невозможно удалить позицию внесенную ранее")
            draw_order()


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profiletab), _translate("GuestWindowUi", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.historytab), _translate("GuestWindowUi", "Tab 2"))
        self.acceptbutton.setText(_translate("GuestWindowUi", "Подтвердить"))

        global guest_number

        self.guestlabel.setText(_translate("GuestWindowUi", "Гость " + str(guest_number)))


class GuestWindow(QtWidgets.QDialog, GuestWindowUi):
    def __init__(self, parent=None):
        super(GuestWindow, self).__init__(parent)
        self.setupUi(self)


class Message(object):
    def create(self, Title, Text):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(Title)
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/i.png')))
        msgbox.setText(Text)
        msgbox.exec()

    def notify(self, Text):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Уведомление")
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/remind.png')))
        msgbox.setText(Text)
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

        try:
            for no in order_no:
                data = (no,)
                query = "select if(client_lvl=3,15,if(client_lvl=2,10,if(client_lvl=1,5,0))) as 'discount' " \
                        "from clients,orders " \
                        "where id_client=id_visitor && no_orders=%s into @c;"
                bcursor.execute(query, data)
                query = "select sum(product_cost) from order_content,products where " \
                        "content=products && id_order=%s && product_category<>'Тарифы' into @a; "
                bcursor.execute(query, data)
                query = "select if(@a is null,0,@a) into @a;"
                bcursor.execute(query)
                query = "select round(sum((Product_cost/60) * ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(times))/60)))" \
                        "from order_content, products " \
                        "where id_order = %s && content = products && product_category = 'Тарифы' into @b;"
                bcursor.execute(query, data)
                query = "select if(@b is null,0,@b) into @b;"
                bcursor.execute(query)
                query = "update orders set total=(@a+@b)/100*(100-@c) where no_orders=%s;"
                bcursor.execute(query, data)
                cnx.commit()

                ui.draw_orders()

        except BaseException as e:
            print(str(e))
            pass

    timer = QTimer()
    timer.timeout.connect(BackgroundThread)
    timer.start(100)

    def CheckNotificationsThread():
        pass
        # TODO Хранение уведомлений в базе


    reminder = QTimer()
    reminder.timeout.connect(CheckNotificationsThread)
    reminder.start(100)

    sys.exit(app.exec_())
