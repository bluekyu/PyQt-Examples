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
from os.path import dirname, basename
from functools import partial
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import simpleSignalConnectDlg as sscDlg
import introDialog as introDlg
import qrc_resource

__version__ = "3.3.3"
__program_name__ = "PyQt Example"
__author__ = "YoungUk Kim"
__date__ = "09.18.2011"

class MainWindow(QMainWindow):
    """메인 윈도우를 구성하는 클래스"""

    def __init__(self, parent=None):
        """각종 객체들 초기화 및 위치 구성"""

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
        
        self.AddRows(buttonLayout, (
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

        self.AddRows(inputLayout, (
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

        self.AddRows(displayLayout, (
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

        self.AddRows(itemLayout, (
                ("리스트 위젯: ", self.listWidget),))

        ################################################ Widget Setting End ###

        #################################################### Action Setting ###

        ### Actions ###
        # Simple Dialog Open
        simpleDialogAction = self.CreateAction("단순 대화상자",
                                ":simpleDialogIcon.png", "Ctrl+S",
                                "단순한 대화 상자를 엽니다",
                                lambda: sscDlg.SimpleDialog(self).exec_())

        # Signal Dialog Open
        signalDialogAction = self.CreateAction("시그널 대화상자",
                                ":signalDialogIcon.png", "Ctrl+G",
                                "여러 시그널로 된 대화 상자를 엽니다",
                                lambda: sscDlg.SignalDialog(self).exec_())

        # Connect Dialog Open
        connectDialogAction = self.CreateAction("Connect 대화상자",
                                ":connectDialogIcon.png", "Ctrl+E",
                            "여러 연결 방식을 갖는 버튼 대화 상자를 엽니다",
                                lambda: sscDlg.ConnectDialog(self).exec_())

        # Dumb Dialog Open
        dumbDialogAction = self.CreateAction("Dumb 대화상자",
                                ":dumbDialogIcon.png", "Ctrl+M",
                                "Dumb 및 Modal 대화 상자를 엽니다",
                                self.DumbCall)

        # Standard Dialog Open
        standardDialogAction = self.CreateAction("Standard 대화상자",
                                ":standardDialogIcon.png", "Ctrl+R",
                                "Standard 및 Modal 대화 상자를 엽니다",
                                self.StandardCall)

        # Smart Dialog Open
        smartDialogAction = self.CreateAction("Smart 대화상자",
                                ":smartDialogIcon.png", "Ctrl+M",
                                "Smart 및 Modaless 대화 상자를 엽니다",
                                self.SmartCall)

        # Live Dialog Open
        liveDialogAction = self.CreateAction("Live 대화상자",
                                ":liveDialogIcon.png", "Ctrl+L",
                                "Live 및 Modaless 대화 상자를 엽니다",
                                self.LiveCall)

        # Group Action
        messageAAction = self.CreateAction("A Action", ":iconA.png", None, None,
                            self.GroupActionMessage, True, "toggled(bool)")
        messageAAction.blockSignals(True)
        messageAAction.setChecked(True)
        messageAAction.blockSignals(False)
        messageBAction = self.CreateAction("B Action", ":iconB.png", None, None,
                            self.GroupActionMessage, True, "toggled(bool)")
        messageCAction = self.CreateAction("C Action", ":iconC.png", None, None,
                            self.GroupActionMessage, True, "toggled(bool)")

        groupAction = QActionGroup(self)
        self.AddActions(groupAction, (
                messageAAction, messageBAction, messageCAction))

        # Open Image Action
        openImageAction = self.CreateAction("이미지 열기", ":openImage.png",
                            "Ctrl+I", "이미지를 나타냅니다", self.OpenImage)

        # Zoom Image Action
        zoomImageAction = self.CreateAction("이미지 확대/축소",
                                ":zoomImage.png", None,
                                "이미지를 확대하거나 축소합니다.",
                                self.ImageZoom)

        # Help About Action
        helpAboutAction = self.CreateAction("{} 정보".format(__program_name__),
                            None, None, "{}에 대한 정보를 보여줍니다.".format(
                            __program_name__), self.HelpAbout)

        # New Text File Action
        newTextFileAction = self.CreateAction("새 텍스트 파일(&N)", 
                ":newTextFileIcon.png", QKeySequence.New, 
                "새 텍스트 파일을 엽니다.", self.NewTextFile)

        # Open Text File Action
        openTextFileAction = self.CreateAction("텍스트 파일 열기(&O)", 
                ":openTextFileIcon.png", QKeySequence.Open, 
                "텍스트 파일을 엽니다.", self.OpenTextFile)

        # Save Text File Action
        saveTextFileAction = self.CreateAction("텍스트 파일 저장(&S)", 
                ":saveTextFileIcon.png", QKeySequence.Save, 
                "텍스트 파일을 저장합니다.", self.SaveTextFile)

        # Save As Text File Action
        saveAsTextFileAction = self.CreateAction(
                "다른 이름으로 텍스트 파일 저장(&A)", 
                ":saveAsTextFileIcon.png", QKeySequence.SaveAs, 
                "다른 이름으로 텍스트 파일을 저장합니다.", self.SaveAsTextFile)

        # Program Quit Action
        quitAction = self.CreateAction("끝내기(&Q)", ":quitApplication.png",
                QKeySequence.Quit, "프로그램을 종료합니다.", self.close)

        ################################################ Action Setting End ###
 
        ############################################### Dock Widget Setting ###

        ### Dock Widget ###
        # Image Label Dock Widget
        self.imageZoom = (100, 100)
        self.sameZoomCheckState = False
        self.image = QImage(":kubuntuLogoIcon.png")

        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setFrameShape(QFrame.StyledPanel)
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))

        imageLabelDock = QDockWidget("이미지 Dock", self)
        imageLabelDock.setObjectName("TextBrowserDockWidget")
        imageLabelDock.setWidget(self.imageLabel)
        self.addDockWidget(Qt.BottomDockWidgetArea, imageLabelDock)

        # Image Label in Dock Context Menu
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.AddActions(self.imageLabel, (openImageAction, zoomImageAction))

        # Plain Text Edit Dock Widget
        self.plainTextEdit = QPlainTextEdit()
        self.plainTextEdit.setMinimumSize(200, 200)
        self.plainTextEditChanged = False
        self.plainTextEditChangedByUser = True
        self.plainTextEditFilePath = None

        def UserChangePlainTextEdit():
            """사용자가 텍스트를 변경시켰을 때에만, 텍스트 변경 여부 작동.
            
            인자: 없음
            리턴: 없음"""

            if (not self.plainTextEditChanged) and \
                                            self.plainTextEditChangedByUser:
                self.plainTextEditChanged = True
                self.UpdatePlainTextEdit(None)

        self.connect(self.plainTextEdit, SIGNAL("textChanged()"), 
                                UserChangePlainTextEdit)
        
        self.plainTextEditDock = QDockWidget("텍스트 에디트 Dock", self)
        self.plainTextEditDock.setObjectName("PlainTextEditDockWidget")
        self.plainTextEditDock.setWidget(self.plainTextEdit)
        self.addDockWidget(Qt.RightDockWidgetArea, self.plainTextEditDock)

        # Plain Test Edit Context Menu
        self.plainTextEditDock.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.AddActions(self.plainTextEditDock, (newTextFileAction,
            openTextFileAction, saveTextFileAction, saveAsTextFileAction))

        ########################################### Dock Widget Setting End ###

        ################################################## Menu Bar Setting ###
       
        ### Menu Bar ###
        # Recent Files List
        self.recentFilesMenu = QMenu("최근에 연 파일")
        self.connect(self.recentFilesMenu, SIGNAL("aboutToShow()"),
                        self.UpdateRecentFilesMenu)

        # File
        fileMenu = QMenu()
        self.AddActions(fileMenu, (newTextFileAction, None, openTextFileAction,
            self.recentFilesMenu, None, saveTextFileAction, saveAsTextFileAction,
            None, quitAction))
        fileMenuAction = self.CreateAction("파일(&F)", None, None, 
                "파일의 열기 및 저장 등을 포함합니다")
        fileMenuAction.setMenu(fileMenu)
        self.menuBar().addAction(fileMenuAction)

        # Dialog
        dialogMenu = QMenu()
        self.AddActions(dialogMenu, (simpleDialogAction, signalDialogAction,
            connectDialogAction, None, dumbDialogAction, standardDialogAction,
            smartDialogAction, liveDialogAction))
        dialogMenuAction = self.CreateAction("대화 상자(&A)", None, None,
                "여러 대화 상자 종류들을 포함합니다")
        dialogMenuAction.setMenu(dialogMenu)
        self.menuBar().addAction(dialogMenuAction)

        # Image
        imageMenu = QMenu()
        self.AddActions(imageMenu, (openImageAction, zoomImageAction))
        imageMenuAction = self.CreateAction("이미지(&M)", None, None,
                "이미지를 조절합니다")
        imageMenuAction.setMenu(imageMenu)
        self.menuBar().addAction(imageMenuAction)

        # Help
        aboutMenu = QMenu()
        self.AddActions(aboutMenu, (helpAboutAction,))
        aboutMenuAction = self.CreateAction("도움말(&H)", None, None,
                "도움말 및 정보를 포함합니다")
        aboutMenuAction.setMenu(aboutMenu)
        self.menuBar().addAction(aboutMenuAction)

        ############################################## Menu Bar Setting End ###

        ################################################## Tool Bar Setting ###

        ### Tool Bar ###
        # Dialog Tool Bar
        dialogToolBar = self.addToolBar("Dialog")
        dialogToolBar.setObjectName("DialogToolBar")
        self.AddActions(dialogToolBar, (simpleDialogAction, signalDialogAction,
            connectDialogAction, None, standardDialogAction, smartDialogAction,
            liveDialogAction))

        # Group Actoin Tool Bar
        groupActionToolBar = self.addToolBar("GruopAction")
        groupActionToolBar.setObjectName("GroupActionToolBar")
        self.AddActions(groupActionToolBar, (messageAAction, messageBAction,
            messageCAction))

        ### Status Bar ###
        statusBarLabel = QLabel("상태표시줄")
        statusBarLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Plain)
        
        self.statusBar = self.statusBar()
        self.statusBar.addPermanentWidget(statusBarLabel)
        self.statusBar.showMessage("실행 완료", 5000)

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
        self.AddActions(centralWidget, (simpleDialogAction, signalDialogAction,
            connectDialogAction, contextSeparator, dumbDialogAction,
            standardDialogAction, smartDialogAction, liveDialogAction))

        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Main Window")

        ### Settings Restore ###
        settings = QSettings()
        self.recentFiles = settings.value("RecentFiles") or []
        self.restoreGeometry(settings.value("mainWindow.Geometry",
                QByteArray()))
        self.restoreState(settings.value("mainWindow.State", QByteArray()))

        ########################################### Main Window Setting End ###

    ################################################################ Method ###

    def CreateAction(self, name, icon=None, shortcut=None, tipHelp=None, 
                            slot=None, checkable=False, signal="triggered()"):
        """액션을 설정하고 생성하는 메소드.
        
        인자: name - 액션 이름
              icon - 액션의 아이콘
              shortcut - 단축키
              tipHelp - 툴팁과 상태표시줄 팁에 들어갈 도움말
              slot - 액션에 connect를 추가할 때, 추가할 slot
              checkable - 선택 가능 여부
              signal - connect에서 작동할 시그널
        리턴: action 객체"""

        action = QAction(name, self)
        if icon:
            action.setIcon(QIcon(icon))
        if shortcut:
            action.setShortcut(shortcut)
        if tipHelp:
            action.setToolTip(tipHelp)
            action.setStatusTip(tipHelp)
        if slot:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)

        return action

    def AddActions(self, target, actions):
        """액션, 메뉴 또는 분리바를 정해진 위치에 추가하는 메소드.
        
        인자: target - 액션을 추가할 객체.
              actions - (QAction | QMenu | None, ...) 형식
        리턴: 없음"""

        for action in actions:
            if isinstance(action, QAction):
                target.addAction(action)
            elif isinstance(action, QMenu):
                target.addMenu(action)
            else:
                target.addSeparator()

    def AddRows(self, layout, rows):
        """폼 레이아웃의 행에 객체를 추가함.

        인자: layout - 폼 레이아웃
              rows - ((label, field | label | field), ...) 형식
        리턴: 없음"""

        for row in rows:
            layout.addRow(*row)

    def TextFileSaveOk(self):
        """텍스트 파일을 저장할 것인지 확인하는 메소드.
        
        인자: 없음
        리턴: 참, 거짓"""

        if self.plainTextEditChanged:
            answer = QMessageBox.question(self, "텍스트 파일 저장 확인",
                    "텍스트 파일이 저장되지 않았습니다. 저장하시겠습니까?",
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if answer == QMessageBox.Cancel:
                return False
            elif answer == QMessageBox.Yes:
                self.SaveTextFile()
        return True

    def NewTextFile(self):
        """새 텍스트 파일 생성.
        
        인자: 없음
        리턴: 없음"""

        if not self.TextFileSaveOk():
            return
        self.plainTextEditFilePath = None
        self.plainTextEditChanged = False
        self.plainTextEditChangedByUser = False
        self.plainTextEdit.clear()
        self.plainTextEditChangedByUser = True

        self.UpdatePlainTextEdit("새 파일이 열림")

    def OpenTextFile(self):
        """텍스트 파일을 열음.
        
        인자: 없음
        리턴: 없음"""

        if not self.TextFileSaveOk():
            return
        fileDir = dirname(self.plainTextEditFilePath) if \
                                    self.plainTextEditFilePath else "."
        filePath = QFileDialog.getOpenFileName(self, "텍스트 파일 열기",
                        fileDir, "텍스트 파일(*.txt);;모든 파일(*.*)")

        if filePath:
            self.LoadTextFile(filePath)

    def LoadTextFile(self, filePath):
        """텍스트 파일을 불러옴.

        인자: filePath - 텍스트 파일 경로.
        리턴: 없음"""

        # 최근 파일을 선택할 경우 파일 저장 여부 확인이 필요함.
        action = self.sender()
        if isinstance(action, QAction) and not self.TextFileSaveOk():
            return

        if filePath:
            self.plainTextEditFilePath = filePath
            self.plainTextEditChanged = False
            self.plainTextEditChangedByUser = False
            text = open(filePath, "r").read()
            self.plainTextEdit.setPlainText(text)
            self.plainTextEditChangedByUser = True
            self.AddRecentFiles(filePath)
            self.UpdatePlainTextEdit("파일 열기 성공")

    def SaveTextFile(self):
        """텍스트 파일을 저장함.
        
        인자: 없음
        리턴: 없음"""

        if not self.plainTextEditChanged:
            return
        if self.plainTextEditFilePath is None:
            self.SaveAsTextFile()
        else:
            textFile = open(self.plainTextEditFilePath, "w")
            textFile.write(self.plainTextEdit.toPlainText())
            self.plainTextEditChanged = False
            self.UpdatePlainTextEdit("파일 저장 완료")

    def SaveAsTextFile(self):
        """텍스트 파일을 다른 이름으로 저장함.
        
        인자: 없음
        리턴: 없음"""

        fileDir = dirname(self.plainTextEditFilePath) if \
                            self.plainTextEditFilePath else "."
        filePath = QFileDialog.getSaveFileName(self, "텍스트 파일 저장",
                                fileDir, "텍스트 파일(*.txt);;모든 파일(*.*)")
        
        if filePath:
            self.AddRecentFiles(filePath)
            self.plainTextEditFilePath = filePath
            self.plainTextEditChanged = True
            self.SaveTextFile()

    def closeEvent(self, event):
        """프로그램 종료 이벤트 발생시 호출되는 메소드에 대한 오버로딩.
        
        인자: event - 프로그램 종료 이벤트
        리턴: 없음"""

        if self.TextFileSaveOk():
            settings = QSettings()
            settings.setValue("RecentFiles", self.recentFiles or [])
            settings.setValue("mainWindow.Geometry", self.saveGeometry())
            settings.setValue("mainWindow.State", self.saveState())
        else:
            event.ignore()

    def AddRecentFiles(self, filePath):
        """최근 파일 추가.
        
        인자: filePath - 파일 경로
        리턴: 없음"""

        if filePath is None:
            return
        # 최근 파일이 존재하는 경우 제거하고 맨 처음으로 넣기 위한 작업
        if filePath in self.recentFiles:
            self.recentFiles.remove(filePath)
        self.recentFiles.insert(0, filePath)
        if len(self.recentFiles) > 9:
            self.recentFiles.pop()

    def UpdateRecentFilesMenu(self):
        """최근 연 파일 메뉴를 볼 경우 메뉴 갱신하는 메소드
        
        인자: 없음
        리턴: 없음"""

        self.recentFilesMenu.clear()
        recentFiles = []
        for filePath in self.recentFiles:
            if filePath != self.plainTextEditFilePath and \
                    QFile.exists(filePath):
                recentFiles.append(filePath)

        for i, filePath in enumerate(recentFiles):
            action = QAction("&{} {}".format(i+1, filePath), self)
            action.setData(filePath)
            self.connect(action, SIGNAL("triggered()"), 
                            partial(self.LoadTextFile, filePath))
            self.recentFilesMenu.addAction(action)

    def UpdatePlainTextEdit(self, message):
        """텍스트 에디터를 수정할 때 정보들을 갱신함.
        
        인자: message - 상태 표시줄에 나타낼 메시지
        리턴: 없음"""

        if message:
            self.statusBar.showMessage(message, 5000)

        fileName = basename(self.plainTextEditFilePath) if \
                        self.plainTextEditFilePath else "이름 없음"
        self.plainTextEditDock.setWindowTitle(
                                "{}[*]".format(fileName))
        self.plainTextEditDock.setWindowModified(self.plainTextEditChanged)

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

    def OpenImage(self):
        """이미지를 여는 메소드.
        
        인자: 없음
        리턴: 없음"""

        imageFormats = ["{0} 파일(*.{0})".format(ext.data().decode()) for ext in
                        QImageReader.supportedImageFormats()]
        imageFormats.append("모든 파일 (*.*)")
        fileDialog = QFileDialog(self, "이미지 열기", ".")
        fileDialog.setFilters(imageFormats)
        fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
        if fileDialog.exec_():
            imageLink = fileDialog.selectedFiles()[0]
            self.image = QImage(imageLink)
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
    
    def ImageZoom(self):
        """이미지 확대/축소 대화 상자를 Dumb Modal 형식으로 열음.
        
        인자: 없음
        리턴: 없음"""

        if self.image.isNull():
            return
        
        zoomDialog = QDialog(self)

        widthSpinBox = QSpinBox()
        widthSpinBox.setRange(0, 500)
        widthSpinBox.setSuffix(" %")
        heightSpinBox = QSpinBox()
        heightSpinBox.setRange(0, 500)
        heightSpinBox.setSuffix(" %")
        
        image = self.imageLabel.pixmap().toImage()

        widthSpinBox.setValue(self.imageZoom[0])
        heightSpinBox.setValue(self.imageZoom[1])

        sameZoomCheckBox = QCheckBox("같은 비율 유지")
        sameZoomCheckBox.setChecked(self.sameZoomCheckState)

        def ValueSameSet(value):
            """같은 비율 유지를 체크 했을 때 값이 같도록 변경
            
            인자: value - 확대 비율 값
            리턴: 없음"""

            if sameZoomCheckBox.isChecked():
                widthSpinBox.setValue(value)
                heightSpinBox.setValue(value)
        
        self.connect(widthSpinBox, SIGNAL("valueChanged(int)"), 
                        ValueSameSet)
        self.connect(heightSpinBox, SIGNAL("valueChanged(int)"),
                        ValueSameSet)
        self.connect(sameZoomCheckBox, SIGNAL("stateChanged(int)"),
                    lambda: ValueSameSet(widthSpinBox.value()))
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | 
                                        QDialogButtonBox.Cancel)
        self.connect(buttonBox, SIGNAL("accepted()"), zoomDialog,
                        SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), zoomDialog,
                        SLOT("reject()"))

        layout = QFormLayout()
        layout.addRow("너비: ", widthSpinBox)
        layout.addRow("높이: ", heightSpinBox)
        layout.addWidget(sameZoomCheckBox)
        layout.addWidget(buttonBox)

        zoomDialog.setLayout(layout)
        zoomDialog.setWindowTitle("이미지 확대/축소")

        if zoomDialog.exec_():
            self.imageZoom = (widthSpinBox.value(), heightSpinBox.value())
            width = self.image.width() * self.imageZoom[0] // 100
            height = self.image.height() * self.imageZoom[1] // 100
            image = self.image.scaled(width, height)
            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.sameZoomCheckState = sameZoomCheckBox.isChecked()

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
