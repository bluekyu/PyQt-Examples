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

PyQt Example 프로그램의 메인 윈도우를 담당하는 파일입니다.
"""

import sys
from functools import partial
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import simpleSignalConnectDlg as sscDlg
import introDialog as introDlg
import dockWidgets as dock
import objectControl as objCont
import qrc_resource

__version__ = "3.4.1"
__program_name__ = "PyQt Example"
__author__ = "YoungUk Kim"
__date__ = "09.18.2011"

class MainWindow(QMainWindow):
    """메인 윈도우를 구성하는 클래스"""

    def __init__(self, parent=None):
        """각종 객체들 초기화 및 위치 구성
        
        인자: parent - 부모 윈도우
        리턴: 없음"""

        super().__init__(parent)

        #################################################### Widget Setting ###

        ### Buttons ###
        buttonLayout = QFormLayout()
        buttonGroup = QGroupBox("버튼")
        buttonGroup.setLayout(buttonLayout)

        # Push Button
        self.mainButton = QPushButton("버튼(&B)")
        buttonMessageBox = QMessageBox(QMessageBox.Information, "버튼 메시지",
                            "버튼이 클릭 됨", QMessageBox.Ok, self)
        self.connect(self.mainButton, SIGNAL("clicked()"), 
                                                    buttonMessageBox.open)

        # Check Box
        self.mainCheckBox = QCheckBox("체크(&K)")
        
        objCont.AddRows(buttonLayout, (
                ("버튼: ", self.mainButton),
                ("체크 상자: ", self.mainCheckBox)))

        ### Input Widgets ###
        inputLayout = QFormLayout()
        inputGroup = QGroupBox("입력 위젯")
        inputGroup.setLayout(inputLayout)
        
        # Combo Box
        self.mainComboBox = QComboBox()
        self.mainComboBox.addItems(["항목 1", "항목 2", "항목 3", "항목 4"])

        # Line Edit
        self.mainLineEdit = QLineEdit("편집 내용")

        # Spin Box
        self.mainSpinBox = QSpinBox()
        self.mainSpinBox.setRange(-1000, 1000)
        self.mainSpinBox.setValue(0)
        self.mainSpinBox.setPrefix("Prefix ")
        self.mainSpinBox.setSuffix(" Suffix")
        self.mainSpinBox.setAccelerated(True)

        # Dial
        self.mainDial = QDial()
        self.mainDial.setMinimumSize(100, 100)
        self.mainDial.setRange(-100, 100)
        self.mainDial.setValue(0)
        self.mainDial.setNotchesVisible(True)

        # Slider
        self.mainSlider = QSlider(Qt.Horizontal)
        self.mainSlider.setRange(-100, 100)
        self.mainSlider.setValue(0)
        self.mainSlider.setTickPosition(QSlider.TicksBelow)

        objCont.AddRows(inputLayout, (
                ("콤보 상자(&C): ", self.mainComboBox),
                ("라인 편집(&I): ", self.mainLineEdit),
                ("스핀 상자(&S): ", self.mainSpinBox),
                ("다이얼(&D): ", self.mainDial),
                ("슬라이더(&L): ", self.mainSlider)))

        ### Display Widgets ###
        displayLayout = QFormLayout()
        displayGroup = QGroupBox("표시 위젯")
        displayGroup.setLayout(displayLayout)

        # Label
        self.mainLabel = QLabel("레이블 내용")

        objCont.AddRows(displayLayout, (
                ("레이블: ", self.mainLabel),))

        ### Item Widgets ###
        itemLayout = QFormLayout()
        itemGroup = QGroupBox("아이템 위젯")
        itemGroup.setLayout(itemLayout)

        # List Widget
        self.listWidget = QListWidget()
        self.listWidget.addItems(["리스트 항목 {}".format(k) 
                                    for k in range(1, 5)])
        self.listWidget.setMinimumSize(100, 100)

        objCont.AddRows(itemLayout, (
                ("리스트 위젯: ", self.listWidget),))

        ################################################ Widget Setting End ###

        #################################################### Action Setting ###

        ### Actions ###
        # Simple Dialog Open
        simpleDialogAction = objCont.CreateAction(self, "단순 대화상자",
                                ":simpleDialogIcon.png", "Ctrl+S",
                                "단순한 대화 상자를 엽니다",
                                lambda: sscDlg.SimpleDialog(self).exec_())

        # Signal Dialog Open
        signalDialogAction = objCont.CreateAction(self, "시그널 대화상자",
                                ":signalDialogIcon.png", "Ctrl+G",
                                "여러 시그널로 된 대화 상자를 엽니다",
                                lambda: sscDlg.SignalDialog(self).exec_())

        # Connect Dialog Open
        connectDialogAction = objCont.CreateAction(self, "Connect 대화상자",
                                ":connectDialogIcon.png", "Ctrl+E",
                            "여러 연결 방식을 갖는 버튼 대화 상자를 엽니다",
                                lambda: sscDlg.ConnectDialog(self).exec_())

        # Dumb Dialog Open
        dumbDialogAction = objCont.CreateAction(self, "Dumb 대화상자",
                                ":dumbDialogIcon.png", "Ctrl+M",
                                "Dumb 및 Modal 대화 상자를 엽니다",
                                self.DumbCall)

        # Standard Dialog Open
        standardDialogAction = objCont.CreateAction(self, "Standard 대화상자",
                                ":standardDialogIcon.png", "Ctrl+R",
                                "Standard 및 Modal 대화 상자를 엽니다",
                                self.StandardCall)

        # Smart Dialog Open
        smartDialogAction = objCont.CreateAction(self, "Smart 대화상자",
                                ":smartDialogIcon.png", "Ctrl+M",
                                "Smart 및 Modaless 대화 상자를 엽니다",
                                self.SmartCall)

        # Live Dialog Open
        liveDialogAction = objCont.CreateAction(self, "Live 대화상자",
                                ":liveDialogIcon.png", "Ctrl+L",
                                "Live 및 Modaless 대화 상자를 엽니다",
                                self.LiveCall)

        # Group Action
        messageAAction = objCont.CreateAction(
                            self, "A Action", ":iconA.png", None, None,
                            self.GroupActionMessage, True, "toggled(bool)")
        messageAAction.blockSignals(True)
        messageAAction.setChecked(True)
        messageAAction.blockSignals(False)
        messageBAction = objCont.CreateAction(
                            self, "B Action", ":iconB.png", None, None,
                            self.GroupActionMessage, True, "toggled(bool)")
        messageCAction = objCont.CreateAction(
                            self, "C Action", ":iconC.png", None, None,
                            self.GroupActionMessage, True, "toggled(bool)")

        groupAction = QActionGroup(self)
        objCont.AddActions(groupAction, (
                messageAAction, messageBAction, messageCAction))

        # Help About Action
        helpAboutAction = objCont.CreateAction(
                            self, "{} 정보".format(__program_name__),
                            None, None, "{}에 대한 정보를 보여줍니다.".format(
                            __program_name__), self.HelpAbout)

        # Program Quit Action
        quitAction = objCont.CreateAction(
                self, "끝내기(&Q)", ":quitApplication.png",
                QKeySequence.Quit, "프로그램을 종료합니다.", self.close)

        ################################################ Action Setting End ###
 
        ############################################### Dock Widget Setting ###

        ### Dock Widget ###
        # Image Label Dock Widget
        self.imageLabel = dock.ImageLabel()

        imageLabelDock = QDockWidget("이미지 Dock", self)
        imageLabelDock.setObjectName("TextBrowserDockWidget")
        imageLabelDock.setWidget(self.imageLabel)
        self.addDockWidget(Qt.BottomDockWidgetArea, imageLabelDock)

        # Plain Text Edit Dock Widget
        self.textEdit = dock.TextEdit()

        self.textEditDock = QDockWidget(self)
        self.textEditDock.setObjectName("PlainTextEditDockWidget")
        self.textEditDock.setTitleBarWidget(self.textEdit.titleLabel)
        self.textEditDock.setWidget(self.textEdit)
        self.addDockWidget(Qt.RightDockWidgetArea, self.textEditDock)

        ########################################### Dock Widget Setting End ###

        ################################################## Menu Bar Setting ###
       
        ### Menu Bar ###
        # Recent Files List
        self.textEditRecentFilesMenu = QMenu("최근에 연 파일")
        self.connect(self.textEditRecentFilesMenu, SIGNAL("aboutToShow()"),
                        self.UpdateTextEditRecentFilesMenu)

        # File
        fileMenu = QMenu()
        objCont.AddActions(fileMenu, (self.textEdit.actions[0], None,
                self.textEdit.actions[1], self.textEditRecentFilesMenu,
                None, self.textEdit.actions[2], self.textEdit.actions[3],
                None, quitAction))
        fileMenuAction = objCont.CreateAction(self, "파일(&F)", None, None, 
                "파일의 열기 및 저장 등을 포함합니다")
        fileMenuAction.setMenu(fileMenu)
        self.menuBar().addAction(fileMenuAction)

        # Dialog
        dialogMenu = QMenu()
        objCont.AddActions(dialogMenu, (simpleDialogAction, signalDialogAction,
            connectDialogAction, None, dumbDialogAction, standardDialogAction,
            smartDialogAction, liveDialogAction))
        dialogMenuAction = objCont.CreateAction(
                self, "대화 상자(&A)", None, None,
                "여러 대화 상자 종류들을 포함합니다")
        dialogMenuAction.setMenu(dialogMenu)
        self.menuBar().addAction(dialogMenuAction)

        # Image
        imageMenu = QMenu()
        objCont.AddActions(imageMenu, self.imageLabel.actions)
        imageMenuAction = objCont.CreateAction(self, "이미지(&M)", None, None,
                "이미지를 조절합니다")
        imageMenuAction.setMenu(imageMenu)
        self.menuBar().addAction(imageMenuAction)

        # Help
        aboutMenu = QMenu()
        objCont.AddActions(aboutMenu, (helpAboutAction,))
        aboutMenuAction = objCont.CreateAction(self, "도움말(&H)", None, None,
                "도움말 및 정보를 포함합니다")
        aboutMenuAction.setMenu(aboutMenu)
        self.menuBar().addAction(aboutMenuAction)

        ############################################## Menu Bar Setting End ###

        ################################################## Tool Bar Setting ###

        ### Tool Bar ###
        # Dialog Tool Bar
        dialogToolBar = self.addToolBar("Dialog")
        dialogToolBar.setObjectName("DialogToolBar")
        objCont.AddActions(dialogToolBar, (simpleDialogAction, signalDialogAction,
            connectDialogAction, None, dumbDialogAction, standardDialogAction,
            smartDialogAction, liveDialogAction))

        # Group Actoin Tool Bar
        groupActionToolBar = self.addToolBar("GruopAction")
        groupActionToolBar.setObjectName("GroupActionToolBar")
        objCont.AddActions(groupActionToolBar, (messageAAction, messageBAction,
            messageCAction))

        ### Status Bar ###
        statusBarLabel = QLabel("상태표시줄")
        statusBarLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Plain)
        
        statusBar = self.statusBar()
        self.textEdit.statusBar = statusBar
        statusBar.addPermanentWidget(statusBarLabel)
        statusBar.showMessage("실행 완료", 5000)

        ############################################## Tool Bar Setting End ###

        ############################################### Main Window Setting ###

        ### Main Window ###
        self.liveDialog = None

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(buttonGroup)
        mainLayout.addWidget(inputGroup)
        mainLayout.addWidget(displayGroup)
        mainLayout.addWidget(itemGroup)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)

        # Central Widget Context Menu
        centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        contextSeparator = QAction(self)
        contextSeparator.setSeparator(True)
        objCont.AddActions(centralWidget, (simpleDialogAction, signalDialogAction,
            connectDialogAction, contextSeparator, dumbDialogAction,
            standardDialogAction, smartDialogAction, liveDialogAction))

        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Main Window")

        ### Settings Restore ###
        settings = QSettings()
        self.textEdit.recentFiles = settings.value("TextEditRecentFiles") or []
        self.restoreGeometry(settings.value("mainWindow.Geometry",
                QByteArray()))
        self.restoreState(settings.value("mainWindow.State", QByteArray()))

        ########################################### Main Window Setting End ###

    ################################################################ Method ###

    def closeEvent(self, event):
        """프로그램 종료 이벤트 발생시 호출되는 메소드에 대한 오버로딩.
        
        인자: event - 프로그램 종료 이벤트
        리턴: 없음"""

        if self.textEdit.TextFileSaveOk():
            settings = QSettings()
            settings.setValue("TextEditRecentFiles", 
                                    self.textEdit.recentFiles or [])
            settings.setValue("mainWindow.Geometry", self.saveGeometry())
            settings.setValue("mainWindow.State", self.saveState())
        else:
            event.ignore()

    def UpdateTextEditRecentFilesMenu(self):
        """최근 연 파일 메뉴를 볼 경우 메뉴 갱신하는 메소드
        
        인자: 없음
        리턴: 없음"""

        self.textEditRecentFilesMenu.clear()
        recentFiles = []
        for filePath in self.textEdit.recentFiles:
            if filePath != self.textEdit.filePath and QFile.exists(filePath):
                recentFiles.append(filePath)

        for i, filePath in enumerate(recentFiles):
            action = QAction("&{} {}".format(i+1, filePath), self)
            action.setData(filePath)
            self.connect(action, SIGNAL("triggered()"), 
                            partial(self.textEdit.LoadTextFile, filePath))
            self.textEditRecentFilesMenu.addAction(action)

    def DumbCall(self):
        """Dumb 대화 상자를 호출하는 메소드.
        
        인자: 없음
        리턴: 없음"""

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
        """Standard 대화 상자를 호출하는 메소드.
        
        인자: 없음
        리턴: 없음"""

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
        """Smart 대화 상자를 호출하는 메소드.
        
        인자: 없음
        리턴: 없음"""

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
        """Live 대화 상자를 호출하는 메소드.
        
        인자: 없음
        리턴: 없음"""

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

    def GroupActionMessage(self, isChecked):
        """그룹 액션이 호출되었을 때 나타낼 메시지
        
        인자: isChecked - 선택 되었는지 확인
        리턴: 없음"""

        action = self.sender()
        if not (action and isChecked and isinstance(action, QAction)):
            return
        QMessageBox(QMessageBox.Information, "메시지 박스의 메시지",
                    "그룹 Action 중 {}이 클릭됨".format(action.text()),
                    QMessageBox.Ok, self).open()

    def HelpAbout(self):
        """프로그램 정보를 알려주는 대화 상자를 열음
        
        인자: 없음
        리턴: 없음"""

        from platform import python_version, system
        QMessageBox.about(self, "{} 정보".format(__program_name__),
                        """<b>{}</b> v. {}
                        <p>이 프로그램은 PyQt4에 대한 예제 프로그램입니다.</p>
                        <p>Python {} - Qt {} - PyQt {} on {}</p>""".format(
                        __program_name__, __version__, python_version(),
                        QT_VERSION_STR, PYQT_VERSION_STR, system()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("bluekyu")
    app.setOrganizationDomain("bluekyu.me")
    app.setApplicationName(__program_name__)
    app.setWindowIcon(QIcon(":mainIcon.png"))
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
