#!/usr/bin/env python3

# Copyright (C) 2011년 bluekyu (http://www.bluekyu.me/)
# 이 프로그램은 자유 소프트웨어입니다. 소프트웨어의 피양도자는 자유 소프트웨어
# 재단이 공표한 GNU 일반 공중 사용 허가서 2판 또는 그 이후 판을 임의로
# 선택해서, 그 규정에 따라 프로그램을 개작하거나 재배포할 수 있습니다.
# 이 프로그램은 유용하게 사용될 수 있으리라는 희망에서 배포되고 있지만,
# 특정한 목적에 맞는 적합성 여부나 판매용으로 사용할 수 있으리라는 묵시적인
# 보증을 포함한 어떠한 형태의 보증도 제공하지 않습니다. 보다 자세한 사항에
# 대해서는 GNU 일반 공중 사용 허가서를 참고하시기 바랍니다.

# Main 윈도우

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import simpleSignalConnectDlg as sscDlg
import introDialog as introDlg

__version__ = "3.1.1"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ### Buttons ###
        buttonGroup = QGroupBox()
        buttonGroup.setTitle("버튼")
        buttonLayout = QFormLayout()
        buttonGroup.setLayout(buttonLayout)

        # Push Button
        mainButtonLabel = QLabel("버튼: ")
        self.mainButton = QPushButton("버튼(&B)")
        buttonMessageBox = QMessageBox(QMessageBox.Information, "버튼 메시지",
                            "버튼이 클릭 됨", QMessageBox.Ok, self)
        self.connect(self.mainButton, SIGNAL("clicked()"), buttonMessageBox.open)

        # Check Box
        mainCheckBoxLabel = QLabel("체크 상자: ")
        self.mainCheckBox = QCheckBox("체크(&K)")
        
        buttonLayout.addRow(mainButtonLabel, self.mainButton)
        buttonLayout.addRow(mainCheckBoxLabel, self.mainCheckBox)

        ### Input Widgets ###
        inputGroup = QGroupBox()
        inputGroup.setTitle("입력 위젯")
        inputLayout = QFormLayout()
        inputGroup.setLayout(inputLayout)
        
        # Combo Box
        mainComboBoxLabel = QLabel("콤보 상자(&C): ")
        self.mainComboBox = QComboBox()
        mainComboBoxLabel.setBuddy(self.mainComboBox)
        self.mainComboBox.addItems(["항목 1", "항목 2", "항목 3", "항목 4"])

        # Line Edit
        mainLineEditLabel = QLabel("라인 편집(&I): ")
        self.mainLineEdit = QLineEdit("편집 내용")
        mainLineEditLabel.setBuddy(self.mainLineEdit)

        # Spin Box
        mainSpinBoxLabel = QLabel("스핀 상자(&S): ")
        self.mainSpinBox = QSpinBox()
        mainSpinBoxLabel.setBuddy(self.mainSpinBox)
        self.mainSpinBox.setRange(-1000, 1000)
        self.mainSpinBox.setValue(0)
        self.mainSpinBox.setPrefix("Prefix ")
        self.mainSpinBox.setSuffix(" Suffix")
        self.mainSpinBox.setAccelerated(True)

        # Dial
        mainDialLabel = QLabel("다이얼(&D): ")
        self.mainDial = QDial()
        mainDialLabel.setBuddy(self.mainDial)
        self.mainDial.setMinimumSize(100, 100)
        self.mainDial.setRange(-100, 100)
        self.mainDial.setValue(0)
        self.mainDial.setNotchesVisible(True)

        # Slider
        mainSliderLabel = QLabel("슬라이더(&L): ")
        self.mainSlider = QSlider(Qt.Horizontal)
        mainSliderLabel.setBuddy(self.mainSlider)
        self.mainSlider.setRange(-100, 100)
        self.mainSlider.setValue(0)
        self.mainSlider.setTickPosition(QSlider.TicksBelow)

        inputLayout.addRow(mainComboBoxLabel, self.mainComboBox)
        inputLayout.addRow(mainLineEditLabel, self.mainLineEdit)
        inputLayout.addRow(mainSpinBoxLabel, self.mainSpinBox)
        inputLayout.addRow(mainDialLabel, self.mainDial)
        inputLayout.addRow(mainSliderLabel, self.mainSlider)

        ### Display Widgets ###
        displayGroup = QGroupBox()
        displayGroup.setTitle("표시 위젯")
        displayLayout = QFormLayout()
        displayGroup.setLayout(displayLayout)

        mainLabelLabel = QLabel("레이블: ")
        self.mainLabel = QLabel("레이블 내용")

        displayLayout.addRow(mainLabelLabel, self.mainLabel)

        ### Actions ###
        # Simple Dialog Open
        simpleDialogAction = QAction("단순 대화상자", self)
        simpleDialogAction.setShortcut("Ctrl+S")
        simpleDialogHelp = "단순한 대화 상자를 엽니다"
        simpleDialogAction.setToolTip(simpleDialogHelp)
        simpleDialogAction.setStatusTip(simpleDialogHelp)
        self.connect(simpleDialogAction, SIGNAL("triggered()"),
                        lambda : sscDlg.SimpleDialog(self).exec_())

        # Signal Dialog Open
        signalDialogAction = QAction("시그널 대화상자", self)
        signalDialogAction.setShortcut("Ctrl+G")
        signalDialogHelp = "여러 시그널로 된 대화 상자를 엽니다"
        signalDialogAction.setToolTip(signalDialogHelp)
        signalDialogAction.setStatusTip(signalDialogHelp)
        self.connect(signalDialogAction, SIGNAL("triggered()"),
                        lambda : sscDlg.SignalDialog(self).exec_())

        # Connect Dialog Open
        connectDialogAction = QAction("Connect 대화상자", self)
        connectDialogAction.setShortcut("Ctrl+E")
        connectDialogHelp = "여러 연결 방식을 갖는 버튼 대화 상자를 엽니다"
        connectDialogAction.setToolTip(connectDialogHelp)
        connectDialogAction.setStatusTip(connectDialogHelp)
        self.connect(connectDialogAction, SIGNAL("triggered()"),
                        lambda : sscDlg.ConnectDialog(self).exec_())

        # Dumb Dialog Open
        dumbDialogAction = QAction("Dumb 대화상자", self)
        dumbDialogAction.setShortcut("Ctrl+M")
        dumbDialogHelp = "Dumb 및 Modal 대화 상자를 엽니다"
        dumbDialogAction.setToolTip(dumbDialogHelp)
        dumbDialogAction.setStatusTip(dumbDialogHelp)
        self.connect(dumbDialogAction, SIGNAL("triggered()"), self.DumbCall)

        # Standard Dialog Open
        standardDialogAction = QAction("Standard 대화상자", self)
        standardDialogAction.setShortcut("Ctrl+R")
        standardDialogHelp = "Standard 및 Modal 대화 상자를 엽니다"
        standardDialogAction.setToolTip(standardDialogHelp)
        standardDialogAction.setStatusTip(standardDialogHelp)
        self.connect(standardDialogAction, SIGNAL("triggered()"), self.StandardCall)

        # Smart Dialog Open
        smartDialogAction = QAction("Smart 대화상자", self)
        smartDialogAction.setShortcut("Ctrl+M")
        smartDialogHelp = "Smart 및 Modaless 대화 상자를 엽니다"
        smartDialogAction.setToolTip(smartDialogHelp)
        smartDialogAction.setStatusTip(smartDialogHelp)
        self.connect(smartDialogAction, SIGNAL("triggered()"), self.SmartCall)

        # Live Dialog Open
        liveDialogAction = QAction("Live 대화상자", self)
        liveDialogAction.setShortcut("Ctrl+L")
        liveDialogHelp = "Live 및 Modaless 대화 상자를 엽니다"
        liveDialogAction.setToolTip(liveDialogHelp)
        liveDialogAction.setStatusTip(liveDialogHelp)
        self.connect(liveDialogAction, SIGNAL("triggered()"), self.LiveCall)

        ### Menu Bar ###
        # 대화 상자
        dialogMenu = self.menuBar().addMenu("대화 상자(&A)")
        dialogMenuHelp = "여러 대화 상자 종류들을 포함합니다"
        dialogMenu.addAction(simpleDialogAction)
        dialogMenu.addAction(signalDialogAction)
        dialogMenu.addAction(connectDialogAction)
        dialogMenu.addSeparator()
        dialogMenu.addAction(dumbDialogAction)
        dialogMenu.addAction(standardDialogAction)
        dialogMenu.addAction(smartDialogAction)
        dialogMenu.addAction(liveDialogAction)

        ### Status Bar ###
        status = self.statusBar()
        status.showMessage("실행 완료", 5000)
        
        ### Main ###
        self.liveDialog = None

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(buttonGroup)
        mainLayout.addWidget(inputGroup)
        mainLayout.addWidget(displayGroup)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

        self.setWindowTitle("Main Window")

    def DumbCall(self):
        dialog = introDlg.DumbDialog(self)
        dialog.dumbLineEdit.setText(self.mainLabel.text())
        dialog.dumbComboBox.clear()
        for idx in range(len(self.mainComboBox)):
            dialog.dumbComboBox.addItem(self.mainComboBox.itemText(idx))
        dialog.dumbComboBox.setCurrentIndex(self.mainComboBox.currentIndex())
        dialog.dumbSlider.setMaximum(self.mainSlider.maximum())
        dialog.dumbSlider.setMinimum(self.mainSlider.minimum())
        dialog.dumbSlider.setValue(self.mainSlider.value())
        
        if dialog.exec_():
            self.mainLabel.setText(dialog.dumbLineEdit.text())
            self.mainComboBox.setCurrentIndex(
                            dialog.dumbComboBox.currentIndex())
            self.mainSlider.setValue(dialog.dumbSlider.value())

    def StandardCall(self):
        mainComboBoxItems = [self.mainComboBox.itemText(idx) for idx in
                                range(len(self.mainComboBox))]
        values = {"labelText": self.mainLabel.text(),
                "comboBoxItems": mainComboBoxItems,
                "comboBoxIndex": self.mainComboBox.currentIndex(),
                "dialValue": self.mainDial.value(),
                "dialMaximum": self.mainDial.maximum(),
                "dialMinimum": self.mainDial.minimum()}
        dialog = introDlg.StandardDialog(values, self)

        if dialog.exec_():
            values = dialog.getValues()
            self.mainLabel.setText(values["labelText"])
            self.mainComboBox.setCurrentIndex(values["comboBoxIndex"])
            self.mainDial.setValue(values["dialValue"])

    def SmartCall(self):
        mainComboBoxItems = [self.mainComboBox.itemText(idx) for idx in
                                range(len(self.mainComboBox))]
        def update():
            self.mainLabel.setText(self.values["labelText"])
            self.mainComboBox.setCurrentIndex(self.values["comboBoxIndex"])
            self.mainSlider.setValue(self.values["sliderValue"])
        self.values = {"labelText": self.mainLabel.text(),
                    "comboBoxItems": mainComboBoxItems,
                    "comboBoxIndex": self.mainComboBox.currentIndex(),
                    "sliderValue": self.mainSlider.value(),
                    "sliderMaximum": self.mainSlider.maximum(),
                    "sliderMinimum": self.mainSlider.minimum()}

        dialog = introDlg.SmartDialog(self.values, self)
        self.connect(dialog, SIGNAL("changed"), update)
        dialog.show()

    def LiveCall(self):
        mainComboBoxItems = [self.mainComboBox.itemText(idx) for idx in
                                range(len(self.mainComboBox))]
        def update():
            self.mainLabel.setText(self.values["labelText"])
            self.mainComboBox.setCurrentIndex(self.values["comboBoxIndex"])
            self.mainSlider.setValue(self.values["sliderValue"])
        self.values = {"labelText": self.mainLabel.text(),
                    "comboBoxItems": mainComboBoxItems,
                    "comboBoxIndex": self.mainComboBox.currentIndex(),
                    "sliderValue": self.mainSlider.value(),
                    "sliderMaximum": self.mainSlider.maximum(),
                    "sliderMinimum": self.mainSlider.minimum()}

        if self.liveDialog is None:
            self.liveDialog = introDlg.LiveDialog(self.values, update, self)
        self.liveDialog.show()
        self.liveDialog.raise_()
        self.liveDialog.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
