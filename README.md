# 説明

## エンコード
連番画像から動画をエンコードするシステム

動画のエンコードにはffmpeg(ローカル環境)を用いる

## コーデック
動画のエンコードにおけるコーデックは以下のようである
```python
{'vcodec':'libx264', 'pix_fmt': 'yuv420p'}
```

nvencを使ったハードウェアエンコーディングを使用する場合は以下のように変更する
```python
{'vcodec':'h264_nvenc', 'pix_fmt': 'yuv420p'}
```



## 監視
動画のエンコードが終わったら指定したアドレスにメールを飛ばす

# envファイル

>FRAMES = エンコードする動画の連番画像のフォルダのパス
>
>OUTPUT  = エンコードした動画の保存先パス

**#process name**

>PROCESSNAME = 監視するプロセス名

**#email settings**

>FROM_ADDR = 送信元アドレス
>
>TO_ADDR = 送信先アドレス
>
>SMTP_SERVER = smtpサーバー
>
>SMTP_PORT = SMTPポートナンバー
>
>GOOGLE_APP_PASS = Googleのアプリパスワード





# バージョン

