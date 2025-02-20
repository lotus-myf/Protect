from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from src.scanner.nmap_scanner import NmapScanner  # 引入 NmapScanner

class ScannerModule(QWidget):
    back_to_main_signal = pyqtSignal()  # 定义信号，返回主界面

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.scanner = NmapScanner()  # 初始化扫描器

    def init_ui(self):
        layout = QVBoxLayout()

        # 输入框：目标 IP 地址
        self.scan_input = QLineEdit(self)
        self.scan_input.setPlaceholderText("Enter target IP address or range (e.g., 192.168.1.0/24)")
        layout.addWidget(self.scan_input)

        # 执行扫描按钮
        self.scan_button_execute = QPushButton('Run Vulnerability Scan', self)
        self.scan_button_execute.clicked.connect(self.run_scan)  # 点击时运行扫描
        layout.addWidget(self.scan_button_execute)

        # 输出框：显示扫描结果
        self.scan_output = QTextEdit(self)
        self.scan_output.setReadOnly(True)
        layout.addWidget(self.scan_output)

        # 返回主界面的按钮
        self.back_button = QPushButton('Back to Main Menu', self)
        self.back_button.clicked.connect(self.go_back_to_main)  # 点击时发送返回信号
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def run_scan(self):
        """执行漏洞扫描"""
        target_ip = self.scan_input.text()
        if target_ip:  # 如果有输入 IP 地址
            result = self.scanner.run_scan(target_ip)  # 执行扫描
            self.scan_output.setText(result)  # 显示扫描结果
        else:
            self.scan_output.setText("Please enter a valid IP address or range.")

    def go_back_to_main(self):
        """发出返回主菜单的信号"""
        self.back_to_main_signal.emit()  # 发送信号


