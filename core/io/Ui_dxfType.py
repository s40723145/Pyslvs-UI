# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/io/dxfType.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(507, 649)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(507, 649))
        Dialog.setMaximumSize(QtCore.QSize(507, 649))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bezier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(Dialog)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.verticalWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.folderPath = QtWidgets.QLabel(self.groupBox)
        self.folderPath.setObjectName("folderPath")
        self.horizontalLayout_2.addWidget(self.folderPath)
        self.setPath = QtWidgets.QToolButton(self.groupBox)
        self.setPath.setObjectName("setPath")
        self.horizontalLayout_2.addWidget(self.setPath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.groupBox_10 = QtWidgets.QGroupBox(self.verticalWidget)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_15 = QtWidgets.QLabel(self.groupBox_10)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.DrillingVal = QtWidgets.QDoubleSpinBox(self.groupBox_10)
        self.DrillingVal.setMinimum(0.01)
        self.DrillingVal.setProperty("value", 6.0)
        self.DrillingVal.setObjectName("DrillingVal")
        self.horizontalLayout_17.addWidget(self.DrillingVal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_17, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_10)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.IntervalVal = QtWidgets.QDoubleSpinBox(self.groupBox_10)
        self.IntervalVal.setProperty("value", 2.0)
        self.IntervalVal.setObjectName("IntervalVal")
        self.horizontalLayout_3.addWidget(self.IntervalVal)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_9.addWidget(self.groupBox_10)
        self.groupBox_7 = QtWidgets.QGroupBox(self.verticalWidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.LinkType = QtWidgets.QComboBox(self.groupBox_7)
        self.LinkType.setObjectName("LinkType")
        self.LinkType.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LinkType)
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.LinkWidthVal = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.LinkWidthVal.setMinimum(0.01)
        self.LinkWidthVal.setProperty("value", 8.0)
        self.LinkWidthVal.setObjectName("LinkWidthVal")
        self.horizontalLayout_13.addWidget(self.LinkWidthVal)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.formLayout_4.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.horizontalLayout_15.addLayout(self.formLayout_4)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.LinkImage = QtWidgets.QLabel(self.groupBox_11)
        self.LinkImage.setText("")
        self.LinkImage.setObjectName("LinkImage")
        self.verticalLayout_7.addWidget(self.LinkImage)
        self.horizontalLayout_15.addWidget(self.groupBox_11)
        self.verticalLayout_9.addWidget(self.groupBox_7)
        self.groupBox_9 = QtWidgets.QGroupBox(self.verticalWidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox_9)
        self.label_12.setObjectName("label_12")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.ChainType = QtWidgets.QComboBox(self.groupBox_9)
        self.ChainType.setObjectName("ChainType")
        self.ChainType.addItem("")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ChainType)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.ChainWidthVal = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.ChainWidthVal.setMinimum(0.01)
        self.ChainWidthVal.setProperty("value", 8.0)
        self.ChainWidthVal.setObjectName("ChainWidthVal")
        self.horizontalLayout_14.addWidget(self.ChainWidthVal)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.formLayout_5.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.label_14 = QtWidgets.QLabel(self.groupBox_9)
        self.label_14.setObjectName("label_14")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_16.addLayout(self.formLayout_5)
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName("groupBox_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_12)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ChainImage = QtWidgets.QLabel(self.groupBox_12)
        self.ChainImage.setText("")
        self.ChainImage.setObjectName("ChainImage")
        self.verticalLayout_8.addWidget(self.ChainImage)
        self.horizontalLayout_16.addWidget(self.groupBox_12)
        self.verticalLayout_9.addWidget(self.groupBox_9)
        spacerItem4 = QtWidgets.QSpacerItem(20, 180, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DXF models"))
        self.groupBox.setTitle(_translate("Dialog", "Files"))
        self.label.setText(_translate("Dialog", "File name: "))
        self.folderPath.setText(_translate("Dialog", "path"))
        self.setPath.setText(_translate("Dialog", "..."))
        self.groupBox_10.setTitle(_translate("Dialog", "Entire"))
        self.label_15.setText(_translate("Dialog", "Drilling size: "))
        self.label_3.setText(_translate("Dialog", "Interval:"))
        self.groupBox_7.setTitle(_translate("Dialog", "Links"))
        self.label_8.setText(_translate("Dialog", "Type: "))
        self.LinkType.setItemText(0, _translate("Dialog", "Round connecting rod"))
        self.label_10.setText(_translate("Dialog", "Fillet diameter: "))
        self.groupBox_11.setTitle(_translate("Dialog", "Preview"))
        self.groupBox_9.setTitle(_translate("Dialog", "Chains"))
        self.label_12.setText(_translate("Dialog", "Type: "))
        self.ChainType.setItemText(0, _translate("Dialog", "Sheet"))
        self.label_14.setText(_translate("Dialog", "Fillet diameter: "))
        self.groupBox_12.setTitle(_translate("Dialog", "Preview"))

import icons_rc
import preview_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

