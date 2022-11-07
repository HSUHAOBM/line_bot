import psycopg2
import datetime
from custom_models import boss
import os

init_data =[
    ('浮士德',None, None,None),
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
    ('死亡騎士', None,None,None),
    ('狼王', None,None,None),
    ('不死鳥', None,None,None),
    ('克特', None,None,None)
 ]

# Update connection string information
# host = "localhost"
# dbname = "localhost"
# user = "postgres"
# password = "postgres"
# sslmode = "allow"
# port = "5432"

host = "db"
dbname = os.environ.get('POSTGRES_NAME')
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
sslmode = "allow"
port = "5432"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(host, user, dbname, password, sslmode, port)


# 重置
def reset_boss_time_record():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    table_columns = '(boss_name, next_time, dead_time, out_text)'
    query = f"""INSERT INTO boss_time_record {table_columns} VALUES (%s, %s, %s, %s);"""

    cursor.executemany(query, init_data)
    conn.commit()

    cursor.close()
    conn.close()


#上傳資料到資料庫
def update_boss_time_record(boss_name, next_time, end_time):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query= f"""UPDATE boss_time_record
    SET next_time = %s, dead_time = %s, out_text = %s
    WHERE boss_name = %s ;"""

    cursor.execute(query, (next_time, end_time, None, boss_name))
    conn.commit()

    cursor.close()
    conn.close()

#清除表單內容
def clear_boss_time_record():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query= """DELETE FROM boss_time_record ;"""

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

#顯示紀錄列表
def show_boss_time_record():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query = f"""SELECT * FROM boss_time_record WHERE next_time IS NOT NULL """
    cursor.execute(query)

    result = cursor.fetchall()
    show_text = ""
    result.sort(key=take_second)

    for items in result:
        if items[3]==None:
            show_text += items[1].strftime('%H:%M:%S') +" -" + items[0] + "\n"
        else:
            show_text += items[1].strftime('%H:%M:%S') +" -" +items[0] + " *過" + str(items[3]) + "\n"

    cursor.close()
    conn.close()

    return show_text


def take_second(elem):# 取第二值
    return elem[1]

def check_boss_time_record(): #檢查過期資料並上傳
    update_list = []
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    # 下次出現時間 != 空 , 且 下次出現時間已經過了
    query = """SELECT * FROM boss_time_record
     WHERE next_time IS NOT NULL
     AND CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Taipei' > next_time"""
    cursor.execute(query)
    result=cursor.fetchall()

    for items in range(len(result)):
        boss_name = result[items][0]
        next_time = result[items][1]
        out_text = result[items][3]
        #取得姓名和間隔
        boss_name, time_range = boss.boss_list(boss_name)
        #檢查過期資料
        next_time, out_text = record_compute(next_time, time_range, out_text)
        update_list.append([next_time, out_text, boss_name])
    #更新資料至資料庫
    update_boss_time_record_out_text(update_list)

    cursor.close()
    conn.close()

    return  "王表\n"

def record_compute(next_time, time_range, out_text):
    now_time = datetime.datetime.now()
    if out_text == None:
        out_text = 0

    while now_time > next_time:
        next_time = next_time + time_range
        out_text += 1
    return next_time, out_text

def update_boss_time_record_out_text(update_list):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query= f"""UPDATE boss_time_record SET next_time=%s ,out_text=%s WHERE boss_name=%s;"""
    cursor.executemany(query, update_list)
    conn.commit()

    cursor.close()
    conn.close()


#表初始建立欄位
def CreadDB():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    create_table_query ='''CREATE TABLE boss_time_record(
       boss_name VARCHAR (50) NOT NULL,
       next_time timestamp,
       dead_time timestamp,
       out_text VARCHAR);'''

    cursor.execute(create_table_query)
    conn.commit()

    cursor.close()
    conn.close()
