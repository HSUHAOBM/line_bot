import os
import psycopg2
import datetime
from custom_models import BossData

DatabosslistName=[('浮士德',None, None,None),
 ('四色法師',None,None,None),
 ('52左龍',None,None,None),
 ('52右龍',None,None,None),
 ('小綠',None,None,None),
 ('小紅',None,None,None),
 ('螞蟻',None,None,None),
 ('蜈蚣', None,None,None),
 ('51飛龍', None,None,None),
 ('53飛龍', None,None,None),
 ('大黑長者', None,None,None),
 ('卡王', None,None,None),
 ('強盜', None,None,None),
 ('鱷魚', None,None,None),
 ('樹精', None,None,None),
 ('巨大飛龍', None,None,None),
 ('暗黑長者', None,None,None),
 ('大足', None,None,None),
 ('賽尼斯', None,None,None),
 ('伊弗利特', None,None,None),
 ('古代巨人', None,None,None),
 ('蜘蛛', None,None,None),
 ('變怪首領', None,None,None),
 ('惡魔監視者', None,None,None),
 ('死亡騎士', None,None,None),('狼王', None,None,None),('不死鳥', None,None,None),('克特', None,None,None)]

def Resetdatabase():#資料庫空時新增相關空數據
    DATABASE_URL = os.environ['DATABASE_URL']
    # DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a bosstimehao66').read()[:-1]
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    table_columns = '(boss_name,next_time,dead_time,out_text)'
    postgres_reset_query = f"""INSERT INTO RossTeamBossList {table_columns} VALUES (%s, %s, %s, %s);"""

    cursor.executemany(postgres_reset_query, DatabosslistName)
    conn.commit()

    message = "表單已重製初始！"
    print(message)

    cursor.close()
    conn.close()
    return message

#上傳資料到資料庫
def Updatebase(BossName,NextForTime,DeadForTime):
    DATABASE_URL = os.environ['DATABASE_URL']

    # DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a bosstimehao66').read()[:-1]
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    postgres_update_query= f"""UPDATE RossTeamBossList SET next_time=%s ,dead_time=%s ,out_text=%s WHERE boss_name=%s;"""
    # postgres_update_query= f"""UPDATE RossTeamBossList SET next_time=%s WHERE boss_name=%s;"""

    cursor.execute(postgres_update_query, (NextForTime,DeadForTime,None,BossName))
    # cursor.execute(postgres_update_query, ('17:51:13','巨大飛龍'))


    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 alpaca_training 表單！"
    print(message)

    cursor.close()
    conn.close()
    return message

#清除表單內容
def DeleteAlldatabase():
    DATABASE_URL = os.environ['DATABASE_URL']
    # DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a bosstimehao66').read()[:-1]
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_update_query= """DELETE FROM RossTeamBossList ;"""
#     postgres_update_query= """DROP TABLE RossTeamBossList; ;"""


    cursor.execute(postgres_update_query)

    conn.commit()

    message = "資料庫清空！"
    print(message)

    cursor.close()
    conn.close()
    
#顯示紀錄列表
def ShowBossTimeList():
    # DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a bosstimehao66').read()[:-1]
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    postgres_select_query = f"""SELECT * FROM RossTeamBossList WHERE next_time IS NOT NULL """

    cursor.execute(postgres_select_query)
    result=cursor.fetchall()
    ListOutText=""
    result.sort(key=takeSecond)

    for items in result:
        if items[3]==None:    
            ListOutText+=items[1].strftime('%H:%M:%S')+" -"+items[0]+"\n"
        else:
            ListOutText+=items[1].strftime('%H:%M:%S')+" -"+items[0]+" *過"+str(items[3])+"\n"
        # print(items[1],items[0],"  過",items[3])


    cursor.close()
    conn.close()   
#     print("listouttext\n\n",listouttext)    
#     print("result:",result)
    return ListOutText


def takeSecond(elem):# 获取列表的第二个元素
    return elem[1]

def updateDB(): #檢查過期資料並上傳
    updatelist=[]

    # DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a bosstimehao66').read()[:-1]
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    postgres_select_query = "SELECT * FROM RossTeamBossList WHERE next_time IS NOT NULL AND CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Taipei'> next_time"
    cursor.execute(postgres_select_query)
    result=cursor.fetchall()
    print("result",result)
    for items in range(len(result)):
        BossName=result[items][0]
        Next_Time=result[items][1]
        oldindex=result[items][3]

        BossName,time_range=BossData.BossNameList(BossName)#取得姓名和間隔

        Next_Time,index=checkDB(Next_Time,time_range,oldindex) #檢查過期資料
        updatelist.append([Next_Time,index,BossName])
    
    ResetNextTime(updatelist) #更新資料至資料庫
    cursor.close()
    conn.close()
    return  "王表\n"

def checkDB(Next_Time,time_range,oldindex):
    NowTime=datetime.datetime.now()
    if(oldindex!=None):
        oldindex=int(oldindex)
    else:
        oldindex=0
    while NowTime > Next_Time:
        Next_Time=Next_Time+time_range
        oldindex+=1
        print("過",oldindex,Next_Time,"間隔",time_range)
    print(Next_Time,oldindex)
    return Next_Time,oldindex

def ResetNextTime(updatelist):
    # DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a bosstimehao66').read()[:-1]
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_ResetNextTime_query= f"""UPDATE RossTeamBossList SET next_time=%s ,out_text=%s WHERE boss_name=%s;"""
    
    cursor.executemany(postgres_ResetNextTime_query, updatelist)
    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 alpaca_training 表單！"
    print(message)

    cursor.close()
    conn.close()