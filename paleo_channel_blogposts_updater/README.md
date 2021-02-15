# Paleo Channel Blogposts Updater

Contents

- [概要](#概要)
- [更新時間](#更新時間)
- [実行環境](#実行環境)

## 概要

"パレオチャンネル過去記事アップデータ" は
[パレオチャンネル](https://ch.nicovideo.jp/paleo/blomaga)
に追従するように
[パレオチャンネルブロマガ過去記事全集 (2019年2月~)](https://typememo.jp/life/paleo-channel-blogposts/)
を自動更新するアプリケーションです．

## 更新時間

毎日 13:00 に自動更新するように `crontab` を設定しています．

```bash
# (minute) (hour) (day) (month) (weekday) command
00 13 * * * /Users/takeru/typememo/tau/paleo_channel_blogposts_updater/run.sh >
/tmp/crontab_paleo_channel_blogposts_updater.log
```

## 実行環境

実行環境

- MacOS 10.15.7
- zsh 5.8 (x86_64-apple-darwin19.3.0)
