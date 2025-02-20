from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from src.ui.scanner_module import ScannerModule
from src.ui.log_module import LogModule
from src.ui.detection_module import DetectionModule

class NetworkSecurityToolboxApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Network Security Toolbox')

        # 创建主布局
        layout = QVBoxLayout()

        # 创建堆叠窗口来显示不同模块的界面
        self.stacked_widget = QStackedWidget(self)

        # 创建并添加主界面到堆叠窗口
        self.main_menu = self.create_main_menu()
        self.stacked_widget.addWidget(self.main_menu)

        # 创建各个模块并添加到堆叠窗口
        self.scanner_module = ScannerModule()
        self.scanner_module.back_to_main_signal.connect(self.show_main_screen)
        self.stacked_widget.addWidget(self.scanner_module)

        self.log_module = LogModule()
        self.log_module.back_to_main_signal.connect(self.show_main_screen)
        self.stacked_widget.addWidget(self.log_module)

        self.detection_module = DetectionModule()
        self.detection_module.back_to_main_signal.connect(self.show_main_screen)
        self.stacked_widget.addWidget(self.detection_module)

        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def create_main_menu(self):
        """创建主菜单界面"""
        menu_widget = QWidget()
        menu_layout = QVBoxLayout()

        # 主菜单界面的三个按钮
        self.scan_button = QPushButton('Run Vulnerability Scan', self)
        self.scan_button.clicked.connect(self.show_scan_module)
        menu_layout.addWidget(self.scan_button)

        self.log_button = QPushButton('Analyze Logs', self)
        self.log_button.clicked.connect(self.show_log_module)
        menu_layout.addWidget(self.log_button)

        self.detect_button = QPushButton('Detect Intrusion', self)
        self.detect_button.clicked.connect(self.show_detection_module)
        menu_layout.addWidget(self.detect_button)

        menu_widget.setLayout(menu_layout)
        return menu_widget

    def show_scan_module(self):
        """显示漏洞扫描模块"""
        self.stacked_widget.setCurrentIndex(1)

    def show_log_module(self):
        """显示日志分析模块"""
        self.stacked_widget.setCurrentIndex(2)

    def show_detection_module(self):
        """显示入侵检测模块"""
        self.stacked_widget.setCurrentIndex(3)

    def show_main_screen(self):
        """返回主菜单"""
        self.stacked_widget.setCurrentIndex(0)

def main():
    app = QApplication([])  # 创建应用程序
    window = NetworkSecurityToolboxApp()  # 创建主窗口
    window.show()  # 显示窗口
    app.exec_()  # 进入应用程序的事件循环

if __name__ == "__main__":
    main()
