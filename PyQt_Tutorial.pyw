#!/usr/bin/env python3

# Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
# 이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
# 재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
# 선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
# 이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
# 특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
# 보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
# 대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

# 다양한 시그널 및 슬록 추가

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__version__ = "1.7.1"

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

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

        layout = QHBoxLayout()
        layout.addLayout(simple_layout)
        layout.addSpacing(30)
        layout.addLayout(signal_layout)

        self.setLayout(layout)

        self.connect(self.simple_lineEidt, SIGNAL("returnPressed()"),
                        self.Simple_UpdateLabel)
        self.connect(self.simple_boldCheckBox, SIGNAL("stateChanged(int)"),
                        self.Simple_LabelBold)
        self.connect(simple_initButton, SIGNAL("clicked()"), self.Simple_Initialize)
        self.connect(signal_spinBox, SIGNAL("countup(QString)"), 
                        signal_spinCountLabel1, SLOT("setText(QString)"))
        self.connect(signal_spinBox, SIGNAL("countup(QString)"), 
                        signal_spinCountLabel2.setText)
        self.connect(signal_spinBox, SIGNAL("countup"), 
                        signal_spinCountLabel3.setText)

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
