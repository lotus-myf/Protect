# src/main.py
from src.scanner.nmap_scanner import NmapScanner
from src.analyzer.log_analyzer import LogAnalyzer
import os
from src.detector.intrusion_detector import IntrusionDetector

def run_vulnerability_scan():
    """
    执行漏洞扫描功能
    """
    target_ip = input("Enter target IP address or subnet (e.g., 192.168.47.0/24): ")
    scanner = NmapScanner()
    print(f"Running Nmap scan on {target_ip}...")
    scan_result = scanner.run_scan(target_ip)
    print("\nScan Results:")
    print(scan_result)

def analyze_logs():
    """
    执行日志分析功能
    """
    log_file = input("Enter the path to the log file to analyze: ")

    # 检查文件路径是否存在
    if not os.path.exists(log_file):
        print(f"Error: The file {log_file} does not exist.")
        return

    # 创建 LogAnalyzer 实例
    analyzer = LogAnalyzer()

    # 执行日志分析
    print(f"Analyzing logs from {log_file}...")
    log_result = analyzer.analyze(log_file)

    # 输出结果
    if log_result:
        print("\nLog Analysis Results:")
        for error in log_result:
            print(error)  # 输出每条包含 'ERROR' 的日志行
    else:
        print("No errors found in the log file.")

def detect_intrusion():
    """
    执行入侵检测功能
    """
    pcap_file = input("Enter the path to the network traffic pcap file for intrusion detection: ")

    # 创建 IntrusionDetector 实例
    detector = IntrusionDetector()

    # 执行入侵检测
    print(f"Detecting intrusion from {pcap_file}...")
    intrusion_result = detector.detect(pcap_file)

    # 输出检测结果
    print("\nIntrusion Detection Results:")
    print(intrusion_result)

def main():
    """
    主程序入口，提供菜单选择不同模块功能
    """
    while True:
        print("\nNetwork Security Toolbox")
        print("1. Run Vulnerability Scan")
        print("2. Analyze Logs")
        print("3. Detect Intrusion")
        print("4. Exit")

        choice = input("\nSelect an option (1/2/3/4): ")

        if choice == '1':
            run_vulnerability_scan()
        elif choice == '2':
            analyze_logs()
        elif choice == '3':
            detect_intrusion()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
