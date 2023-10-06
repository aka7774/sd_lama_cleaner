# sd_lama_cleaner

Lama Cleaner 1111 Extension

「LamaCreaner」タブが追加されます。

## 作者について

- 現在メインでWSL2を使っているため、Windows固有の問題には対応が鈍いです。
- ユーザーがどれだけいるのかチェックしてないので、需要があったら教えてください。

## Install

最初に使い始める前に、一回だけ実行してください。

- extensionを入れただけでは何もしません
- Installボタンを押す

### うまくいかないとき

コマンドラインから手動でInstallできます。

for Windows:
```bash
cd stable-diffusion-webui
venv/Scripts/pip install -U lama-cleaner
```

for Linux:
```bash
cd stable-diffusion-webui
venv/bin/pip install -U lama-cleaner
```

## Start

webuiが再起動するたびに、毎回実行してください。

- Startボタンを押す(窓が開く)
- Linuxで使う時は少し書き換えてください

for Windows:
```bash
start venv/Scripts/lama-cleaner --model=lama --device=cpu --port=7870
```

for Linux:
```bash
venv/bin/lama-cleaner --model=lama --device=cpu --port=7870
```

読み込み中の表示のままになった場合はブラウザをリロードすると直るかも。

## Enjoy

- Openを押す(画面が開く)
  - Openが不満なら「Open New Window」をお好みで押す

### Open New Window

for Windows:
```bash
start http://127.0.0.1:7870/
```

Linuxだと動かないかも？
