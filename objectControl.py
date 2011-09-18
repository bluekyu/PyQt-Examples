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

객체들에서 공통적으로 쓰이는 유용한 함수들을 모아둔 것
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

__version__ = "3.4.1"
__author__ = "YoungUk Kim"
__date__ = "09.18.2011"

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

def AddActions(target, actions):
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

def AddRows(layout, rows):
    """폼 레이아웃의 행에 객체를 추가함.

    인자: layout - 폼 레이아웃
          rows - ((label, field | label | field), ...) 형식
    리턴: 없음"""

    for row in rows:
        layout.addRow(*row)

if __name__ == "__main__":
    pass
