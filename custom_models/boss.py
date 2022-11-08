import datetime
from custom_models import db

time_range = datetime.timedelta(hours=0,minutes=0)
def boss_record(text):
    # time + name  -> 2030 克特
    text = text.split(' ')
    # 補上秒
    # 2105 -> 210500
    if len(text[0]) == 4:
        text[0] = text[0] + "00"
    name = text[1]
    time = text[0]

    # 輸入當下的日期
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    # boss 死亡時間
    end_time = datetime.datetime.strptime(date + " " + time ,'%Y-%m-%d %H%M%S')

    # 取 真正名稱 重生區間
    boss_name , time_range = boss_list(name)

    if time_range:
        message = ""

        # 計算下次時間
        next_time = end_time + time_range

        #check input erorr
        check_time_range = datetime.timedelta(days=0,hours=0,minutes=30,seconds=0)
        now_time = datetime.datetime.now()

        if( abs(end_time-now_time) > check_time_range):
            message = "\n--- Time-Maybe-Error ---"

        # 更新資料庫
        db.update_boss_time_record(boss_name, next_time, end_time)

        # 轉 str
        next_time = next_time.strftime('%m/%d %H:%M:%S')
        end_time = end_time.strftime('%m/%d %H:%M:%S')

        return boss_name, end_time, next_time, message

listboss001 = ["17","奇岩","浮士德","クライン"]
listboss002 = ["4","4c","4C","4色","四色","68","四賢者","カスパー","カスパーズ","四色法師"]
listboss003 = ["左飛","52左","701","左","左ドレ","49左","52左龍"]
listboss004 = ["右飛","52右","702","右","右ドレ","49右","52右龍"]
listboss005 = ["小綠","綠","8","G","08","g"]
listboss006 = ["小紅","紅","red","RED","R","09","赤","r"]
listboss007 = ["蟻","螞蟻","ant","3","03","アリ","あり","ANT"]
listboss008 = ["10","蜈蚣","包皮","海蟲","巨大蜈蚣","ワーム"]
listboss009 = ["51","51龍","46","46ドレ","51飛龍"]
listboss010 = ["53","53龍","48","48ドレ","53飛龍"]
listboss011 = ["大黑","黑","703","大黑長者","黑老","BE","ハイエルダー","ハイエル","be"]
listboss012 = ["卡王","卡","14","卡司特","ガースト","ca","CA"]
listboss013 = ["強盜","34","36","強盜頭目","山賊"]
listboss014 = ["27","鱷魚","巨鱷","クロコ","クロコダイル","ワニ"]
listboss015 = ["樹精","樹","12","13","木","52","スピリッド","スピ"]
listboss016 = ["巨飛","巨乳","結衣","50","巨ドレ","巨大ドレ","爆乳","巨大飛龍"]
listboss017 = ["暗黑長者","75","ベリス","暗黒","77"]
listboss018 = ["大足","大腳","雪怪","63","大腳瑪幽","マーヨ","マヨ"]
listboss019 = ["賽尼斯","塞尼斯","塞","賽","ケレニス"]
listboss020 = ["EF","ef","if","伊弗利特","イフ","45","IF"]
listboss021 = ["古巨","乞丐","74","古代巨人","巨人","AG","70","ag"]
listboss022 = ["蜘蛛","D","58","65","アルフィア","d"]
listboss023 = ["變王","變怪","變形怪","變形怪首領","變","ドッペボス","ドッペ","變怪首領"]
listboss024 = ["7F","監視者","7","藍惡魔","青惡魔","惡魔監視者","象7","青"]
listboss025 = ["死亡騎士","死騎","28","死","木村","騎","dead","DK","デスナイト","TT","tt","dk"]
listboss026 = ["狼王","狼","力卡溫","狼人","リカント","力","小棟","力王"]
listboss027 = ["不死鳥","鳥","bird","火鳥","紫","フェニ","BIRD"]
listboss028 = ["克特","隊長","話島","阿塔","ROSE","rose","カーツ"]
listboss029 = ["18"]
# BossTureNameList=["浮士德","四色法師","52左龍","52右龍","小綠","小紅","螞蟻","蜈蚣","49飛龍",
#                   "51飛龍","大黑長者","卡王","強盜","鱷魚","樹精","巨大飛龍","暗黑長者","大足賽尼斯",
#                   "伊弗利特","古代巨人","蜘蛛","變怪首領","惡魔監視者","死亡騎士","不死鳥","克特"]

# 時間間隔
def boss_list(name):
    if name in listboss001:
        time_range = datetime.timedelta(days=0,hours=6,minutes=0,seconds=0)
        boss_name = "17"
        return boss_name, time_range
    elif name in listboss002:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        boss_name = "四色法師"
        return boss_name, time_range
    elif name in listboss003:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        boss_name = "52左龍"
        return boss_name, time_range
    elif name in listboss004:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        boss_name = "52右龍"
        return boss_name, time_range
    elif name in listboss005:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        boss_name = "小綠"
        return boss_name, time_range
    elif name in listboss006:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        boss_name = "小紅"
        return boss_name, time_range
    elif name in listboss007:
        time_range = datetime.timedelta(days=0,hours=3,minutes=30,seconds=0)
        boss_name = "螞蟻"
        return boss_name, time_range
    elif name in listboss008:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        boss_name = "蜈蚣"
        return boss_name, time_range
    elif name in listboss009:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        boss_name = "51飛龍"
        return boss_name, time_range
    elif name in listboss010:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        boss_name = "53飛龍"
        return boss_name, time_range
    elif name in listboss011:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        boss_name = "大黑長者"
        return boss_name, time_range
    elif name in listboss012:
        time_range = datetime.timedelta(days=0,hours=7,minutes=30,seconds=0)
        boss_name = "卡王"
        return boss_name, time_range
    elif name in listboss013:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        boss_name = "強盜"
        return boss_name, time_range
    elif name in listboss014:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        boss_name = "鱷魚"
        return boss_name, time_range
    elif name in listboss015:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        boss_name = "樹精"
        return boss_name, time_range
    elif name in listboss016:
        boss_name = "巨大飛龍"
        time_range = datetime.timedelta(days=0,hours=6,minutes=0,seconds=0)
        return boss_name, time_range
    elif name in listboss017:
        boss_name = "暗黑長者"
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        return boss_name, time_range
    elif name in listboss018:
        boss_name = "大足"
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        return boss_name, time_range
    elif name in listboss019:
        boss_name = "賽尼斯"
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        return boss_name, time_range
    elif name in listboss020:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        boss_name = "伊弗利特"
        return boss_name, time_range
    elif name in listboss021:
        boss_name = "古代巨人"
        time_range = datetime.timedelta(days=0,hours=8,minutes=30,seconds=0)
        return boss_name, time_range
    elif name in listboss022:
        time_range = datetime.timedelta(days=0,hours=4,minutes=0,seconds=0)
        boss_name = "蜘蛛"
        return boss_name, time_range
    elif name in listboss023:
        time_range = datetime.timedelta(days=0,hours=7,minutes=0,seconds=0)
        boss_name = "變怪首領"
        return boss_name, time_range
    elif name in listboss024:
        time_range = datetime.timedelta(days=0,hours=6,minutes=0,seconds=0)
        boss_name = "惡魔監視者"
        return boss_name, time_range
    elif name in listboss025:
        time_range = datetime.timedelta(days=0,hours=9,minutes=0,seconds=0)
        boss_name = "死亡騎士"
        return boss_name,time_range
    elif name in listboss026:
        time_range = datetime.timedelta(days=0,hours=8,minutes=0,seconds=0)
        boss_name = "狼王"
        return boss_name, time_range
    elif name in listboss027:
        time_range = datetime.timedelta(days=0,hours=8,minutes=0,seconds=0)
        boss_name = "不死鳥"
        return boss_name, time_range
    elif name in listboss028:
        time_range = datetime.timedelta(days=0,hours=10,minutes=0,seconds=0)
        boss_name = "克特"
        return boss_name, time_range
    elif name in listboss029:
        time_range = datetime.timedelta(days=0,hours=7,minutes=0,seconds=0)
        boss_name = "18"
        return boss_name, time_range
    else:
        return boss_name, time_range
