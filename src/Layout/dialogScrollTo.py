# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/weizlian/Desktop/MyPrj/github-repos/Python/AndroidBoyPublic/src/Layout/dialogScrollTo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 50)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(40, 10, 245, 21))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self._lbScrollTo = QtWidgets.QLabel(self.splitter)
        self._lbScrollTo.setObjectName("_lbScrollTo")
        self._editorRow = QtWidgets.QLineEdit(self.splitter)
        self._editorRow.setObjectName("_editorRow")
        self._lbRange = QtWidgets.QLabel(self.splitter)
        self._lbRange.setObjectName("_lbRange")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Scroll to"))
        self._lbScrollTo.setText(_translate("Dialog", "Scroll to:"))
        self._lbRange.setText(_translate("Dialog", "(0~0)"))
