import sys
import os.path
from PySide2 import QtWidgets, QtCore, QtUiTools


class MyCal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        script_path = os.path.realpath(__file__)
        ui_path = os.path.join(os.path.dirname(script_path), 'my_cal.ui')
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        self.ui.show()

        # 버튼 입력 코드 줄이기
        central_widget = self.ui.findChild(QtWidgets.QWidget, 'centralwidget')
        for child in central_widget.findChildren(QtWidgets.QPushButton):
            child.clicked.connect(self.apply_value)

    def apply_value(self):
        button = self.sender()
        if button.objectName().startswith(('button_')):
            self.number(button.accessibleName())

    # 연산자 또는 0이 처음에 입력 되지 않게 함
    def number(self, num):
        exist_text = self.ui.label.text()
        if num == "0" and exist_text == "0":
            return
        if num == "+" and exist_text == "":
            return
        if num == "-" and exist_text == "":
            return
        if num == "*" and exist_text == "":
            return
        if num == "/" and exist_text == "":
            return

        self.ui.label.setText(exist_text + num)

        self.ui.button_del.clicked.connect(self.btn_del)
        self.ui.button_AC.clicked.connect(self.btn_clear)
        self.ui.button_ent.clicked.connect(self.btn_result)

    def btn_del(self):
        exist_text = self.ui.label.text()
        self.ui.label.setText(exist_text[:-1])

    def btn_clear(self):
        self.ui.label.setText("")
        self.ui.lcdNumber.display("0")

    def btn_result(self):
        exist_text = self.ui.label.text()

        try:
            ans = eval(exist_text)
            self.ui.label.setText(str(ans))
            self.ui.lcdNumber.display(ans)

        except Exception as e:
            print(e)

    def float_filter(self, num):
        try:
            int(num)
            return int(num)
        except ValueError:
            return float(num)


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication()
    cal = MyCal()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
