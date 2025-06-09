import os
import datetime
from git import Repo

def write_log(summary, output_dir="logs"):
    os.makedirs(output_dir, exist_ok=True)
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(output_dir, f"analysis_log_{now}.md")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"# Analysis Log {now}\n\n")
        f.write(summary)
    return log_path

def commit_and_push(repo_dir, message="Update analysis logs"):
    repo = Repo(repo_dir)
    repo.git.add(A=True)
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == "__main__":
    repo_path = r"C:\Users\user\Desktop\ruin\Z2interpreter"  # 環境に合わせて変更してね

    # ログ内容サンプル（後で編集可）
    log_summary = """
## 使用モデル
- Open Interpreter vX.X
- Codex GPT-4o

## 実行概要
簡易ログの自動作成テストです。
"""

    log_file = write_log(log_summary)
    print(f"ログを書き出しました: {log_file}")

    commit_and_push(repo_path, "自動ログ更新テスト")
    print("GitHubへコミット＆プッシュしました")
