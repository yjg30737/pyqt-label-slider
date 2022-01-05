from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt


class LabelSlider(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__slider_value = 50

        self.__slider = QSlider()
        self.__slider.setOrientation(Qt.Horizontal)
        self.__slider.setRange(10, 100) # default range
        self.__slider.setValue(self.__slider_value)
        self.__slider.valueChanged.connect(self.__valueChanged)
        self.__slider.setTickInterval(10)
        self.__slider.setSingleStep(10)

        self.__zoomLabel = QLabel()
        self.__zoomLabel.setText(str(self.__slider_value))
        self.__zoomLabel.setFixedWidth(self.__zoomLabel.fontMetrics().boundingRect(
                                         self.__zoomLabel.text()).width()+5)

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        lay.addWidget(self.__zoomLabel)
        lay.addWidget(self.__slider)

        self.setLayout(lay)

    def __valueChanged(self, v):
        v = v - v % 10
        self.__zoomLabel.setText(str(v))
        self.__zoomLabel.setFixedWidth(self.__zoomLabel.fontMetrics().boundingRect(
                                         self.__zoomLabel.text()).width()+5)

    def getLabel(self):
        return self.__zoomLabel

    def getSlider(self):
        return self.__slider
