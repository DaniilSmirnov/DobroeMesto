# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'additem.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_AddItemWindowUi(object):
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
        AddItemWindowUi.setWindowTitle(_translate("AddItemWindowUi", "Dialog"))
        self.label_5.setText(_translate("AddItemWindowUi", "Штрихкод"))
        self.addbutton.setText(_translate("AddItemWindowUi", "Добавить"))
        self.label.setText(_translate("AddItemWindowUi", "Название позиции"))
        self.label_2.setText(_translate("AddItemWindowUi", "Цена"))
        self.label_4.setText(_translate("AddItemWindowUi", "Категория"))
        self.label_3.setText(_translate("AddItemWindowUi", "Количество"))

        self.addbutton.clicked.connect(self.writedata)

    def writedata(self):
        string = self.productedit.text() + " " + self.costedit.text() + " " + self.amountedit.text() + " " + self.categoryedit.text() + " " + self.barcodeedit.text()
        f = open('data.txt', 'a')
        f.write(string + '\n')
        f.close()

        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Ура, ты молодец!")
        msgbox.setText("Ты добавил еще одну позицию, так держать!")
        msgbox.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    AddItemWindowUi = QtWidgets.QDialog()
    ui = Ui_AddItemWindowUi()
    ui.setupUi(AddItemWindowUi)
    AddItemWindowUi.show()
    sys.exit(app.exec_())
