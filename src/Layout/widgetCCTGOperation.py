# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgetCCTGOperation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(663, 35)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._ckSelect = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ckSelect.sizePolicy().hasHeightForWidth())
        self._ckSelect.setSizePolicy(sizePolicy)
        self._ckSelect.setMinimumSize(QtCore.QSize(24, 24))
        self._ckSelect.setMaximumSize(QtCore.QSize(24, 24))
        self._ckSelect.setText("")
        self._ckSelect.setObjectName("_ckSelect")
        self.horizontalLayout.addWidget(self._ckSelect)
        self._btStart = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btStart.sizePolicy().hasHeightForWidth())
        self._btStart.setSizePolicy(sizePolicy)
        self._btStart.setMinimumSize(QtCore.QSize(28, 24))
        self._btStart.setMaximumSize(QtCore.QSize(28, 24))
        self._btStart.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/bt_start.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btStart.setIcon(icon)
        self._btStart.setObjectName("_btStart")
        self.horizontalLayout.addWidget(self._btStart)
        self._btStop = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btStop.sizePolicy().hasHeightForWidth())
        self._btStop.setSizePolicy(sizePolicy)
        self._btStop.setMinimumSize(QtCore.QSize(28, 24))
        self._btStop.setMaximumSize(QtCore.QSize(28, 24))
        self._btStop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/bt_stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btStop.setIcon(icon1)
        self._btStop.setObjectName("_btStop")
        self.horizontalLayout.addWidget(self._btStop)
        self._btDelete = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btDelete.sizePolicy().hasHeightForWidth())
        self._btDelete.setSizePolicy(sizePolicy)
        self._btDelete.setMinimumSize(QtCore.QSize(28, 24))
        self._btDelete.setMaximumSize(QtCore.QSize(28, 24))
        self._btDelete.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/bt_clear.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btDelete.setIcon(icon2)
        self._btDelete.setObjectName("_btDelete")
        self.horizontalLayout.addWidget(self._btDelete)
        self._btBrowser = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btBrowser.sizePolicy().hasHeightForWidth())
        self._btBrowser.setSizePolicy(sizePolicy)
        self._btBrowser.setMinimumSize(QtCore.QSize(28, 24))
        self._btBrowser.setMaximumSize(QtCore.QSize(28, 24))
        self._btBrowser.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btBrowser.setIcon(icon3)
        self._btBrowser.setObjectName("_btBrowser")
        self.horizontalLayout.addWidget(self._btBrowser)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 24))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 24))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import AndroidBoy_rc
