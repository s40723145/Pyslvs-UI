# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/panel/run_Path_Solving.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 548)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 475, 501))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Tabs = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.Tabs.setObjectName("Tabs")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settings)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.algorithmPanel = QtWidgets.QWidget(self.settings)
        self.algorithmPanel.setObjectName("algorithmPanel")
        self.algorithmPanelLayout = QtWidgets.QHBoxLayout(self.algorithmPanel)
        self.algorithmPanelLayout.setContentsMargins(6, 6, 6, 6)
        self.algorithmPanelLayout.setObjectName("algorithmPanelLayout")
        self.label_6 = QtWidgets.QLabel(self.algorithmPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.algorithmPanelLayout.addWidget(self.label_6)
        self.type0 = QtWidgets.QRadioButton(self.algorithmPanel)
        self.type0.setChecked(True)
        self.type0.setObjectName("type0")
        self.algorithmPanelLayout.addWidget(self.type0)
        self.type1 = QtWidgets.QRadioButton(self.algorithmPanel)
        self.type1.setObjectName("type1")
        self.algorithmPanelLayout.addWidget(self.type1)
        self.type2 = QtWidgets.QRadioButton(self.algorithmPanel)
        self.type2.setObjectName("type2")
        self.algorithmPanelLayout.addWidget(self.type2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.algorithmPanelLayout.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.algorithmPanel)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.isCustomize = QtWidgets.QCheckBox(self.settings)
        self.isCustomize.setObjectName("isCustomize")
        self.verticalLayout_4.addWidget(self.isCustomize)
        self.limitPanel = QtWidgets.QWidget(self.settings)
        self.limitPanel.setEnabled(False)
        self.limitPanel.setObjectName("limitPanel")
        self.gridLayout = QtWidgets.QGridLayout(self.limitPanel)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.limitPanel)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.AxMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AxMax.setMinimum(-999.0)
        self.AxMax.setMaximum(999.0)
        self.AxMax.setProperty("value", 50.0)
        self.AxMax.setObjectName("AxMax")
        self.gridLayout.addWidget(self.AxMax, 1, 1, 1, 1)
        self.AyMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AyMax.setMinimum(-999.0)
        self.AyMax.setMaximum(999.0)
        self.AyMax.setProperty("value", 50.0)
        self.AyMax.setObjectName("AyMax")
        self.gridLayout.addWidget(self.AyMax, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.limitPanel)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.DxMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DxMax.setMinimum(-999.0)
        self.DxMax.setMaximum(999.0)
        self.DxMax.setProperty("value", 50.0)
        self.DxMax.setObjectName("DxMax")
        self.gridLayout.addWidget(self.DxMax, 3, 1, 1, 1)
        self.AxMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AxMin.setMinimum(-999.0)
        self.AxMin.setMaximum(999.0)
        self.AxMin.setProperty("value", -50.0)
        self.AxMin.setObjectName("AxMin")
        self.gridLayout.addWidget(self.AxMin, 1, 2, 1, 1)
        self.DxMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DxMin.setMinimum(-999.0)
        self.DxMin.setMaximum(999.0)
        self.DxMin.setProperty("value", -50.0)
        self.DxMin.setObjectName("DxMin")
        self.gridLayout.addWidget(self.DxMin, 3, 2, 1, 1)
        self.AyMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AyMin.setMinimum(-999.0)
        self.AyMin.setMaximum(999.0)
        self.AyMin.setProperty("value", -50.0)
        self.AyMin.setObjectName("AyMin")
        self.gridLayout.addWidget(self.AyMin, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.limitPanel)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.limitPanel)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.DyMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DyMin.setMinimum(-999.0)
        self.DyMin.setMaximum(999.0)
        self.DyMin.setProperty("value", -50.0)
        self.DyMin.setObjectName("DyMin")
        self.gridLayout.addWidget(self.DyMin, 4, 2, 1, 1)
        self.DyMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DyMax.setMinimum(-999.0)
        self.DyMax.setMaximum(999.0)
        self.DyMax.setProperty("value", 50.0)
        self.DyMax.setObjectName("DyMax")
        self.gridLayout.addWidget(self.DyMax, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.limitPanel)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.LMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.LMax.setMinimum(0.01)
        self.LMax.setMaximum(999.0)
        self.LMax.setProperty("value", 50.0)
        self.LMax.setObjectName("LMax")
        self.gridLayout.addWidget(self.LMax, 5, 1, 1, 1)
        self.LMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.LMin.setMinimum(0.01)
        self.LMin.setMaximum(999.0)
        self.LMin.setProperty("value", 5.0)
        self.LMin.setObjectName("LMin")
        self.gridLayout.addWidget(self.LMin, 5, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.limitPanel)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.limitPanel)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.limitPanel)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)
        self.AMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AMin.setMinimum(0.0)
        self.AMin.setMaximum(359.99)
        self.AMin.setProperty("value", 0.0)
        self.AMin.setObjectName("AMin")
        self.gridLayout.addWidget(self.AMin, 6, 1, 1, 1)
        self.AMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AMax.setMinimum(0.01)
        self.AMax.setMaximum(360.0)
        self.AMax.setProperty("value", 360.0)
        self.AMax.setObjectName("AMax")
        self.gridLayout.addWidget(self.AMax, 6, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.limitPanel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.Tabs.addTab(self.settings, "")
        self.path = QtWidgets.QWidget()
        self.path.setObjectName("path")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.path)
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pointNum = QtWidgets.QLabel(self.path)
        self.pointNum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pointNum.setObjectName("pointNum")
        self.horizontalLayout_2.addWidget(self.pointNum)
        self.label_5 = QtWidgets.QLabel(self.path)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Point_list = QtWidgets.QListWidget(self.path)
        self.Point_list.setObjectName("Point_list")
        self.verticalLayout_2.addWidget(self.Point_list)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.path)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.X_coordinate = QtWidgets.QLineEdit(self.path)
        self.X_coordinate.setObjectName("X_coordinate")
        self.horizontalLayout_3.addWidget(self.X_coordinate)
        self.label_4 = QtWidgets.QLabel(self.path)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.Y_coordinate = QtWidgets.QLineEdit(self.path)
        self.Y_coordinate.setObjectName("Y_coordinate")
        self.horizontalLayout_3.addWidget(self.Y_coordinate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.clearAll = QtWidgets.QPushButton(self.path)
        self.clearAll.setAutoDefault(False)
        self.clearAll.setObjectName("clearAll")
        self.verticalLayout_3.addWidget(self.clearAll)
        self.series = QtWidgets.QPushButton(self.path)
        self.series.setAutoDefault(False)
        self.series.setObjectName("series")
        self.verticalLayout_3.addWidget(self.series)
        spacerItem3 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.moveUp = QtWidgets.QPushButton(self.path)
        self.moveUp.setAutoDefault(False)
        self.moveUp.setObjectName("moveUp")
        self.verticalLayout_3.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QPushButton(self.path)
        self.moveDown.setAutoDefault(False)
        self.moveDown.setObjectName("moveDown")
        self.verticalLayout_3.addWidget(self.moveDown)
        spacerItem4 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.remove = QtWidgets.QPushButton(self.path)
        self.remove.setAutoDefault(False)
        self.remove.setObjectName("remove")
        self.verticalLayout_3.addWidget(self.remove)
        self.add = QtWidgets.QPushButton(self.path)
        self.add.setAutoDefault(False)
        self.add.setObjectName("add")
        self.verticalLayout_3.addWidget(self.add)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.Tabs.addTab(self.path, "")
        self.results = QtWidgets.QWidget()
        self.results.setObjectName("results")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.results)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.results)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.Result_list = QtWidgets.QListWidget(self.results)
        self.Result_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Result_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Result_list.setObjectName("Result_list")
        self.verticalLayout_7.addWidget(self.Result_list)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.deleteButton = QtWidgets.QPushButton(self.results)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_6.addWidget(self.deleteButton)
        self.getTimeAndFitness = QtWidgets.QPushButton(self.results)
        self.getTimeAndFitness.setEnabled(False)
        self.getTimeAndFitness.setObjectName("getTimeAndFitness")
        self.horizontalLayout_6.addWidget(self.getTimeAndFitness)
        self.mergeButton = QtWidgets.QPushButton(self.results)
        self.mergeButton.setEnabled(False)
        self.mergeButton.setObjectName("mergeButton")
        self.horizontalLayout_6.addWidget(self.mergeButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.Tabs.addTab(self.results, "")
        self.verticalLayout_6.addWidget(self.Tabs)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timePanel = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.timePanel.setObjectName("timePanel")
        self.timePanelLayout = QtWidgets.QHBoxLayout(self.timePanel)
        self.timePanelLayout.setContentsMargins(6, 0, 6, 0)
        self.timePanelLayout.setObjectName("timePanelLayout")
        self.label_7 = QtWidgets.QLabel(self.timePanel)
        self.label_7.setObjectName("label_7")
        self.timePanelLayout.addWidget(self.label_7)
        self.timeShow = QtWidgets.QLabel(self.timePanel)
        self.timeShow.setObjectName("timeShow")
        self.timePanelLayout.addWidget(self.timeShow)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timePanelLayout.addItem(spacerItem7)
        self.horizontalLayout_4.addWidget(self.timePanel)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.Generate = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Generate.setMinimumSize(QtCore.QSize(100, 0))
        self.Generate.setDefault(False)
        self.Generate.setObjectName("Generate")
        self.horizontalLayout.addWidget(self.Generate)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        self.Tabs.setCurrentIndex(0)
        self.isCustomize.toggled['bool'].connect(self.limitPanel.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "<html><head/><body><p>Dimensional Synthesis of Planar Four-bar Linkages.</p></body></html>"))
        self.label_6.setText(_translate("Form", "Algorithm: "))
        self.type0.setText(_translate("Form", "Genetic"))
        self.type1.setText(_translate("Form", "Firefly"))
        self.type2.setText(_translate("Form", "Differential Evolution"))
        self.isCustomize.setText(_translate("Form", "Customize:"))
        self.label_8.setText(_translate("Form", "Ax: "))
        self.label_9.setText(_translate("Form", "Ay: "))
        self.label_10.setText(_translate("Form", "Dx: "))
        self.label_11.setText(_translate("Form", "Dy: "))
        self.label_12.setText(_translate("Form", "Links: "))
        self.label_13.setText(_translate("Form", "Max"))
        self.label_14.setText(_translate("Form", "Min"))
        self.label_15.setText(_translate("Form", "Angle (degree):"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.settings), _translate("Form", "Settings"))
        self.pointNum.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">0</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">Point(s)</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "x: "))
        self.X_coordinate.setPlaceholderText(_translate("Form", "0.0"))
        self.label_4.setText(_translate("Form", "y: "))
        self.Y_coordinate.setPlaceholderText(_translate("Form", "0.0"))
        self.clearAll.setText(_translate("Form", "Clear All"))
        self.series.setText(_translate("Form", "Series..."))
        self.moveUp.setText(_translate("Form", "Move up"))
        self.moveDown.setText(_translate("Form", "Move down"))
        self.remove.setText(_translate("Form", "-"))
        self.add.setText(_translate("Form", "+"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.path), _translate("Form", "Path"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">This is the result from the algorithm.</span></p></body></html>"))
        self.deleteButton.setText(_translate("Form", "Delete"))
        self.getTimeAndFitness.setText(_translate("Form", "Convergence value"))
        self.mergeButton.setText(_translate("Form", "Merge"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.results), _translate("Form", "Results"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Time spent: </span></p></body></html>"))
        self.timeShow.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt\">[No record]</span></p></body></html>"))
        self.Generate.setText(_translate("Form", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

