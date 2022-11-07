#軍

from __future__ import unicode_literals
import os
from flask import Flask, request, abort,render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, JoinEvent, LeaveEvent

import configparser

from custom_models import boss, db


app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line', 'channel_access_token'))
handler = WebhookHandler(config.get('line', 'channel_secret'))

@app.route("/")
def home():
    return 'Web App with Python Flask!'

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
def handle_message(event):
    print(event)
    # 驗證群組
    if event.source.group_id =="C5a67676a5c08556a78b107c1ec642106":

        input_text = event.message.text
        print('使用者輸入',input_text)
        try:
            if len(input_text.split())==1:
                # 介紹
                if input_text == "指令":
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(
                        text='''清除:資料庫重建、\n出:時間BoSS顯示、\n
                                名稱:現有代號、\n紀錄:時間+名稱 \n ex.0101 不死鳥'''))
                # 初始化DB
                if input_text == "清除":
                    print('清除')

                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="初始化"))
                    db.clear_boss_time_record()
                    db.reset_boss_time_record()

                # 王代稱
                if input_text == "名稱":
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=boss_nick_name))

                # 回報王表
                if input_text == "出":
                    outtext = db.check_boss_time_record()
                    listouttext = db.show_boss_time_record()
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=outtext+listouttext))

            else:
                boss_name, end_time, next_time, message = boss.boss_record(event.message.text)
                line_bot_api.reply_message(event.reply_token,TextSendMessage(
                    text = "BOSS："+ boss_name +"\n"+"死亡時間："+ end_time +"\n"+"重生時間："+next_time+"\n" + message))
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="輸入錯誤"))

# 邀請事件
@handler.add(JoinEvent)
def handle_join(event):
    newcoming_text = "Hello 此機器人已綁定特定用戶群"

    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=newcoming_text)
    )

# 剔除群組事件
@handler.add(LeaveEvent)
def handle_leave(event):
    print("踢出-相關資訊", event.source)

boss_nick_name = """
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