# tests/test_scanner.py
import unittest
from src.scanner.nmap_scanner import NmapScanner

class TestNmapScanner(unittest.TestCase):
    def test_run_scan_valid_ip(self):
        """
        测试有效的 IP 地址，确保能返回扫描结果。
        """
        scanner = NmapScanner()
        target_ip = "172.17.170.69"  # 使用虚拟机的 IP 地址
        result = scanner.run_scan(target_ip)

        # 确保扫描结果不为空
        self.assertIsNotNone(result)
        self.assertIn("Nmap scan report for", result)  # 检查扫描结果是否包含“扫描报告”

    def test_run_scan_invalid_ip(self):
        """
        测试无效的 IP 地址，确保能正确处理错误。
        """
        scanner = NmapScanner()
        target_ip = "999.999.999.999"  # 无效的 IP 地址
        result = scanner.run_scan(target_ip)

        # 确保扫描结果不为空
        self.assertIsNotNone(result)
        self.assertIn("0 IP addresses", result)  # 检查结果中是否包含 "0 IP addresses"

if __name__ == "__main__":
    unittest.main()

