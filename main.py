import sys
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from ADC import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.graphWidget = pg.GraphicsLayoutWidget(show=True, parent=self.ui.graphWidget)
        self.ui.graphWidget.setGeometry(QtCore.QRect(0, 0, 460, 360))
        self.plt = self.ui.graphWidget.addPlot()
        self.x = []
        self.y = []
        self.curve = self.plt.plot(self.x, self.y)
        self.plt.axes['bottom']['item'].setLabel(text='номер такта')
        self.plt.axes['left']['item'].setLabel(text='U, В')
        self.curve.setPen((255, 0, 0))
        self.input_voltage_line = pg.InfiniteLine(movable=False,
                                                  angle=0,
                                                  pen=(255, 0, 255),
                                                  pos=0,
                                                  label="Uвх",
                                                  labelOpts={
                                                      'color': (255, 0, 255),
                                                      'fill': (255, 0, 255, 50),
                                                      'movable': True
                                                  }
                                                  )
        self.plt.addItem(self.input_voltage_line)
        self.connect_events()

    def connect_events(self):
        self.ui.pushButton.clicked.connect(self.calculating_output_code)

    def calculating_output_code(self):
        bit_amount = int(self.ui.bit_depth.value())  # Запись в переменную разрядность АЦП
        input_voltage = float(self.ui.line_input.text())  # Запись в переменную значения входного напряжения
        reference_voltage = float(self.ui.line_ref.text())  # Запись в переменную значения опорного напряжения

        code_output = []
        deviation_buffer = []
        deviation = 0
        self.input_voltage_line.setPos(input_voltage)

        if (reference_voltage == input_voltage):  # Проверка входных данных на совпадение напряжений
            self.ui.line_output.setText(self.ui.line_input.text())
            self.ui.line_code.setText(f"----")
            self.ui.line_error.setText("0")
        else:
            for i in range(bit_amount):  # Цикл от 0 до [разрядность АЦП]
                if (deviation < input_voltage):
                    deviation += reference_voltage / (2 ** (i + 1))
                    deviation_buffer.append(deviation)

                elif (deviation > input_voltage):
                    deviation -= reference_voltage / (2 ** (i + 1))
                    deviation_buffer.append(deviation)
            for i in range(len(deviation_buffer)):  # Цикл от 0 до [кол-во отклонений от входного напряжения]
                if (deviation_buffer[i] < input_voltage):
                    code_output.append('1')
                elif (deviation_buffer[i] > input_voltage):
                    code_output.append('0')
            self.ui.line_output.setText(str(round(deviation, 6)))  # Запись выходного напряжения в line_output
            self.ui.line_code.setText(''.join(code_output))  # Запись выходного кода в line_cod
            self.ui.line_error.setText(str(round(abs(input_voltage - deviation) / input_voltage * 100, 6)))  # Запись относительной погрешности в line_error
            self.x = [0] + sorted([i for i in range(1, bit_amount)] * 2) + [bit_amount]
            self.y = sum([[i, i] for i in deviation_buffer], [])
            # code_buffer = [f'{round((i / reference_voltage) * (2 ** bit_amount)):{bit_amount}b}'.replace(" ", "0") for i in deviation_buffer] # похуй
            self.curve.setData(self.x, self.y)
            self.x, self.y = [], []


if __name__ == "__main__":
    pg.setConfigOption('background', 'w')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

