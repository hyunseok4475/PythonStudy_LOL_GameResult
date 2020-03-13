# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rank_Finder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.ID_Insert = QtWidgets.QLabel(Dialog)
        self.ID_Insert.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.ID_Insert.setFont(font)
        self.ID_Insert.setObjectName("ID_Insert")
        self.ID_TxtBox = QtWidgets.QTextEdit(Dialog)
        self.ID_TxtBox.setGeometry(QtCore.QRect(80, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.ID_TxtBox.setFont(font)
        self.ID_TxtBox.setObjectName("ID_TxtBox")
        self.Search_Button = QtWidgets.QPushButton(Dialog)
        self.Search_Button.setGeometry(QtCore.QRect(290, 20, 75, 31))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.Search_Button.setFont(font)
        self.Search_Button.setObjectName("Search_Button")
        self.Game_Result = QtWidgets.QListWidget(Dialog)
        self.Game_Result.setGeometry(QtCore.QRect(10, 90, 381, 201))
        self.Game_Result.setObjectName("Game_Result")
        self.Tier_Lb = QtWidgets.QLabel(Dialog)
        self.Tier_Lb.setGeometry(QtCore.QRect(10, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.Tier_Lb.setFont(font)
        self.Tier_Lb.setObjectName("Tier_Lb")
        self.Tier_Result = QtWidgets.QLabel(Dialog)
        self.Tier_Result.setGeometry(QtCore.QRect(80, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.Tier_Result.setFont(font)
        self.Tier_Result.setText("")
        self.Tier_Result.setObjectName("Tier_Result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ID_Insert.setText(_translate("Dialog", "ID Insert"))
        self.Search_Button.setText(_translate("Dialog", "Search!"))
        self.Tier_Lb.setText(_translate("Dialog", "Tier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
