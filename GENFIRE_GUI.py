# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(845, 634)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_4.setMargin(11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setMargin(11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setMinimumSize(QtCore.QSize(512, 93))
        self.widget.setStyleSheet(_fromUtf8("background-image: url(/Users/ajpryor/Documents/GENFIRE/GENFIRE/logo.png)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3.addWidget(self.widget)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 9, 0, 1, 1)
        self.lineEdit_angle = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_angle.setObjectName(_fromUtf8("lineEdit_angle"))
        self.gridLayout.addWidget(self.lineEdit_angle, 5, 2, 1, 1)
        self.checkBox_provide_io = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_provide_io.setObjectName(_fromUtf8("checkBox_provide_io"))
        self.gridLayout.addWidget(self.checkBox_provide_io, 7, 0, 1, 1)
        self.btn_angles = QtGui.QPushButton(self.centralWidget)
        self.btn_angles.setObjectName(_fromUtf8("btn_angles"))
        self.gridLayout.addWidget(self.btn_angles, 5, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)
        self.checkBox_default_support = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_default_support.setObjectName(_fromUtf8("checkBox_default_support"))
        self.gridLayout.addWidget(self.checkBox_default_support, 3, 0, 1, 1)
        self.lineEdit_pj = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_pj.setObjectName(_fromUtf8("lineEdit_pj"))
        self.gridLayout.addWidget(self.lineEdit_pj, 0, 2, 1, 1)
        self.btn_io = QtGui.QPushButton(self.centralWidget)
        self.btn_io.setObjectName(_fromUtf8("btn_io"))
        self.gridLayout.addWidget(self.btn_io, 8, 0, 1, 1)
        self.lineEdit_support = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_support.setObjectName(_fromUtf8("lineEdit_support"))
        self.gridLayout.addWidget(self.lineEdit_support, 2, 2, 1, 1)
        self.btn_support = QtGui.QPushButton(self.centralWidget)
        self.btn_support.setObjectName(_fromUtf8("btn_support"))
        self.gridLayout.addWidget(self.btn_support, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout.addLayout(self.horizontalLayout, 12, 0, 1, 1)
        self.lineEdit_io = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_io.setObjectName(_fromUtf8("lineEdit_io"))
        self.gridLayout.addWidget(self.lineEdit_io, 8, 2, 1, 1)
        self.lineEdit_results = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_results.setObjectName(_fromUtf8("lineEdit_results"))
        self.gridLayout.addWidget(self.lineEdit_results, 11, 2, 1, 1)
        self.btn_projections = QtGui.QPushButton(self.centralWidget)
        self.btn_projections.setObjectName(_fromUtf8("btn_projections"))
        self.gridLayout.addWidget(self.btn_projections, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_on = QtGui.QRadioButton(self.groupBox)
        self.radioButton_on.setObjectName(_fromUtf8("radioButton_on"))
        self.verticalLayout.addWidget(self.radioButton_on)
        self.radioButton_off = QtGui.QRadioButton(self.groupBox)
        self.radioButton_off.setObjectName(_fromUtf8("radioButton_off"))
        self.verticalLayout.addWidget(self.radioButton_off)
        self.radioButton_extension = QtGui.QRadioButton(self.groupBox)
        self.radioButton_extension.setObjectName(_fromUtf8("radioButton_extension"))
        self.verticalLayout.addWidget(self.radioButton_extension)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_oversamplingRatio = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_oversamplingRatio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_oversamplingRatio.setObjectName(_fromUtf8("lineEdit_oversamplingRatio"))
        self.gridLayout_2.addWidget(self.lineEdit_oversamplingRatio, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_interpolationCutoffDistance = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_interpolationCutoffDistance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_interpolationCutoffDistance.setObjectName(_fromUtf8("lineEdit_interpolationCutoffDistance"))
        self.gridLayout_2.addWidget(self.lineEdit_interpolationCutoffDistance, 2, 1, 1, 1)
        self.lineEdit_numIterations = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_numIterations.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_numIterations.setObjectName(_fromUtf8("lineEdit_numIterations"))
        self.gridLayout_2.addWidget(self.lineEdit_numIterations, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setMargin(11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.checkBox_displayFigure = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_displayFigure.setObjectName(_fromUtf8("checkBox_displayFigure"))
        self.gridLayout_3.addWidget(self.checkBox_displayFigure, 0, 0, 1, 2)
        self.lineEdit_displayFrequency = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_displayFrequency.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_displayFrequency.setObjectName(_fromUtf8("lineEdit_displayFrequency"))
        self.gridLayout_3.addWidget(self.lineEdit_displayFrequency, 1, 1, 1, 1)
        self.checkBox_rfree = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_rfree.setObjectName(_fromUtf8("checkBox_rfree"))
        self.gridLayout_3.addWidget(self.checkBox_rfree, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 4, 3, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.btn_reconstruct = QtGui.QPushButton(self.centralWidget)
        self.btn_reconstruct.setObjectName(_fromUtf8("btn_reconstruct"))
        self.verticalLayout_4.addWidget(self.btn_reconstruct)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_log = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_log.setObjectName(_fromUtf8("checkBox_log"))
        self.verticalLayout_2.addWidget(self.checkBox_log)
        self.log = QtGui.QTextEdit(self.centralWidget)
        self.log.setObjectName(_fromUtf8("log"))
        self.verticalLayout_2.addWidget(self.log)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuGENFIRE = QtGui.QMenu(self.menuBar)
        self.menuGENFIRE.setObjectName(_fromUtf8("menuGENFIRE"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.action_Create_Support = QtGui.QAction(MainWindow)
        self.action_Create_Support.setObjectName(_fromUtf8("action_Create_Support"))
        self.menuTools.addAction(self.action_Create_Support)
        self.menuBar.addAction(self.menuGENFIRE.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_pj, self.lineEdit_support)
        MainWindow.setTabOrder(self.lineEdit_support, self.lineEdit_angle)
        MainWindow.setTabOrder(self.lineEdit_angle, self.lineEdit_io)
        MainWindow.setTabOrder(self.lineEdit_io, self.lineEdit_numIterations)
        MainWindow.setTabOrder(self.lineEdit_numIterations, self.lineEdit_oversamplingRatio)
        MainWindow.setTabOrder(self.lineEdit_oversamplingRatio, self.lineEdit_interpolationCutoffDistance)
        MainWindow.setTabOrder(self.lineEdit_interpolationCutoffDistance, self.radioButton_on)
        MainWindow.setTabOrder(self.radioButton_on, self.radioButton_off)
        MainWindow.setTabOrder(self.radioButton_off, self.radioButton_extension)
        MainWindow.setTabOrder(self.radioButton_extension, self.btn_angles)
        MainWindow.setTabOrder(self.btn_angles, self.btn_io)
        MainWindow.setTabOrder(self.btn_io, self.btn_projections)
        MainWindow.setTabOrder(self.btn_projections, self.btn_support)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GENFIRE", None))
        self.label_4.setText(_translate("MainWindow", "Results Filename", None))
        self.checkBox_provide_io.setText(_translate("MainWindow", "Provide initial object", None))
        self.btn_angles.setText(_translate("MainWindow", "Select Angle File", None))
        self.checkBox_default_support.setText(_translate("MainWindow", "Use default support", None))
        self.btn_io.setText(_translate("MainWindow", "Select Inital Object File", None))
        self.btn_support.setText(_translate("MainWindow", "Select Support File", None))
        self.btn_projections.setText(_translate("MainWindow", "Select Projection File", None))
        self.groupBox.setTitle(_translate("MainWindow", "Resolution Extension/Suppression", None))
        self.radioButton_on.setText(_translate("MainWindow", "On", None))
        self.radioButton_off.setText(_translate("MainWindow", "Off", None))
        self.radioButton_extension.setText(_translate("MainWindow", "Extension Only", None))
        self.label_2.setText(_translate("MainWindow", "Oversampling Ratio", None))
        self.label_3.setText(_translate("MainWindow", "Interpolation Cutoff Distance (pixels)", None))
        self.label.setText(_translate("MainWindow", "Number of Iterations", None))
        self.label_5.setText(_translate("MainWindow", "Display Frequency (iterations)", None))
        self.checkBox_displayFigure.setText(_translate("MainWindow", "Display Figure", None))
        self.checkBox_rfree.setText(_translate("MainWindow", "Calculate Rfree", None))
        self.btn_reconstruct.setText(_translate("MainWindow", "Launch Reconstruction", None))
        self.checkBox_log.setText(_translate("MainWindow", "Activate Log", None))
        self.menuGENFIRE.setTitle(_translate("MainWindow", "GENFIRE", None))
        self.menuTools.setTitle(_translate("MainWindow", "Projection Calculator", None))
        self.action_Create_Support.setText(_translate("MainWindow", "Launch Projection Calculator", None))

