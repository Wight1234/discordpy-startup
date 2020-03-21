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
    if now == '14:56':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('問題')  

    if now == '14:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('明日は何の日でしょうか。')  

    if now == '14:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('正解は、')  

    if now == '14:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('やまとの誕生日です。')  

    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('3月22日(日)\n本日21時よりクラン活動があります。')  

    if now == '11:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動\n30分前') 

    if now == '12:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動') 

    if now == '13:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone\nクラン活動\n終了') 

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(pytoken)
