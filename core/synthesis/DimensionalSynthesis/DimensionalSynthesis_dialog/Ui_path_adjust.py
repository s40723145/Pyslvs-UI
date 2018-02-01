# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/synthesis/DimensionalSynthesis/DimensionalSynthesis_dialog/path_adjust.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/DimensionalSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.path_list = QtWidgets.QListWidget(self.widget)
        self.path_list.setObjectName("path_list")
        self.verticalLayout.addWidget(self.path_list)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.point_up = QtWidgets.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.point_up.setIcon(icon1)
        self.point_up.setObjectName("point_up")
        self.horizontalLayout_5.addWidget(self.point_up)
        self.point_down = QtWidgets.QPushButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.point_down.setIcon(icon2)
        self.point_down.setObjectName("point_down")
        self.horizontalLayout_5.addWidget(self.point_down)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.point_delete = QtWidgets.QPushButton(self.widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.point_delete.setIcon(icon3)
        self.point_delete.setObjectName("point_delete")
        self.horizontalLayout_5.addWidget(self.point_delete)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.moving = QtWidgets.QWidget()
        self.moving.setObjectName("moving")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.moving)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.moving)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.moving)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.moving_y_coordinate = QtWidgets.QDoubleSpinBox(self.moving)
        self.moving_y_coordinate.setMinimum(-1000000.0)
        self.moving_y_coordinate.setMaximum(1000000.0)
        self.moving_y_coordinate.setObjectName("moving_y_coordinate")
        self.gridLayout.addWidget(self.moving_y_coordinate, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.moving_x_coordinate = QtWidgets.QDoubleSpinBox(self.moving)
        self.moving_x_coordinate.setMinimum(-1000000.0)
        self.moving_x_coordinate.setMaximum(1000000.0)
        self.moving_x_coordinate.setObjectName("moving_x_coordinate")
        self.gridLayout.addWidget(self.moving_x_coordinate, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.moving_button = QtWidgets.QPushButton(self.moving)
        self.moving_button.setDefault(True)
        self.moving_button.setObjectName("moving_button")
        self.horizontalLayout_3.addWidget(self.moving_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.moving, "")
        self.scaling = QtWidgets.QWidget()
        self.scaling.setObjectName("scaling")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scaling)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 2, 1, 1)
        self.scaling_h = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_h.setMinimum(1.0)
        self.scaling_h.setMaximum(10000.0)
        self.scaling_h.setObjectName("scaling_h")
        self.gridLayout_2.addWidget(self.scaling_h, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scaling)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scaling)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 1, 2, 1, 1)
        self.scaling_v = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_v.setMinimum(1.0)
        self.scaling_v.setMaximum(10000.0)
        self.scaling_v.setObjectName("scaling_v")
        self.gridLayout_2.addWidget(self.scaling_v, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(self.scaling)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.scaling)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.scaling_rx = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_rx.setMinimum(-1000000.0)
        self.scaling_rx.setMaximum(1000000.0)
        self.scaling_rx.setObjectName("scaling_rx")
        self.horizontalLayout_2.addWidget(self.scaling_rx)
        self.scaling_ry = QtWidgets.QDoubleSpinBox(self.scaling)
        self.scaling_ry.setMinimum(-1000000.0)
        self.scaling_ry.setMaximum(1000000.0)
        self.scaling_ry.setObjectName("scaling_ry")
        self.horizontalLayout_2.addWidget(self.scaling_ry)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.scaling_button = QtWidgets.QPushButton(self.scaling)
        self.scaling_button.setDefault(True)
        self.scaling_button.setObjectName("scaling_button")
        self.horizontalLayout_4.addWidget(self.scaling_button)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.scaling, "")
        self.curve_fitting = QtWidgets.QWidget()
        self.curve_fitting.setObjectName("curve_fitting")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.curve_fitting)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.curve_fitting)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.curve_fitting)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.points_num = QtWidgets.QLabel(self.curve_fitting)
        self.points_num.setObjectName("points_num")
        self.horizontalLayout_7.addWidget(self.points_num)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.curve_fitting)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.match_num = QtWidgets.QSpinBox(self.curve_fitting)
        self.match_num.setObjectName("match_num")
        self.horizontalLayout_6.addWidget(self.match_num)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.match_button = QtWidgets.QPushButton(self.curve_fitting)
        self.match_button.setDefault(True)
        self.match_button.setObjectName("match_button")
        self.horizontalLayout_8.addWidget(self.match_button)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.curve_fitting, "")
        self.verticalLayout_5.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Process ..."))
        self.label.setText(_translate("Dialog", "X coordinate: "))
        self.label_2.setText(_translate("Dialog", "Y coordinate: "))
        self.moving_button.setText(_translate("Dialog", "Moving"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.moving), _translate("Dialog", "Moving"))
        self.label_3.setText(_translate("Dialog", "Horizontal: "))
        self.label_4.setText(_translate("Dialog", "Vertical: "))
        self.label_5.setText(_translate("Dialog", "Reference point: "))
        self.scaling_button.setText(_translate("Dialog", "Scaling"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scaling), _translate("Dialog", "Scaling"))
        self.label_8.setText(_translate("Dialog", "This function can minimize the number of coordinate points."))
        self.label_7.setText(_translate("Dialog", "The number of points: "))
        self.points_num.setText(_translate("Dialog", "0"))
        self.label_6.setText(_translate("Dialog", "Reduced to: "))
        self.match_button.setText(_translate("Dialog", "Match"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.curve_fitting), _translate("Dialog", "Curve Fitting"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

