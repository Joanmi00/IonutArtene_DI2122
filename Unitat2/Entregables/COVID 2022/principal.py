import os

from pathlib import Path
from PySide6.QtWidgets import (
    QMainWindow, QGraphicsDropShadowEffect, QSizePolicy)
from PySide6.QtGui import QPainter, QColor, QIcon, QPixmap, QBrush
from PySide6.QtCharts import QChart, QLineSeries, QChartView
from PySide6.QtCore import (
    QSize, QEasingCurve, QPropertyAnimation)
from PySide6.QtUiTools import QUiLoader

import login
import urllib.request
import json as j

shadow_elements = {
    "left_menu_widget",
    "widget_4", "label_3",
    "label_4", "but_menu",
    "label_6"
}


class mainw(QMainWindow):
    def __init__(self, parent=None):
        super(mainw, self).__init__()
        url = "https://dadesobertes.gva.es/va/api/3/action/datastore_search?" + \
            "resource_id=7968883a-2329-4c26-8304-83f19ec54ab1&limit=500"
        self.carga()
        self.cargar_datos(url)
        self.window = self.load_ui()
        self.setMinimumSize(850, 600)

        imagen_covid = QPixmap(os.path.join(os.path.dirname(
            __file__), "iconos covid/coronavirus_covid_corona_virus_" +
            "bacterium_covid_icon_149135.svg"))
        self.window.but_menu.setIcon(QIcon(os.path.join(os.path.dirname(
            __file__), "iconos covid/left-arrow.png")))

        self.window.label.setPixmap(imagen_covid)
       
        # Acciones a ejectuar cuando se presione un boton
        self.window.but_menu.clicked.connect(lambda: self.slideLeftMenu())
        self.window.but_datos.clicked.connect(
            lambda: self.window.ventanas.setCurrentWidget
            (self.window.page_datos))
        self.window.but_graficos.clicked.connect(
            lambda: self.window.ventanas.setCurrentWidget
            (self.window.page_graficos))
        self.window.but_sesion.clicked.connect(lambda: self.login())
        self.window.but_salir.clicked.connect(lambda: self.close())
        self.window.castellon.clicked.connect(self.introducir_mun)
        self.window.valencia.clicked.connect(self.introducir_mun)
        self.window.alicante.clicked.connect(self.introducir_mun)
        self.window.combo_municipios.activated.connect(self.info)

        # Cargamos grafica de la COVID
        self.create_line_chart()

        # Aqui aplicamos la sombra a los widget seleccionados
        for widget in shadow_elements:

            effect = QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(128, 128, 128))
            getattr(self.window, widget).setGraphicsEffect(effect)

    # Cargamos el fichero que contiene lo que hemos preparado en QT Designer

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "c.ui")
        return loader.load(path, self)

    def create_line_chart(self):
        """
        Esta funciona se encarga de leer el csv con los datos y  cargarlos en
        un Line Chart para ver la estadistica
        """
        datos_acc = []
        acc_cases = 0
        month = ""
        row_count = 0
        with open(os.path.join(os.path.dirname(
                __file__), 'csv/covid.csv')) as csvfile:
            for line in csvfile.readlines():
                grup, sexe, percentage, casos, percentage_m, defuncions, date = line.split(
                    ';')
                if row_count > 0:
                    if(row_count == 20):
                        acc_cases += int(casos)
                        datos_acc.append(
                            acc_cases)
                        row_count = 0
                        acc_cases = 0
                    month = date
                    acc_cases += int(casos)

                else:
                    if date == month:
                        acc_cases += int(casos)
                row_count += 1

        casos_covid = QLineSeries()
        for valor in datos_acc[::-1]:

            casos_covid.append(
                datos_acc[::-1].index(valor), valor)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(casos_covid)
        chart.createDefaultAxes()
        chart.setTitle("Tendencia de la COVID desde 31-01-2020 C.V.")
        chart.setAnimationOptions(QChart.AllAnimations)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.chart().setTheme(QChart.ChartThemeQt)
        chartView.setBackgroundBrush(QBrush(QColor("transparent")))

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            chartView.sizePolicy().hasHeightForWidth())
        chartView.setSizePolicy(sizePolicy)
        chartView.setMinimumSize(QSize(0, 300))
        self.window.line_chart.addWidget(chartView)

    def slideLeftMenu(self):
        """_summary_
        Funcion que se encarga del movimiento del menu lateral
                y de cambiar la imagen en funcion del estado del menu
        """
        width = self.window.widget_3.width()

        if width == 0:
            newWidth = 200
            self.window.but_menu.setIcon(QIcon(os.path.join(os.path.dirname(
                __file__), "iconos covid/left-arrow.png")))
        else:
            newWidth = 0
            self.window.but_menu.setIcon(QIcon(
                os.path.join(os.path.dirname(
                    __file__), "iconos covid/Menu_icon_icon-" +
                    "icons.com_71858.svg")))

        self.animation = QPropertyAnimation(
            self.window.left_menu_widget, b"maximumWidth")
        self.animation.setDuration(1000)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()

    def login(self):
        """
        Función que se encarga  de cargar el login y de ocultar
         la ventana principal
        """
        w = login.Login()
        w.show()
        if(w.isVisible()):
            self.window.hide()

    def introducir_mun(self):
        """Funcion que se encarga de cargar los distintos 
                municipios segun su provincia 
        """ 
        self.window.combo_municipios.clear()
        prov = self.sender().text()
        if(prov == "Castellon"):
            self.window.combo_municipios.addItems(self.carga_castellon)
        elif(prov == "Valencia"):
            self.window.combo_municipios.addItems(self.carga_valencia)
        elif(prov == "Alicante"):
            self.window.combo_municipios.addItems(self.carga_alicante)

    def info(self):
        """Funcion que es llamada cuando cambiamos el  municipio y que se encarga 
        de llamar a su vez a cargar_datos con la nueva url creada 
        apartir del municipio seleccionado"""
        municipio = self.window.combo_municipios.currentText().replace(
            "à", "%C3%A0").replace("ú", "%C3%BA").replace(
                "ó", "%C3%B3").replace("á", "%C3%A1").replace(
                    "ñ", "%C3%B1").replace("í", "%C3%AD")
        part_principal = "https://dadesobertes.gva.es/va/api/3/action" + \
            "/datastore_search?"
        muni = "q={"+"\""+"Municipi"+"\""+":" + \
            "\""+"{}".format(municipio).replace(" ",
                                                "%20")+"\""+"}"
        part_final = "&resource_id=7968883a-2329-4c26-8304-83f19ec54ab1"

        url = part_principal + muni + part_final
        self.cargar_datos(url)
        for dictionary in self.datos_python:
            try:
                for key in dictionary.keys():
                    if(key == "Incidència acumulada PCR+14"):
                        self.window.label_pcr.setText(str(dictionary[key]))
                    if(key == "Casos PCR+ 14 dies"):
                        self.window.label_casos.setText(str(dictionary[key]))
                    if(key == "Defuncions"):
                        self.window.label_muertes.setText(str(dictionary[key]))

            except KeyError:
                pass

    def carga(self):
        self.carga_castellon = []
        self.carga_valencia = []
        self.carga_alicante = []

    def cargar_datos(self, url):
        """Funcion que se encarga de conectarse al api ,leer los datos y si la 
        variable que contiene los municipios esta vacia se encarga de cargar los
        municipios segun su CodMunicpio desde la api

        Args:
            url (Str): La url es la que le dice donde conectarse para recoger 
            la informacion necesaria 
        """

        with urllib.request.urlopen(url) as response:
            datos = response.read()
            datos_json = j.loads(datos)
            self.datos_python = datos_json['result']['records']
            if(len(self.carga_castellon) == 0):
                for dictionary in self.datos_python:
                    try:
                        if(str(dictionary["CodMunicipio"]).startswith("12")):
                            self.carga_castellon.append(
                                dictionary["Municipi"])
                        elif(str(dictionary["CodMunicipio"]).startswith("46")):
                            self.carga_valencia.append(
                                dictionary["Municipi"])
                        elif(str(dictionary["CodMunicipio"]).startswith("3")):
                            self.carga_alicante.append(
                                dictionary["Municipi"])
                    except KeyError:
                        pass
