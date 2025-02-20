# src/scanner.py
import subprocess

def run_vulnerability_scan(target_ip):
    """
    使用 Nmap 执行漏洞扫描。
    :param target_ip: 目标 IP 地址或子网范围
    :return: 扫描结果
    """
    try:
        # 调用 Nmap 命令，-sV 选项用于版本检测
        result = subprocess.run(['nmap', '-sV', target_ip], capture_output=True, text=True)
        
        if result.returncode == 0:
            return result.stdout  # 返回扫描的结果
        else:
            return f"Scan failed: {result.stderr}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
