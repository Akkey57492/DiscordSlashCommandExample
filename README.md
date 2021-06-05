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
from discord_slash import SlashCommand, SlashContext

# コマンド登録
slash = SlashCommand(bot, sync_commands=True)
