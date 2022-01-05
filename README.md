# pyqt-label-slider
PyQt QSlider with QLabel(QLabel is on the left side, QSlider is on the right side, horizontal direction only) QLabel's value synchronizes with QSlider's value.

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-label-slider.git --upgrade```

## Usage
* ```getSlider()``` to get QSlider.
* ```getLabel()``` to get QLabel.

## Note
* Tick interval is set at 10.

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqt_label_slider.labelSlider import LabelSlider


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        widget = LabelSlider()
        slider = widget.getSlider()
        slider.setMaximumWidth(150)
        slider.setRange(10, 200)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/148164060-30f842f1-a64e-4553-abba-f37c7d0f8365.mp4


