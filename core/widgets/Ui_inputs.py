# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\widgets\inputs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 707)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputs_points_groupBox = QtWidgets.QGroupBox(Form)
        self.inputs_points_groupBox.setObjectName("inputs_points_groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.inputs_points_groupBox)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.inputs_points_lable = QtWidgets.QLabel(self.inputs_points_groupBox)
        self.inputs_points_lable.setObjectName("inputs_points_lable")
        self.verticalLayout_13.addWidget(self.inputs_points_lable)
        self.inputs_points = QtWidgets.QListWidget(self.inputs_points_groupBox)
        self.inputs_points.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.inputs_points.setObjectName("inputs_points")
        self.verticalLayout_13.addWidget(self.inputs_points)
        self.horizontalLayout.addLayout(self.verticalLayout_13)
        self.inputs_label_right1 = QtWidgets.QLabel(self.inputs_points_groupBox)
        self.inputs_label_right1.setObjectName("inputs_label_right1")
        self.horizontalLayout.addWidget(self.inputs_label_right1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.inputs_baseLinks_lable = QtWidgets.QLabel(self.inputs_points_groupBox)
        self.inputs_baseLinks_lable.setObjectName("inputs_baseLinks_lable")
        self.verticalLayout_15.addWidget(self.inputs_baseLinks_lable)
        self.inputs_baseLinks = QtWidgets.QListWidget(self.inputs_points_groupBox)
        self.inputs_baseLinks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.inputs_baseLinks.setObjectName("inputs_baseLinks")
        self.verticalLayout_15.addWidget(self.inputs_baseLinks)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.inputs_label_right2 = QtWidgets.QLabel(self.inputs_points_groupBox)
        self.inputs_label_right2.setObjectName("inputs_label_right2")
        self.horizontalLayout.addWidget(self.inputs_label_right2)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.inputs_driveLinks_lable = QtWidgets.QLabel(self.inputs_points_groupBox)
        self.inputs_driveLinks_lable.setObjectName("inputs_driveLinks_lable")
        self.verticalLayout_16.addWidget(self.inputs_driveLinks_lable)
        self.inputs_driveLinks = QtWidgets.QListWidget(self.inputs_points_groupBox)
        self.inputs_driveLinks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.inputs_driveLinks.setObjectName("inputs_driveLinks")
        self.verticalLayout_16.addWidget(self.inputs_driveLinks)
        self.inputs_variable_add = QtWidgets.QPushButton(self.inputs_points_groupBox)
        self.inputs_variable_add.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inputs_variable_add.setIcon(icon)
        self.inputs_variable_add.setObjectName("inputs_variable_add")
        self.verticalLayout_16.addWidget(self.inputs_variable_add)
        self.horizontalLayout.addLayout(self.verticalLayout_16)
        self.verticalLayout.addWidget(self.inputs_points_groupBox)
        self.inputs_variable_groupBox = QtWidgets.QGroupBox(Form)
        self.inputs_variable_groupBox.setObjectName("inputs_variable_groupBox")
        self.inputs_dial_layout = QtWidgets.QHBoxLayout(self.inputs_variable_groupBox)
        self.inputs_dial_layout.setObjectName("inputs_dial_layout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.inputs_variable = QtWidgets.QListWidget(self.inputs_variable_groupBox)
        self.inputs_variable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.inputs_variable.setObjectName("inputs_variable")
        self.verticalLayout_10.addWidget(self.inputs_variable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.inputs_variable_remove = QtWidgets.QPushButton(self.inputs_variable_groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inputs_variable_remove.setIcon(icon1)
        self.inputs_variable_remove.setObjectName("inputs_variable_remove")
        self.horizontalLayout_3.addWidget(self.inputs_variable_remove)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.line_7 = QtWidgets.QFrame(self.inputs_variable_groupBox)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_3.addWidget(self.line_7)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.inputs_variable_speed_label = QtWidgets.QLabel(self.inputs_variable_groupBox)
        self.inputs_variable_speed_label.setObjectName("inputs_variable_speed_label")
        self.horizontalLayout_4.addWidget(self.inputs_variable_speed_label)
        self.inputs_variable_speed = QtWidgets.QSpinBox(self.inputs_variable_groupBox)
        self.inputs_variable_speed.setEnabled(False)
        self.inputs_variable_speed.setMinimum(-100)
        self.inputs_variable_speed.setMaximum(100)
        self.inputs_variable_speed.setSingleStep(5)
        self.inputs_variable_speed.setProperty("value", -10)
        self.inputs_variable_speed.setObjectName("inputs_variable_speed")
        self.horizontalLayout_4.addWidget(self.inputs_variable_speed)
        self.verticalLayout_18.addLayout(self.horizontalLayout_4)
        self.extremeRebound = QtWidgets.QCheckBox(self.inputs_variable_groupBox)
        self.extremeRebound.setChecked(True)
        self.extremeRebound.setObjectName("extremeRebound")
        self.verticalLayout_18.addWidget(self.extremeRebound)
        self.horizontalLayout_3.addLayout(self.verticalLayout_18)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.inputs_variable_play = QtWidgets.QPushButton(self.inputs_variable_groupBox)
        self.inputs_variable_play.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.inputs_variable_play.setIcon(icon2)
        self.inputs_variable_play.setCheckable(True)
        self.inputs_variable_play.setObjectName("inputs_variable_play")
        self.verticalLayout_3.addWidget(self.inputs_variable_play)
        self.inputs_variable_stop = QtWidgets.QPushButton(self.inputs_variable_groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/interrupted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inputs_variable_stop.setIcon(icon3)
        self.inputs_variable_stop.setObjectName("inputs_variable_stop")
        self.verticalLayout_3.addWidget(self.inputs_variable_stop)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.inputs_dial_layout.addLayout(self.verticalLayout_10)
        self.line_5 = QtWidgets.QFrame(self.inputs_variable_groupBox)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.inputs_dial_layout.addWidget(self.line_5)
        self.verticalLayout.addWidget(self.inputs_variable_groupBox)
        self.inputs_record_groupBox = QtWidgets.QGroupBox(Form)
        self.inputs_record_groupBox.setObjectName("inputs_record_groupBox")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.inputs_record_groupBox)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.inputs_record_interval_text = QtWidgets.QLabel(self.inputs_record_groupBox)
        self.inputs_record_interval_text.setObjectName("inputs_record_interval_text")
        self.horizontalLayout_6.addWidget(self.inputs_record_interval_text)
        self.inputs_record_interval = QtWidgets.QDoubleSpinBox(self.inputs_record_groupBox)
        self.inputs_record_interval.setMinimum(0.5)
        self.inputs_record_interval.setMaximum(10.0)
        self.inputs_record_interval.setProperty("value", 6.0)
        self.inputs_record_interval.setObjectName("inputs_record_interval")
        self.horizontalLayout_6.addWidget(self.inputs_record_interval)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.inputs_record_show = QtWidgets.QCheckBox(self.inputs_record_groupBox)
        self.inputs_record_show.setChecked(True)
        self.inputs_record_show.setObjectName("inputs_record_show")
        self.horizontalLayout_6.addWidget(self.inputs_record_show)
        self.verticalLayout_22.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.inputs_record = QtWidgets.QListWidget(self.inputs_record_groupBox)
        self.inputs_record.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.inputs_record.setObjectName("inputs_record")
        item = QtWidgets.QListWidgetItem()
        self.inputs_record.addItem(item)
        self.horizontalLayout_8.addWidget(self.inputs_record)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputs_record_record = QtWidgets.QPushButton(self.inputs_record_groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inputs_record_record.setIcon(icon4)
        self.inputs_record_record.setCheckable(True)
        self.inputs_record_record.setObjectName("inputs_record_record")
        self.verticalLayout_2.addWidget(self.inputs_record_record)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.inputs_record_remove = QtWidgets.QPushButton(self.inputs_record_groupBox)
        self.inputs_record_remove.setIcon(icon1)
        self.inputs_record_remove.setObjectName("inputs_record_remove")
        self.verticalLayout_2.addWidget(self.inputs_record_remove)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_22.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.inputs_record_groupBox)

        self.retranslateUi(Form)
        self.inputs_record.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.inputs_points_groupBox.setTitle(_translate("Form", "Inputs"))
        self.inputs_points_lable.setText(_translate("Form", "Points"))
        self.inputs_points.setStatusTip(_translate("Form", "Choose a point to be a revolute joint."))
        self.inputs_label_right1.setText(_translate("Form", ">>"))
        self.inputs_baseLinks_lable.setText(_translate("Form", "Base link"))
        self.inputs_baseLinks.setStatusTip(_translate("Form", "Coordinate reference."))
        self.inputs_label_right2.setText(_translate("Form", ">>"))
        self.inputs_driveLinks_lable.setText(_translate("Form", "Drive link"))
        self.inputs_driveLinks.setStatusTip(_translate("Form", "Coordinate movement reference."))
        self.inputs_variable_add.setStatusTip(_translate("Form", "Add to variable list with above settings."))
        self.inputs_variable_groupBox.setTitle(_translate("Form", "Variables"))
        self.inputs_variable.setStatusTip(_translate("Form", "All the variable of this mechanism."))
        self.inputs_variable_remove.setStatusTip(_translate("Form", "Delete the specified variable."))
        self.inputs_variable_speed_label.setText(_translate("Form", "Speed:"))
        self.inputs_variable_speed.setStatusTip(_translate("Form", "Speed value of the auto driver."))
        self.inputs_variable_speed.setSuffix(_translate("Form", " rpm"))
        self.extremeRebound.setStatusTip(_translate("Form", "When solver calls error, auto driver will change the direction."))
        self.extremeRebound.setText(_translate("Form", "Extreme rebound"))
        self.inputs_variable_play.setStatusTip(_translate("Form", "Start / Pause the auto driver of this variables."))
        self.inputs_variable_stop.setStatusTip(_translate("Form", "Stop the auto driver and return to original place."))
        self.inputs_record_groupBox.setTitle(_translate("Form", "Records"))
        self.inputs_record_interval_text.setText(_translate("Form", "Interval: "))
        self.inputs_record_interval.setStatusTip(_translate("Form", "Each coordinate will be recorded after this angle value."))
        self.inputs_record_interval.setSuffix(_translate("Form", "°"))
        self.inputs_record_show.setStatusTip(_translate("Form", "Show path data on the canvas."))
        self.inputs_record_show.setText(_translate("Form", "Show path data"))
        self.inputs_record.setStatusTip(_translate("Form", "All recorded path data of this workbook."))
        __sortingEnabled = self.inputs_record.isSortingEnabled()
        self.inputs_record.setSortingEnabled(False)
        item = self.inputs_record.item(0)
        item.setText(_translate("Form", "Auto preview"))
        self.inputs_record.setSortingEnabled(__sortingEnabled)
        self.inputs_record_record.setStatusTip(_translate("Form", "Start / Stop record."))
        self.inputs_record_remove.setStatusTip(_translate("Form", "Delete the specified path data."))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
