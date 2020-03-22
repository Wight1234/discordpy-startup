#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 

pytoken = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 653100735281758208 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    await client.wait_until_ready()
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('3月23日(月)\n本日クラン活動はありません。')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(pytoken)
