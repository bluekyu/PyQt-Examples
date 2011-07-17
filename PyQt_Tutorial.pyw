#!/usr/bin/env python3

# Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
# 이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
# 재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
# 선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
# 이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
# 특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
# 보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
# 대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

# Connect 구분 방법 종합

import sys
from functools import partial 
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__version__ = "1.8.4"

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # simple part
        simple_partName = QLabel("Simple Widget")
        self.simple_label = QLabel("Hello, PyQt!")
        self.simple_labelFormat = "{}"

        self.simple_lineEidt = QLineEdit("This is LineEdit Widget")
        self.simple_boldCheckBox = QCheckBox("굵게(&B)")
        simple_initButton = QPushButton("초기화(&I)")
        simple_initButton.setAutoDefault(False)
        
        simple_buttonLayout = QHBoxLayout()
        simple_buttonLayout.addWidget(simple_initButton)
        simple_buttonLayout.addStretch()

        simple_layout = QGridLayout()
        simple_layout.addWidget(simple_partName, 0, 0, 1, 2)
        simple_layout.addWidget(self.simple_label, 1, 0, 1, 2)
        simple_layout.addWidget(self.simple_lineEidt, 2, 0, 1, 2)
        simple_layout.addWidget(self.simple_boldCheckBox, 3, 0)
        simple_layout.addLayout(simple_buttonLayout, 4, 0)
        simple_layout.setRowStretch(5, 1)

        self.connect(self.simple_lineEidt, SIGNAL("returnPressed()"),
                        self.Simple_UpdateLabel)
        self.connect(self.simple_boldCheckBox, SIGNAL("stateChanged(int)"),
                        self.Simple_LabelBold)
        self.connect(simple_initButton, SIGNAL("clicked()"), self.Simple_Initialize)

        # signal part
        signal_partName = QLabel("Signal Test")
        signal_spinCountLabel1 = QLabel("0")
        signal_spinCountLabel2 = QLabel("0")
        signal_spinCountLabel3 = QLabel("0")
        signal_spinBox = MySignalSpinBox()

        signal_layout = QVBoxLayout()
        signal_layout.addWidget(signal_partName)
        signal_layout.addWidget(signal_spinCountLabel1)
        signal_layout.addWidget(signal_spinCountLabel2)
        signal_layout.addWidget(signal_spinCountLabel3)
        signal_layout.addWidget(signal_spinBox)
        signal_layout.addStretch()

        self.connect(signal_spinBox, SIGNAL("countup(QString)"), 
                        signal_spinCountLabel1, SLOT("setText(QString)"))
        self.connect(signal_spinBox, SIGNAL("countup(QString)"), 
                        signal_spinCountLabel2.setText)
        self.connect(signal_spinBox, SIGNAL("countup"), 
                        signal_spinCountLabel3.setText)

        # connect part
        connect_partName = QLabel("Connect Test")
        self.connect_label = QLabel("Button Name")
        connect_button1 = QPushButton("Button1")
        connect_button2 = QPushButton("Button2")
        connect_button3 = QPushButton("Button3")
        
        # partial connect
        self.connect(connect_button1, SIGNAL("clicked()"),
                        partial(self.Connect_ButtonClick, "Button1"))
        self.connect(connect_button2, SIGNAL("clicked()"),
                        partial(self.Connect_ButtonClick, "Button2"))
        self.connect(connect_button3, SIGNAL("clicked()"),
                        partial(self.Connect_ButtonClick, "Button3"))

        connect_button4 = QPushButton("Button4")
        connect_button5 = QPushButton("Button5")
        connect_button6 = QPushButton("Button6")

        # lambda connect
        self.connect(connect_button4, SIGNAL("clicked()"),
                lambda name="Button4": self.Connect_ButtonClick(name))
        self.connect(connect_button5, SIGNAL("clicked()"),
                lambda name="Button5": self.Connect_ButtonClick(name))
        self.connect(connect_button6, SIGNAL("clicked()"),
                lambda name="Button6": self.Connect_ButtonClick(name))

        connect_button7 = QPushButton("Button7")
        connect_button8 = QPushButton("Button8")
        connect_button9 = QPushButton("Button9")

        # sender connect
        self.connect(connect_button7, SIGNAL("clicked()"),
                        self.Connect_SenderButtonClick)
        self.connect(connect_button8, SIGNAL("clicked()"),
                        self.Connect_SenderButtonClick)
        self.connect(connect_button9, SIGNAL("clicked()"),
                        self.Connect_SenderButtonClick)

        connect_layout = QGridLayout()
        connect_layout.addWidget(connect_partName, 0, 0)
        connect_layout.addWidget(self.connect_label, 1, 0)
        connect_layout.addWidget(connect_button1, 2, 0)
        connect_layout.addWidget(connect_button2, 3, 0)
        connect_layout.addWidget(connect_button3, 4, 0)
        connect_layout.addWidget(connect_button4, 2, 1)
        connect_layout.addWidget(connect_button5, 3, 1)
        connect_layout.addWidget(connect_button6, 4, 1)
        connect_layout.addWidget(connect_button7, 2, 2)
        connect_layout.addWidget(connect_button8, 3, 2)
        connect_layout.addWidget(connect_button9, 4, 2)
        connect_layout.setRowStretch(5, 1)
        connect_layout.setColumnStretch(3, 1)

        # Main dialog part
        layout = QHBoxLayout()
        layout.addLayout(simple_layout)
        layout.addSpacing(30)
        layout.addLayout(signal_layout)
        layout.addSpacing(30)
        layout.addLayout(connect_layout)

        self.setLayout(layout)
        
        self.setWindowTitle("Main Dialog")

    def Simple_UpdateLabel(self):
        self.simple_label.setText(self.simple_labelFormat.format(
                    self.simple_lineEidt.text()))

    def Simple_LabelBold(self):
        if self.simple_boldCheckBox.isChecked():
            self.simple_labelFormat = "<b>{}</b>"
        else:
            self.simple_labelFormat = "{}"
        self.Simple_UpdateLabel()

    def Simple_Initialize(self):
        self.simple_labelFormat = "{}"
        self.simple_boldCheckBox.setCheckState(Qt.Unchecked)
        self.simple_lineEidt.setText("This is LineEdit Widget")
        self.simple_label.setText("Hello, PyQt!")

    def Connect_ButtonClick(self, buttonName):
        self.connect_label.setText(buttonName)

    def Connect_SenderButtonClick(self):
        button = self.sender()
        if not (button and isinstance(button, QPushButton)):
            return
        self.connect_label.setText(button.text())
    
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
    form = Form()
    form.show()
    app.exec_()
