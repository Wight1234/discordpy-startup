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
        await channel.send('3月22日(日)\n本日21時よりクラン活動があります。')  

    if now == '03:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nFNCS 第一週\n30分前')  

    if now == '07:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nFNCS 第一週\n30分前')  

    if now == '08:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nアジア ハイプナイト\n30分前') 

    if now == '04:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動\n30分前') 

    if now == '05:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動') 

    if now == '06:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動\n終了') 

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(pytoken)
