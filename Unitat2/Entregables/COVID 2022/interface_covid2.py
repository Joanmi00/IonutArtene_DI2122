# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cjrksdZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Custom_Widgets.Widgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu_widget = QCustomSlideMenu(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.left_menu_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/iconos/iconos covid/coronavirus_covid_corona_virus_bacterium_covid_icon_149135.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.left_menu_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.but_datos = QPushButton(self.widget_4)
        self.but_datos.setObjectName(u"but_datos")

        self.verticalLayout_2.addWidget(self.but_datos)

        self.but_graficos = QPushButton(self.widget_4)
        self.but_graficos.setObjectName(u"but_graficos")

        self.verticalLayout_2.addWidget(self.but_graficos)

        self.but_sesion = QPushButton(self.widget_4)
        self.but_sesion.setObjectName(u"but_sesion")

        self.verticalLayout_2.addWidget(self.but_sesion)

        self.but_salir = QPushButton(self.widget_4)
        self.but_salir.setObjectName(u"but_salir")

        self.verticalLayout_2.addWidget(self.but_salir)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.left_menu_widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_6 = QWidget(self.frame_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.but_menu = QPushButton(self.widget_9)
        self.but_menu.setObjectName(u"but_menu")
        font1 = QFont()
        font1.setFamily(u"Syamala Ramana")
        self.but_menu.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/iconos/iconos covid/Menu_icon_icon-icons.com_71858.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/iconos/iconos covid/left-arrow.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/iconos/iconos covid/Menu_icon_icon-icons.com_71858.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.but_menu.setIcon(icon)
        self.but_menu.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.but_menu)

        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.widget_9)

        self.frame_10 = QFrame(self.widget_6)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ventanas = QStackedWidget(self.frame_7)
        self.ventanas.setObjectName(u"ventanas")
        sizePolicy1.setHeightForWidth(self.ventanas.sizePolicy().hasHeightForWidth())
        self.ventanas.setSizePolicy(sizePolicy1)
        self.page_datos = QWidget()
        self.page_datos.setObjectName(u"page_datos")
        self.verticalLayout_7 = QVBoxLayout(self.page_datos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.page_datos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.combo_municipios = QComboBox(self.frame)
        self.combo_municipios.setObjectName(u"combo_municipios")
        self.combo_municipios.setGeometry(QRect(240, 140, 171, 25))
        self.combo_municipios.setCurrentText(u"")
        self.valencia = QRadioButton(self.frame)
        self.valencia.setObjectName(u"valencia")
        self.valencia.setGeometry(QRect(240, 70, 112, 23))
        self.castellon = QRadioButton(self.frame)
        self.castellon.setObjectName(u"castellon")
        self.castellon.setGeometry(QRect(240, 40, 112, 23))
        self.alicante = QRadioButton(self.frame)
        self.alicante.setObjectName(u"alicante")
        self.alicante.setGeometry(QRect(240, 100, 112, 23))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 50, 67, 17))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(140, 150, 81, 17))
        self.label_8.setFont(font)

        self.verticalLayout_7.addWidget(self.frame)

        self.frame_3 = QFrame(self.page_datos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_3)

        self.ventanas.addWidget(self.page_datos)
        self.page_graficos = QWidget()
        self.page_graficos.setObjectName(u"page_graficos")
        self.verticalLayout_6 = QVBoxLayout(self.page_graficos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.page_graficos)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.gridFrame = QFrame(self.frame_4)
        self.gridFrame.setObjectName(u"gridFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy2)
        self.line_chart = QGridLayout(self.gridFrame)
        self.line_chart.setObjectName(u"line_chart")

        self.verticalLayout_9.addWidget(self.gridFrame)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.ventanas.addWidget(self.page_graficos)

        self.verticalLayout_8.addWidget(self.ventanas)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.ventanas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"COVID-19", None))
        self.but_datos.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.but_graficos.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficos", None))
        self.but_sesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesi\u00f3n", None))
        self.but_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ionut Artene", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IES El Just 2022", None))
        self.but_menu.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" MENU", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"COVID-19", None))
        self.combo_municipios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Elija un Municipio", None))
        self.valencia.setText(QCoreApplication.translate("MainWindow", u"Valencia", None))
        self.castellon.setText(QCoreApplication.translate("MainWindow", u"Castellon", None))
        self.alicante.setText(QCoreApplication.translate("MainWindow", u"Alicante", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Provincia", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Municipios", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Grafico COVID", None))
    # retranslateUi

