
import sys


from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtGui import QPainter
from PySide6.QtCharts import QChart, QLineSeries, QChartView

from interface_covid2 import *
from Custom_Widgets.Widgets import loadJsonStyle


shadow_elements = {
    "left_menu_widget",
    "widget_4", "label_3",
    "label_4", "but_menu",
    "label_6"
}


class mainw(QMainWindow):
    def __init__(self, parent=None):
        super(mainw, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.setMinimumSize(850, 600)
        loadJsonStyle(self, self.window)

        for widget in shadow_elements:

            effect = QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(128, 128, 128))
            getattr(self.window, widget).setGraphicsEffect(effect)
        

    def create_line_chart(self):
        monthList = []
        acc_cases = 0
        month = ""
        row_count = 0
        with open('csv/covid.csv') as csvfile:
            for line in csvfile.readlines():
                grup, sexe, percentage, casos, percentage_m, defuncions, date = line.split(
                    ';')
                if row_count > 0:
                    if(row_count == 20):
                        acc_cases += int(casos)
                        monthList.append(
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

        for valor in monthList:
            casos_covid.append(
                monthList.index(valor), valor)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(casos_covid)
        chart.createDefaultAxes()
        chart.setTitle("Casos acumulados cada mes desde 31-01-2020")
        chart.setAnimationOptions(QChart.AllAnimations)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.chart().setTheme(QChart.ChartThemeDark)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            chartView.sizePolicy().hasHeightForWidth())
        chartView.setSizePolicy(sizePolicy)
        chartView.setMinimumSize(QSize(0, 300))

        self.window.line_chart.addWidget(chartView)
        self.window.gridFrame.setStyleSheet(u"background-color: transparent")


if __name__ == "__main__":
    app = QApplication([])
    window = mainw()
    window.create_line_chart()
    window.show()
    sys.exit(app.exec_())
