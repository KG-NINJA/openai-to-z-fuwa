import subprocess
import sys
from datetime import datetime

def print_and_log(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] {msg}")

def run_command(command, desc=""):
    try:
        print_and_log(f"{desc} 実行: {command}")
        subprocess.run(command, check=True, shell=True)
        print_and_log(f"{desc} 完了")
    except subprocess.CalledProcessError:
        print_and_log(f"{desc} 失敗")
        sys.exit(1)

def main():
    # 1. 解析の実行
    run_command("python run_analysis.py", desc="解析")
    # 2. レポート生成
    run_command("python scripts/report_generator.py", desc="レポート生成")

if __name__ == "__main__":
    print_and_log("===== OpenAI to Z 自動パイプライン開始 =====")
    main()
    print_and_log("===== 完了 =====")
