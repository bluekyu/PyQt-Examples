#!/usr/bin/env python3

# Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
# 이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
# 재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
# 선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
# 이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
# 특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
# 보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
# 대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

# 대화 상자 종류들

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__version__ = "2.2.5"

class LiveDialog(QDialog):
    def __init__(self, arg, update, parent=None):
        super().__init__(parent)

        textEditLabel = QLabel("Main 레이블 변경: ")
        self.textLineEdit = QLineEdit(arg["label"])
        
        valueEditLabel = QLabel("Main 슬라이더 변경: ")
        self.valueLineEdit = QLineEdit(str(arg["slider"]))
        self.valueLineEdit.setInputMask("900")

        comboBoxLabel = QLabel("Combo Box(&C): ")
        self.comboBox = QComboBox()
        comboBoxLabel.setBuddy(self.comboBox)
        for item in ["item1", "item2", "item3", "item4", "item5"]:
            self.comboBox.addItem(item)
        comboBoxIndex = self.comboBox.findText(arg["comboBox"])
        if comboBoxIndex == -1:
            comboBoxIndex = 0
        self.comboBox.setCurrentIndex(comboBoxIndex)

        self.result = arg
        self.update = update

        widgetLayout = QFormLayout()
        widgetLayout.addRow(textEditLabel, self.textLineEdit)
        widgetLayout.addRow(valueEditLabel, self.valueLineEdit)
        widgetLayout.addRow(comboBoxLabel, self.comboBox)

        self.connect(self.textLineEdit, SIGNAL("textEdited(QString)"),
                        self.apply)
        self.connect(self.valueLineEdit, SIGNAL("textEdited(QString)"),
                        self.checkFix)
        self.connect(self.comboBox, SIGNAL("currentIndexChanged(int)"),
                        self.apply)

        layout = QVBoxLayout()
        layout.addLayout(widgetLayout)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(layout)
        self.setWindowTitle("Live Dialog")

    def checkFix(self):
        valueText = self.valueLineEdit.text()
        if len(valueText) == 0 or int(valueText) < 0 or int(valueText) > 100:
            self.valueLineEdit.setText("0")
            self.valueLineEdit.selectAll()
            self.valueLineEdit.setFocus()
        self.apply()

    def apply(self):
        value = int(self.valueLineEdit.text())
        self.result["label"] = self.textLineEdit.text()
        self.result["comboBox"] = self.comboBox.currentText()
        self.result["slider"] = value
        self.update()
    
    def refresh(self, arg):
        self.textLineEdit.setText(arg["label"])
        self.valueLineEdit.setText(str(arg["slider"]))
        comboBoxIndex = self.comboBox.findText(arg["comboBox"])
        if comboBoxIndex == -1:
            comboBoxIndex = 0
        self.comboBox.setCurrentIndex(comboBoxIndex)
        self.result = arg

class SmartDialog(QDialog):
    def __init__(self, arg, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        textEditLabel = QLabel("Main 레이블 변경: ")
        self.textLineEdit = QLineEdit(arg["label"])
        
        valueEditLabel = QLabel("Main 슬라이더 변경: ")
        self.valueLineEdit = QLineEdit(str(arg["slider"]))
        self.valueLineEdit.setInputMask("900")

        comboBoxLabel = QLabel("Combo Box(&C): ")
        self.comboBox = QComboBox()
        comboBoxLabel.setBuddy(self.comboBox)
        for item in ["item1", "item2", "item3", "item4", "item5"]:
            self.comboBox.addItem(item)
        comboBoxIndex = self.comboBox.findText(arg["comboBox"])
        if comboBoxIndex == -1:
            comboBoxIndex = 0
        self.comboBox.setCurrentIndex(comboBoxIndex)

        self.result = arg

        widgetLayout = QFormLayout()
        widgetLayout.addRow(textEditLabel, self.textLineEdit)
        widgetLayout.addRow(valueEditLabel, self.valueLineEdit)
        widgetLayout.addRow(comboBoxLabel, self.comboBox)

        applyButton = QPushButton("적용(&A)")
        cancelButton = QPushButton("취소")
        buttonBox = QDialogButtonBox()
        buttonBox.addButton(applyButton, QDialogButtonBox.ApplyRole)
        buttonBox.addButton(cancelButton, QDialogButtonBox.RejectRole)
        applyButton.setDefault(True)
        self.connect(applyButton, SIGNAL("clicked()"), self.apply)
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))

        layout = QVBoxLayout()
        layout.addLayout(widgetLayout)
        layout.addWidget(buttonBox)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(layout)
        self.setWindowTitle("Smart Dialog")

    def apply(self):
        class OutOfRangeNumberError(Exception): pass

        try:
            value = int(self.valueLineEdit.text())
            if value < 0 or value > 100:
                raise OutOfRangeNumberError("This value is out of range "
                                            "from 0 to 100.")
        except ValueError:
            QMessageBox.warning(self, "Value is Empty",
                                    "This may not be empty")
            self.valueLineEdit.selectAll()
            self.valueLineEdit.setFocus()
            return
        except OutOfRangeNumberError as e:
            QMessageBox.warning(self, "Out of Range of number", str(e))
            self.valueLineEdit.selectAll()
            self.valueLineEdit.setFocus()
            return

        self.result["label"] = self.textLineEdit.text()
        self.result["comboBox"] = self.comboBox.currentText()
        self.result["slider"] = value
        self.emit(SIGNAL("changed"))

class StandardDialog(QDialog):
    def __init__(self, arg, parent=None):
        super().__init__(parent)

        textEditLabel = QLabel("Main 레이블 변경: ")
        self.textLineEdit = QLineEdit(arg["label"])
        
        valueEditLabel = QLabel("Main 다이얼 변경: ")
        self.valueLineEdit = QLineEdit(str(arg["dial"]))

        comboBoxLabel = QLabel("Combo Box(&C): ")
        self.comboBox = QComboBox()
        comboBoxLabel.setBuddy(self.comboBox)
        for item in ["item1", "item2", "item3", "item4", "item5"]:
            self.comboBox.addItem(item)
        comboBoxIndex = self.comboBox.findText(arg["comboBox"])
        if comboBoxIndex == -1:
            comboBoxIndex = 0
        self.comboBox.setCurrentIndex(comboBoxIndex)

        self.result = arg.copy()

        widgetLayout = QFormLayout()
        widgetLayout.addRow(textEditLabel, self.textLineEdit)
        widgetLayout.addRow(valueEditLabel, self.valueLineEdit)
        widgetLayout.addRow(comboBoxLabel, self.comboBox)

        okButton = QPushButton("확인(&O)")
        cancelButton = QPushButton("취소")
        buttonBox = QDialogButtonBox()
        buttonBox.addButton(okButton, QDialogButtonBox.AcceptRole)
        buttonBox.addButton(cancelButton, QDialogButtonBox.RejectRole)
        okButton.setDefault(True)
        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))

        layout = QVBoxLayout()
        layout.addLayout(widgetLayout)
        layout.addWidget(buttonBox)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(layout)
        self.setWindowTitle("Standard Dialog")

    def accept(self):
        class OutOfRangeNumberError(Exception): pass

        try:
            value = int(self.valueLineEdit.text())
            if value < 0 or value > 100:
                raise OutOfRangeNumberError("This value is out of range "
                                            "from 0 to 100.")
        except ValueError:
            QMessageBox.warning(self, "Invalid number format",
                                    "This is not a integer")
            self.valueLineEdit.selectAll()
            self.valueLineEdit.setFocus()
            return
        except OutOfRangeNumberError as e:
            QMessageBox.warning(self, "Out of Range of number", str(e))
            self.valueLineEdit.selectAll()
            self.valueLineEdit.setFocus()
            return

        self.result["label"] = self.textLineEdit.text()
        self.result["comboBox"] = self.comboBox.currentText()
        self.result["dial"] = value
        QDialog.accept(self)

    def getResult(self):
        return self.result

class DumbDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        textEditLabel = QLabel("Main 레이블 변경: ")
        self.textLineEdit = QLineEdit("Hello, PyQt!")
        
        valueEditLabel = QLabel("Main 값 변경: ")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)

        comboBoxLabel = QLabel("Combo Box(&C): ")
        self.comboBox = QComboBox()
        comboBoxLabel.setBuddy(self.comboBox)
        for item in ["item1", "item2", "item3", "item4", "item5"]:
            self.comboBox.addItem(item)

        widgetLayout = QFormLayout()
        widgetLayout.addRow(textEditLabel, self.textLineEdit)
        widgetLayout.addRow(comboBoxLabel, self.comboBox)
        widgetLayout.addRow(valueEditLabel, self.slider)

        okButton = QPushButton("확인(&O)")
        cancelButton = QPushButton("취소")
        buttonBox = QDialogButtonBox()
        buttonBox.addButton(okButton, QDialogButtonBox.AcceptRole)
        buttonBox.addButton(cancelButton, QDialogButtonBox.RejectRole)
        okButton.setDefault(True)
        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))

        layout = QVBoxLayout()
        layout.addLayout(widgetLayout)
        layout.addWidget(buttonBox) 
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(layout)
        self.setWindowTitle("Dumb Dialog") 

if __name__ == "__main__":
    pass
