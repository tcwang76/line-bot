# 載入需要的模組
from __future__ import unicode_literals
import os
import psycopg2
import datetime as dt
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, PostbackEvent, LocationMessage
import configparser
import flexmsg

app = Flask(__name__)


# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

#check upload
@app.route("/")
def hello():
    return "Hello, world!"

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    print(body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    
     if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        #連結到heroku資料庫
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()

        
        if event.message.text == "~open":
            line_bot_api.reply_message(
                event.reply_token,
                flexmsg.activity_type)

            print("prepare to open the group")

            #把只創建卻沒有寫入資料的列刪除
            postgres_delete_query = f"""DELETE FROM group_data WHERE (condition) = ('initial');"""
            cursor.execute(postgres_delete_query)
            conn.commit()
            
            #創建一列(condition = initial)
            postgres_insert_query = f"""INSERT INTO group_data (condition, user_id, attendee, photo, description) VALUES ('initial', '{event.source.user_id}', '1', '無', '無');"""
            cursor.execute(postgres_insert_query)
            conn.commit()
            #撈主揪的資料
            postgres_select_query=f'''SELECT name,phone FROM group_data WHERE user_id = '{event.source.user_id}' AND condition!= 'initial' ORDER BY activity_no DESC;'''
            cursor.execute(postgres_select_query)
            data_for_basicinfo = cursor.fetchone()

            if data_for_basicinfo:
                postgres_insert_query = f"""UPDATE group_data SET name='{data_for_basicinfo[0]}' , phone='{data_for_basicinfo[1]}' WHERE (condition, user_id) = ('initial', '{event.source.user_id}');"""
                cursor.execute(postgres_insert_query)
                conn.commit()

            cursor.close()
            conn.close()

        #中途想結束輸入~delete, 把initial那列刪除
        elif event.message.text == "取消" :
            postgres_select_query=f'''SELECT * FROM group_data WHERE user_id = '{event.source.user_id}' AND condition= 'initial';'''
            cursor.execute(postgres_select_query)
            data = cursor.fetchone()
            
            postgres_select_query=f'''SELECT * FROM group_data WHERE user_id = '{event.source.user_id}' AND condition= 'initial';'''
            cursor.execute(postgres_select_query)
            data_2 = cursor.fetchone()

            postgres_delete_query = f"""DELETE FROM group_data WHERE (condition, user_id) = ('initial', '{event.source.user_id}');"""
            cursor.execute(postgres_delete_query)
            conn.commit()
            postgres_delete_query = f"""DELETE FROM registration_data WHERE (condition, user_id) = ('initial', '{event.source.user_id}');"""
            cursor.execute(postgres_delete_query)
            conn.commit()
            
            
            if data or data_2:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='取消成功')
                )
            else:
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='無可取消的開團/報名資料')
                )
        
        elif event.message.text == "~join":
            msg=flexmsg.activity_type
            line_bot_api.reply_message(
                event.reply_token,
                msg
            )


        
        #如果有創建了一列, 則接下來的資料繼續寫入
        else:
            postgres_select_query = f"""SELECT * FROM registration_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
            cursor.execute(postgres_select_query)
            #準備寫入報名資料的那一列
            data_2 = cursor.fetchone() 
            column_all_registration = ['record_no', 'activity_no', 
                                       'activity_name', 'attendee_name', 'phone', 
                                       'mail', 'condition', 'user_id']
            
            activity_type = ['登山踏青', '桌遊麻將', '吃吃喝喝', '唱歌跳舞']
            
            postgres_select_query = f"""SELECT * FROM group_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
            cursor.execute(postgres_select_query)
            data = cursor.fetchone()
            print('data = ', data)
            column_all = ['acrivity_no', 'activity_type', 'activity_name', 
                          'activity_date', 'activity_time', 'location_tittle', 'lat', 'long', 'people', 'cost', 
                          'due_date', 'description', 'photo', 'name', 
                          'phone', 'mail', 'attendee', 'condition', 'user_id']

            if data:
                
                if None in data:
                    i = data.index(None)
                    print("i= ",i)
                    record = event.message.text
                    #如果使用者輸入的資料不符合資料庫的資料型態, 則輸入N/A
                    if event.message.type == 'text':
                        postgres_update_query = f"""UPDATE group_data SET {column_all[i]} = '{record}' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                        cursor.execute(postgres_update_query)
                        conn.commit()
                    else:
                        postgres_update_query = f"""UPDATE group_data SET {column_all[i]} = 'N/A' WHERE condition = 'initial'AND user_id = '{event.source.user_id}';"""
                        cursor.execute(postgres_update_query)
                        conn.commit()
                    
                   #如果還沒輸入到最後一格, 則繼續詢問下一題
                    postgres_select_query = f"""SELECT * FROM group_data WHERE condition = 'initial'AND user_id = '{event.source.user_id}';"""
                    cursor.execute(postgres_select_query)
                    data = cursor.fetchone()
                
                    if None in data: 
                        msg=flexmsg.flex(i,data)
                        line_bot_api.reply_message(
                            event.reply_token,
                            msg)

                    #如果已經到最後一格, condition改為finish, 回覆summary，
                    elif None not in data:
                        
                        postgres_select_query = f"""SELECT * FROM group_data WHERE user_id = '{event.source.user_id}' ORDER BY activity_no DESC;"""
                        cursor.execute(postgres_select_query)
                        data = cursor.fetchone()
                        msg=flexmsg.summary(data)
                        line_bot_api.reply_message(
                            event.reply_token,
                            msg
                        )
  
                else:
                    if event.message.text == '確認開團':

                        postgres_update_query = f"""UPDATE group_data SET condition = 'pending' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                        cursor.execute(postgres_update_query)
                        conn.commit()

                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="finish!!")
                        )

                        cursor.close()
                        conn.close()
                        
                    else:
                        column = event.message.text
                         # 處理location 因為location 跟資料庫的名字不一樣
                        if column == "location":
                            postgres_update_query = f"""UPDATE group_data SET location_tittle = Null WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                            cursor.execute(postgres_update_query)
                            conn.commit()
                            msg=flexmsg.flex(column,data)
                            line_bot_api.reply_message(
                                event.reply_token,
                                msg
                            )
                        elif column in column_all:
                            postgres_update_query = f"""UPDATE group_data SET {column} = Null WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                            cursor.execute(postgres_update_query)
                            conn.commit()
                            msg=flexmsg.flex(column,data)
                            line_bot_api.reply_message(
                                event.reply_token,
                                msg
                            )
                        else :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text= 'please enter the column you want to edit')
                            )

            elif event.message.text in activity_type: #這裡的event.message.text會是上面quick reply回傳的訊息(四種type其中一種)        
                DATABASE_URL = os.environ['DATABASE_URL']
                conn = psycopg2.connect(DATABASE_URL, sslmode='require')
                cursor = conn.cursor()
                postgres_select_query = f"""SELECT * FROM group_data WHERE activity_date >= '{dt.date.today()}' AND activity_type='{event.message.text}'  and people > attendee and condition = 'pending' ORDER BY activity_date ASC ;"""
                cursor.execute(postgres_select_query)
                data_2 = cursor.fetchall()
                msg=flexmsg.carousel(data_2)
                line_bot_api.reply_message(
                    event.reply_token,
                    msg
                )

            elif "詳細資訊" in event.message.text :
                record=event.message.text.split("_")
                DATABASE_URL = os.environ['DATABASE_URL']
                conn = psycopg2.connect(DATABASE_URL, sslmode='require')
                cursor = conn.cursor()
                postgres_select_query = f"""SELECT * FROM group_data WHERE activity_no = '{record[0]}' ;"""
                cursor.execute(postgres_select_query)
                data_tmp = cursor.fetchone()
                msg=flexmsg.MoreInfoSummary(data_tmp)

                line_bot_api.reply_message(
                    event.reply_token,
                    msg
                )
                
                #~~點了carousel的"了解更多"，跳出該團的summary

            elif '立即報名' in event.message.text: #點了"立即報名後即回傳activity_no和activity_name"
                record=event.message.text.split("_")
                #刪掉報名失敗的列
                postgres_delete_query = f"""DELETE FROM registration_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                cursor.execute(postgres_delete_query)
                conn.commit()

                #創建一列
                postgres_insert_query = f"""INSERT INTO registration_data (condition, user_id, activity_no, activity_name ) VALUES ('initial', '{event.source.user_id}','{record[1]}', '{record[2]}');"""
                cursor.execute(postgres_insert_query)   
                conn.commit()

                postgres_select_query = f"""SELECT * FROM registration_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                cursor.execute(postgres_select_query)
                data_2 = cursor.fetchone() #準備寫入報名資料的那一列
                i_2 = data_2.index(None)

                msg_2 = flexmsg.extend(i_2,data_2) #flexmsg需要新增報名情境
                line_bot_api.reply_message(
                    event.reply_token,
                    msg_2
                )

            elif data_2:
                if None in data_2:
                    
                    i_2 = data_2.index(None)

                    record = event.message.text

                    #當進行到輸入電話時(i_2==4)，開始檢驗是否重複
                    if i_2 == 4:
                        postgres_select_query = f"""SELECT activity_no FROM registration_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                        cursor.execute(postgres_select_query)
                        activity_no = cursor.fetchone()[0] 

                        postgres_select_query = f"""SELECT phone FROM registration_data WHERE activity_no = '{activity_no}';"""
                        cursor.execute(postgres_select_query)
                        phone_registration = cursor.fetchall()

                        #如果使用者輸入的電話重複則報名失敗，刪掉原本創建的列
                        for phone in phone_registration:
                            if record in phone_registration:
                                postgres_delete_query = f"""DELETE FROM registration_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                                cursor.execute(postgres_delete_query)
                                conn.commit()

                                line_bot_api.reply_message(
                                    event.reply_token,
                                    TextSendMessage(text="不可重複報名")
                                )
                                #~~~這邊感覺可以設計一個flex_msg，出現[返回]按鈕，重新回到報名第一步(按鈕回傳~join)

                            else:
                                postgres_update_query = f"""UPDATE registration_data SET {column_all_registration[i_2]} = '{record}' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                                cursor.execute(postgres_update_query)
                                conn.commit()
           

                    else:    
                        #如果使用者輸入的資料不符合資料庫的資料型態, 則輸入N/A
                        if event.message.type == 'text':
                            postgres_update_query = f"""UPDATE registration_data SET {column_all_registration[i_2]} = '{record}' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                            cursor.execute(postgres_update_query)
                            conn.commit()
                        else:
                            postgres_update_query = f"""UPDATE registration_data SET {column_all_registration[i_2]} = 'N/A' WHERE condition = 'initial'AND user_id = '{event.source.user_id}';"""
                            cursor.execute(postgres_update_query)
                            conn.commit()  

                    postgres_select_query = f"""SELECT * FROM registration_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                    cursor.execute(postgres_select_query)
                    data_2 = cursor.fetchone() #準備寫入報名資料的那一列  
                    print("i_2 = ",i_2)
                    print("data_2 = ",data_2)


                    if None in data_2:
                        msg_2 = flexmsg.extend(i_2+1,data_2) #flexmsg需要新增報名情境
                        line_bot_api.reply_message(
                            event.reply_token,
                            msg_2
                        )               
                    #出現summary
                    elif None not in data_2:
                        msg_2 = flexmsg.summary_for_attend(data_2)
                        line_bot_api.reply_message(
                            event.reply_token,
                            msg_2
                        )

                else:
                    if event.message.text == '確認報名':
                        #找到他報的團的編號activity_no
                        postgres_select_query = f"""SELECT activity_no FROM registration_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                        cursor.execute(postgres_select_query)
                        activity_no = cursor.fetchone()[0]

                        #找報該團現在的報名人數attendee並更新(+1)
                        postgres_select_query = f"""SELECT attendee FROM group_data WHERE activity_no = {activity_no};"""
                        cursor.execute(postgres_select_query)
                        attendee = cursor.fetchone()[0]
                        attendee += 1 

                        #將更新的報名人數attendee記錄到報名表單group_data裡
                        postgres_update_query = f"""UPDATE group_data SET attendee = {attendee} WHERE activity_no = {activity_no};"""
                        cursor.execute(postgres_update_query)
                        conn.commit()

                        #檢查報名人數attendee是否達上限people
                        postgres_select_query = f"""SELECT people FROM group_data WHERE activity_no = {activity_no};"""
                        cursor.execute(postgres_select_query)
                        people = cursor.fetchone()[0]

                        if attendee == people:
                            postgres_update_query = f"""UPDATE group_data SET condition = 'closed' WHERE activity_no = {activity_no};"""
                            cursor.execute(postgres_update_query)
                            conn.commit()


                        #將報名表單的condition改成closed
                        postgres_update_query = f"""UPDATE registration_data SET condition = 'closed' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                        cursor.execute(postgres_update_query)
                        conn.commit()

                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="finish!!")
                        )

                        cursor.close()
                        conn.close()
                    elif event.message.text in column_all_registration:
                        postgres_update_query = f"""UPDATE registration_data SET {event.message.text} = Null WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                        cursor.execute(postgres_update_query)
                        conn.commit()
                        msg_2 = flexmsg.extend(event.message.text,data_2) #flexmsg需要新增報名情境
                        line_bot_api.reply_message(
                            event.reply_token,
                            msg_2
                        ) 
                    else:
                        line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text= 'please enter the column you want to edit')
                            )
            
            
            else:

                if event.message.text.encode == "double":
                    line_bot_api.reply_message(
                        event.reply_token,
                        flexmsg.summary(data)
                    )

                elif event.message.text == "早安":
                    img = 'https://pic.pimg.tw/ellenlee0409/1566550498-3560465550.jpg'
                    line_bot_api.reply_message(
                        event.reply_token,
                        ImageSendMessage(original_content_url=img ,preview_image_url=img)
                    )
            
#                 else:    
#                     line_bot_api.reply_message(
#                         event.reply_token,
#                         TextSendMessage(text=event.message.text)
#                     )
#處理postback 事件，例如datetime picker
@handler.add(PostbackEvent)
def gathering(event):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_select_query = f"""SELECT * FROM group_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
    cursor.execute(postgres_select_query)
    data = cursor.fetchone()

    i = data.index(None)
    print("i =",i)
    column_all = ['acrivity_no', 'activity_type', 'activity_name', 
                  'activity_date', 'activity_time', 'location_tittle', 'lat', 'long', 'people', 'cost', 
                  'due_date', 'description', 'photo', 'name', 
                  'phone', 'mail', 'attendee', 'condition', 'user_id']
    #處理activity date and time
    if event.postback.data == "Activity_time" :

        record = event.postback.params['datetime']
        record=record.split("T")
        temp=dt.date.fromisoformat(record[0])-dt.timedelta(days=1)
        postgres_update_query = f"""UPDATE group_data SET ({column_all[i]},{column_all[i+1]},{column_all[i+7]} ) = ('{record[0]}','{record[1]}','{temp}') WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
        cursor.execute(postgres_update_query)
        conn.commit()
        
        #處理due date
    elif event.postback.data == "Due_time":

        record = event.postback.params['date']
        postgres_update_query = f"""UPDATE group_data SET {column_all[i]} = '{record}' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
        cursor.execute(postgres_update_query)
        conn.commit()
        
    cursor.execute(postgres_select_query)
    data = cursor.fetchone()

    if None in data:
        msg=flexmsg.flex(i,data)
        line_bot_api.reply_message(
            event.reply_token,
            msg)
    elif None not in data:
        postgres_select_query = f"""SELECT * FROM group_data WHERE user_id = '{event.source.user_id}' ORDER BY activity_no DESC;"""
        cursor.execute(postgres_select_query)
        data = cursor.fetchone()
        msg=flexmsg.summary(data)
        line_bot_api.reply_message(
            event.reply_token,
            msg
        )
    cursor.close()
    conn.close()

# location 事件
@handler.add(MessageEvent, message=LocationMessage)
def gathering(event):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_select_query = f"""SELECT * FROM group_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
    cursor.execute(postgres_select_query)
    data = cursor.fetchone()
    i = data.index(None)
    print("i =",i)
    column_all = ['acrivity_no', 'activity_type', 'activity_name', 
                  'activity_date', 'activity_time', 'location_tittle', 'lat', 'long', 'people', 'cost', 
                  'due_date', 'description', 'photo', 'name', 
                  'phone', 'mail', 'attendee', 'condition', 'user_id']

    record =[ event.message.title, event.message.latitude, event.message.longitude]
    postgres_update_query = f"""UPDATE group_data SET ({column_all[i]}, {column_all[i+1]}, {column_all[i+2]}) = ('{record[0]}', '{record[1]}', '{record[2]}') WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
    cursor.execute(postgres_update_query)
    conn.commit()
    cursor.execute(postgres_select_query)
    data = cursor.fetchone()

    if None in data:
        msg=flexmsg.flex(i,data)
        line_bot_api.reply_message(
            event.reply_token,
            msg)
    elif None not in data:
        postgres_select_query = f"""SELECT * FROM group_data WHERE user_id = '{event.source.user_id}' ORDER BY record_no DESC;"""
        cursor.execute(postgres_select_query)
        data = cursor.fetchone()
        msg=flexmsg.summary(data)
        line_bot_api.reply_message(
            event.reply_token,
            msg
        )
    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    app.run()
