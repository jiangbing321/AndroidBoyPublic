# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(242, 158)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 201, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbUserName = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbUserName.sizePolicy().hasHeightForWidth())
        self.lbUserName.setSizePolicy(sizePolicy)
        self.lbUserName.setMinimumSize(QtCore.QSize(60, 25))
        self.lbUserName.setMaximumSize(QtCore.QSize(60, 25))
        self.lbUserName.setObjectName("lbUserName")
        self.horizontalLayout.addWidget(self.lbUserName)
        self.editorUserName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.editorUserName.setObjectName("editorUserName")
        self.horizontalLayout.addWidget(self.editorUserName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbPassword = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbPassword.sizePolicy().hasHeightForWidth())
        self.lbPassword.setSizePolicy(sizePolicy)
        self.lbPassword.setMinimumSize(QtCore.QSize(60, 25))
        self.lbPassword.setMaximumSize(QtCore.QSize(60, 25))
        self.lbPassword.setObjectName("lbPassword")
        self.horizontalLayout_2.addWidget(self.lbPassword)
        self.editorPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.editorPassword.setObjectName("editorPassword")
        self.horizontalLayout_2.addWidget(self.editorPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ckSave = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ckSave.setObjectName("ckSave")
        self.horizontalLayout_3.addWidget(self.ckSave)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btOK = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btOK.sizePolicy().hasHeightForWidth())
        self.btOK.setSizePolicy(sizePolicy)
        self.btOK.setMinimumSize(QtCore.QSize(80, 25))
        self.btOK.setMaximumSize(QtCore.QSize(80, 25))
        self.btOK.setObjectName("btOK")
        self.horizontalLayout_4.addWidget(self.btOK)
        self.btCancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btCancel.sizePolicy().hasHeightForWidth())
        self.btCancel.setSizePolicy(sizePolicy)
        self.btCancel.setMinimumSize(QtCore.QSize(80, 25))
        self.btCancel.setMaximumSize(QtCore.QSize(80, 25))
        self.btCancel.setObjectName("btCancel")
        self.horizontalLayout_4.addWidget(self.btCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbUserName.setText(_translate("Dialog", "User name"))
        self.lbPassword.setText(_translate("Dialog", "Password"))
        self.ckSave.setText(_translate("Dialog", "Save to config file"))
        self.btOK.setText(_translate("Dialog", "OK"))
        self.btCancel.setText(_translate("Dialog", "Cancel"))
