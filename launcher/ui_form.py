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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainLauncher(object):
    def setupUi(self, MainLauncher):
        if not MainLauncher.objectName():
            MainLauncher.setObjectName(u"MainLauncher")
        MainLauncher.resize(750, 500)
        MainLauncher.setAutoFillBackground(False)
        MainLauncher.setStyleSheet(u"")
        self.centralwidget = QWidget(MainLauncher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"image: url(:/images/resources/750x500_bg.png);")
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(700, 0, 19, 19))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"background: transparent;\n"
"image: url(:/images/resources/buttons_Close_off.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background: transparent;\n"
"	image: url(:/images/resources/buttons_Close_over.png);\n"
"}\n"
"")
        self.minusButton = QPushButton(self.centralwidget)
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setGeometry(QRect(680, 0, 19, 19))
        self.minusButton.setMouseTracking(True)
        self.minusButton.setStyleSheet(u"QPushButton {\n"
"background: transparent;\n"
"image: url(:/images/resources/buttons_Minimize_off.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	\n"
"	image: url(:/images/resources/buttons_Minimize_over.png);\n"
"}\n"
"")
        self.minusButton.setCheckable(False)
        MainLauncher.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainLauncher)
        self.closeButton.clicked.connect(MainLauncher.close)
        self.minusButton.clicked.connect(MainLauncher.showMinimized)

        QMetaObject.connectSlotsByName(MainLauncher)
    # setupUi

    def retranslateUi(self, MainLauncher):
        MainLauncher.setWindowTitle(QCoreApplication.translate("MainLauncher", u"Launcher", None))
        self.closeButton.setText("")
        self.minusButton.setText("")
    # retranslateUi

