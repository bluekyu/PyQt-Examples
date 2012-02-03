# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findReplaceDlg.ui'
#
# Created: Fri Feb  3 15:24:08 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FindReplaceDialog(object):
    def setupUi(self, FindReplaceDialog):
        FindReplaceDialog.setObjectName(_fromUtf8("FindReplaceDialog"))
        FindReplaceDialog.resize(388, 146)
        FindReplaceDialog.setWindowTitle(QtGui.QApplication.translate("FindReplaceDialog", "찾기 및 바꾸기", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(FindReplaceDialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.findLabel = QtGui.QLabel(FindReplaceDialog)
        self.findLabel.setText(QtGui.QApplication.translate("FindReplaceDialog", "찾을 단어:", None, QtGui.QApplication.UnicodeUTF8))
        self.findLabel.setObjectName(_fromUtf8("findLabel"))
        self.gridLayout.addWidget(self.findLabel, 0, 0, 1, 1)
        self.findLineEdit = QtGui.QLineEdit(FindReplaceDialog)
        self.findLineEdit.setObjectName(_fromUtf8("findLineEdit"))
        self.gridLayout.addWidget(self.findLineEdit, 0, 1, 1, 1)
        self.replaceLabel = QtGui.QLabel(FindReplaceDialog)
        self.replaceLabel.setText(QtGui.QApplication.translate("FindReplaceDialog", "바꿀 단어:", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceLabel.setObjectName(_fromUtf8("replaceLabel"))
        self.gridLayout.addWidget(self.replaceLabel, 1, 0, 1, 1)
        self.replaceLineEdit = QtGui.QLineEdit(FindReplaceDialog)
        self.replaceLineEdit.setObjectName(_fromUtf8("replaceLineEdit"))
        self.gridLayout.addWidget(self.replaceLineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.caseCheckBox = QtGui.QCheckBox(FindReplaceDialog)
        self.caseCheckBox.setText(QtGui.QApplication.translate("FindReplaceDialog", "대소문자 구별", None, QtGui.QApplication.UnicodeUTF8))
        self.caseCheckBox.setObjectName(_fromUtf8("caseCheckBox"))
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtGui.QCheckBox(FindReplaceDialog)
        self.wholeCheckBox.setText(QtGui.QApplication.translate("FindReplaceDialog", "단어 단위로 찾기", None, QtGui.QApplication.UnicodeUTF8))
        self.wholeCheckBox.setChecked(False)
        self.wholeCheckBox.setObjectName(_fromUtf8("wholeCheckBox"))
        self.horizontalLayout.addWidget(self.wholeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.syntaxLabel = QtGui.QLabel(FindReplaceDialog)
        self.syntaxLabel.setText(QtGui.QApplication.translate("FindReplaceDialog", "문법(&S):", None, QtGui.QApplication.UnicodeUTF8))
        self.syntaxLabel.setObjectName(_fromUtf8("syntaxLabel"))
        self.horizontalLayout_2.addWidget(self.syntaxLabel)
        self.syntaxComboBox = QtGui.QComboBox(FindReplaceDialog)
        self.syntaxComboBox.setObjectName(_fromUtf8("syntaxComboBox"))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.syntaxComboBox.setItemText(0, QtGui.QApplication.translate("FindReplaceDialog", "문자열", None, QtGui.QApplication.UnicodeUTF8))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.syntaxComboBox.setItemText(1, QtGui.QApplication.translate("FindReplaceDialog", "정규표현식", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_2.addWidget(self.syntaxComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(FindReplaceDialog)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.findButton = QtGui.QPushButton(FindReplaceDialog)
        self.findButton.setText(QtGui.QApplication.translate("FindReplaceDialog", "찾기(&F)", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.verticalLayout_2.addWidget(self.findButton)
        self.replaceButton = QtGui.QPushButton(FindReplaceDialog)
        self.replaceButton.setText(QtGui.QApplication.translate("FindReplaceDialog", "바꾸기(&R)", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.verticalLayout_2.addWidget(self.replaceButton)
        self.replaceAllButton = QtGui.QPushButton(FindReplaceDialog)
        self.replaceAllButton.setText(QtGui.QApplication.translate("FindReplaceDialog", "모두 바꾸기(&A)", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceAllButton.setObjectName(_fromUtf8("replaceAllButton"))
        self.verticalLayout_2.addWidget(self.replaceAllButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(FindReplaceDialog)
        self.closeButton.setText(QtGui.QApplication.translate("FindReplaceDialog", "닫기", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.findLabel.setBuddy(self.findLineEdit)
        self.replaceLabel.setBuddy(self.replaceLineEdit)
        self.syntaxLabel.setBuddy(self.syntaxComboBox)

        self.retranslateUi(FindReplaceDialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), FindReplaceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FindReplaceDialog)
        FindReplaceDialog.setTabOrder(self.findLineEdit, self.replaceLineEdit)
        FindReplaceDialog.setTabOrder(self.replaceLineEdit, self.caseCheckBox)
        FindReplaceDialog.setTabOrder(self.caseCheckBox, self.wholeCheckBox)
        FindReplaceDialog.setTabOrder(self.wholeCheckBox, self.syntaxComboBox)
        FindReplaceDialog.setTabOrder(self.syntaxComboBox, self.findButton)
        FindReplaceDialog.setTabOrder(self.findButton, self.replaceButton)
        FindReplaceDialog.setTabOrder(self.replaceButton, self.replaceAllButton)
        FindReplaceDialog.setTabOrder(self.replaceAllButton, self.closeButton)

    def retranslateUi(self, FindReplaceDialog):
        pass

