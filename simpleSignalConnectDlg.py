#!/usr/bin/env python3

# Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
# 이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
# 재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
# 선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
# 이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
# 특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
# 보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
# 대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

# Simple, Signal, Connect 대화 상자들

import sys
from functools import partial 
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__version__ = "2.2.5"

class ConnectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # connect part
        self.label = QLabel("Button Name")
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        
        # partial connect
        self.connect(button1, SIGNAL("clicked()"),
                        partial(self.ButtonClick, "Button1"))
        self.connect(button2, SIGNAL("clicked()"),
                        partial(self.ButtonClick, "Button2"))
        self.connect(button3, SIGNAL("clicked()"),
                        partial(self.ButtonClick, "Button3"))

        button4 = QPushButton("Button4")
        button5 = QPushButton("Button5")
        button6 = QPushButton("Button6")

        # lambda connect
        self.connect(button4, SIGNAL("clicked()"),
                lambda name="Button4": self.ButtonClick(name))
        self.connect(button5, SIGNAL("clicked()"),
                lambda name="Button5": self.ButtonClick(name))
        self.connect(button6, SIGNAL("clicked()"),
                lambda name="Button6": self.ButtonClick(name))

        button7 = QPushButton("Button7")
        button8 = QPushButton("Button8")
        button9 = QPushButton("Button9")

        # sender connect
        self.connect(button7, SIGNAL("clicked()"),
                        self.SenderButtonClick)
        self.connect(button8, SIGNAL("clicked()"),
                        self.SenderButtonClick)
        self.connect(button9, SIGNAL("clicked()"),
                        self.SenderButtonClick)

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(button1, 1, 0)
        layout.addWidget(button2, 2, 0)
        layout.addWidget(button3, 3, 0)
        layout.addWidget(button4, 1, 1)
        layout.addWidget(button5, 2, 1)
        layout.addWidget(button6, 3, 1)
        layout.addWidget(button7, 1, 2)
        layout.addWidget(button8, 2, 2)
        layout.addWidget(button9, 3, 2)
        layout.setRowStretch(4, 1)
        layout.setColumnStretch(3, 1)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(layout)
        self.setWindowTitle("Connect Title")

    def ButtonClick(self, buttonName):
        self.label.setText(buttonName)

    def SenderButtonClick(self):
        button = self.sender()
        if not (button and isinstance(button, QPushButton)):
            return
        self.label.setText(button.text())

class SignalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # signal part
        nameLabel1 = QLabel("Qt SIGNAL - Qt SLOT: ")
        nameLabel2 = QLabel("Qt SIGNAL - Method: ")
        nameLabel3 = QLabel("Short Circuit SIGNAL - Method: ")
        spinBoxLabel = QLabel("값 변경: ")

        spinCountLabel1 = QLabel("0")
        spinCountLabel2 = QLabel("0")
        spinCountLabel3 = QLabel("0")
        spinBox = MySignalSpinBox()

        layout = QFormLayout()
        layout.addRow(nameLabel1, spinCountLabel1)
        layout.addRow(nameLabel2, spinCountLabel2)
        layout.addRow(nameLabel3, spinCountLabel3)
        layout.addRow(spinBoxLabel, spinBox)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.connect(spinBox, SIGNAL("countup(QString)"), 
                        spinCountLabel1, SLOT("setText(QString)"))
        self.connect(spinBox, SIGNAL("countup(QString)"), 
                        spinCountLabel2.setText)
        self.connect(spinBox, SIGNAL("countup"), spinCountLabel3.setText)

        self.setLayout(layout)
        self.setWindowTitle("Signal Test")

class SimpleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # simple part
        self.label = QLabel("Hello, PyQt!")
        self.labelFormat = "{}"

        self.lineEidt = QLineEdit("This is LineEdit Widget")
        self.boldCheckBox = QCheckBox("굵게(&B)")
        initButton = QPushButton("초기화(&I)")
        initButton.setAutoDefault(False)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(initButton)
        buttonLayout.addStretch()

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.lineEidt, 1, 0, 1, 2)
        layout.addWidget(self.boldCheckBox, 2, 0)
        layout.addLayout(buttonLayout, 3, 0)
        layout.setRowStretch(4, 1)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(layout)
        self.setWindowTitle("Simple Widget")

        self.connect(self.lineEidt, SIGNAL("returnPressed()"),
                        self.UpdateLabel)
        self.connect(self.boldCheckBox, SIGNAL("stateChanged(int)"),
                        self.LabelBold)
        self.connect(initButton, SIGNAL("clicked()"), self.Initialize)
    
    def UpdateLabel(self):
        self.label.setText(self.labelFormat.format(self.lineEidt.text()))

    def LabelBold(self):
        if self.boldCheckBox.isChecked():
            self.labelFormat = "<b>{}</b>"
        else:
            self.labelFormat = "{}"
        self.UpdateLabel()

    def Initialize(self):
        self.labelFormat = "{}"
        self.boldCheckBox.setCheckState(Qt.Unchecked)
        self.lineEidt.setText("This is LineEdit Widget")
        self.label.setText("Hello, PyQt!")

class MySignalSpinBox(QSpinBox):
    changedCount = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"), self.CountChanged)

    def CountChanged(self):
        self.changedCount += 1
        self.emit(SIGNAL("countup(QString)"), str(self.changedCount))
        self.emit(SIGNAL("countup"), str(self.changedCount))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    simpleDlg = SimpleDialog()
    signalDlg = SignalDialog()
    connectDlg = ConnectDialog()
    simpleDlg.show()
    signalDlg.show()
    connectDlg.show()
    app.exec_()
