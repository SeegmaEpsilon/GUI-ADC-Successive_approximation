import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from ADC import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connectUi()

    def connectUi(self):
            self.ui.pushButton.clicked.connect(self.calculating_output_code)

    def calculating_output_code(self):
        bit_amount = int(self.ui.bit_depth.value())           # Запись в переменную разрядность АЦП
        input_voltage = float(self.ui.line_input.text())      # Запись в переменную значения входного напряжения
        reference_voltage = float(self.ui.line_ref.text())    # Запись в переменную значения опорного напряжения
        code_output = []
        deviation_buffer = []
        deviation = 0
        if (reference_voltage == input_voltage):              # Проверка входных данных на совпадение напряжений
            self.ui.line_output.setText(self.ui.line_input.text())
            self.ui.line_code.setText("----")
            self.ui.line_error.setText("0")

        else:
            for i in range(bit_amount):                       # Цикл от 0 до [разрядность АЦП]
                if (deviation < input_voltage):
                    deviation += reference_voltage / (2 ** (i+1))
                    deviation_buffer.append(deviation)

                elif (deviation > input_voltage):
                    deviation -= reference_voltage / (2 ** (i+1))
                    deviation_buffer.append(deviation)

            for i in range(len(deviation_buffer)):            # Цикл от 0 до [кол-во отклонений от входного напряжения]
                if   (deviation_buffer[i] < input_voltage):
                    code_output.append('1')
                elif (deviation_buffer[i] > input_voltage):
                    code_output.append('0')

            self.ui.line_output.setText(str(round(deviation, 6))) # Запись выходного напряжения в line_output
            self.ui.line_code.setText(''.join(code_output))       # Запись выходного кода в line_cod
            self.ui.line_error.setText(str(round(abs(input_voltage-deviation)/input_voltage*100, 6))) # Запись относительной погрешности в line_error

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())