#!/usr/bin/env python3

# Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
# 이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
# 재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
# 선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
# 이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
# 특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
# 보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
# 대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

# 체크 박스 추가

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__version__ = "1.5.2"

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel("Hello, PyQt!")
        self.labelFormat = "{}"

        self.lineEdit = QLineEdit("This is LineEdit Widget")
        self.boldCheckBox = QCheckBox("굵게(&B)")
        closeButton = QPushButton("닫기(&C)")
        closeButton.setAutoDefault(False)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.boldCheckBox)
        layout.addWidget(closeButton)
        self.setLayout(layout)

        self.connect(self.lineEdit, SIGNAL("returnPressed()"),
                        self.UpdateLabel)
        self.connect(closeButton, SIGNAL("clicked()"),
                        self, SLOT("reject()"))
        self.connect(self.boldCheckBox, SIGNAL("stateChanged(int)"),
                        self.LabelBold)

        self.setWindowTitle("Main Dialog")

    def UpdateLabel(self):
        self.label.setText(self.labelFormat.format(self.lineEdit.text()))

    def LabelBold(self):
        if self.boldCheckBox.isChecked():
            self.labelFormat = "<b>{}</b>"
        else:
            self.labelFormat = "{}"
        self.UpdateLabel()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
