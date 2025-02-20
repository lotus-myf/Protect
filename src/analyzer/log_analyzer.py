# src/analyzer/log_analyzer.py

class LogAnalyzer:
    def __init__(self):
        """
        初始化日志分析器。
        """
        pass

    def analyze(self, log_file):
        """
        分析给定的日志文件，查找所有包含 'ERROR' 的行。

        :param log_file: 日志文件的路径
        :return: 含有 'ERROR' 的日志行列表
        """
        error_lines = []

        try:
            with open(log_file, 'r') as file:
                lines = file.readlines()

                # 查找日志文件中包含 'ERROR' 的行
                for line in lines:
                    if 'ERROR' in line:
                        error_lines.append(line)

            if not error_lines:
                print("No errors found in the log file.")
            return error_lines

        except FileNotFoundError:
            print(f"Error: The file {log_file} was not found.")
            return []

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

