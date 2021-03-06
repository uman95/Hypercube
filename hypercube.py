from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sys
import itertools as it
from collections import defaultdict 
from operator import itemgetter
import random
import tkinter as tk
from tkinter import filedialog
import pickle
import dill

class Ui_PoolTestingCalculator(object):

    def __init__(self, slices=3, constant=0.35):
        self.slices = slices
        self.constant = constant
        self.text = {}
        self.D = ""
        self.poolSize = ""
        self.text["dimension"] = ""
        self.text["prevalence"] = ""
        self.text["samples"] = ""
        self.text["secondRound"] = ""
        self.text["positiveList"] = ""
        self.text["subTest"] = ""
        
    def setupUi(self, PoolTestingCalculator):
        PoolTestingCalculator.setObjectName("PoolTestingCalculator")
        PoolTestingCalculator.resize(1112, 643)
        PoolTestingCalculator.setMouseTracking(True)
        PoolTestingCalculator.setStyleSheet("text-align: middle;")
        PoolTestingCalculator.setWindowTitle("Hypercube Pool Testing Calculator")
        PoolTestingCalculator.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        PoolTestingCalculator.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(PoolTestingCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.testSetup = QtWidgets.QWidget(self.centralwidget)
        self.testSetup.setGeometry(QtCore.QRect(276, 60, 817, 331))
        self.testSetup.setStyleSheet("border-radius: 5px;border: 1px solid rgb(2, 83, 121);background: #fff;")
        self.testSetup.setObjectName("testSetup")
        self.testSetupTitle = QtWidgets.QLabel(self.testSetup)
        self.testSetupTitle.setGeometry(QtCore.QRect(300, 10, 191, 21))
        self.testSetupTitle.setText("Tests Setup")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.testSetupTitle.setFont(font)
        self.testSetupTitle.setStyleSheet("border: none;font-size: 14pt;font-weight: 600;color:#02655e;")
        self.testSetupTitle.setObjectName("testSetupTitle")
        self.outPoolSize = QtWidgets.QLabel(self.testSetup)
        self.outPoolSize.setAlignment(QtCore.Qt.AlignRight)
        self.outPoolSize.setGeometry(QtCore.QRect(20, 65, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.outPoolSize.setFont(font)
        self.outPoolSize.setMouseTracking(True)
        self.outPoolSize.setAutoFillBackground(False)
        self.outPoolSize.setStyleSheet("border: none;")
        self.outPoolSize.setText("Pool size:")
        self.outPoolSize.setObjectName("outPoolSize")
        self.numberPools = QtWidgets.QLabel(self.testSetup)
        self.numberPools.setGeometry(QtCore.QRect(20, 90, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.numberPools.setFont(font)
        self.numberPools.setMouseTracking(True)
        self.numberPools.setAutoFillBackground(False)
        self.numberPools.setStyleSheet("border: none;")
        self.numberPools.setText("Number of pools:")
        
        self.numberPools.setObjectName("numberPools")
        self.line_4 = QtWidgets.QFrame(self.testSetup)
        self.line_4.setGeometry(QtCore.QRect(0, 40, 817, 16))
        self.line_4.setStyleSheet("border-bottom: 0;border-radius: 0;")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.firstSetup = QtWidgets.QLabel(self.testSetup)
        self.firstSetup.setGeometry(QtCore.QRect(80, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.firstSetup.setFont(font)
        self.firstSetup.setMouseTracking(True)
        self.firstSetup.setAutoFillBackground(False)
        self.firstSetup.setStyleSheet("background: #02655e;color: rgb(255, 255, 255);transform: rotate(45deg);")
        self.firstSetup.setText("     First round")
        self.firstSetup.setObjectName("firstSetup")
        self.sizeNumber = QtWidgets.QLabel(self.testSetup)
        self.sizeNumber.setGeometry(QtCore.QRect(160, 63, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sizeNumber.setFont(font)
        self.sizeNumber.setMouseTracking(True)
        self.sizeNumber.setAutoFillBackground(False)
        self.sizeNumber.setStyleSheet("border: none;")
        self.sizeNumber.setText("0")
        self.sizeNumber.setObjectName("sizeNumber")
        self.valueNumberOfPools = QtWidgets.QLabel(self.testSetup)
        self.sizeNumber.setAlignment(QtCore.Qt.AlignRight)
        self.valueNumberOfPools.setGeometry(QtCore.QRect(160, 93, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valueNumberOfPools.setFont(font)
        self.valueNumberOfPools.setMouseTracking(True)
        self.valueNumberOfPools.setAutoFillBackground(False)
        self.valueNumberOfPools.setStyleSheet("border: none;")
        self.valueNumberOfPools.setText("0")
        self.valueNumberOfPools.setAlignment(QtCore.Qt.AlignRight)
        self.valueNumberOfPools.setObjectName("valueNumberOfPools")
        self.line_5 = QtWidgets.QFrame(self.testSetup)
        self.line_5.setGeometry(QtCore.QRect(0, 120, 817, 20))
        self.line_5.setStyleSheet("border-bottom: 0;border-radius: 0;")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.secondSetup = QtWidgets.QLabel(self.testSetup)
        self.secondSetup.setGeometry(QtCore.QRect(490, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.secondSetup.setFont(font)
        self.secondSetup.setMouseTracking(True)
        self.secondSetup.setAutoFillBackground(False)
        self.secondSetup.setStyleSheet("background:rgb(77, 69, 23);color: rgb(255, 255, 255);transform: rotate(45deg);")
        self.secondSetup.setText("  Second round")
        self.secondSetup.setObjectName("secondSetup")
        self.numSlices = QtWidgets.QLabel(self.testSetup)
        self.numSlices.setGeometry(QtCore.QRect(300, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.numSlices.setFont(font)
        self.numSlices.setMouseTracking(True)
        self.numSlices.setAutoFillBackground(False)
        self.numSlices.setStyleSheet("border: none;")
        self.numSlices.setText("Number of slices:")
        self.numSlices.setObjectName("numSlices")
        self.valueDimension = QtWidgets.QLabel(self.testSetup)
        self.valueDimension.setGeometry(QtCore.QRect(440, 63, 71, 16))
        self.valueDimension.setAlignment(QtCore.Qt.AlignRight)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valueDimension.setFont(font)
        self.valueDimension.setMouseTracking(True)
        self.valueDimension.setAutoFillBackground(False)
        self.valueDimension.setStyleSheet("border: none;")
        self.valueDimension.setText("0")
        self.valueDimension.setAlignment(QtCore.Qt.AlignRight)
        self.valueDimension.setObjectName("valueDimension")
        self.slicesTitle = QtWidgets.QLabel(self.testSetup)
        self.slicesTitle.setGeometry(QtCore.QRect(300, 130, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.slicesTitle.setFont(font)
        self.slicesTitle.setStyleSheet("border: none;font-size: 14pt;font-weight: 600;color:rgb(77, 69, 23);")
        self.slicesTitle.setText("Sliced samples")
        self.slicesTitle.setObjectName("slicesTitle")
        self.line_3 = QtWidgets.QFrame(self.testSetup)
        self.line_3.setGeometry(QtCore.QRect(273, 40, 16, 81))
        self.line_3.setStyleSheet("border-left: none;border-radius: 0;")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.dimension = QtWidgets.QLabel(self.testSetup)
        self.dimension.setGeometry(QtCore.QRect(300, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dimension.setFont(font)
        self.dimension.setMouseTracking(True)
        self.dimension.setAutoFillBackground(False)
        self.dimension.setStyleSheet("border: none;")
        self.dimension.setText("Dimension:")
        self.dimension.setObjectName("dimension")
        self.maxSizeSlice = QtWidgets.QLabel(self.testSetup)
        self.maxSizeSlice.setGeometry(QtCore.QRect(544, 60, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maxSizeSlice.setFont(font)
        self.maxSizeSlice.setMouseTracking(True)
        self.maxSizeSlice.setAutoFillBackground(False)
        self.maxSizeSlice.setStyleSheet("border: none;")
        self.maxSizeSlice.setText("Max size of a slice:")
        self.maxSizeSlice.setObjectName("maxSizeSlice")
        self.valueSlices = QtWidgets.QLabel(self.testSetup)
        self.valueSlices.setGeometry(QtCore.QRect(440, 93, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valueSlices.setFont(font)
        self.valueSlices.setMouseTracking(True)
        self.valueSlices.setAutoFillBackground(False)
        self.valueSlices.setStyleSheet("border: none;")
        self.valueSlices.setText("0")
        self.valueSlices.setAlignment(QtCore.Qt.AlignRight)
        self.valueSlices.setObjectName("valueSlices")
        self.numMaxSlice = QtWidgets.QLabel(self.testSetup)
        self.numMaxSlice.setGeometry(QtCore.QRect(702, 63, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.numMaxSlice.setFont(font)
        self.numMaxSlice.setMouseTracking(True)
        self.numMaxSlice.setAutoFillBackground(False)
        self.numMaxSlice.setStyleSheet("border: none;")
        self.numMaxSlice.setText("0")
        self.numMaxSlice.setAlignment(QtCore.Qt.AlignRight)
        self.numMaxSlice.setObjectName("numMaxSlice")
        self.dimensionTabs = QtWidgets.QTabWidget(self.testSetup)
        self.dimensionTabs.setGeometry(QtCore.QRect(1, 150, 815, 180))
        self.dimensionTabs.setObjectName("dimensionTabs")
        self.dimensionTabs.currentChanged.connect(self.onTabChange)
        self.poolNumbers = QtWidgets.QLabel()
        self.poolNumbers.setGeometry(QtCore.QRect(30, 60, 481, 20))
        self.poolNumbers.setStyleSheet("border: none;")
        self.poolNumbers.setText("")
        self.poolNumbers.setWordWrap(True)
        self.poolNumbers.setObjectName("poolNumbers")
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidget(self.poolNumbers)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(400)
        self.resOutput = QtWidgets.QWidget(self.centralwidget)
        self.resOutput.setGeometry(QtCore.QRect(276, 400, 817, 181))
        self.resOutput.setStyleSheet("border-radius: 5px;border: 1px solid rgb(2, 83, 121);background: #fff;")
        self.resOutput.setObjectName("resOutput")
        self.resutlTitle = QtWidgets.QLabel(self.resOutput)
        self.resutlTitle.setGeometry(QtCore.QRect(350, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resutlTitle.setFont(font)
        self.resutlTitle.setStyleSheet("border: none;font-size: 14pt;font-weight: 600;color:rgb(118, 37, 26);")
        self.resutlTitle.setText("Tests results")
        self.resutlTitle.setObjectName("resutlTitle")
        self.subResutlTitle = QtWidgets.QLabel(self.resOutput)
        self.subResutlTitle.setGeometry(QtCore.QRect(320, 10, 200, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.subResutlTitle.setFont(font)
        self.subResutlTitle.setStyleSheet("border: none;font-size: 14pt;font-weight: 600;color:rgb(118, 37, 26);")
        self.subResutlTitle.setText("Sub-tests results")
        self.subResutlTitle.setObjectName("subResutlTitle")
        self.subResutlTitle.setHidden(True)
        self.line_6 = QtWidgets.QFrame(self.resOutput)
        self.line_6.setGeometry(QtCore.QRect(0, 40, 817, 16))
        self.line_6.setStyleSheet("border-bottom: 0;border-radius: 0;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.posSlices = QtWidgets.QLabel(self.resOutput)
        self.posSlices.setGeometry(QtCore.QRect(220, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.posSlices.setFont(font)
        self.posSlices.setMouseTracking(True)
        self.posSlices.setAutoFillBackground(False)
        self.posSlices.setStyleSheet("background: rgb(130, 89, 17);color: rgb(255, 255, 255);transform: rotate(45deg);")
        self.posSlices.setText("  Positive slices")
        self.posSlices.setObjectName("posSlices")
        self.posSamples = QtWidgets.QLabel(self.resOutput)
        self.posSamples.setGeometry(QtCore.QRect(651, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.posSamples.setFont(font)
        self.posSamples.setMouseTracking(True)
        self.posSamples.setAutoFillBackground(False)
        self.posSamples.setStyleSheet("background: rgb(118, 37, 26);color: rgb(255, 255, 255);transform: rotate(45deg);")
        self.posSamples.setText("  Positive samples")
        self.posSamples.setObjectName("posSamples")
        self.line_9 = QtWidgets.QFrame(self.resOutput)
        self.line_9.setGeometry(QtCore.QRect(611, 40, 16, 141))
        self.line_9.setStyleSheet("border-left: none;border-radius: 0;")
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.okButton = QtWidgets.QPushButton(self.resOutput)
        self.okButton.setGeometry(QtCore.QRect(580, 150, 41, 25))
        self.okButton.setMouseTracking(True)
        self.okButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.okButton.setAutoFillBackground(False)
        self.okButton.setStyleSheet("background:#02655e;color: #fff;font-weight: 600")
        self.okButton.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.okButton.setAutoDefault(True)
        self.okButton.setFlat(True)
        self.okButton.setText("OK")
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(self.find_positive)
        self.resetButton = QtWidgets.QPushButton(self.resOutput)
        self.resetButton.setGeometry(QtCore.QRect(510, 150, 61, 25))
        self.resetButton.setMouseTracking(True)
        self.resetButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.resetButton.setAutoFillBackground(False)
        self.resetButton.setStyleSheet("background: rgb(156, 3, 3);color: #fff;font-weight: 600")
        self.resetButton.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.resetButton.setAutoDefault(True)
        self.resetButton.setFlat(True)
        self.resetButton.setText("Reset")
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.resetPositiveSlices)
        self.positiveSamples = QtWidgets.QLabel(self.resOutput)
        self.positiveSamples.setGeometry(QtCore.QRect(640, 60, 161, 111))
        self.positiveSamples.setStyleSheet("text-align: justify; border: none; font-size: 14pt; font-weight: 600; color:rgb(118, 37, 26)")
        self.positiveSamples.setText("")
        self.positiveSamples.setWordWrap(True)
        self.positiveSamples.setObjectName("positiveSamples")
        self.positiveSlices = QtWidgets.QLabel(self.resOutput)
        self.positiveSlices.setGeometry(QtCore.QRect(20, 50, 591, 121))
        self.positiveSlices.setStyleSheet("text-align: justify; border: none; font-size: 14pt; font-weight: 600; color:rgb(130, 89, 17)")
        self.positiveSlices.setText("")
        self.positiveSlices.setWordWrap(True)
        self.positiveSlices.setObjectName("positiveSlices")
        self.line_6.raise_()
        self.resutlTitle.raise_()
        self.posSlices.raise_()
        self.posSamples.raise_()
        self.line_9.raise_()
        self.positiveSlices.raise_()
        self.okButton.raise_()
        self.resetButton.raise_()
        self.positiveSamples.raise_()
        self.input = QtWidgets.QWidget(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 10, 251, 582))
        self.input.setAutoFillBackground(False)
        self.input.setStyleSheet("border-radius: 5px;border: 1px solid rgb(2, 83, 121);background: rgb(185, 198, 180)")
        self.input.setObjectName("input")
        self.prevalence_4 = QtWidgets.QLabel(self.input)
        self.prevalence_4.setGeometry(QtCore.QRect(20, 100, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prevalence_4.setFont(font)
        self.prevalence_4.setMouseTracking(True)
        self.prevalence_4.setAutoFillBackground(False)
        self.prevalence_4.setStyleSheet("border: none;")
        self.prevalence_4.setText("")
        self.prevalence_4.setObjectName("prevalence_4")
        self.resInput = QtWidgets.QWidget(self.input)
        self.resInput.setGeometry(QtCore.QRect(10, 390, 231, 181))
        self.resInput.setAutoFillBackground(False)
        self.resInput.setStyleSheet("border-radius: 0 ;border: 1px solid rgb(2, 83, 121);background: #fff;")
        self.resInput.setObjectName("resInput")
        self.dimensionInput = QtWidgets.QLabel(self.resInput)
        self.dimensionInput.setGeometry(QtCore.QRect(20, 60, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dimensionInput.setFont(font)
        self.dimensionInput.setMouseTracking(True)
        self.dimensionInput.setAutoFillBackground(False)
        self.dimensionInput.setStyleSheet("border: none;")
        self.dimensionInput.setText("Dimension")
        self.dimensionInput.setObjectName("dimensionInput")
        self.prevalence_3 = QtWidgets.QLabel(self.resInput)
        self.prevalence_3.setGeometry(QtCore.QRect(20, 100, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prevalence_3.setFont(font)
        self.prevalence_3.setMouseTracking(True)
        self.prevalence_3.setAutoFillBackground(False)
        self.prevalence_3.setStyleSheet("border: none;")
        self.prevalence_3.setText("")
        self.prevalence_3.setObjectName("prevalence_3")
        self.addSliceButton = QtWidgets.QPushButton(self.resInput)
        self.addSliceButton.setGeometry(QtCore.QRect(90, 140, 71, 25))
        self.addSliceButton.setMouseTracking(True)
        self.addSliceButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.addSliceButton.setAutoFillBackground(False)
        self.addSliceButton.setStyleSheet("background: rgb(130, 89, 17);color: #fff; border-radius: 5px; font-weight: 600")
        self.addSliceButton.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.addSliceButton.setAutoDefault(True)
        self.addSliceButton.setFlat(True)
        self.addSliceButton.setText("Add slice")
        self.addSliceButton.setObjectName("addSliceButton")
        self.addSliceButton.clicked.connect(self.addSlice)
        self.addSliceTitle = QtWidgets.QLabel(self.resInput)
        self.addSliceTitle.setGeometry(QtCore.QRect(49, 10, 151, 19))
        self.addSliceTitle = QtWidgets.QLabel(self.resInput)
        self.addSliceTitle.setGeometry(QtCore.QRect(49, 10, 151, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addSliceTitle.setFont(font)
        self.addSliceTitle.setMouseTracking(True)
        self.addSliceTitle.setAutoFillBackground(False)
        self.addSliceTitle.setStyleSheet("border: none;color: rgb(130, 89, 17);")
        self.addSliceTitle.setText("Add a positive slice")
        self.addSliceTitle.setObjectName("addSliceTitle")
        self.addSubSliceTitle = QtWidgets.QLabel(self.resInput)
        self.addSubSliceTitle.setGeometry(QtCore.QRect(15, 10, 200, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addSubSliceTitle.setFont(font)
        self.addSubSliceTitle.setMouseTracking(True)
        self.addSubSliceTitle.setAutoFillBackground(False)
        self.addSubSliceTitle.setStyleSheet("border: none;color: rgb(130, 89, 17);")
        self.addSubSliceTitle.setText("Add a sub-test positive slice")
        self.addSubSliceTitle.setObjectName("addSubSliceTitle")
        self.addSubSliceTitle.setHidden(True)
        self.line_7 = QtWidgets.QFrame(self.resInput)
        self.line_7.setGeometry(QtCore.QRect(0, 40, 231, 16))
        self.line_7.setStyleSheet("border-bottom: 0;border-radius: 0;")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.colorInput = QtWidgets.QLabel(self.resInput)
        self.colorInput.setGeometry(QtCore.QRect(20, 100, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.colorInput.setFont(font)
        self.colorInput.setMouseTracking(True)
        self.colorInput.setAutoFillBackground(False)
        self.colorInput.setStyleSheet("border: none;")
        self.colorInput.setText("Color")
        self.colorInput.setObjectName("colorInput")
        self.dimSelect = QtWidgets.QComboBox(self.resInput)
        self.dimSelect.setGeometry(QtCore.QRect(110, 60, 111, 27))
        self.dimSelect.setObjectName("dimSelect")
        self.dimSelect.setStyleSheet("font-size: 14pt; color:rgb(77, 69, 23)")
        self.colorSelect = QtWidgets.QComboBox(self.resInput)
        self.colorSelect.setGeometry(QtCore.QRect(110, 100, 111, 27))
        self.colorSelect.setObjectName("colorSelect")
        self.colorSelect.setStyleSheet("font-size: 14pt; color:rgb(77, 69, 23)")
        self.colorSelect.addItems(["Yellow", "Red", "Green"])      
        self.secondRound = QtWidgets.QWidget(self.input)
        self.secondRound.setGeometry(QtCore.QRect(10, 239, 231, 141))
        self.secondRound.setAutoFillBackground(False)
        self.secondRound.setStyleSheet("border-radius: 0px;border: 1px solid rgb(2, 83, 121);background: #fff;")
        self.secondRound.setObjectName("secondRound")
        self.poolSizeEdit = QtWidgets.QLineEdit(self.secondRound)
        self.poolSizeEdit.setGeometry(QtCore.QRect(120, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.poolSizeEdit.setFont(font)
        self.poolSizeEdit.setStyleSheet("border: 1px solid rgb(72, 72, 72);border-radius: 0;text-align: right;")
        self.poolSizeEdit.setAlignment(QtCore.Qt.AlignRight)
        self.poolSizeEdit.setObjectName("poolSizeEdit")
        self.inPoolSize = QtWidgets.QLabel(self.secondRound)
        self.inPoolSize.setGeometry(QtCore.QRect(20, 60, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inPoolSize.setFont(font)
        self.inPoolSize.setMouseTracking(True)
        self.inPoolSize.setAutoFillBackground(False)
        self.inPoolSize.setStyleSheet("border: none;")
        self.inPoolSize.setText("Pool size:")
        self.inPoolSize.setObjectName("inPoolSize")
        self.calcSecondButton = QtWidgets.QPushButton(self.secondRound)
        self.calcSecondButton.setGeometry(QtCore.QRect(120, 100, 71, 25))
        self.calcSecondButton.setMouseTracking(True)
        self.calcSecondButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.calcSecondButton.setAutoFillBackground(False)
        self.calcSecondButton.setStyleSheet("background:  rgb(77, 69, 23);color: #fff; border-radius: 5px; font-weight: 600")
        self.calcSecondButton.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.calcSecondButton.setAutoDefault(True)
        self.calcSecondButton.setFlat(True)
        self.calcSecondButton.setText("Calculate")
        self.calcSecondButton.setObjectName("calcSecondButton")
        self.calcSecondButton.clicked.connect(self.secondGrouping)
        self.poolSizeEdit.returnPressed.connect(self.calcSecondButton.click) 
        self.secondInputTitle = QtWidgets.QLabel(self.secondRound)
        self.secondInputTitle.setGeometry(QtCore.QRect(60, 10, 101, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.secondInputTitle.setFont(font)
        self.secondInputTitle.setMouseTracking(True)
        self.secondInputTitle.setAutoFillBackground(False)
        self.secondInputTitle.setStyleSheet("border: none;color: rgb(77, 69, 23);")
        self.secondInputTitle.setText("Second round")
        self.secondInputTitle.setObjectName("secondInputTitle")
        self.line_2 = QtWidgets.QFrame(self.secondRound)
        self.line_2.setGeometry(QtCore.QRect(0, 40, 231, 16))
        self.line_2.setStyleSheet("border-bottom: 0;border-radius: 0;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.error_2 = QtWidgets.QLabel(self.secondRound)
        self.error_2.setGeometry(QtCore.QRect(10, 124, 211, 15))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.error_2.setFont(font)
        self.error_2.setStyleSheet("border: none;color:rgb(255, 0, 4);font: 10pt DejaVu Sans Mono;")
        self.error_2.setText("")
        self.error_2.setObjectName("error_2")
        self.resetButton_3 = QtWidgets.QPushButton(self.secondRound)
        self.resetButton_3.setGeometry(QtCore.QRect(40, 100, 61, 25))
        self.resetButton_3.setMouseTracking(True)
        self.resetButton_3.setFocusPolicy(QtCore.Qt.TabFocus)
        self.resetButton_3.setAutoFillBackground(False)
        self.resetButton_3.setStyleSheet("background: rgb(156, 3, 3);border-radius: 5px; color: #fff;font-weight: 600;")
        self.resetButton_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.resetButton_3.setAutoDefault(True)
        self.resetButton_3.setFlat(True)
        self.resetButton_3.setText("Reset")
        self.resetButton_3.setObjectName("resetButton_3")
        self.resetButton_3.clicked.connect(self.resetSecondRound)
        self.poolSizeEdit.raise_()
        self.inPoolSize.raise_()
        self.calcSecondButton.raise_()
        self.secondInputTitle.raise_()
        self.line_2.raise_()
        self.resInput.raise_()
        self.firstRound = QtWidgets.QWidget(self.input)
        self.firstRound.setGeometry(QtCore.QRect(10, 49, 231, 181))
        self.firstRound.setAutoFillBackground(False)
        self.firstRound.setStyleSheet("border: 1px solid rgb(2, 83, 121);background: #fff;border-radius: 0;")
        self.firstRound.setObjectName("firstRound")
        self.samplesEdit = QtWidgets.QLineEdit(self.firstRound)
        self.samplesEdit.setGeometry(QtCore.QRect(120, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.samplesEdit.setValidator(QtGui.QIntValidator())
        self.samplesEdit.setMaxLength(6)
        self.samplesEdit.setAlignment(QtCore.Qt.AlignRight)
        self.samplesEdit.setFont(font)
        self.samplesEdit.setStyleSheet("border: 1px solid rgb(72, 72, 72);border-radius: 0;text-align: right;")
        self.samplesEdit.setObjectName("samplesEdit")
        self.samplesEdit.setStatusTip('Enter the number of samples')
        self.samples = QtWidgets.QLabel(self.firstRound)
        self.samples.setGeometry(QtCore.QRect(20, 60, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.samples.setFont(font)
        self.samples.setMouseTracking(True)
        self.samples.setAutoFillBackground(False)
        self.samples.setStyleSheet("border: none;")
        self.samples.setText("Samples:")
        self.samples.setObjectName("samples")
        self.prevalence = QtWidgets.QLabel(self.firstRound)
        self.prevalence.setGeometry(QtCore.QRect(20, 100, 91, 19))
        self.prevalence.setText("Prevalence:")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prevalence.setFont(font)
        self.prevalence.setMouseTracking(True)
        self.prevalence.setAutoFillBackground(False)
        self.prevalence.setStyleSheet("border: none;")
        self.prevalence.setObjectName("prevalence")
        self.prevalenceEdit = QtWidgets.QLineEdit(self.firstRound)
        self.prevalenceEdit.setGeometry(QtCore.QRect(120, 100, 91, 21))
        self.prevalenceEdit.setStatusTip('Enter the value of the prevalence as a rational number and press enter or calculate')
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prevalenceEdit.setFont(font)
        self.prevalenceEdit.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.prevalenceEdit.setStyleSheet("border: 1px solid rgb(72, 72, 72);border-radius: 0;")
        self.prevalenceEdit.setValidator(QtGui.QDoubleValidator(0.0009,0.9000,5))
        self.prevalenceEdit.setMaxLength(7)
        self.prevalenceEdit.setAlignment(QtCore.Qt.AlignRight)
        self.prevalenceEdit.setObjectName("prevalenceEdit")
        self.calcFirstButton = QtWidgets.QPushButton(self.firstRound)
        self.calcFirstButton.setGeometry(QtCore.QRect(120, 140, 71, 25))
        self.calcFirstButton.setMouseTracking(True)
        self.calcFirstButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.calcFirstButton.setAutoFillBackground(False)
        self.calcFirstButton.setStyleSheet("background: #02655e;color: #fff; border-radius: 5px; font-weight: 600")
        self.calcFirstButton.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.calcFirstButton.setAutoDefault(True)
        self.calcFirstButton.setFlat(True)
        self.calcFirstButton.setText("Calculate")
        self.calcFirstButton.setObjectName("calcFirstButton")
        self.calcFirstButton.clicked.connect(self.grouping)
        self.prevalenceEdit.returnPressed.connect(self.calcFirstButton.click)
        self.firstInputTitle = QtWidgets.QLabel(self.firstRound)
        self.firstInputTitle.setGeometry(QtCore.QRect(70, 10, 81, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.firstInputTitle.setFont(font)
        self.firstInputTitle.setMouseTracking(True)
        self.firstInputTitle.setAutoFillBackground(False)
        self.firstInputTitle.setStyleSheet("border: none;color: #02655e;")
        self.firstInputTitle.setText("First round")
        self.firstInputTitle.setObjectName("firstInputTitle")
        self.line = QtWidgets.QFrame(self.firstRound)
        self.line.setGeometry(QtCore.QRect(0, 40, 231, 16))
        self.line.setStyleSheet("border-bottom: 0;border-radius: 0;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.error_1 = QtWidgets.QLabel(self.firstRound)
        self.error_1.setGeometry(QtCore.QRect(10, 164, 211, 15))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.error_1.setFont(font)
        self.error_1.setStyleSheet("border: none;color:rgb(255, 0, 4);font: 10pt DejaVu Sans Mono")
        self.error_1.setObjectName("error_1")
        self.error_1.setText("")
        self.resetButton_2 = QtWidgets.QPushButton(self.firstRound)
        self.resetButton_2.setGeometry(QtCore.QRect(40, 140, 61, 25))
        self.resetButton_2.setMouseTracking(True)
        self.resetButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.resetButton_2.setAutoFillBackground(False)
        self.resetButton_2.setStyleSheet("background: rgb(156, 3, 3);border-radius: 5px; color: #fff;font-weight: 600;")
        self.resetButton_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.resetButton_2.setAutoDefault(True)
        self.resetButton_2.setFlat(True)
        self.resetButton_2.setText("Reset")
        self.resetButton_2.setObjectName("resetButton_2")
        self.resetButton_2.clicked.connect(self.resetFirstRound)
        self.inputTitle = QtWidgets.QLabel(self.input)
        self.inputTitle.setGeometry(QtCore.QRect(90, 8, 81, 31))
        self.inputTitle.setStyleSheet("border: none;color: rgb(4, 62, 20);font-size: 20pt;font-weight: 700;")
        self.inputTitle.setText("Input")
        self.inputTitle.setObjectName("inputTitle")
        self.output = QtWidgets.QWidget(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(266, 10, 837, 582))
        self.output.setAutoFillBackground(False)
        self.output.setStyleSheet("border-radius: 5px;border: 1px solid rgb(2, 83, 121);background: rgb(255, 241, 238);")
        self.output.setObjectName("output")
        self.prevalence_5 = QtWidgets.QLabel(self.output)
        self.prevalence_5.setGeometry(QtCore.QRect(20, 100, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prevalence_5.setFont(font)
        self.prevalence_5.setMouseTracking(True)
        self.prevalence_5.setAutoFillBackground(False)
        self.prevalence_5.setStyleSheet("border: none;")
        self.prevalence_5.setText("")
        self.prevalence_5.setObjectName("prevalence_5")
        self.outputTitle = QtWidgets.QLabel(self.output)
        self.outputTitle.setGeometry(QtCore.QRect(347, 8, 111, 31))
        self.outputTitle.setStyleSheet("border: none;color: #800000;font-size: 20pt;font-weight: 700;")
        self.outputTitle.setText("Output")
        self.outputTitle.setObjectName("outputTitle")
        self.output.raise_()
        self.input.raise_()
        self.testSetup.raise_()
        self.resOutput.raise_()
        self.error_1.raise_()
        PoolTestingCalculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PoolTestingCalculator)
        self.statusbar.setObjectName("statusbar")
        PoolTestingCalculator.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(PoolTestingCalculator)
        self.action.setObjectName("action")
        self.comboBox = QtWidgets.QComboBox(self.testSetup)
        self.comboBox.setGeometry(QtCore.QRect(714, 152, 100, 27))
        self.comboBox.addItems(["Yellow", "Red", "Green"])
        self.comboBox.activated.connect(self.onActivated)
        self.comboBox.setStyleSheet("font-size: 14pt; color:rgb(77, 69, 23)")
        self.comboBox.setObjectName("comboBox")
        self.sliceShow = QtWidgets.QLabel(self.testSetup)
        self.sliceShow.setGeometry(QtCore.QRect(18,215, 780,105))
        self.sliceShow.setWordWrap(True)
        self.sliceShow.setAlignment(QtCore.Qt.AlignCenter)
        self.sliceShow.setStyleSheet("text-align: justify; border: none; font-size: 14pt; font-weight: 600; color:rgb(77, 69, 23)")
        self.sliceShow.setObjectName("sliceShow")
        self.sliceId = QtWidgets.QLabel(self.dimensionTabs)
        self.sliceId.setGeometry(QtCore.QRect(10, 34, 400, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sliceId.setFont(font)
        self.sliceId.setMouseTracking(True)
        self.sliceId.setAutoFillBackground(False)
        self.sliceId.setStyleSheet("border: none")
        self.sliceId.setObjectName("sliceId") 
        self.sliceId.raise_()
        self.sliceTitle = QtWidgets.QLabel(self.secondRound)
        self.sliceTitle.setGeometry(QtCore.QRect(20, 70, 41, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sliceSelect = QtWidgets.QComboBox(self.secondRound)
        self.sliceSelect.setGeometry(QtCore.QRect(90, 70, 121, 27))
        self.sliceSelect.setObjectName("sliceSelect")
        self.sliceSelect.setHidden(True)
        self.sliceSelect.setStyleSheet("font-size: 14pt; color:rgb(77, 69, 23)")
        self.sliceSelect.activated.connect(self.currentSlice)
        self.sliceTitle.setFont(font)
        self.sliceTitle.setMouseTracking(True)
        self.sliceTitle.setAutoFillBackground(True)
        self.sliceTitle.setStyleSheet("border: none;")
        self.sliceTitle.setObjectName("sliceTitle")
        self.sliceTitle.setText("Slice:")
        self.sliceTitle.setHidden(True)
        self.resetSubTest = QtWidgets.QPushButton(self.secondRound)
        self.resetSubTest.setGeometry(QtCore.QRect(90, 110, 61, 25))
        self.resetSubTest.setMouseTracking(True)
        self.resetSubTest.setFocusPolicy(QtCore.Qt.TabFocus)
        self.resetSubTest.setAutoFillBackground(False)
        self.resetSubTest.setStyleSheet("background: rgb(156, 3, 3); border-radius: 5px; color: #fff;font-weight: 600")
        self.resetSubTest.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.resetSubTest.setAutoDefault(True)
        self.resetSubTest.setFlat(True)
        self.resetSubTest.setObjectName("resetSubTest")
        self.resetSubTest.setText("Reset")
        self.resetSubTest.clicked.connect(self.resetSubTests)
        self.resetSubTest.setHidden(True)
        self.menubar = QtWidgets.QMenuBar(PoolTestingCalculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PoolTestingCalculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PoolTestingCalculator)
        self.statusbar.setObjectName("statusbar")
        PoolTestingCalculator.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(PoolTestingCalculator)      
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setText("Open")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setStatusTip('Open File')
        self.actionOpen.triggered.connect(self.fileOpen)             
        
        self.actionSave = QtWidgets.QAction(PoolTestingCalculator)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setText("Save")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip('Save File')
        self.actionSave.triggered.connect(self.fileSave) 
        
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.setTitle("File")
       
        self.positiveSamplesList = []
        self.tabContent = []
        self.positiveSlicesList = []
        self.positiveSets = []
        self.results = {}
        self.round = 1
        self.subtested = 0

        
    def fileOpen(self):
        root = tk.Tk()
        root.withdraw()
        try:
            name = filedialog.askopenfilename(title = "Select file",filetypes = (("Hypercube Files","*.hcb"),))
            f = open(name, 'r')
            with f: 
               try: 
                   text = f.read()
                   readDict = dill.loads(text)
               except: 
                   print("Failed to read file \n'%s'"%name)
                   return
            dim = readDict['dimension']
            prev = readDict['prevalence']
            samp = readDict['samples']
            slic = readDict['secondRound']
            posl = readDict['positiveList']
            self.myDict = readDict['subTest']
            self.prevalenceEdit.setText(str(prev))
            self.samplesEdit.setText(str(samp)) 
            self.positiveSlicesList = []     
            self.grouping(samples = samp, prevalence = prev)
            self.secondGrouping(dimension = dim, fixedSlices = slic)
            self.addSlice(positiveList = posl, indic = 0)
            self.subClicked = 0
        except:
            pass
            
    def fileSave(self):
        root = tk.Tk()
        root.withdraw()
        try:
            f=filedialog.asksaveasfile(mode='w',defaultextension=".hcb") 
            dill.dump(self.text, f)
            f.close() 
        except:
            pass
        
    def labelledCube(self, dim=None, sample=None):
        """ If a group tests positive, this function creates a label for samples in the group"""
        if dim is None:
            dim = self.D
        if sample is None:
            sample = range(1, int(self.poolSize)+1)
            
        all_labels = list(it.product(*(range(self.slices),) * dim))
        self.sample_labels = set(random.sample(all_labels, k= len(sample)))
        labelled_sample = {label : sample for label, sample in zip(self.sample_labels, sample)}
        self.text["labelledSamples"] = labelled_sample
        return labelled_sample

    def create_slices(self, dim=None, sample=None):
        
        """ Here different slices are created using the labels for further testing"""
        
        if dim is None:
            dim = self.D
        if sample is None:
            sample = range(1, int(self.poolSize)+1)
        labelsCube = self.labelledCube(dim, sample)
        init = [range(3)] * (dim-1)
        slice_colors = ['yellow', 'red', 'green']
        initialize = defaultdict(lambda: defaultdict(lambda:'Error'))
        for d in range(dim):
            for l in range(self.slices):
                copy = list(init)
                copy.insert(d, (l,))
                slices = set(it.product(*copy))
                slices_sample_label = self.sample_labels.intersection(slices)
                if len(slices_sample_label)>0:
                    elts = itemgetter(*slices_sample_label)(labelsCube)
                else:
                    elts=""
                if type(elts)==int:
                    initialize['D'+str(d+1)][slice_colors[l]] = set([elts])
                else:
                    initialize['D'+str(d+1)][slice_colors[l]] = set([ i for i in elts])
        self.text["slices"] = str(initialize)
        return initialize                 

    def createTabs(self, dimension, labelledCube):
        self.resetTabs()
        for i in range(dimension):
            self.setNames.append("D" + str(i+1))
            self.tabNames["D"+str(i+1)] = "tab_" + str(i+1)
        
        for name in self.setNames:   
            self.name = QtWidgets.QWidget()
            self.tabContent = labelledCube
            self.name.setObjectName(name)
            self.dimensionTabs.addTab(self.name, "D"+name[-1])
        self.dimSelect.addItems(self.setNames)
   
    def onTabChange(self,i):
        currentTabText = self.dimensionTabs.tabText(i)
        if self.dimensionTabs.count() == 0:
            dispText = ""
        else:
            dispText  = ', '.join(str(s) for s in self.tabContent[currentTabText]["yellow"] if s <= self.editablePoolSize)
        self.comboBox.setCurrentIndex(0)
        self.sliceShow.setText(dispText)
        self.sliceLength = len(dispText.split(", "))
        self.sliceId.setText("Direction "+ str(i+1) +", "+"Yellow slice with "+str(self.sliceLength)+" Samples.")

    def onActivated(self, i):
        index = self.dimensionTabs.currentIndex();
        currentTabText = self.dimensionTabs.tabText(index)
        currentComboText = ["yellow", "red", "green"][i]
        if self.tabContent == []:
            pass
        else:
            dispText  = ', '.join(str(s) for s in self.tabContent[currentTabText][currentComboText] if s <= self.editablePoolSize)
            self.sliceShow.setText(dispText)
            self.sliceLength = len(dispText.split(", "))
            self.sliceId.setText("Direction "+ str(index+1) +", "+currentComboText+" Slice with "+str(self.sliceLength)+" Samples.")

    def grouping(self, samples = None, prevalence = None):
        if samples is None or prevalence is None:
            if self.samplesEdit.text() == "" or self.prevalenceEdit.text() == "":
                self.error_1.setText("Enter both values")
            elif float(self.samplesEdit.text())<=0:
                self.error_1.setText("Enter a valid number")
            elif float(self.prevalenceEdit.text())>0.35:
                self.error_1.setText("Enter a valid prevalence")
            else:
                self.error_1.setText("")
                self.prevalence = float(self.prevalenceEdit.text())
                self.samples = float(self.samplesEdit.text())
        else:
            self.prevalence = prevalence
            self.samples = samples      
        self.poolSize = int(round(self.constant / self.prevalence))
        self.numberOfPools = float(self.samples / self.poolSize)      
        self.sizeNumber.setText( str(self.poolSize))
        self.valueNumberOfPools.setText( str(int(np.ceil(self.numberOfPools))))
        self.poolSizeEdit.setText(str(self.poolSize))
        self.editablePoolSize = self.poolSize
        self.text["prevalence"] = float(self.prevalenceEdit.text())
        self.text["samples"] = float(self.samplesEdit.text())
        
    def secondGrouping(self, dimension = None, fixedSlices = None):
        self.dimensionTabs.setCurrentIndex(0)
        self.setNames = []
        self.tabNames = {}
        self.positiveSlicesList = []
        self.positiveSets = []
        self.resetTabs()
        if dimension is None or fixedSlices is None:
            if self.poolSizeEdit.text() == "":
                self.error_2.setText("Enter a number")
            elif int(self.poolSizeEdit.text())<=3:
                self.error_2.setText("Enter a valid number")
            else:
                self.error_2.setText("")
                self.editablePoolSize = int(self.poolSizeEdit.text())
                self.D = int(np.ceil(np.log(self.editablePoolSize) / np.log(self.slices)))
                self.slicedCube = self.create_slices(dim = self.D)
        else:
            self.D = dimension
            self.slicedCube = fixedSlices
        self.text["dimension"] = self.D
        self.valueDimension.setText( str(self.D))
        self.valueSlices.setText(str(self.D*3))
        self.numMaxSlice.setText(str(3**(self.D-1)))
        self.createTabs(self.D, self.slicedCube)
        self.initText = ', '.join(str(s) for s in self.tabContent["D1"]["yellow"] if s <= self.editablePoolSize)
        self.sliceLength = len(self.tabContent["D1"]["yellow"])
        self.sliceId.setText("Direction "+"1, "+"Yellow Slice with "+str(self.sliceLength)+" Samples.")
        self.sliceShow.setText(self.initText)
        self.text["secondRound"] = self.slicedCube
        
    def subTest(self, comboText = None, inDict = None):
        if self.round == 2 or self.round == 1 :
            self.myDict = defaultdict(lambda: defaultdict(lambda:'Error'))
            sub_dim = self.D - 1
            for i in list(self.results.keys()):
                for j in self.results[i]:
                    slices = self.SLICES[i][j]
                    self.myDict[i][j] = self.create_slices(dim = sub_dim, sample = slices)
                    self.round = 3
        elif inDict is not None:
            self.myDict = inDict
        else:
            pass
        self.secondInputTitle.setText("Subtests")
        self.resetButton_3.setHidden(True)
        self.calcSecondButton.setHidden(True)
        self.poolSizeEdit.setHidden(True)
        self.inPoolSize.setHidden(True)
        self.sliceSelect.setHidden(False)
        self.sliceTitle.setHidden(False)
        self.resetSubTest.setHidden(False)
        self.addSubSliceTitle.setHidden(False)
        self.addSliceTitle.setHidden(True)
        self.resutlTitle.setHidden(True)
        self.subResutlTitle.setHidden(False)
        
        self.sliceSelect.addItems(self.res)
        self.setNames = []
        self.tabNames = {}
        self.positiveSlicesList = []
        self.positiveSets = []
        self.resetTabs()
        if comboText == None:
            x, z, y = list(self.res)[0].partition('-')
        else:
            x, z, y = list(comboText.partition('-'))
        self.partRes = self.myDict[x][y]
        self.numTabs = len(self.partRes.keys())
        self.partRes = self.myDict[x][y]
        self.createTabs(self.numTabs, self.partRes)
        self.positiveSlicesList = []
        self.subtested = 1
    
    def addSlice(self, positiveList = None, indic = 1 ):
        self.color = self.colorSelect.currentIndex()
        self.colorName = ["yellow", "red", "green"][self.color]
        self.dim = str(self.dimensionTabs.tabText(self.dimSelect.currentIndex()))
        if indic == 1:
            self.positiveSlicesList.append( self.dim +"-"+self.colorName)
        else: 
            if positiveList == "":  
                self.positiveSlicesList = []
            else:
                self.positiveSlicesList = positiveList
        if self.tabContent == []:
            pass
        else:
            self.positiveSets.append(self.tabContent[self.dim][self.colorName])
            if self.subtested == 0:
                self.res = set(self.positiveSlicesList)
                self.text["positiveList"] = self.positiveSlicesList
                dispText  = '; '.join(str(s) for s in self.res)
            else:
                self.res2 = set(self.positiveSlicesList)
                self.text["positiveList2"] = self.positiveSlicesList
                dispText  = '; '.join(str(s) for s in self.res2)
            self.positiveSlices.setText(dispText)
            self.positiveSamplesList = set.intersection(*self.positiveSets)
        try:
            self.results[self.dim].append(self.colorName)
        except KeyError:
            self.results[self.dim] = [self.colorName]
                  
    def resetPositiveSlices(self):
        self.results = {}
        self.positiveSlicesList = []
        self.positiveSets = []
        dispText  = ""
        self.positiveSlices.setText(dispText)
        self.positiveSamples.setText("")
        self.round = 1

    def resetSubTests(self):
        self.resetPositiveSlices()
        self.secondInputTitle.setText("Second round")
        self.resetButton_3.setHidden(False)
        self.calcSecondButton.setHidden(False)
        self.poolSizeEdit.setHidden(False)
        self.inPoolSize.setHidden(False)
        self.sliceSelect.setHidden(True)
        self.sliceTitle.setHidden(True)
        self.resetSubTest.setHidden(True)
        self.addSubSliceTitle.setHidden(True)
        self.addSliceTitle.setHidden(False)
        self.resutlTitle.setHidden(False)
        self.subResutlTitle.setHidden(True)
        self.dimensionTabs.setCurrentIndex(0)
        self.setNames = []
        self.tabNames = {}
        self.positiveSlicesList = []
        self.positiveSets = []
        self.resetTabs()
        self.createTabs(self.D, self.slicedCube)
        self.initText = ', '.join(str(s) for s in self.tabContent["D1"]["yellow"] if s <= self.editablePoolSize)
        self.sliceLength = len(self.tabContent["D1"]["yellow"])
        self.sliceId.setText("Direction "+"1, "+"Yellow Slice with "+str(self.sliceLength)+" Samples.")
        self.sliceShow.setText(self.initText)
        self.text["secondRound"] = self.slicedCube
        self.subtested = 0

    def resetTabs(self):
        self.dimSelect.clear()
        self.dimensionTabs.clear()
        self.sliceId.setText("")
        self.round = 1

    def resetFirstRound(self):
        self.samplesEdit.setText("")
        self.prevalenceEdit.setText("")
        self.sizeNumber.setText("0")
        self.valueNumberOfPools.setText("0")
        self.resetSecondRound()
	
    def resetSecondRound(self):
        self.poolSizeEdit.setText("")
        self.valueDimension.setText("0")
        self.valueSlices.setText("0")
        self.numMaxSlice.setText("0")
        self.resetTabs()
        self.resetPositiveSlices()
        self.round = 1

    def find_positive(self):
        """ This function finds the positive samples from the STAGE TWO testing
        
        input: dictionary containing the result of the STAGE TWO test. keys of the dictionary are the dimension 
        while values of each key is a list of slice colours that have tested positive
        Output: Positive samples"""
        if self.round == 2:
            pass
            
        elif self.subtested == 1:
            try:
                dim = self.D-1
                sample = range(1, int(self.poolSize)+1)
                self.SLICES = self.partRes
                dim_positive_slices = itemgetter(*self.results.keys())(self.results)
                dim_positive_slices_count = list(map(len,dim_positive_slices))
                one_pos_slice_count = dim_positive_slices_count.count(1)
                two_pos_slice_count = dim_positive_slices_count.count(2)
                three_pos_slice_count = dim_positive_slices_count.count(3)
                if one_pos_slice_count == dim:
                    positive_slice_samples = [self.SLICES[keys][value] for keys in self.results.keys() for value in self.results[keys]]
                    self.positiveSamples.setText('; '.join(str(s) for s in set.intersection(*positive_slice_samples)))
                    return set.intersection(*positive_slice_samples)
                    
                elif (one_pos_slice_count == dim-1) and (two_pos_slice_count == 1 or three_pos_slice_count ==1):
                    positive_slice_samples = [itemgetter(*self.results[key])(self.SLICES[key]) 
                                            if len(self.results[key])==1 else set.union(*itemgetter(*self.results[key])(self.SLICES[key])) 
                                            for key in self.results.keys()]
                    self.positiveSamples.setText('; '.join(str(s) for s in set.intersection(*positive_slice_samples)))

                else:
                    self.positiveSamples.setText('Indeterministic')
            except:
                pass
        else:
            try:
                dim = self.D
                sample = range(1, int(self.poolSize)+1)
                self.SLICES = self.slicedCube
                dim_positive_slices = itemgetter(*self.results.keys())(self.results)
                dim_positive_slices_count = list(map(len,dim_positive_slices))
                one_pos_slice_count = dim_positive_slices_count.count(1)
                two_pos_slice_count = dim_positive_slices_count.count(2)
                three_pos_slice_count = dim_positive_slices_count.count(3)
                if one_pos_slice_count == dim:
                    positive_slice_samples = [self.SLICES[keys][value] for keys in self.results.keys() for value in self.results[keys]]
                    self.positiveSamples.setText('; '.join(str(s) for s in set.intersection(*positive_slice_samples)))
                    return set.intersection(*positive_slice_samples)
                    
                elif (one_pos_slice_count == dim-1) and (two_pos_slice_count == 1 or three_pos_slice_count ==1):
                    positive_slice_samples = [itemgetter(*self.results[key])(self.SLICES[key]) 
                                            if len(self.results[key])==1 else set.union(*itemgetter(*self.results[key])(self.SLICES[key])) 
                                            for key in self.results.keys()]
                    self.positiveSamples.setText('; '.join(str(s) for s in set.intersection(*positive_slice_samples)))

                else:
                    self.positiveSamples.setText('Indeterministic: \n Proceed to sub- \n directional testing')
                    self.labelsCube = self.labelledCube()
                    self.subTest()
                    self.sliceSelect.clear()
                    self.sliceSelect.addItems(self.res)
                    if self.round == 1:
                        self.round = 2
                    else:
                        self.round = 3
            except:
                pass

    def currentSlice(self, i):
        currentComboText = list(self.res)[i]
        self.secondInputTitle.setText("Subtests")
        self.resetButton_3.setHidden(True)
        self.calcSecondButton.setHidden(True)
        self.poolSizeEdit.setHidden(True)
        self.inPoolSize.setHidden(True)
        self.sliceSelect.setHidden(False)
        self.sliceTitle.setHidden(False)
        self.resetSubTest.setHidden(False)
        self.setNames = []
        self.tabNames = {}
        self.positiveSlicesList = []
        self.positiveSets = []
        self.resetTabs()
        self.text["subTest"] = self.myDict
        if currentComboText == []:
            x, z, y = list(self.res)[0].partition('-')
        else:
            x, z, y = list(currentComboText.partition('-'))
        self.partRes = self.myDict[x][y]
        self.numTabs = len(self.partRes.keys())
        self.partRes = self.myDict[x][y]
        self.createTabs(self.numTabs, self.partRes)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PoolTestingCalculator = QtWidgets.QMainWindow()
    ui = Ui_PoolTestingCalculator()
    ui.setupUi(PoolTestingCalculator)
    PoolTestingCalculator.show()
    sys.exit(app.exec_())
