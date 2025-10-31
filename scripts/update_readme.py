#!/usr/bin/env python3
"""
README.mdの最終更新日時を自動更新するスクリプト
"""

import re
from datetime import datetime, timezone

def update_readme():
    """README.mdの日時を更新する"""
    
    # README.mdを読み込む
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 現在の日時を取得（UTC）
    now = datetime.now(timezone.utc)
    date_str = now.strftime('%Y-%m-%d %H:%M:%S UTC')
    
    # 日時を更新するパターン
    pattern = r'(<!-- AUTO_UPDATE_DATE -->)(.*?)(<!-- END_AUTO_UPDATE_DATE -->)'
    replacement = f'\\1\n**{date_str}**\n\\3'
    
    # 日時を更新
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # README.mdに書き込む
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f'README.md updated at {date_str}')

if __name__ == '__main__':
    update_readme()

