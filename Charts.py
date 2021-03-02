from PyQt5.QtWidgets import QApplication, QMainWindow
import sys,random,decimal
from PyQt5.QtChart import QChart, QChartView, QSplineSeries, QPolarChart,QBarSet, QLineSeries, QBarSeries,QBarCategoryAxis, QBarCategoryAxis,QValueAxis
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
 
#Para usar o grafico:
    #from Charts import LineChart, BarChart
    #self.linechart = LineChart()
    #self.chartlayout = QtWidgets.QHBoxLayout(self.linechart_container)
    #self.chartlayout.setContentsMargins(0, 0, 0, 0)
    #self.chartlayout.addWidget(self.linechart.chartview)
    #self.barchart = BarChart()
    #self.barchartlayout = QtWidgets.QHBoxLayout(self.barchart_container)
    #self.barchartlayout.setContentsMargins(0, 0, 0, 0)
    #self.barchartlayout.addWidget(self.barchart.chartview)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.LineChart = PolarChart()
        self.setCentralWidget(self.LineChart.chartview)
 
class LineChart(QChart):
    def __init__(self):
        super().__init__()
 
        

        self.create_linechart()

    def create_linechart(self):
        
        self.chartview = QChartView(self)
        self.chartview.setRenderHint(QPainter.Antialiasing)
 
        series = QSplineSeries()
        series.setName("Produtividade")
        self.addSeries(series)
        
        series2 = QSplineSeries()
        series2.setName("Yield")
        self.addSeries(series2)
        
        axisY = QValueAxis()
        axisY.setRange(50, 100)
        axisX = QValueAxis()
        axisX.setRange(0, 9)
        axisX.setTickCount(9)
        axisY.setTickCount(5)
        axisX.setLabelFormat("WK%.0f")
        axisY.setLabelFormat("%.1f%")
        
        self.setAxisY(axisY,series2)
        self.setAxisX(axisX,series2)
        self.setAxisY(axisY,series)
        self.setAxisX(axisX,series)

        for i in range(10):
            series.append(i,random.randrange(80,90))
            series2.append(i,random.randrange(90,99))

        self.setAnimationOptions(QChart.SeriesAnimations)
        self.setTitle("Performance Historica")
 
        self.legend().setVisible(True)
        self.legend().setAlignment(Qt.AlignBottom)


class PolarChart(QPolarChart):
    def __init__(self):
        super().__init__()
        self.create_polarchart()
    
    def create_polarchart(self):
        
        axis = QValueAxis()
        axis.setLabelFormat("%.1f")
        axis.setShadesVisible(True)
        
        for i in range(10):
            axis.append(i,random.randrange(80,90))
        
        
        
        
class BarChart(QChart):
    def __init__(self):
        super().__init__()
 
        

        self.create_linechart()

    def create_linechart(self):
 
        flex = QBarSet('FLEX')
        pth = QBarSet('PTH')
        smt = QBarSet('SMT')
        box = QBarSet('BOX')
        cus = QBarSet('CUS')
        sie = QBarSet('SIE')
        
        flex.append(random.randrange(80,90))
        pth.append(random.randrange(80,90))
        smt.append(random.randrange(80,90))
        box.append(random.randrange(80,90))
        cus.append(random.randrange(80,90))
        sie.append(random.randrange(80,90))


        


        series = QBarSeries()
        series.append(flex)
        series.append(smt)
        series.append(pth)
        series.append(box)
        series.append(cus)
        series.append(sie)


        
        self.addSeries(series)
        self.setTitle('Produtividade por Área')
        self.setAnimationOptions(QChart.SeriesAnimations)

        

        axisY = QValueAxis()
        axisY.setRange(0, 100)
        axisY.setLabelFormat("%.1f%")

        
        self.setAxisY(axisY,series)
        
        
        self.legend().setVisible(True)
        self.legend().setAlignment(Qt.AlignBottom)

        
 
 
        self.chartview = QChartView(self)
        self.chartview.setRenderHint(QPainter.Antialiasing)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
 
