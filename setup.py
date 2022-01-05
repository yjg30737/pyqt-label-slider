from setuptools import setup, find_packages

setup(
    name='pyqt-label-slider',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QSlider with QLabel(QLabel is on the left side, QSlider is on the right side, horizontal direction only) '
                'QLabel\'s value synchronizes with QSlider\'s value.',
    url='https://github.com/yjg30737/pyqt-label-slider.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)
