# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, PostbackEvent, JoinEvent, LeaveEvent, MemberJoinEvent, MemberLeaveEvent,
    FollowEvent, UnfollowEvent, BeaconEvent, AccountLinkEvent, DeviceLinkEvent, DeviceUnlinkEvent,
    TextSendMessage, StickerSendMessage, ImageSendMessage, VideoSendMessage, AudioSendMessage,
    LocationSendMessage, FlexSendMessage, TemplateSendMessage,
    MessageAction, PostbackAction, DatetimePickerAction, LocationAction, URIAction, CameraAction, CameraRollAction, 
    TextMessage, StickerMessage, ImageMessage, VideoMessage, AudioMessage, FileMessage, LocationMessage,
    BubbleContainer, ImageComponent, BoxComponent, TextComponent, SpacerComponent, IconComponent, ButtonComponent, SeperatorComponent, 
    ButtonsTemplate, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn,
    ConfirmTemplate, QuickReply, QuickReplyButton)
import configparser as cfg

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = cfg.ConfigParser()
config.read("config.ini")

# 聊天機器人的 Chennel access token
line_bot_api = LineBotApi(config.get("line-bot", "channel_access_token"))
# 聊天機器人的 Channel secret
handler = WebhookHandler(config.get("line-bot", "channel_secret"))

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text = True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()
#處理postback event
@handler.add(PostbackEvent)
def postback(event):
    print("postback event: ",event)
    line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text= str(event.postback),
                                quick_reply=qreply))
    
# 學你說話
@handler.add(MessageEvent, message = TextMessage)
def echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = event.message.text)
            )
        #reply_message只能在收到其他使用者信息的時候，回傳一則信息

if __name__ == "__main__":
    app.run()
