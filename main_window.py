# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1625, 1225)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("/*\n"
" *  BreezeDark stylesheet.\n"
" *\n"
" *  :author: Colin Duquesnoy\n"
" *  :editor: Alex Huszagh\n"
" *  :license: MIT, see LICENSE.md\n"
" *\n"
" *  This is originally a fork of QDarkStyleSheet, and is based on Breeze/\n"
" *  BreezeDark color scheme, but is in no way affiliated with KDE.\n"
" *\n"
" * ---------------------------------------------------------------------\n"
" *  The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" * Copyright (c) <2015-2016> <Alex Huszagh>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining\n"
" * a copy of this software and associated documentation files (the\n"
" * \"Software\"), to deal in the Software without restriction, including\n"
" * without limitation the rights to use, copy, modify, merge, publish,\n"
" * distribute, sublicense, and/or sell copies of the Software, and to\n"
" * permit persons to whom the Software is furnished to do so, subject to\n"
" * the following conditions:\n"
" *\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
" *\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS\n"
" * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF\n"
" * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\n"
" * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY\n"
" * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,\n"
" * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE\n"
" * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
" * ---------------------------------------------------------------------\n"
" */\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 0.1ex solid #eff0f1;\n"
"    background-color: #31363b;\n"
"    alternate-background-color: #3b4045;\n"
"    color: #eff0f1;\n"
"    padding: 0.5ex;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    selection-background-color:#3daee9;\n"
"    selection-color: #eff0f1;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    border: 0px transparent black;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 0.5ex;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 0.2ex;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #76797c;\n"
"}\n"
"\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 0.2ex;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:focus\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    border-image: url(:/dark/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate\n"
"{\n"
"    border-image: url(:/dark/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"{\n"
"    border-image: url(:/dark/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_indeterminate_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 0.5ex;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 0.2ex;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #76797c;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:focus\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:unchecked:hover,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_unchecked.svg);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked_disabled.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #31363b;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    background-color: #3daee9;\n"
"    color: #eff0f1;\n"
"    margin-bottom: -0.1ex;\n"
"    padding-bottom: 0.1ex;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    color: #eff0f1;\n"
"    margin: 0.2ex;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 0.5ex;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 0.5ex 3ex 0.5ex 3ex;\n"
"    margin-left: 0.5ex;\n"
"    border: 0.1ex solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 0.2ex;\n"
"    background: lightblue;\n"
"    margin-left: 1ex;\n"
"    margin-right: 0.5ex;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked\n"
"{\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::right-arrow\n"
"{\n"
"    margin: 0.5ex;\n"
"    border-image: url(:/light/right_arrow.svg);\n"
"    width: 0.6ex;\n"
"    height: 0.9ex;\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #454545;\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #31363b;\n"
"    color: #eff0f1;\n"
"    border: 0.1ex solid 3A3939;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"QWidget:focus,\n"
"QMenuBar:focus\n"
"{\n"
"    border: 0.1ex solid #3daee9;\n"
"}\n"
"\n"
"QTabWidget:focus,\n"
"QCheckBox:focus,\n"
"QRadioButton:focus,\n"
"QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #232629;\n"
"    padding: 0.5ex;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    padding-top: 1ex;\n"
"    margin-top: 1ex;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 0.1ex;\n"
"    padding-right: 0.1ex;\n"
"    margin-top: -0.7ex;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 1.5ex;\n"
"    margin: 0.3ex 1.5ex 0.3ex 1.5ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #3daee9;\n"
"    min-width: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 0.3ex 0px 0.3ex;\n"
"    border-image: url(:/dark/right_arrow_disabled.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0ex 0.3ex 0ex 0.3ex;\n"
"    border-image: url(:/dark/left_arrow_disabled.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark/right_arrow.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark/left_arrow.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 1.5ex;\n"
"    margin: 1.5ex 0.3ex 1.5ex 0.3ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #3daee9;\n"
"    min-height: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/dark/up_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark/up_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #232629;\n"
"    color: #eff0f1;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #232629;;\n"
"    color: #eff0f1;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #76797c;\n"
"    color: #eff0f1;\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QSizeGrip\n"
"{\n"
"    border-image: url(:/dark/sizegrip.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #31363b;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    spacing: 0.2ex;\n"
"    border: 0.1ex dashed #76797c;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    spacing: 0.2ex;\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 0.1ex;\n"
"    background-color: #76797c;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    margin-left: 1ex;\n"
"    margin-right: 0.5ex;\n"
"}\n"
"\n"
"QFrame[frameShape=\"2\"],  /* QFrame::Panel == 0x0003 */\n"
"QFrame[frameShape=\"3\"],  /* QFrame::WinPanel == 0x0003 */\n"
"QFrame[frameShape=\"4\"],  /* QFrame::HLine == 0x0004 */\n"
"QFrame[frameShape=\"5\"],  /* QFrame::VLine == 0x0005 */\n"
"QFrame[frameShape=\"6\"]  /* QFrame::StyledPanel == 0x0006 */\n"
"{\n"
"    border-width: 0.1ex;\n"
"    padding: 0.1ex;\n"
"    border-style: solid;\n"
"    border-color: #31363b;\n"
"    background-color: #76797c;\n"
"    border-radius: 0.5ex;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 0.1ex transparent black;\n"
"}\n"
"\n"
"QToolBar\n"
"{\n"
"    border: 0.1ex transparent #393838;\n"
"    background: 0.1ex solid #31363b;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    border-image: url(:/dark/hmovetoolbar.svg);\n"
"    width = 1.6ex;\n"
"    height = 6.4ex;\n"
"}\n"
"\n"
"QToolBar::handle:vertical\n"
"{\n"
"    border-image: url(:/dark/vmovetoolbar.svg);\n"
"    width = 5.4ex;\n"
"    height = 1ex;\n"
"}\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    border-image: url(:/dark/hsepartoolbar.svg);\n"
"    width = 0.7ex;\n"
"    height = 6.3ex;\n"
"}\n"
"\n"
"QToolBar::separator:vertical\n"
"{\n"
"    border-image: url(:/dark/vsepartoolbars.svg);\n"
"    width = 6.3ex;\n"
"    height = 0.7ex;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #3b4045, stop: 0.5 #31363b);\n"
"    border-width: 0.1ex;\n"
"    border-color: #76797c;\n"
"    border-style: solid;\n"
"    padding: 0.5ex;\n"
"    border-radius: 0.2ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"    border-width: 0.1ex;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 0.5ex;\n"
"    padding-bottom: 0.5ex;\n"
"    padding-left: 1ex;\n"
"    padding-right: 1ex;\n"
"    border-radius: 0.2ex;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #31363b;\n"
"    padding-top: -1.5ex;\n"
"    padding-bottom: -1.7ex;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3daee9;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    padding: 0.5ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    background-color: #76797c;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #454a4f, stop: 0.5 #3b4045);\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #808386, stop: 0.5 #76797c);\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox:hover,\n"
"QAbstractSpinBox:hover,\n"
"QLineEdit:hover,\n"
"QTextEdit:hover,\n"
"QPlainTextEdit:hover,\n"
"QAbstractView:hover,\n"
"QTreeView:hover\n"
"{\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox:hover:pressed,\n"
"QPushButton:hover:pressed,\n"
"QAbstractSpinBox:hover:pressed,\n"
"QLineEdit:hover:pressed,\n"
"QTextEdit:hover:pressed,\n"
"QPlainTextEdit:hover:pressed,\n"
"QAbstractView:hover:pressed,\n"
"QTreeView:hover:pressed\n"
"{\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0.3ex;\n"
"    padding-left: 0.4ex;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #232629;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    selection-background-color: #3daee9;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 1.5ex;\n"
"\n"
"    border-left-width: 0ex;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 0.3ex;\n"
"    border-bottom-right-radius: 0.3ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox\n"
"{\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    background-color: #232629;\n"
"    color: #eff0f1;\n"
"    border-radius: 0.2ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QAbstractSpinBox::up-arrow:off\n"
"{\n"
"    border-image: url(:/dark/up_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    border-image: url(:/dark/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow,\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0ex solid black;\n"
"}\n"
"\n"
"/* BORDERS */\n"
"QTabWidget::pane\n"
"{\n"
"    padding: 0.5ex;\n"
"    margin: 0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:top\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    top: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:bottom\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    bottom: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:left\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    right: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:right\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    left: -0.1ex;\n"
"}\n"
"\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 0.5ex; /* move to the right by 0.5ex */\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0ex transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button\n"
"{\n"
"    border-image: url(:/dark/close.svg);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    border-image: url(:/dark/close-hover.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed\n"
"{\n"
"    border-image: url(:/dark/close-pressed.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    min-width: 50px;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:last,\n"
"QTabBar::tab:top:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    min-width: 50px;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:first:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"    border-left: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"\n"
"QTabBar::tab:bottom\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-bottom: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:last,\n"
"QTabBar::tab:bottom:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    border-bottom: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:first:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"    border-left: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:left:last,\n"
"QTabBar::tab:left:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-bottom: 0.1ex solid #76797c;\n"
"    border-right: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"    border-top: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"}\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:right:last,\n"
"QTabBar::tab:right:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-bottom: 0.1ex solid #76797c;\n"
"    border-left: 0.1ex solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #76797c;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"    border-top: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.2);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled\n"
"{\n"
"    border-image: url(:/dark/right_arrow.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled\n"
"{\n"
"    border-image: url(:/dark/left_arrow.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled\n"
"{\n"
"    border-image: url(:/dark/right_arrow_disabled.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled\n"
"{\n"
"    border-image: url(:/dark/left_arrow_disabled.svg);\n"
"}\n"
"\n"
"QDockWidget\n"
"{\n"
"    background: #31363b;\n"
"    border: 0.1ex solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark/transparent.svg);\n"
"    titlebar-normal-icon: url(:/dark/transparent.svg);\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button\n"
"{\n"
"    border: 0.1ex solid transparent;\n"
"    border-radius: 0.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::float-button\n"
"{\n"
"    border-image: url(:/dark/undock.svg);\n"
"}\n"
"\n"
"QDockWidget::float-button:hover\n"
"{\n"
"    border-image: url(:/dark/undock-hover.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button\n"
"{\n"
"    border-image: url(:/dark/close.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover\n"
"{\n"
"    border-image: url(:/dark/close-hover.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed\n"
"{\n"
"    border-image: url(:/dark/close-pressed.svg) ;\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    background-color: #232629;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item\n"
"{\n"
"    border-image: url(:/dark/stylesheet-vline.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/dark/stylesheet-branch-more.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/dark/stylesheet-branch-end.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings\n"
"{\n"
"    border-image: url(:/dark/stylesheet-branch-end-closed.svg) 0;\n"
"    image: url(:/dark/branch_closed.svg);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings\n"
"{\n"
"    border-image: url(:/dark/stylesheet-branch-end-open.svg) 0;\n"
"    image: url(:/dark/branch_open.svg);\n"
"}\n"
"\n"
"/*\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"        background: cyan;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"        background: red;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"        background: blue;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        background: pink;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed {\n"
"        background: gray;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"        background: magenta;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings {\n"
"        background: green;\n"
"}\n"
"*/\n"
"\n"
"QTableView::item,\n"
"QListView::item,\n"
"QTreeView::item\n"
"{\n"
"    padding: 0.3ex;\n"
"}\n"
"\n"
"QTableView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.2);\n"
"    outline: 0;\n"
"    color: #eff0f1;\n"
"    padding: 0.3ex;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal\n"
"{\n"
"    border: 0.1ex solid #31363b;\n"
"    height: 1ex;\n"
"    background: #565a5e;\n"
"    margin: 0ex;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    background: #dddd00;\n"
"    border: 0.1ex solid #ffff00;\n"
"    width: 3ex;\n"
"    height: 7ex;\n"
"    margin: -3ex 0;\n"
"    border-radius: 0.5ex;\n"
"}\n"
"\n"
"QSlider::groove:vertical\n"
"{\n"
"    border: 0.1ex solid #31363b;\n"
"    width: 0.4ex;\n"
"    background: #565a5e;\n"
"    margin: 0ex;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QSlider::handle:vertical\n"
"{\n"
"    background: #232629;\n"
"    border: 0.1ex solid #626568;\n"
"    width: 1.6ex;\n"
"    height: 1.6ex;\n"
"    margin: 0 -0.8ex;\n"
"    border-radius: 0.9ex;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover,\n"
"QSlider::handle:horizontal:focus,\n"
"QSlider::handle:vertical:hover,\n"
"QSlider::handle:vertical:focus\n"
"{\n"
"    border: 0.1ex solid #3daee9;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal,\n"
"QSlider::add-page:vertical\n"
"{\n"
"    background: #ffff00;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal,\n"
"QSlider::sub-page:vertical\n"
"{\n"
"    background: #626568;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    margin: 0.3ex;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]  /* only for MenuButtonPopup */\n"
"{\n"
"    padding-right: 2ex; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"]  /* only for InstantPopup */\n"
"{\n"
"    padding-right: 1ex; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-indicator\n"
"{\n"
"    border-image: none;\n"
"    image: url(:/dark/down_arrow.svg);\n"
"    top: -0.7ex;\n"
"    left: -0.2ex;\n"
"}\n"
"\n"
"QToolButton::menu-arrow\n"
"{\n"
"    border-image: none;\n"
"    image: url(:/dark/down_arrow.svg);\n"
"}\n"
"\n"
"QToolButton:hover,\n"
"QToolButton::menu-button:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.1ex solid #3daee9;\n"
"}\n"
"\n"
"QToolButton:checked,\n"
"QToolButton:pressed,\n"
"QToolButton::menu-button:pressed\n"
"{\n"
"    background-color: #3daee9;\n"
"    border: 0.1ex solid #3daee9;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolButton::menu-button\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 1ex width + 0.4ex for border + no text = 2ex allocated above */\n"
"    width: 1ex;\n"
"    padding: 0.5ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QPushButton::menu-indicator\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 0.8ex;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 0.1ex solid #76797c;\n"
"    gridline-color: #31363b;\n"
"    background-color: #232629;\n"
"}\n"
"\n"
"\n"
"QTableView,\n"
"QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTreeView::item:pressed\n"
"{\n"
"    background: #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QTableView::item:selected:active,\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active\n"
"{\n"
"    background: #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QListView::item:selected:hover,\n"
"QTreeView::item:selected:hover\n"
"{\n"
"    background-color: #47b8f3;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #31363b;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #31363b;\n"
"    color: #eff0f1;\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: white;\n"
"    background-color: #334e5e;\n"
"}\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow\n"
"{\n"
"    image: url(:/dark/down_arrow.svg);\n"
"}\n"
"\n"
"QHeaderView::up-arrow\n"
"{\n"
"    image: url(:/dark/up_arrow.svg);\n"
"}\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #31363b;\n"
"    border: 0.1ex transparent #76797c;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QToolBox\n"
"{\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex transparent black;\n"
"}\n"
"\n"
"QToolBox:selected\n"
"{\n"
"    background-color: #31363b;\n"
"    border-color: #3daee9;\n"
"}\n"
"\n"
"QToolBox:hover\n"
"{\n"
"    border-color: #3daee9;\n"
"}\n"
"\n"
"QStatusBar::item\n"
"{\n"
"    border: 0px transparent dark;\n"
"}\n"
"\n"
"QFrame[height=\"3\"],\n"
"QFrame[width=\"3\"]\n"
"{\n"
"    background-color: #76797c;\n"
"}\n"
"\n"
"QSplitter::handle\n"
"{\n"
"    border: 0.1ex dashed #76797c;\n"
"}\n"
"\n"
"QSplitter::handle:hover\n"
"{\n"
"    background-color: #787876;\n"
"    border: 0.1ex solid #76797c;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal\n"
"{\n"
"    width: 0.1ex;\n"
"}\n"
"\n"
"QSplitter::handle:vertical\n"
"{\n"
"    height: 0.1ex;\n"
"}\n"
"\n"
"QProgressBar:horizontal\n"
"{\n"
"    background-color: #626568;\n"
"    border: 0.1ex solid #31363b;\n"
"    border-radius: 0.3ex;\n"
"    height: 0.5ex;\n"
"    text-align: right;\n"
"    margin-top: 0.5ex;\n"
"    margin-bottom: 0.5ex;\n"
"    margin-right: 15ex;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal\n"
"{\n"
"    background-color: #ffff00;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QSpinBox,\n"
"QDoubleSpinBox\n"
"{\n"
"    padding-right: 1.5ex;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right top;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    border-image: url(:/dark/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover,\n"
"QSpinBox::up-arrow:pressed,\n"
"QDoubleSpinBox::up-arrow:hover,\n"
"QDoubleSpinBox::up-arrow:pressed\n"
"{\n"
"    border-image: url(:/dark/up_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:off,\n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QDoubleSpinBox::up-arrow:off\n"
"{\n"
"   border-image: url(:/dark/up_arrow_disabled.svg);\n"
"}\n"
"\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right bottom;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:hover,\n"
"QSpinBox::down-arrow:pressed,\n"
"QDoubleSpinBox::down-arrow:hover,\n"
"QDoubleSpinBox::down-arrow:pressed\n"
"{\n"
"    border-image: url(:/dark/down_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off,\n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QDoubleSpinBox::down-arrow:off\n"
"{\n"
"   border-image: url(:/dark/down_arrow_disabled.svg);\n"
"}\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.status_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.status_title.setFont(font)
        self.status_title.setObjectName("status_title")
        self.horizontalLayout_3.addWidget(self.status_title)
        self.status_indicator = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.status_indicator.setFont(font)
        self.status_indicator.setObjectName("status_indicator")
        self.horizontalLayout_3.addWidget(self.status_indicator)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.nozzle_pos_title_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nozzle_pos_title_2.setFont(font)
        self.nozzle_pos_title_2.setObjectName("nozzle_pos_title_2")
        self.verticalLayout.addWidget(self.nozzle_pos_title_2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.x_pos_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.x_pos_title.setFont(font)
        self.x_pos_title.setObjectName("x_pos_title")
        self.horizontalLayout_10.addWidget(self.x_pos_title)
        self.x_pos = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.x_pos.setFont(font)
        self.x_pos.setObjectName("x_pos")
        self.horizontalLayout_10.addWidget(self.x_pos)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.y_pos_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.y_pos_title.setFont(font)
        self.y_pos_title.setObjectName("y_pos_title")
        self.horizontalLayout_9.addWidget(self.y_pos_title)
        self.y_pos = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.y_pos.setFont(font)
        self.y_pos.setObjectName("y_pos")
        self.horizontalLayout_9.addWidget(self.y_pos)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.z_pos_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.z_pos_title.setFont(font)
        self.z_pos_title.setObjectName("z_pos_title")
        self.horizontalLayout_4.addWidget(self.z_pos_title)
        self.z_pos = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.z_pos.setFont(font)
        self.z_pos.setObjectName("z_pos")
        self.horizontalLayout_4.addWidget(self.z_pos)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        self.trajectory_prefs_layout = QtWidgets.QVBoxLayout()
        self.trajectory_prefs_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.trajectory_prefs_layout.setObjectName("trajectory_prefs_layout")
        self.trajectory_preferences_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.trajectory_preferences_title.setFont(font)
        self.trajectory_preferences_title.setObjectName("trajectory_preferences_title")
        self.trajectory_prefs_layout.addWidget(self.trajectory_preferences_title)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.trajectory_prefs_layout.addWidget(self.line_2)
        self.vel_disp = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.vel_disp.setFont(font)
        self.vel_disp.setObjectName("vel_disp")
        self.trajectory_prefs_layout.addWidget(self.vel_disp)
        self.velocitySlider = QtWidgets.QSlider(self.centralwidget)
        self.velocitySlider.setMaximum(100)
        self.velocitySlider.setSingleStep(0)
        self.velocitySlider.setProperty("value", 50)
        self.velocitySlider.setSliderPosition(50)
        self.velocitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.velocitySlider.setInvertedAppearance(False)
        self.velocitySlider.setInvertedControls(False)
        self.velocitySlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.velocitySlider.setObjectName("velocitySlider")
        self.trajectory_prefs_layout.addWidget(self.velocitySlider)
        self.stroke_spacing_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.stroke_spacing_label.setFont(font)
        self.stroke_spacing_label.setObjectName("stroke_spacing_label")
        self.trajectory_prefs_layout.addWidget(self.stroke_spacing_label)
        self.stroke_spacing_slider = QtWidgets.QSlider(self.centralwidget)
        self.stroke_spacing_slider.setMaximum(100)
        self.stroke_spacing_slider.setProperty("value", 100)
        self.stroke_spacing_slider.setSliderPosition(100)
        self.stroke_spacing_slider.setOrientation(QtCore.Qt.Horizontal)
        self.stroke_spacing_slider.setObjectName("stroke_spacing_slider")
        self.trajectory_prefs_layout.addWidget(self.stroke_spacing_slider)
        self.depth_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.depth_label.setFont(font)
        self.depth_label.setObjectName("depth_label")
        self.trajectory_prefs_layout.addWidget(self.depth_label)
        self.depth_slider = QtWidgets.QSlider(self.centralwidget)
        self.depth_slider.setMaximum(100)
        self.depth_slider.setSliderPosition(0)
        self.depth_slider.setOrientation(QtCore.Qt.Horizontal)
        self.depth_slider.setObjectName("depth_slider")
        self.trajectory_prefs_layout.addWidget(self.depth_slider)
        self.horizontalLayout_13.addLayout(self.trajectory_prefs_layout)
        self.horizontalLayout_13.setStretch(0, 7)
        self.horizontalLayout_13.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.knot_points_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.knot_points_title.setFont(font)
        self.knot_points_title.setObjectName("knot_points_title")
        self.horizontalLayout_5.addWidget(self.knot_points_title)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.cart_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cart_btn.sizePolicy().hasHeightForWidth())
        self.cart_btn.setSizePolicy(sizePolicy)
        self.cart_btn.setMinimumSize(QtCore.QSize(0, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cart_btn.setFont(font)
        self.cart_btn.setObjectName("cart_btn")
        self.horizontalLayout_5.addWidget(self.cart_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.knot_point_list = QtWidgets.QListWidget(self.centralwidget)
        self.knot_point_list.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.knot_point_list.setFont(font)
        self.knot_point_list.setObjectName("knot_point_list")
        self.verticalLayout_7.addWidget(self.knot_point_list)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout_6.addWidget(self.reset_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout_6.addWidget(self.remove_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ik_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.ik_btn.setFont(font)
        self.ik_btn.setObjectName("ik_btn")
        self.horizontalLayout.addWidget(self.ik_btn)
        self.spray_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.spray_btn.setFont(font)
        self.spray_btn.setObjectName("spray_btn")
        self.horizontalLayout.addWidget(self.spray_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.plot_layout = QtWidgets.QVBoxLayout()
        self.plot_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.plot_layout.setObjectName("plot_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.nozzle_pos_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nozzle_pos_title.setFont(font)
        self.nozzle_pos_title.setObjectName("nozzle_pos_title")
        self.horizontalLayout_2.addWidget(self.nozzle_pos_title)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.plot_layout.addLayout(self.horizontalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.plot_layout.addWidget(self.line_3)
        self.plot_widget = MplWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy)
        self.plot_widget.setMinimumSize(QtCore.QSize(250, 170))
        self.plot_widget.setObjectName("plot_widget")
        self.plot_layout.addWidget(self.plot_widget)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.toggle_can_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_can_btn.sizePolicy().hasHeightForWidth())
        self.toggle_can_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.toggle_can_btn.setFont(font)
        self.toggle_can_btn.setObjectName("toggle_can_btn")
        self.horizontalLayout_11.addWidget(self.toggle_can_btn)
        self.plot_layout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_14.addWidget(self.progressBar)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem10)
        self.x_pos_title_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.x_pos_title_2.setFont(font)
        self.x_pos_title_2.setObjectName("x_pos_title_2")
        self.horizontalLayout_14.addWidget(self.x_pos_title_2)
        self.can_indicator = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.can_indicator.setFont(font)
        self.can_indicator.setObjectName("can_indicator")
        self.horizontalLayout_14.addWidget(self.can_indicator)
        self.can_led = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.can_led.sizePolicy().hasHeightForWidth())
        self.can_led.setSizePolicy(sizePolicy)
        self.can_led.setMinimumSize(QtCore.QSize(19, 19))
        self.can_led.setObjectName("can_led")
        self.horizontalLayout_14.addWidget(self.can_led)
        self.plot_layout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_8.addLayout(self.plot_layout)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1625, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HMI AMV 4200H"))
        self.status_title.setText(_translate("MainWindow", "Status:"))
        self.status_indicator.setText(_translate("MainWindow", "init"))
        self.nozzle_pos_title_2.setText(_translate("MainWindow", "Nozzle position"))
        self.x_pos_title.setText(_translate("MainWindow", "X:"))
        self.x_pos.setText(_translate("MainWindow", "TextLabel"))
        self.y_pos_title.setText(_translate("MainWindow", "Y:"))
        self.y_pos.setText(_translate("MainWindow", "TextLabel"))
        self.z_pos_title.setText(_translate("MainWindow", "Z:"))
        self.z_pos.setText(_translate("MainWindow", "TextLabel"))
        self.trajectory_preferences_title.setText(_translate("MainWindow", "Trajectory preferences"))
        self.vel_disp.setText(_translate("MainWindow", "Velocity"))
        self.stroke_spacing_label.setText(_translate("MainWindow", "Stroke spacing"))
        self.depth_label.setText(_translate("MainWindow", "Depth"))
        self.knot_points_title.setText(_translate("MainWindow", "Knot points"))
        self.cart_btn.setText(_translate("MainWindow", "Generate surface"))
        self.reset_btn.setText(_translate("MainWindow", "Reset all"))
        self.remove_btn.setText(_translate("MainWindow", "Remove selected"))
        self.ik_btn.setText(_translate("MainWindow", "Inverse kinematics"))
        self.spray_btn.setText(_translate("MainWindow", "Spray"))
        self.nozzle_pos_title.setText(_translate("MainWindow", "3D plot"))
        self.toggle_can_btn.setText(_translate("MainWindow", "Toggle CAN"))
        self.x_pos_title_2.setText(_translate("MainWindow", "CAN status:"))
        self.can_indicator.setText(_translate("MainWindow", "not initialised"))


from mplwidget import MplWidget
