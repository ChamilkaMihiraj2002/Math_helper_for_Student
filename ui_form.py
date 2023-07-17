# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)
import random

class Ui_Widget(object):
    operator = '' 
    answer,num1,num2 = 0,0,0
    def addition(self,data):
        if(data == True):
            self.operator = '+'
        return 0
    
    def subtraction(self,data):
        if(data == True):
            self.operator = '-'
        return 0
    
    def divide(self,data):
        if(data == True):
            self.operator = '/'
        return 0
    
    def multiplication(self,data):
        if(data == True):
            self.operator = 'X'
        return 0
    
    def power(self,data):
        if(data == True):
            self.operator = '^'
        return 0
    
    def check_answer(self):
        if(self.answer == float(self.lineEdit.text())):
            self.label_3.setText("Correct Answer")
        else:
            self.label_3.setText("Wrong Answer")
            
    def Try_Again(self):
        if (self.operator == '^'):
            self.label_3.setText("{A} {B} {C} = ".format(A=self.num1//10,B=self.operator,C=self.num2//10))
        else:
            self.label_3.setText("{A} {B} {C} = ".format(A=self.num1,B=self.operator,C=self.num2))
    
    def show_correct_answer(self):
        if (self.operator == '^'):
            self.label_3.setText("{A} {B} {C} = {D}".format(A=self.num1//10,B=self.operator,C=self.num2//10,D=self.answer))
        else:
            self.label_3.setText("{A} {B} {C} = {D}".format(A=self.num1,B=self.operator,C=self.num2,D=self.answer))  
              
    def set_answer(self,num1,num2,operator):
       
        if(operator == '+'):
            answer = num1 + num2
        elif(operator == '-'):
            answer = num1 - num2
        elif(operator == 'X'):
            answer = num1 * num2
        elif(operator == '/'):
            answer = num1 / num2
            answer = float("{:.2f}".format(answer))
        elif(operator == '^'):
            answer = (num1//10) ** (num2//10)
        else:
            answer = "Error"
            
        return answer
        
    def display(self,num1,num2,operator):
        if (operator == '^'):
            self.label_3.setText("{A} {B} {C} = ".format(A=num1//10,B=operator,C=num2//10))
        else:
            self.label_3.setText("{A} {B} {C} = ".format(A=num1,B=operator,C=num2))
        
    def system_start(self):
        self.num1 = random.randint(1,100)
        self.num2 = random.randint(1,100)
        self.display(self.num1,self.num2,self.operator)
        self.answer = self.set_answer(self.num1,self.num2,self.operator)
    
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(622, 421)
        self.label_01 = QLabel(Widget)
        self.label_01.setObjectName(u"label_01")
        self.label_01.setGeometry(QRect(10, 10, 621, 61))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        
        self.label_01.setFont(font)
        self.label_01.setAlignment(Qt.AlignCenter)
        self.label_02 = QLabel(Widget)
        self.label_02.setObjectName(u"label_02")
        self.label_02.setGeometry(QRect(10, 200, 81, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_02.setFont(font1)
        
        self.add_button = QRadioButton(Widget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(30, 230, 112, 26))
        self.add_button.setCheckable(True)
        self.add_button.clicked.connect(self.addition)
        
    
        self.Sub_button = QRadioButton(Widget)
        self.Sub_button.setObjectName(u"Sub_button")
        self.Sub_button.setGeometry(QRect(30, 260, 112, 26))
        self.Sub_button.setCheckable(True)
        self.Sub_button.clicked.connect(self.subtraction)
        
        
        self.div_button = QRadioButton(Widget)
        self.div_button.setObjectName(u"div_button")
        self.div_button.setGeometry(QRect(30, 290, 112, 26))
        self.div_button.setCheckable(True)
        self.div_button.clicked.connect(self.divide)
        
        
        self.mul_button = QRadioButton(Widget)
        self.mul_button.setObjectName(u"mul_button")
        self.mul_button.setGeometry(QRect(30, 320, 112, 26))
        self.mul_button.setCheckable(True)
        self.mul_button.clicked.connect(self.multiplication)
        
        
        self.pow_button = QRadioButton(Widget)
        self.pow_button.setObjectName(u"pow_button")
        self.pow_button.setGeometry(QRect(30, 350, 112, 26))
        self.pow_button.setCheckable(True)
        self.pow_button.clicked.connect(self.power)
        
        
        self.Start_button = QPushButton(Widget)
        self.Start_button.setObjectName(u"Start_button")
        self.Start_button.setGeometry(QRect(10, 380, 111, 29))
        self.Start_button.clicked.connect(self.system_start)
        
        
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 180, 401, 21))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        
        self.show_correct_answer_button = QPushButton(Widget)
        self.show_correct_answer_button.setObjectName(u"show_correct_answer_button")
        self.show_correct_answer_button.setGeometry(QRect(450, 300, 161, 29))
        self.show_correct_answer_button.clicked.connect(self.show_correct_answer)
        
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 230, 341, 51))
        font2 = QFont()
        font2.setPointSize(20)
        self.lineEdit.setFont(font2)
        
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 200, 63, 20))
        self.label_2.setFont(font1)
        
        self.Enter_Button = QPushButton(Widget)
        self.Enter_Button.setObjectName(u"Enter_Button")
        self.Enter_Button.setGeometry(QRect(270, 300, 83, 29))
        self.Enter_Button.clicked.connect(self.check_answer)
        
        self.Tryagain_Button = QPushButton(Widget)
        self.Tryagain_Button.setObjectName(u"Tryagain_Button")
        self.Tryagain_Button.setGeometry(QRect(360, 300, 83, 29))
        self.Tryagain_Button.clicked.connect(self.Try_Again)
        
        
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 601, 101))
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(False)
        self.label_3.setFont(font3)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShape(QFrame.WinPanel)
        self.label_3.setFrameShadow(QFrame.Raised)
        self.label_3.setLineWidth(0)
        self.label_3.setMidLineWidth(0)
        
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 360, 41, 21))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 370, 171, 21))
        
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 390, 321, 20))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_01.setText(QCoreApplication.translate("Widget", u"Math helper for students", None))
        self.label_02.setText(QCoreApplication.translate("Widget", u"Operator", None))
        self.add_button.setText(QCoreApplication.translate("Widget", u"Addition", None))
        self.Sub_button.setText(QCoreApplication.translate("Widget", u"Subtraction", None))
        self.div_button.setText(QCoreApplication.translate("Widget", u"Divide", None))
        self.mul_button.setText(QCoreApplication.translate("Widget", u"Multiplication", None))
        self.pow_button.setText(QCoreApplication.translate("Widget", u"Power", None))
        self.Start_button.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Select the Mathematical Operator and press the start button.", None))
        self.show_correct_answer_button.setText(QCoreApplication.translate("Widget", u"Show Correct Answer", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Answer", None))
        self.Enter_Button.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.Tryagain_Button.setText(QCoreApplication.translate("Widget", u"Try Again", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"Hint :", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Use denominators with ", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"only two decimal places to answer the division.", None))
    # retranslateUi

