#!/usr/bin/env python3

# Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
# 이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
# 재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
# 선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
# 이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
# 특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
# 보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
# 대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

# Main 대화 상자

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import simpleSignalConnectDlg as sscDlg
import introDialog as introDlg

__version__ = "2.2.5"

class MainDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.liveDialog = None

        # Buttons
        simpleButton = QPushButton("Simple Dialog")
        signalButton = QPushButton("Signal Dialog")
        connectButton = QPushButton("Connect Dialog")
        dumbButton = QPushButton("Dumb Dialog")
        standardButton = QPushButton("Standard Dialog")
        smartButton = QPushButton("Smart Dialog")
        liveButton = QPushButton("Live Dialog")
        buttonLayout = QGridLayout()
        buttonLayout.addWidget(simpleButton, 0, 0)
        buttonLayout.addWidget(signalButton, 0, 1)
        buttonLayout.addWidget(connectButton, 0, 2)
        buttonLayout.addWidget(dumbButton, 1, 0)
        buttonLayout.addWidget(standardButton, 1, 1)
        buttonLayout.addWidget(smartButton, 1, 2)
        buttonLayout.addWidget(liveButton, 1, 3)
        buttonLayout.setColumnStretch(3, 1)
        self.connect(simpleButton, SIGNAL("clicked()"), self.SimpleCall)
        self.connect(signalButton, SIGNAL("clicked()"), self.SignalCall)
        self.connect(connectButton, SIGNAL("clicked()"), self.ConnectCall)
        self.connect(dumbButton, SIGNAL("clicked()"), self.DumbCall)
        self.connect(standardButton, SIGNAL("clicked()"), self.StandardCall)
        self.connect(smartButton, SIGNAL("clicked()"), self.SmartCall)
        self.connect(liveButton, SIGNAL("clicked()"), self.LiveCall)
        
        # Label
        textNameLabel = QLabel("Text Name: ")
        self.textLabel = QLabel("Hello, PyQt")
        
        # ComboBox Label
        comboBoxNameLabel = QLabel("ComboBox Name: ")
        self.comboBoxLabel = QLabel("What Item")
        labelLayout = QFormLayout()
        labelLayout.addRow(textNameLabel, self.textLabel)
        labelLayout.addRow(comboBoxNameLabel, self.comboBoxLabel)
        
        # SpinBox
        spinBoxLabel = QLabel("Spin Box(&S): ")
        self.spinBox = QSpinBox()
        spinBoxLabel.setBuddy(self.spinBox)
        self.spinBox.setRange(0, 100)
        self.spinBox.setValue(0)
        spinBoxLayout = QHBoxLayout()
        spinBoxLayout.addWidget(spinBoxLabel)
        spinBoxLayout.addWidget(self.spinBox)

        # Dial
        dialLabel = QLabel("Dial(&D): ")
        self.dial = QDial()
        dialLabel.setBuddy(self.dial)
        self.dial.setRange(0, 100)
        self.dial.setValue(0)
        self.dial.setNotchesVisible(True)
        dialLayout = QHBoxLayout()
        dialLayout.addWidget(dialLabel)
        dialLayout.addWidget(self.dial)

        # Slider
        sliderLabel = QLabel("Slider(&L): ")
        self.slider = QSlider(Qt.Horizontal)
        sliderLabel.setBuddy(self.slider)
        self.slider.setRange(0, 100)
        self.slider.setValue(0)
        sliderLayout = QHBoxLayout()
        sliderLayout.addWidget(sliderLabel)
        sliderLayout.addWidget(self.slider)

        # Widget layout
        widgetLayout = QVBoxLayout()
        widgetLayout.addLayout(labelLayout)
        widgetLayout.addLayout(spinBoxLayout)
        widgetLayout.addLayout(dialLayout)
        widgetLayout.addLayout(sliderLayout)
        widgetLayout.addStretch()

        # Main Layout
        layout = QVBoxLayout()
        layout.addLayout(buttonLayout)
        layout.addLayout(widgetLayout)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        
        self.setLayout(layout)
        self.setWindowTitle("Main Dialog")

    def SimpleCall(self):
        sscDlg.SimpleDialog(self).exec_()
       
    def SignalCall(self):
        sscDlg.SignalDialog(self).exec_()

    def ConnectCall(self):
        sscDlg.ConnectDialog(self).exec_()

    def DumbCall(self):
        dialog = introDlg.DumbDialog(self)
        comboBoxIndex = dialog.comboBox.findText(self.comboBoxLabel.text())
        if comboBoxIndex == -1:
            comboBoxIndex = 0
        dialog.comboBox.setCurrentIndex(comboBoxIndex)
        dialog.textLineEdit.setText(self.textLabel.text())
        dialog.slider.setValue(self.spinBox.value())
        
        if dialog.exec_():
            self.comboBoxLabel.setText(dialog.comboBox.currentText())
            self.textLabel.setText(dialog.textLineEdit.text())
            self.spinBox.setValue(dialog.slider.value())

    def StandardCall(self):
        values = {"label" : self.textLabel.text(), 
                    "comboBox" : self.comboBoxLabel.text(),
                    "dial" : self.dial.value()}
        dialog = introDlg.StandardDialog(values, self)
        if dialog.exec_():
            values = dialog.getResult()
            self.textLabel.setText(values["label"])
            self.comboBoxLabel.setText(values["comboBox"])
            self.dial.setValue(values["dial"])

    def SmartCall(self):
        def update():
            self.textLabel.setText(self.values["label"])
            self.comboBoxLabel.setText(self.values["comboBox"])
            self.slider.setValue(self.values["slider"])

        self.values = {"label" : self.textLabel.text(), 
                        "comboBox" : self.comboBoxLabel.text(),
                        "slider" : self.slider.value()}
        dialog = introDlg.SmartDialog(self.values, self)
        self.connect(dialog, SIGNAL("changed"), update)
        dialog.show()

    def LiveCall(self):
        def update():
            self.textLabel.setText(self.values["label"])
            self.comboBoxLabel.setText(self.values["comboBox"])
            self.slider.setValue(self.values["slider"])

        self.values = {"label" : self.textLabel.text(), 
                        "comboBox" : self.comboBoxLabel.text(),
                        "slider" : self.slider.value()}
        if self.liveDialog is None:
            self.liveDialog = introDlg.LiveDialog(self.values, update, self)
        self.liveDialog.refresh(self.values)
        self.liveDialog.show()
        self.liveDialog.raise_()
        self.liveDialog.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainDlg = MainDialog()
    mainDlg.show()
    app.exec_()
