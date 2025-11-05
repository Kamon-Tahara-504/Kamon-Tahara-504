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

### 3. Personal Access Token (PAT) の作成と設定

GitHub Actionsのコミットを草（contribution graph）に反映させるために、Personal Access Tokenが必要です。

#### 3-1. PATの作成

1. GitHubにログインして、右上のプロフィールアイコンをクリック
2. **Settings** をクリック
3. 左サイドバーの一番下にある **Developer settings** をクリック
4. **Personal access tokens** → **Tokens (classic)** をクリック
5. **Generate new token** → **Generate new token (classic)** をクリック
6. 以下の設定を行います：
   - **Note**: `Profile Auto Update` など、わかりやすい名前を入力
   - **Expiration**: 有効期限を設定（推奨: 90日または1年）
   - **Select scopes**: `repo` にチェックを入れる
     - これにより、リポジトリへの読み書き権限が付与されます
7. **Generate token** をクリック
8. **重要**: 表示されたトークンをコピーしてください（再表示できません）

#### 3-2. PATをリポジトリのSecretsに保存

1. プロフィールリポジトリのページに戻る
2. **Settings** → **Secrets and variables** → **Actions** に移動
3. **New repository secret** をクリック
4. 以下を入力：
   - **Name**: `PAT`
   - **Secret**: 先ほどコピーしたPATを貼り付け
5. **Add secret** をクリック

#### 3-3. GitHub Actions の権限設定

1. **Settings** → **Actions** → **General** に移動
2. **Workflow permissions** セクションで以下を選択：
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
3. **Save** をクリック

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
3. PATが正しく設定されているか確認
   - Settings → Secrets and variables → Actions で `PAT` が存在するか確認
   - PATの有効期限が切れていないか確認

### 草（contribution graph）に反映されない
1. PATが正しく設定されているか確認（`GITHUB_TOKEN`ではなく`PAT`を使用しているか）
2. ワークフローファイルでコミット作成者が正しく設定されているか確認
   - ユーザー名: `Kamon-Tahara-504`
   - メールアドレス: `Kamon-Tahara-504@users.noreply.github.com`
3. コミットが実際に作成されているか確認（Actionsタブでログを確認）

## 📝 注意事項

- GitHub Actions の無料枠: Public リポジトリは無制限
- 最初の実行には数分かかる場合があります
- PATを使用することで、コミットがあなたのアカウントとして記録され、GitHubの草（contribution graph）に反映されます
- PATは機密情報です。絶対に公開しないでください
- PATの有効期限が切れた場合は、新しいPATを作成してSecretsを更新してください
- PATには最小限の権限（`repo`スコープ）のみを付与してください

## 🎉 完了！

これで、毎日自動的にREADME.mdが更新されるようになりました！


