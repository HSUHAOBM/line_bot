#新增資料庫更新功能

import time
import datetime
from custom_models import CallBossData


import time
import datetime
# from custom_models import CallBossData


time_range = datetime.timedelta(hours=0,minutes=0) 
def BossTime_record(text):
    InputText = text.split(' ')
    if int(len(InputText))==1:
        OtherText=InputText[0]
        BossName=None
        DeadForTime=None
        NextForTime=None
        ErrorText=None

    else:
        OtherText=None
        BossName = InputText[1]
        
        
        if len(InputText[0])==4:
            InputText[0]=InputText[0]+"00"

        DeadForTime=datetime.datetime.strptime((datetime.datetime.now().strftime('%Y-%m-%d'))+" "+InputText[0],'%Y-%m-%d %H%M%S')
        
        # BossDeadTime=datetime.datetime.strptime(InputText[0],'%H%M%S')
        BossName,time_range=BossNameList(BossName)

        # next_time = BossDeadTime + time_range
        # next_time = next_time.strftime('%H:%M:%S')

        NextForTime=DeadForTime + time_range
        
        # NextForTime = NextForTime.strftime('%Y/%m/%d %H:%M:%S')
        # DBForTime=DBForTime.strftime('%Y/%m/%d %H:%M:%S')

        print("BossName:",BossName,"time_range:",time_range,"DeadForTime",DeadForTime,"NextForTime",NextForTime)
        #check input erorr
        check_time_range= datetime.timedelta(days=0,hours=0,minutes=30,seconds=0)
        InputNowTime=datetime.datetime.now()
        if(abs(DeadForTime-InputNowTime)>check_time_range):
            ErrorText="--- Time-Maybe-Error ---"
        else:
            ErrorText=None


        CallBossData.Updatebase(BossName,NextForTime,DeadForTime)


    return BossName,DeadForTime,NextForTime,OtherText,ErrorText

listboss001=["17","奇岩","浮士德","クライン"]
listboss002=["4","4c","4C","4色","四色","68","四賢者","カスパー","カスパーズ","四色法師"]
listboss003=["左飛","52左","701","左","左ドレ","49左","52左龍"]
listboss004=["右飛","52右","702","右","右ドレ","49右","52右龍"]
listboss005=["小綠","綠","8","G","08","g"]
listboss006=["小紅","紅","red","RED","R","09","赤","r"]
listboss007=["蟻","螞蟻","ant","3","03","アリ","あり","ANT"]
listboss008=["10","蜈蚣","包皮","海蟲","巨大蜈蚣","ワーム"]
listboss009=["51","51龍","46","46ドレ","51飛龍"]
listboss010=["53","53龍","48","48ドレ","53飛龍"]
listboss011=["大黑","黑","703","大黑長者","黑老","BE","ハイエルダー","ハイエル","be"]
listboss012=["卡王","卡","14","卡司特","ガースト","ca","CA"]
listboss013=["強盜","34","36","強盜頭目","山賊"]
listboss014=["27","鱷魚","巨鱷","クロコ","クロコダイル","ワニ"]
listboss015=["樹精","樹","12","13","木","52","スピリッド","スピ"]
listboss016=["巨飛","巨乳","結衣","50","巨ドレ","巨大ドレ","爆乳","巨大飛龍"]
listboss017=["暗黑長者","75","ベリス","暗黒","77"]
listboss018=["大足","大腳","雪怪","63","大腳瑪幽","マーヨ","マヨ"]
listboss019=["賽尼斯","塞尼斯","塞","賽","ケレニス"]
listboss020=["EF","ef","if","伊弗利特","イフ","45","IF"]
listboss021=["古巨","乞丐","74","古代巨人","巨人","AG","70","ag"]
listboss022=["蜘蛛","D","58","65","アルフィア","d"]
listboss023=["變王","變怪","變形怪","變形怪首領","變","ドッペボス","ドッペ","變怪首領"]
listboss024=["7F","監視者","7","藍惡魔","青惡魔","惡魔監視者","象7","青"]
listboss025=["死亡騎士","死騎","28","死","木村","騎","dead","DK","デスナイト","TT","tt","dk"]
listboss026=["狼王","狼","力卡溫","狼人","リカント","力","小棟","力王"]
listboss027=["不死鳥","鳥","bird","火鳥","紫","フェニ","BIRD"]
listboss028=["克特","隊長","話島","阿塔","ROSE","rose","カーツ"]
BossTureNameList=["浮士德","四色法師","52左龍","52右龍","小綠","小紅","螞蟻","蜈蚣","49飛龍",
                  "51飛龍","大黑長者","卡王","強盜","鱷魚","樹精","巨大飛龍","暗黑長者","大足賽尼斯",
                  "伊弗利特","古代巨人","蜘蛛","變怪首領","惡魔監視者","死亡騎士","不死鳥","克特"]
def BossNameList(BossName):
    if BossName in listboss001:
        time_range = datetime.timedelta(days=0,hours=1,minutes=0,seconds=0) 
        BossName="浮士德"
        return BossName,time_range
    
    elif BossName in listboss002:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0) 
        BossName="四色法師"
        return BossName,time_range
    elif BossName in listboss003:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0) 
        BossName="52左龍"
        return BossName,time_range
    elif BossName in listboss004:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0) 
        BossName="52右龍"
        return BossName,time_range
    elif BossName in listboss005:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0) 
        BossName="小綠"
        return BossName,time_range
    elif BossName in listboss006:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0) 
        BossName="小紅"
        return BossName,time_range
    elif BossName in listboss007:
        time_range = datetime.timedelta(days=0,hours=3,minutes=30,seconds=0) 
        BossName="螞蟻"
        return BossName,time_range
    elif BossName in listboss008:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0) 
        BossName="蜈蚣"
        return BossName,time_range
    elif BossName in listboss009:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        BossName="51飛龍"
        return BossName,time_range
    elif BossName in listboss010:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        BossName="53飛龍"
        return BossName,time_range
    elif BossName in listboss011:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        BossName="大黑長者"
        return BossName,time_range
    elif BossName in listboss012:
        time_range = datetime.timedelta(days=0,hours=7,minutes=30,seconds=0)
        BossName="卡王"
        return BossName,time_range
    elif BossName in listboss013:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        BossName="強盜"
        return BossName,time_range
    elif BossName in listboss014:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        BossName="鱷魚"
        return BossName,time_range
    elif BossName in listboss015:
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        BossName="樹精"
        return BossName,time_range
    elif BossName in listboss016:
        BossName="巨大飛龍"
        time_range = datetime.timedelta(days=0,hours=6,minutes=0,seconds=0)        
        return BossName,time_range
    elif BossName in listboss017:
        BossName="暗黑長者"        
        time_range = datetime.timedelta(days=0,hours=6,minutes=0,seconds=0)
        return BossName,time_range
    elif BossName in listboss018:
        BossName="大足"
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        return BossName,time_range
    elif BossName in listboss019:
        BossName="賽尼斯"
        time_range = datetime.timedelta(days=0,hours=3,minutes=0,seconds=0)
        return BossName,time_range
    elif BossName in listboss020:
        time_range = datetime.timedelta(days=0,hours=2,minutes=0,seconds=0)
        BossName="伊弗利特"
        return BossName,time_range
    elif BossName in listboss021:
        BossName="古代巨人"
        time_range = datetime.timedelta(days=0,hours=8,minutes=30,seconds=0)      
        return BossName,time_range
    elif BossName in listboss022:
        time_range = datetime.timedelta(days=0,hours=4,minutes=0,seconds=0)    
        BossName="蜘蛛"
        return BossName,time_range
    elif BossName in listboss023:
        time_range = datetime.timedelta(days=0,hours=7,minutes=0,seconds=0)    
        BossName="變怪首領"
        return BossName,time_range
    elif BossName in listboss024:
        time_range = datetime.timedelta(days=0,hours=6,minutes=0,seconds=0)    
        BossName="惡魔監視者"
        return BossName,time_range
    
    elif BossName in listboss025:
        time_range = datetime.timedelta(days=0,hours=9,minutes=0,seconds=0)      
        BossName="死亡騎士"
        return BossName,time_range
    
    elif BossName in listboss026:
        time_range = datetime.timedelta(days=0,hours=8,minutes=0,seconds=0) 
        BossName="狼王"
        return BossName,time_range
    
    elif BossName in listboss027:
        time_range = datetime.timedelta(days=0,hours=8,minutes=0,seconds=0)
        BossName="不死鳥"
        return BossName,time_range
    elif BossName in listboss028:
        time_range = datetime.timedelta(days=0,hours=10,minutes=0,seconds=0)
        BossName="克特"
        return BossName,time_range
    else:
        print("---")