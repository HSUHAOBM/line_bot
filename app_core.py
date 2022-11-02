#軍

from __future__ import unicode_literals
import os
from flask import Flask, request, abort,render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, JoinEvent, LeaveEvent

import configparser

import urllib
import re
import random

from custom_models import BossData,CallBossData
import psycopg2


app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

@app.route("/")
def home():
    return render_template("home.html")

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def pixabay_isch(event):
    print(event)
    if event.source.group_id =="C43a948aa2bf6460a64e1ebf916a44612":
        print("群組編號，驗證成功")

        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
            BossName,DeadForTime,NextForTime,OtherText,ErrorText=BossData.BossTime_record(event.message.text)
            try:
                if OtherText=="指令":
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="清除:資料庫重建、\n出:時間BoSS顯示、\n名稱:現有代號、\n紀錄:時間+名稱 \n ex.0101 不死鳥 \n"))
                if OtherText=="清除":
                    print("初始化")

                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="初始化"))
                    CallBossData.DeleteAlldatabase()
                    CallBossData.Resetdatabase()            
                elif OtherText=="名稱": 
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=NAME))  
                elif OtherText=="出": 
                    outtext=CallBossData.updateDB()
                    listouttext=CallBossData.ShowBossTimeList()
                    # print("listouttext:",listouttext)
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=outtext+listouttext))
                elif BossName!=None and NextForTime != None:
                    NextForTime = NextForTime.strftime('%m/%d %H:%M:%S')
                    DeadForTime=DeadForTime.strftime('%m/%d %H:%M:%S')
                    if(ErrorText!=None):
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="BOSS："+ BossName +"\n"+"死亡時間："+ DeadForTime +"\n"+"重生時間："+NextForTime+"\n"+ErrorText))
                    else:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="BOSS："+ BossName +"\n"+"死亡時間："+ DeadForTime +"\n"+"重生時間："+NextForTime))

            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="無資料"))            
                #TextSendMessage(text=str(event.source.user_id)+"　　？？？　　"+(event.message.text))) 

@handler.add(JoinEvent)
def handle_join(event):
    # newcoming_text = "謝謝邀請我這個機器來至此群組！！我會盡力為大家服務的～"
    newcoming_text = "Hello 0.0"

    line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=newcoming_text)
        )
    print("JoinEvent =", JoinEvent)
    print("新群組的相關資訊", event.source)
    print("event:",event)

@handler.add(LeaveEvent)
def handle_leave(event):
    print("leave Event =", event)
    print("我被踢掉了QQ 相關資訊", event.source)


if __name__ == "__main__":
    app.run()

NAME="""
["17","奇岩","浮士德","クライン"]
["4","4c","4C","4色","四色","68","四賢者","カスパー","カスパーズ","四色法師"]
["左飛","52左","701","左","左ドレ","49左","52左龍"]
["右飛","52右","702","右","右ドレ","49右","52右龍"]
["小綠","綠","8","G","08","g"]
["小紅","紅","red","RED","R","09","赤"]
["蟻","螞蟻","ant","3","03","アリ","あり","ANT"]
["10","蜈蚣","包皮","海蟲","巨大蜈蚣","ワーム"]
["49","49龍","46","46ドレ","49飛龍"]
["51","51龍","48","48ドレ","51飛龍"]
["大黑","黑","703","大黑長者","黑老","BE","ハイエルダー","ハイエル","be"]
["卡王","卡","14","卡司特","ガースト","ca","CA"]
["強盜","34","36","強盜頭目","山賊"]
["27","鱷魚","巨鱷","クロコ","クロコダイル","ワニ"]
["樹精","樹","12","13","木","52","スピリッド","スピ"]
["巨飛","巨乳","結衣","50","巨ドレ","巨大ドレ","爆乳","巨大飛龍"]
["暗黑長者","75"]
["大足","大腳","雪怪","63","大腳瑪幽","マーヨ","マヨ"]
["賽尼斯","塞尼斯","塞","賽"]
["EF","ef","if","伊弗利特","イフ","45","IF"]
["古巨","乞丐","74","古代巨人","巨人","AG","70","ag"]
["蜘蛛","D","58","65","アルフィア","d"]
["變王","變怪","變形怪","變形怪首領","變","ドッペボス","ドッペ","變怪首領"]
["7F","監視者","7","藍惡魔","青惡魔","惡魔監視者","象7","青"]
["死亡騎士","死騎","28","死","木村","騎","dead","DK","デスナイト","TT","tt","dk"]
["狼王","狼","力卡溫","狼人","リカント","力","小棟","力王"]
["不死鳥","鳥","bird","火鳥","紫","フェニ","BIRD"]
["克特","隊長","話島","阿塔","ROSE","rose","カーツ"]
"""

OUT_TEXT="""
清除:資料庫重建、
出:時間BoSS顯示、
名稱:現有代號、
紀錄:時間+名稱
ex.0101 不死鳥
2021/05/02 -新增輸入提示
2021/06/04 -modify,bird 8H,bossname 
2011/11/17 -modify,巨飛,卡,變
"""