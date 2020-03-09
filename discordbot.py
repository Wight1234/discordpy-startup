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
        await channel.send('3月10日(火)\n本日はクラン活動があります。')  

    if now == '09:00':
        channel = client.get_channel(CHANNEL_ID)

    A_user = discord.utils.get(client.users,name="VE1L")

    reply = A_user.mention + "さん\n幸福はノスタルジーに眠る杯\n30分前"
    await channel.send(reply)

    if now == '11:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動\n30分前')  

    if now == '12:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動')  

    if now == '04:51':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動\n終了') 

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(pytoken)
