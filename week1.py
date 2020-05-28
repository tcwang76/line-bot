# 載入需要的模組
from __future__ import unicode_literals
import os
import psycopg2
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, PostbackEvent, LocationMessage
#如果你的access token跟secret有顯示在下面，請把下面這行註解掉。
import configparser
import flexmsg

app = Flask(__name__)


# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

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
            postgres_insert_query = f"""INSERT INTO group_data (condition, user_id) VALUES ('initial', '{event.source.user_id}');"""
            cursor.execute(postgres_insert_query)
            conn.commit()

            cursor.close()
            conn.close()

        #中途想結束輸入~delete, 把initial那列刪除
        elif event.message.text == "~delete":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='取消成功')
            )

            postgres_delete_query = f"""DELETE FROM group_data WHERE (condition, user_id) = ('initial', '{event.source.user_id}');"""
            cursor.execute(postgres_delete_query)
            conn.commit()


        #如果有創建了一列, 則接下來的資料繼續寫入
        else:
            postgres_select_query = f"""SELECT * FROM group_data WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
            cursor.execute(postgres_select_query)
            data = cursor.fetchone()
            print('data = ', data)
            column_all = ['record_no', 'activity_type', 'activity_name', 
                          'activity_time', 'location', 'people', 'cost', 
                          'due_time', 'description', 'photo', 'your_name', 
                          'your_phone', 'your_mail', 'condition', 'user_id']

            if data:
                
                if None in data:
                    i = data.index(None)
                    
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
                        msg=flexmsg.flex(i)
                        line_bot_api.reply_message(
                            event.reply_token,
                            msg)

                    #如果已經到最後一格, condition改為finish, 回覆summary，
                    elif None not in data:
                        
                        postgres_select_query = f"""SELECT * FROM group_data ORDER BY record_no DESC;"""
                        cursor.execute(postgres_select_query)
                        data = cursor.fetchone()
    
                        summary_lst = []
                        for j in range(1,len(data)-1):
                            summary_lst.append(f"{column_all[j]}:{data[j]}")
                        summary = "\n".join(summary_lst)+"\n\nIf all infomation is correct, please enter [correct], otherwise please enter the column you want to edit"
                        msg=flexmsg.sumerary(data)
                        TextSendMessage(text=summary)
                        line_bot_api.reply_message(
                            event.reply_token,
                            msg
                        )
  
                else:
                    if event.message.text == '確認開團':

                        postgres_update_query = f"""UPDATE group_data SET condition = 'finish' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
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
                        if column in column_all:
                            postgres_update_query = f"""UPDATE group_data SET {column} = Null WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
                            cursor.execute(postgres_update_query)
                            conn.commit()
                            msg=flexmsg.flex(column)
                            line_bot_api.reply_message(
                                event.reply_token,
                                msg
                            )
                        else :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text= 'please enter the column you want to edit')
                            )

            else:

                if event.message.text.encode == "double":
                    line_bot_api.reply_message(
                        event.reply_token,
                        flexmsg.sumerary
                    )

                elif event.message.text.encode == "早安":
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
    column_all = ['record_no', 'activity_type', 'activity_name', 
                  'activity_time', 'location', 'people', 'cost', 
                  'due_time', 'description', 'photo', 'your_name', 
                  'your_phone', 'your_mail', 'condition']
    if event.postback.data == "Activity_time" or event.postback.data == "Due_time":

        record = event.postback.params['datetime']
        postgres_update_query = f"""UPDATE group_data SET {column_all[i]} = '{record}' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
        cursor.execute(postgres_update_query)
        conn.commit()
        cursor.execute(postgres_select_query)
        data = cursor.fetchone()
        if None in data:
            msg=flexmsg.flex(i)
            line_bot_api.reply_message(
                event.reply_token,
                msg)
        elif None not in data:
            postgres_select_query = f"""SELECT * FROM group_data ORDER BY record_no DESC;"""
            cursor.execute(postgres_select_query)
            data = cursor.fetchone()
            msg=flexmsg.sumerary(data)
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
    column_all = ['record_no', 'activity_type', 'activity_name', 
                  'activity_time', 'location', 'people', 'cost', 
                  'due_time', 'description', 'photo', 'your_name', 
                  'your_phone', 'your_mail', 'condition']

    record = "latitude"+ str(event.message.latitude)+ " longitude" + str(event.message.longitude)
    postgres_update_query = f"""UPDATE group_data SET {column_all[i]} = '{record}' WHERE condition = 'initial' AND user_id = '{event.source.user_id}';"""
    cursor.execute(postgres_update_query)
    conn.commit()
    cursor.execute(postgres_select_query)
    data = cursor.fetchone()
    if None in data:
        msg=flexmsg.flex(i)
        line_bot_api.reply_message(
            event.reply_token,
            msg)
    elif None not in data:
        postgres_select_query = f"""SELECT * FROM group_data ORDER BY record_no DESC;"""
        cursor.execute(postgres_select_query)
        data = cursor.fetchone()
        msg=flexmsg.sumerary(data)
        line_bot_api.reply_message(
            event.reply_token,
            msg
        )
    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    app.run()
