# GitHub プロフィール自動更新のセットアップ方法

このリポジトリには、毎日自動的にREADME.mdを更新する機能が含まれています。

## 📋 必要な設定

### 1. リポジトリの作成
GitHubでプロフィール用のリポジトリを作成してください：
- リポジトリ名: あなたのGitHubユーザー名と同じ名前
- 例: ユーザー名が `Kamon-Tahara-504` の場合、リポジトリ名も `Kamon-Tahara-504`
- 公開設定: Public

### 2. リポジトリにコードをプッシュ

```bash
cd /Users/kt/Desktop/Profile
git init
git add .
git commit -m "Initial commit with auto-update feature"
git branch -M main
git remote add origin https://github.com/あなたのユーザー名/あなたのユーザー名.git
git push -u origin main
```

### 3. GitHub Actions の権限設定

1. GitHubのリポジトリページにアクセス
2. **Settings** → **Actions** → **General** に移動
3. **Workflow permissions** セクションで以下を選択：
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
4. **Save** をクリック

### 4. 動作確認

#### 手動でワークフローを実行
1. リポジトリの **Actions** タブに移動
2. 左サイドバーから **Update README** を選択
3. **Run workflow** ボタンをクリック
4. **Run workflow** を再度クリックして実行

#### 自動実行の確認
- 毎日UTC 0:00（日本時間 9:00）に自動実行されます
- README.mdの「Last Updated」セクションが更新されます

## 📁 ファイル構成

```
Profile/
├── README.md                          # プロフィールページ
├── .github/
│   └── workflows/
│       └── update-readme.yml         # GitHub Actions ワークフロー
├── scripts/
│   └── update_readme.py              # 更新スクリプト
└── SETUP.md                          # このファイル
```

## 🛠️ カスタマイズ

### 実行時間の変更
`.github/workflows/update-readme.yml` の `cron` 設定を変更してください：

```yaml
schedule:
  # 例: 毎日午後6時（UTC 18:00 = 日本時間 午前3:00）
  - cron: '0 18 * * *'
```

### 更新内容の変更
`scripts/update_readme.py` を編集して、更新する内容をカスタマイズできます。

例：
- ランダムな名言を追加
- GitHubの統計情報を取得
- カウンターを追加
- その日の気分を追加

## 🔍 トラブルシューティング

### ワークフローが実行されない
1. リポジトリ名がユーザー名と一致しているか確認
2. GitHub Actions の権限設定を確認
3. `.github/workflows/update-readme.yml` の構文エラーを確認

### コミットが失敗する
1. GitHub Actions に書き込み権限があるか確認
2. リポジトリが Public になっているか確認

## 📝 注意事項

- GitHub Actions の無料枠: Public リポジトリは無制限
- 最初の実行には数分かかる場合があります
- コミット履歴にbot による更新履歴が残ります

## 🎉 完了！

これで、毎日自動的にREADME.mdが更新されるようになりました！


