from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

cnx = mysql.connector.connect(user='root', password='i130813',
                              host='127.0.0.1',
                              database='dobroe_mesto2')
cursor = cnx.cursor()

'''
select * from trip;
'''

items = []

trip = []
product_data = {}
product_k = {}

passenger = []
passenger_data = {}
passenger_k = {}


class Ui_MainWindow(object):

    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 391, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.loginedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginedit.setObjectName("loginedit")
        self.verticalLayout.addWidget(self.loginedit)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.passedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passedit.setObjectName("passedit")
        self.passedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.passedit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.verticalLayoutWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupMainUi(self):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 555, 291))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.addproductbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addproductbutton.setObjectName("addproductbutton")
        self.verticalLayout.addWidget(self.addproductbutton)
        self.workerbutton = QtWidgets.QPushButton(self.centralwidget)
        self.workerbutton.setObjectName("workerbutton")
        self.verticalLayout.addWidget(self.workerbutton)
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.closebutton.setObjectName("cancelbutton")
        self.verticalLayout.addWidget(self.closebutton)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateMainUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateMainUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.savebutton.setText(_translate("MainWindow", "Сохранить"))
        self.closebutton.setText(_translate("MainWindow", "Выйти"))
        self.addproductbutton.setText(_translate("MainWindow", "Добавить товар"))
        self.workerbutton.setText(_translate("MainWindow", "Добавить сотрудника"))

        self.addproductbutton.clicked.connect(self.setupproductUi)
        self.closebutton.clicked.connect(self.setupUi)
        self.workerbutton.clicked.connect(self.setupworkUi)

        line_item = QtWidgets.QLabel("Товары")
        self.gridLayout.addWidget(line_item, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(18)
        line_item.setFont(font)

        line_item = QtWidgets.QLabel("Название")
        self.gridLayout.addWidget(line_item, 0, 1, 1, 1)
        line_item = QtWidgets.QLabel("Стоимость")
        self.gridLayout.addWidget(line_item, 0, 2, 1, 1)
        line_item = QtWidgets.QLabel("Количество")
        self.gridLayout.addWidget(line_item, 0, 3, 1, 1)
        line_item = QtWidgets.QLabel("Категория")
        self.gridLayout.addWidget(line_item, 0, 4, 1, 1)

        query = ("select * from products;")
        cursor.execute(query)
        i = 1
        j = 4
        k = 1
        for item in cursor:
            trip.append(item[0])
            for value in item:
                if k == 1:
                    line_item = QtWidgets.QLineEdit(str(value))
                    self.gridLayout.addWidget(line_item, j, k, 1, 1)
                    row = str(value)
                    product_data.update({line_item: line_item.text()})
                    product_k.update({line_item: k})
                    line_item.textChanged.connect(lambda state, line=line_item: modify_product(line))
                    k += 1
                    continue
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=line_item: modify_product(line))

                product_data.update({line_item: line_item.text()})
                product_k.update({line_item: k})

                but_item = QtWidgets.QPushButton("Удалить")
                self.gridLayout.addWidget(but_item, j, 5, 1, 1)
                but_item.clicked.connect(lambda state, name=row: delete_product(name))

                k += 1
                if k % 5 == 0:
                    j += 1
                    k = 1

        query = ("select * from cliens;")
        cursor.execute(query)
        k = 0
        j += 2
        i = 0
        line_item = QtWidgets.QLabel("Пассажиры")
        self.gridLayout.addWidget(line_item, j, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(18)
        line_item.setFont(font)

        line_item = QtWidgets.QLabel("Имя")
        self.gridLayout.addWidget(line_item, j, 1, 1, 1)
        line_item = QtWidgets.QLabel("Фамилия")
        self.gridLayout.addWidget(line_item, j, 2, 1, 1)
        line_item = QtWidgets.QLabel("Отчество")
        self.gridLayout.addWidget(line_item, j, 3, 1, 1)
        line_item = QtWidgets.QLabel("Паспорт")
        self.gridLayout.addWidget(line_item, j, 4, 1, 1)
        j += 1
        for item in cursor:
            passenger.append(item[0])
            for value in item:
                if k == 0:
                    line_item = QtWidgets.QLabel(str(value))
                    self.gridLayout.addWidget(line_item, j, k, 1, 1)
                    passenger_data.update({line_item: line_item.text()})
                    passenger_k.update({line_item: k})
                    k += 1
                    continue
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=line_item: modify_pass(line))

                passenger_data.update({line_item: line_item.text()})
                passenger_k.update({line_item: k})

                but_item = QtWidgets.QPushButton("Удалить")
                self.gridLayout.addWidget(but_item, j, 5, 1, 1)
                but_item.clicked.connect(lambda state, row=i: delete_pass(row))

                k += 1
                if k % 5 == 0:
                    j += 1
                    i += 1
                    k = 0

        line_item = QtWidgets.QLabel("Работники")
        self.gridLayout.addWidget(line_item, j, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(18)
        line_item.setFont(font)

        line_item = QtWidgets.QLabel("Имя")
        self.gridLayout.addWidget(line_item, j, 1, 1, 1)
        line_item = QtWidgets.QLabel("Фамилия")
        self.gridLayout.addWidget(line_item, j, 2, 1, 1)
        line_item = QtWidgets.QLabel("Логин")
        self.gridLayout.addWidget(line_item, j, 3, 1, 1)
        line_item = QtWidgets.QLabel("Пароль")
        self.gridLayout.addWidget(line_item, j, 4, 1, 1)

        j += 1
        i = 0
        query = ("select * from users;")
        cursor.execute(query)
        k = 0
        for item in cursor:
            trip.append(item[0])
            for value in item:
                if k == 0:
                    line_item = QtWidgets.QLabel(str(value))
                    self.gridLayout.addWidget(line_item, j, k, 1, 1)
                    k += 1
                    continue
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout.addWidget(line_item, j, k, 1, 1)

                but_item = QtWidgets.QPushButton("Удалить")
                self.gridLayout.addWidget(but_item, j, 5, 1, 1)
                but_item.clicked.connect(lambda state, row=i: delete_work(row))

                k += 1
                if k % 5 == 0:
                    j += 1
                    i += 1
                    k = 0

        def save_pass(item):
            k = passenger_k.get(item)
            position = passenger_data.get(item)
            text = item.text()
            data = (text, position)
            if k == 1:
                query = ("update passenger set NameP = %s where NameP = %s;")
            if k == 2:
                query = ("update passenger set SurnameP = %s where SurnameP = %s;")
            if k == 3:
                query = ("update passenger set Patronymic = %s where Patronymic = %s;")
            if k == 4:
                query = ("update passenger set Passport = %s where Passport = %s;")
            cursor.execute(query, data)
            cnx.commit()

        def modify_pass(item):
            self.savebutton.clicked.connect(lambda: save_pass(item))

        def delete_product(row):
            query = "delete from products where Products = %s;"
            data = (row,)
            cursor.execute(query, data)
            cnx.commit()
            self.setupMainUi()

        def delete_pass(row):
            query = "delete from passenger where idPassenger=%s;"
            data = row
            cursor.execute(query, (data,))
            cnx.commit()
            self.setupMainUi()

        def delete_work(row):
            query = "delete from worker where idWorker=%s;"
            data = row
            cursor.execute(query, (data,))
            cnx.commit()
            self.setupMainUi()

        def save_product(item):
            k = product_k.get(item)
            position = product_data.get(item)
            text = item.text()
            data = (text, position)
            if k == 1:
                query = ("update products set Products = %s where Products = %s;")
            if k == 2:
                query = ("update products set Product_cost = %s where Product_cost = %s;")
            if k == 3:
                query = ("update products set Product_Amount = %s where Product_Amount = %s;")
            if k == 4:
                query = ("update products set Product_category = %s where Product_category = %s;")
            cursor.execute(query, data)
            cnx.commit()

            self.setupMainUi()

        def modify_product(item):
            self.savebutton.clicked.connect(lambda: save_product(item))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))

        self.pushButton.clicked.connect(self.login)

    def login(self):
        username_entered = self.loginedit.text()
        password_entered = self.passedit.text()

        query = ("SELECT login from worker;")
        cursor.execute(query)

        for (login) in cursor:
            if login[0] == username_entered:
                query = ("SELECT pass from worker;")
                cursor.execute(query)
                for (password) in cursor:
                    if password[0] == password_entered:
                        self.setupMainUi()

    def setupproductUi(self):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateproductUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateproductUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.label_4.setText(_translate("MainWindow", "Категория"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.label_2.setText(_translate("MainWindow", "Стоимость"))
        self.label_3.setText(_translate("MainWindow", "Количество"))

        self.pushButton_2.clicked.connect(self.setupMainUi)
        self.pushButton.clicked.connect(self.writeproduct)

    def writeproduct(self):
        query = "insert into products(Products, Product_cost, Product_Amount, Product_category)values(%s, %s, %s, %s);"
        data = (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        cursor.execute(query, data)
        cnx.commit()
        self.setupMainUi()

    def setupworkUi(self):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateworkUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateworkUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.label_4.setText(_translate("MainWindow", "Пароль"))
        self.label.setText(_translate("MainWindow", "Имя"))
        self.label_2.setText(_translate("MainWindow", "Фамилия"))
        self.label_3.setText(_translate("MainWindow", "Логин"))

        self.pushButton_2.clicked.connect(self.setupMainUi)
        self.pushButton.clicked.connect(self.writeworker)

    def writeworker(self):
        query = "insert into worker(NameWorker, SurnameWorker, login, pass)values(%s, %s, %s, %s);"
        data = (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),)
        cursor.execute(query, data)
        cnx.commit()
        self.setupMainUi()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupMainUi()
    MainWindow.show()
    sys.exit(app.exec_())
