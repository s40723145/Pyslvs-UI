# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/info/info.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About_Dialog(object):
    def setupUi(self, About_Dialog):
        About_Dialog.setObjectName("About_Dialog")
        About_Dialog.setEnabled(True)
        About_Dialog.resize(500, 480)
        About_Dialog.setMinimumSize(QtCore.QSize(500, 480))
        About_Dialog.setMaximumSize(QtCore.QSize(500, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About_Dialog.setWindowIcon(icon)
        About_Dialog.setSizeGripEnabled(False)
        About_Dialog.setModal(True)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(About_Dialog)
        self.verticalLayout_7.setContentsMargins(-1, 6, 6, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.iconLabel = QtWidgets.QLabel(About_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setText("")
        self.iconLabel.setPixmap(QtGui.QPixmap(":/icons/main.png"))
        self.iconLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.iconLabel.setObjectName("iconLabel")
        self.verticalLayout_2.addWidget(self.iconLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Title = QtWidgets.QLabel(About_Dialog)
        self.Title.setText("")
        self.Title.setObjectName("Title")
        self.verticalLayout_3.addWidget(self.Title)
        self.tabWidget = QtWidgets.QTabWidget(About_Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.IntroductionTab = QtWidgets.QWidget()
        self.IntroductionTab.setObjectName("IntroductionTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.IntroductionTab)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.IntroductionTab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 407, 353))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Content = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Content.sizePolicy().hasHeightForWidth())
        self.Content.setSizePolicy(sizePolicy)
        self.Content.setText("")
        self.Content.setTextFormat(QtCore.Qt.RichText)
        self.Content.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Content.setWordWrap(True)
        self.Content.setOpenExternalLinks(True)
        self.Content.setObjectName("Content")
        self.verticalLayout.addWidget(self.Content)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.IntroductionTab, "")
        self.license = QtWidgets.QWidget()
        self.license.setObjectName("license")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.license)
        self.verticalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QtWidgets.QLabel(self.license)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.tabWidget.addTab(self.license, "")
        self.VersionsTab = QtWidgets.QWidget()
        self.VersionsTab.setObjectName("VersionsTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.VersionsTab)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.VersionsTab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 407, 353))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Versions = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Versions.sizePolicy().hasHeightForWidth())
        self.Versions.setSizePolicy(sizePolicy)
        self.Versions.setText("")
        self.Versions.setTextFormat(QtCore.Qt.RichText)
        self.Versions.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Versions.setWordWrap(True)
        self.Versions.setOpenExternalLinks(True)
        self.Versions.setObjectName("Versions")
        self.verticalLayout_5.addWidget(self.Versions)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.VersionsTab, "")
        self.ArgumentsTab = QtWidgets.QWidget()
        self.ArgumentsTab.setObjectName("ArgumentsTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ArgumentsTab)
        self.verticalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.ArgumentsTab)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 407, 353))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Arguments = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Arguments.sizePolicy().hasHeightForWidth())
        self.Arguments.setSizePolicy(sizePolicy)
        self.Arguments.setText("")
        self.Arguments.setTextFormat(QtCore.Qt.RichText)
        self.Arguments.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Arguments.setWordWrap(True)
        self.Arguments.setOpenExternalLinks(True)
        self.Arguments.setObjectName("Arguments")
        self.verticalLayout_8.addWidget(self.Arguments)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.ArgumentsTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(About_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.retranslateUi(About_Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(About_Dialog.accept)
        self.buttonBox.rejected.connect(About_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(About_Dialog)

    def retranslateUi(self, About_Dialog):
        _translate = QtCore.QCoreApplication.translate
        About_Dialog.setWindowTitle(_translate("About_Dialog", "About Pyslvs"))
        self.iconLabel.setWhatsThis(_translate("About_Dialog", "Pyslvs Icon!"))
        self.Content.setWhatsThis(_translate("About_Dialog", "Version Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IntroductionTab), _translate("About_Dialog", "Introduction"))
        self.label.setText(_translate("About_Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">This program is free software; you can redistribute it and/or modify it under the terms of the Affero General Public License (AGPL) as published by Affero, Inc. version 3. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.license), _translate("About_Dialog", "LICENSE"))
        self.Versions.setWhatsThis(_translate("About_Dialog", "Version Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VersionsTab), _translate("About_Dialog", "Versions"))
        self.Arguments.setWhatsThis(_translate("About_Dialog", "Version Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ArgumentsTab), _translate("About_Dialog", "Arguments"))
        self.buttonBox.setWhatsThis(_translate("About_Dialog", "Click to exit"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About_Dialog = QtWidgets.QDialog()
    ui = Ui_About_Dialog()
    ui.setupUi(About_Dialog)
    About_Dialog.show()
    sys.exit(app.exec_())

