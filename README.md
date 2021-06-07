# DiscordSlashCommandExample
discord.pyのスラッシュコマンド作成の例です。(ライブラリ使用)

# 使い方
一部の構文をコピーして使用すればスラッシュコマンドを実装できます。

# ライブラリ
discord.py
discord-slash-command

# 保障動作Pythonバージョン
3.8.6

# import文
ライブラリを使っているのでまずはインポート文を追加する必要があります。
discord-slash-commandライブラリは公式ライブラリではありません。
```python
from discord_slash import SlashCommand, SlashContext
```
discord.pyとは別にインストールする必要があるのでご注意ください。
```python
pip install discord-slash-command
or
py -m pip install discord-slash-command
```

# コマンド登録
スラッシュコマンドを登録するための下準備として
```python
slash = SlashCommand(bot, sync_commands=True)
```
このコードが必要です。
```python
sync_commands=True
```
これをTrueにすることで自動的にグローバルコマンドを登録してくれます。

# コマンド追加
追加は
```python
@slash.slash(name="コマンド名")
async def _コマンド名(ctx, arg=None):
  if arg == None:
    return
  await ctx.send("test")
```
となります。
```python
await ctx.send("test", hidden=True)
```
メッセージの送信時に「hidden=True」を追加すれば個人あてにメッセージを送信できます。
