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

Dock 위젯들을 모아둔 파일
"""

from os.path import dirname, basename
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import objectControl as objCont
import qrc_resource

__version__ = "3.4.1"
__author__ = "YoungUk Kim"
__date__ = "09.18.2011"

class TextEdit(QPlainTextEdit):
    """텍스트 에디터 클래스"""

    titleLabel = None
    statusBar = None
    isChanged = False
    isChangedByUser = True
    filePath = None
    recentFiles = []
    actions = []

    def __init__(self, parent=None):
        """객체 초기화

        인자: parent - 부모 윈도우
        리턴: 없음"""

        super().__init__(parent)

        self.setMinimumSize(200, 200)
        self.titleLabel = QLabel("텍스트 에디터")

        # New Text File Action
        newTextFileAction = objCont.CreateAction(self, "새 텍스트 파일(&N)", 
                ":newTextFileIcon.png", QKeySequence.New, 
                "새 텍스트 파일을 엽니다.", self.NewTextFile)

        # Open Text File Action
        openTextFileAction = objCont.CreateAction(self, "텍스트 파일 열기(&O)",
                ":openTextFileIcon.png", QKeySequence.Open, 
                "텍스트 파일을 엽니다.", self.OpenTextFile)

        # Save Text File Action
        saveTextFileAction = objCont.CreateAction(self, "텍스트 파일 저장(&S)",
                ":saveTextFileIcon.png", QKeySequence.Save, 
                "텍스트 파일을 저장합니다.", self.SaveTextFile)

        # Save As Text File Action
        saveAsTextFileAction = objCont.CreateAction(self,
                "다른 이름으로 텍스트 파일 저장(&A)", 
                ":saveAsTextFileIcon.png", QKeySequence.SaveAs, 
                "다른 이름으로 텍스트 파일을 저장합니다.", self.SaveAsTextFile)
        self.actions = [newTextFileAction, openTextFileAction,
                        saveTextFileAction, saveAsTextFileAction]

        # Plain Text Edit Context Menu
        self.titleLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        objCont.AddActions(self.titleLabel, self.actions)

        self.connect(self, SIGNAL("textChanged()"), self.UserChange)

    ################################################################ Method ###

    def UserChange(self):
        """사용자가 텍스트를 변경시켰을 때에만, 텍스트 변경 여부 작동.
        
        인자: 없음
        리턴: 없음"""

        if (not self.isChanged) and self.isChangedByUser:
            self.isChanged = True
            self.UpdateInfo(None)

    def UpdateInfo(self, message):
        """텍스트 에디터를 수정할 때 정보들을 갱신함.
        
        인자: 없음 
        리턴: 없음"""

        fileName = basename(self.filePath) if self.filePath else "이름 없음"
        if self.isChanged:
            self.titleLabel.setText("{} *".format(fileName))
        else:
            self.titleLabel.setText("{}".format(fileName))
        if self.statusBar is not None:
            self.statusBar.showMessage(message, 5000)

    def TextFileSaveOk(self):
        """텍스트 파일을 저장할 것인지 확인하는 메소드.
        
        인자: 없음
        리턴: 참, 거짓"""

        if self.isChanged:
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
        self.filePath = None
        self.isChanged = False
        self.isChangedByUser = False
        self.clear()
        self.isChangedByUser = True

        self.UpdateInfo("새 텍스트 파일 생성")

    def OpenTextFile(self):
        """텍스트 파일을 열음.
        
        인자: 없음
        리턴: 없음"""

        if not self.TextFileSaveOk():
            return
        fileDir = dirname(self.filePath) if self.filePath else "."
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
            self.filePath = filePath
            self.isChanged = False
            self.isChangedByUser = False
            text = open(filePath, "r").read()
            self.setPlainText(text)
            self.isChangedByUser = True
            self.AddRecentFiles(filePath)
            self.UpdateInfo("파일 열기 완료")

    def SaveTextFile(self):
        """텍스트 파일을 저장함.
        
        인자: 없음
        리턴: 없음"""

        if not self.isChanged:
            return
        if self.filePath is None:
            self.SaveAsTextFile()
        else:
            textFile = open(self.filePath, "w")
            textFile.write(self.toPlainText())
            self.isChanged = False
            self.UpdateInfo("파일 저장 완료")

    def SaveAsTextFile(self):
        """텍스트 파일을 다른 이름으로 저장함.
        
        인자: 없음
        리턴: 없음"""

        fileDir = dirname(self.filePath) if self.filePath else "."
        filePath = QFileDialog.getSaveFileName(self, "텍스트 파일 저장",
                                fileDir, "텍스트 파일(*.txt);;모든 파일(*.*)")
        
        if filePath:
            self.AddRecentFiles(filePath)
            self.filePath = filePath
            self.isChanged = True
            self.SaveTextFile()

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

class ImageLabel(QLabel):
    """이미지 레이블 클래스"""

    imageZoom = (100, 100)
    sameZoomCheckState = False
    image = QImage(":kubuntuLogoIcon.png")
    actions = []

    def __init__(self, parent=None):
        """객체 초기화
        
        인자: parent - 부모 윈도우
        리턴: 없음"""

        super().__init__(parent)

        self.setMinimumSize(200, 200)
        self.setAlignment(Qt.AlignCenter)
        self.setFrameShape(QFrame.StyledPanel)
        self.setPixmap(QPixmap.fromImage(self.image))

        # Open Image Action
        openImageAction = objCont.CreateAction(
                            self, "이미지 열기", ":openImage.png",
                            "Ctrl+I", "이미지를 나타냅니다", self.OpenImage)

        # Zoom Image Action
        zoomImageAction = objCont.CreateAction(self, "이미지 확대/축소",
                                ":zoomImage.png", None,
                                "이미지를 확대하거나 축소합니다.",
                                self.ImageZoom)
        self.actions = [openImageAction, zoomImageAction]

        # Image Label in Context Menu
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        objCont.AddActions(self, self.actions)

    ############################################################### Methods ###

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
            self.setPixmap(QPixmap.fromImage(self.image))
    
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
        
        image = self.pixmap().toImage()

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
            self.setPixmap(QPixmap.fromImage(image))
            self.sameZoomCheckState = sameZoomCheckBox.isChecked()

if __name__ == "__main__":
    pass
