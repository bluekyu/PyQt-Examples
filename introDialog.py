#!/usr/bin/env python3

"""
Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

대화 상자를 소개하는 부분에 대한 프로그램.
호출된 대화 상자를 생성하는 메소드들로 구성되어 있음.
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__version__ = "3.1.1"
__author__ = "YoungUk Kim"
__date__ = "09.18.2011"

class LiveDialog(QDialog):
    """Live 대화 상자 객체"""

    def __init__(self, values, update, parent=None):
        """대화 상자 초기화"""

        super().__init__(parent)

        liveLineEditLabel = QLabel("Main 레이블 변경(&L): ")
        self.liveLineEdit = QLineEdit(values["labelText"])
        liveLineEditLabel.setBuddy(self.liveLineEdit)

        liveComboBoxLabel = QLabel("Main 콤보 상자 변경(&C): ")
        self.liveComboBox = QComboBox()
        liveComboBoxLabel.setBuddy(self.liveComboBox)
        self.liveComboBox.addItems(values["comboBoxItems"])
        self.liveComboBox.setCurrentIndex(values["comboBoxIndex"])

        liveSliderEditLabel = QLabel("Main 슬라이더 변경(&S): ")
        self.liveSliderEdit = QLineEdit(str(values["sliderValue"]))
        liveSliderEditLabel.setBuddy(self.liveSliderEdit)
        maxLen = max(len(str(abs(values["sliderMaximum"]))), 
                    len(str(abs(values["sliderMinimum"]))))
        self.liveSliderEdit.setInputMask("#" + "0" * maxLen)

        self.values = values
        self.update = update

        widgetLayout = QFormLayout()
        widgetLayout.addRow(liveLineEditLabel, self.liveLineEdit)
        widgetLayout.addRow(liveSliderEditLabel, self.liveSliderEdit)
        widgetLayout.addRow(liveComboBoxLabel, self.liveComboBox)

        self.connect(self.liveLineEdit, SIGNAL("textEdited(QString)"),
                        self.apply)
        self.connect(self.liveSliderEdit, SIGNAL("textEdited(QString)"),
                        self.checkFix)
        self.connect(self.liveComboBox, SIGNAL("currentIndexChanged(int)"),
                        self.apply)

        layout = QVBoxLayout()
        layout.addLayout(widgetLayout)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(layout)
        self.setWindowTitle("Live Dialog")

    def checkFix(self):
        sliderEditValueText = self.liveSliderEdit.text()
        if sliderEditValueText == "-":
            self.liveSliderEdit.setText("-0")
            self.liveSliderEdit.setCursorPosition(1)
            self.liveSliderEdit.setFocus()
        elif len(sliderEditValueText) == 0: 
            self.liveSliderEdit.setText("0")
            self.liveSliderEdit.setCursorPosition(0)
            self.liveSliderEdit.setFocus()
        elif int(sliderEditValueText) < self.values["sliderMinimum"] or \
            int(sliderEditValueText) > self.values["sliderMaximum"]:
            self.liveSliderEdit.backspace()
               
        self.apply()

    def apply(self):
        sliderEditValue = int(self.liveSliderEdit.text())
        self.values["labelText"] = self.liveLineEdit.text()
        self.values["comboBoxIndex"] = self.liveComboBox.currentIndex()
        self.values["sliderValue"] = sliderEditValue
        self.update()

class SmartDialog(QDialog):
    def __init__(self, values, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        smartLineEditLabel = QLabel("Main 레이블 변경(&L): ")
        self.smartLineEdit = QLineEdit(values["labelText"])
        smartLineEditLabel.setBuddy(self.smartLineEdit)

        smartComboBoxLabel = QLabel("Main 콤보 상자 변경(&C): ")
        self.smartComboBox = QComboBox()
        smartComboBoxLabel.setBuddy(self.smartComboBox)
        self.smartComboBox.addItems(values["comboBoxItems"])
        self.smartComboBox.setCurrentIndex(values["comboBoxIndex"])

        smartSliderEditLabel = QLabel("Main 슬라이더 변경(&S): ")
        self.smartSliderEdit = QLineEdit(str(values["sliderValue"]))
        smartSliderEditLabel.setBuddy(self.smartSliderEdit)
        maxLen = max(len(str(abs(values["sliderMaximum"]))), 
                    len(str(abs(values["sliderMinimum"]))))
        self.smartSliderEdit.setInputMask("#" + "0" * maxLen)

        self.values = values

        widgetLayout = QFormLayout()
        widgetLayout.addRow(smartLineEditLabel, self.smartLineEdit)
        widgetLayout.addRow(smartSliderEditLabel, self.smartSliderEdit)
        widgetLayout.addRow(smartComboBoxLabel, self.smartComboBox)

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
            sliderEditValue = int(self.smartSliderEdit.text())
            sliderMaximum = self.values["sliderMaximum"]
            sliderMinimum = self.values["sliderMinimum"]
            if sliderEditValue < sliderMinimum or \
                sliderEditValue > sliderMaximum:
                raise OutOfRangeNumberError("This value is out of range "
                        "from {} to {}.".format(sliderMinimum, sliderMaximum))
        except ValueError:
            QMessageBox.warning(self, "Number is Empty",
                                    "This number may not be empty")
            self.smartSliderEdit.selectAll()
            self.smartSliderEdit.setFocus()
            return
        except OutOfRangeNumberError as e:
            QMessageBox.warning(self, "Out of Range of number", str(e))
            self.smartSliderEdit.selectAll()
            self.smartSliderEdit.setFocus()
            return

        self.values["labelText"] = self.smartLineEdit.text()
        self.values["comboBoxIndex"] = self.smartComboBox.currentIndex()
        self.values["sliderValue"] = sliderEditValue
        self.emit(SIGNAL("changed"))

class StandardDialog(QDialog):
    def __init__(self, values, parent=None):
        super().__init__(parent)

        standardLineEditLabel = QLabel("Main 레이블 변경(&L): ")
        self.standardLineEdit = QLineEdit(values["labelText"])
        standardLineEditLabel.setBuddy(self.standardLineEdit)
        
        standardComboBoxLabel = QLabel("Main 콤보 상자 변경(&C): ")
        self.standardComboBox = QComboBox()
        standardComboBoxLabel.setBuddy(self.standardComboBox)
        self.standardComboBox.addItems(values["comboBoxItems"])
        self.standardComboBox.setCurrentIndex(values["comboBoxIndex"])

        standardDialEditLabel = QLabel("Main 다이얼 변경(&D): ")
        self.standardDialEdit = QLineEdit(str(values["dialValue"]))
        standardDialEditLabel.setBuddy(self.standardDialEdit)

        self.values = values.copy()

        widgetLayout = QFormLayout()
        widgetLayout.addRow(standardLineEditLabel, self.standardLineEdit)
        widgetLayout.addRow(standardDialEditLabel, self.standardDialEdit)
        widgetLayout.addRow(standardComboBoxLabel, self.standardComboBox)

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
        class OutOfRangeError(Exception): pass

        try:
            dialEditValue = int(self.standardDialEdit.text())
            dialMaximum = self.values["dialMaximum"]
            dialMinimum = self.values["dialMinimum"]
            if dialEditValue < dialMinimum or dialEditValue > dialMaximum:
                raise OutOfRangeError("This value is out of a range "
                            "from {} to {}.".format(dialMinimum, dialMaximum))
        except ValueError:
            QMessageBox.warning(self, "Invalid Number Format",
                                    "This is not a integer")
            self.standardDialEdit.selectAll()
            self.standardDialEdit.setFocus()
            return
        except OutOfRangeError as e:
            QMessageBox.warning(self, "Out of Range", str(e))
            self.standardDialEdit.selectAll()
            self.standardDialEdit.setFocus()
            return

        self.values["labelText"] = self.standardLineEdit.text()
        self.values["comboBoxIndex"] = self.standardComboBox.currentIndex()
        self.values["dialValue"] = dialEditValue
        QDialog.accept(self)

    def getValues(self):
        return self.values

class DumbDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        dumbLineEditLabel = QLabel("Main 레이블 변경(&L): ")
        self.dumbLineEdit = QLineEdit()
        dumbLineEditLabel.setBuddy(self.dumbLineEdit)

        dumbComboBoxLabel = QLabel("Main 콤보 상자 변경(&C): ")
        self.dumbComboBox = QComboBox()
        dumbComboBoxLabel.setBuddy(self.dumbComboBox)

        dumbSliderLabel = QLabel("Main 슬라이더 변경(&S): ")
        self.dumbSlider = QSlider(Qt.Horizontal)
        dumbSliderLabel.setBuddy(self.dumbSlider)

        widgetLayout = QFormLayout()
        widgetLayout.addRow(dumbLineEditLabel, self.dumbLineEdit)
        widgetLayout.addRow(dumbComboBoxLabel, self.dumbComboBox)
        widgetLayout.addRow(dumbSliderLabel, self.dumbSlider)

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
