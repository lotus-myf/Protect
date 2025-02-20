# src/scanner/nmap_scanner.py
import subprocess

class NmapScanner:
    def __init__(self):
        self.scan_result = None

    def run_scan(self, target_ip):
        """
        使用 Nmap 执行漏洞扫描。
        :param target_ip: 目标 IP 地址或子网范围
        :return: 扫描结果
        """
        try:
            # 使用 Nmap 执行扫描，-sV 表示服务版本检测
            print(f"Running Nmap scan on {target_ip}...")
            result = subprocess.run(
                ['nmap', '-sV', target_ip],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                self.scan_result = result.stdout
            else:
                self.scan_result = f"Scan failed: {result.stderr}"

            return self.scan_result
        except Exception as e:
            return f"An error occurred: {str(e)}"

# 示例使用
if __name__ == "__main__":
    scanner = NmapScanner()
    target = "172.17.170.69"  # 示例目标 IP 地址
    result = scanner.run_scan(target)
    print(result)
