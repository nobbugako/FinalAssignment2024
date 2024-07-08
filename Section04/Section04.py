import os
from datetime import datetime

# ログフォルダのパスを定義
log_dir = 'log'
log_file = os.path.join(log_dir, 'execution.log')

# フォルダが存在しない場合は作成
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# ログファイルに実行ログを追記
with open(log_file, 'a') as f:
    f.write(f'プログラムが実行されました: {datetime.now()}\n')

# .gitignoreファイルにログフォルダを追加（存在しない場合のみ）
gitignore_file = '.gitignore'
if not os.path.exists(gitignore_file):
    with open(gitignore_file, 'w') as f:
        f.write(f'{log_dir}/\n')
else:
    with open(gitignore_file, 'r') as f:
        lines = f.readlines()
    if f'{log_dir}/\n' not in lines:
        with open(gitignore_file, 'a') as f:
            f.write(f'{log_dir}/\n')
