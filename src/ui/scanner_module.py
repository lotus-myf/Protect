from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit

class ScannerModule(QWidget):
    back_to_main_signal = pyqtSignal()  # 定义信号，返回主界面

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 输入框、按钮等界面元素
        self.scan_input = QLineEdit(self)
        self.scan_input.setPlaceholderText("Enter target IP range (e.g., 192.168.1.0/24)")
        layout.addWidget(self.scan_input)

        self.scan_button_execute = QPushButton('Run Vulnerability Scan', self)
        layout.addWidget(self.scan_button_execute)

        self.scan_output = QTextEdit(self)
        self.scan_output.setReadOnly(True)
        layout.addWidget(self.scan_output)

        # 返回按钮，点击时发出信号
        self.back_button = QPushButton('Back to Main Menu', self)
        self.back_button.clicked.connect(self.go_back_to_main)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def go_back_to_main(self):
        """发出返回主菜单的信号"""
        self.back_to_main_signal.emit()  # 发送信号

