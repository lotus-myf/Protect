from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import pyqtSignal

class DetectionModule(QWidget):
    # 定义信号，用于返回主界面
    back_to_main_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Intrusion Detection Module')

        layout = QVBoxLayout()

        # 创建输入框
        self.pcap_input = QLineEdit(self)
        self.pcap_input.setPlaceholderText("Enter the path to the pcap file")
        layout.addWidget(self.pcap_input)

        # 创建执行按钮
        self.detect_button_execute = QPushButton('Detect Intrusion', self)
        self.detect_button_execute.clicked.connect(self.detect_intrusion)
        layout.addWidget(self.detect_button_execute)

        # 创建输出框
        self.detect_output = QTextEdit(self)
        self.detect_output.setReadOnly(True)
        layout.addWidget(self.detect_output)

        # 创建返回按钮
        self.back_button = QPushButton('Back to Main Menu', self)
        self.back_button.clicked.connect(self.go_back_to_main)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def detect_intrusion(self):
        """模拟入侵检测"""
        pcap_file = self.pcap_input.text()
        if pcap_file:
            self.detect_output.setText(f"Detecting intrusion from pcap file: {pcap_file}")
        else:
            self.detect_output.setText("Please provide a pcap file path.")

    def go_back_to_main(self):
        """返回主界面"""
        self.back_to_main_signal.emit()  # 发射信号
