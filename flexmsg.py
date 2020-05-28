from linebot.models import (
    TextSendMessage, MessageAction, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)
def flex(i):
    if i == 1 or i =="activity_name":
        msg=activity_name
    elif i == 2 or i =="activity_time":
        msg=activity_time
    elif i == 3 or i =="location":
        msg=location
    elif i == 4 or i=="people":
        msg=people
    elif i == 5 or i == "cost":
        msg=cost
    elif i == 6 or i == "due_time":
        msg=due_time
    elif i == 7 or i == "description":
        msg=description
    elif i == 8 or i == "photo":
        msg=photo
    elif i == 9 or i == "your_name":
        msg=name
    elif i == 10 or i =="your_phone":
        msg=phone
    elif i == 11 or i == "your_mail":
        msg=mail
    elif i == "activity_type":
        msg=activity_type
    else:
        msg="try again"
    return msg

activity_type=TextSendMessage(
    text = "請選擇您的活動類型",
    quick_reply = QuickReply(
        items = [
            QuickReplyButton(
                action = MessageAction(label = "登山踏青", text = "登山踏青")
                ),
            QuickReplyButton(
                action = MessageAction(label = "桌遊麻將", text = "桌遊麻將")
                ),
            QuickReplyButton(
                action = MessageAction(label = "吃吃喝喝", text = "吃吃喝喝")
                ),
            QuickReplyButton(
                action = MessageAction(label = "唱歌跳舞", text = "唱歌跳舞")
                )
            ]))

activity_name=FlexSendMessage(
    alt_text = "請填寫活動名稱", 
    contents = BubbleContainer(
        direction = "ltr",
        body = BoxComponent(
            layout = "vertical",
            contents = [
                TextComponent(text = "活動名稱", weight = "bold", size = "lg", align = "center"),
                BoxComponent(layout = "baseline", margin = "md", contents = [
                    TextComponent(text = "請問您的活動名稱要叫什麼呢？", 
                                  size = "md", flex = 0, color = "#666666"
                        )
                    ]
                )
            ]
        )))

activity_time=FlexSendMessage(
    alt_text = "請挑選活動時間", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請選擇活動時間",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        ),
        footer=BoxComponent(
          layout= "horizontal",
          contents= [
            ButtonComponent(
              DatetimePickerAction(
                label= "點我選時間",
                data="Activity_time",
                mode= "datetime",
                initial= "2020-05-26T15:25",
                max= "2021-05-26T15:25",
                min= "2019-05-26T15:25"
              )
            )
          ]
        )
    )
)

location=FlexSendMessage(
    alt_text = "請挑選活動地點", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請選擇活動地點",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        ),
        footer=BoxComponent(
          layout= "horizontal",
          contents= [
            ButtonComponent(
              URIAction(
                label= "點我選地點",
                uri= "https://line.me/R/nv/location"
              )
            )
          ]
        )
    )
)

people=FlexSendMessage(
    alt_text = "請填寫人數", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請填寫活動參加人數",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        )
    )
)

cost=FlexSendMessage(
    alt_text = "請填寫預計支出", 
    contents =BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請填寫預計支出",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        )
    )
)

due_time=FlexSendMessage(
    alt_text = "請挑選截止時間", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請選擇報名截止時間",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        ),
        footer=BoxComponent(
          layout= "horizontal",
          contents= [
            ButtonComponent(
              DatetimePickerAction(
                label= "點我選時間",
                data="Due_time",
                mode= "datetime",
                initial= "2020-05-26T15:25",
                max= "2021-05-26T15:25",
                min= "2019-05-26T15:25"
              )
            )
          ]
        )
    )
)

description=FlexSendMessage(
    alt_text = "請填寫活動內容", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請填寫詳細活動內容",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        )
    )
)

photo=FlexSendMessage(
    alt_text = "請提供照片網址", 
    contents =BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請提供照片網址，若無網址\n請先上傳至網路平台（imgurl...等）",
              size= "md",
              align= "center",
              weight= "bold"
              )
          ]
        )
    )
)

name=FlexSendMessage(
    alt_text = "請提供名稱", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請提供您的姓名或是可以辨識之暱稱",
              size= "md",
              align= "center",
              weight= "bold"
              )
          ]
        )
    )
)

phone=FlexSendMessage(
    alt_text = "請提供電話", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請提供可以聯絡您的電話號碼",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        )
    )
)

mail=FlexSendMessage(
    alt_text = "請提供信箱", 
    contents = BubbleContainer(
        direction= "ltr",
        body=BoxComponent(
          layout= "vertical",
          contents=[
          TextComponent(
              text="請提供可以聯絡您的電子信箱",
              size= "lg",
              align= "center",
              weight= "bold"
              )
          ]
        )
    )
)
def sumerary(data):
    sumer = FlexSendMessage(
        alt_text = "請確認開團資訊",
        contents = BubbleContainer(
            direction = "ltr",
            header = BoxComponent(
              layout = "vertical",
              contents = [
              TextComponent(
                  text = "請確認開團資訊：",
                  weight = "bold",
                  size = "md",
                  align = "start",
                  color = "#000000"
                  )
              ]
            ),
            body = BoxComponent(
                layout = "vertical",
                contents = [
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動類型：{data[1]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "activity_type"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動名稱：{data[2]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "activity_name"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動時間：{data[3]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "activity_time"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動地點：{data[4]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "location"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動人數：{data[5]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "people"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動費用：{data[6]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "cost"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動報名截止時間：{data[7]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "due_time"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動敘述：{data[8]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "description"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動照片：{data[9]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "photo"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"主揪姓名：{data[10]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "your_name"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"主揪電話：{data[11]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "your_phone"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"主揪email：{data[12]}",
                                size = "md",
                                align = "start"
                            ),
                            ButtonComponent(
                                style = "primary",
                                action = MessageAction(
                                    label = "修改",
                                    text = "your_mail"
                                )
                            )
                        ]
                    ),
                ]
            ),
            footer = BoxComponent(
                layout = "vertical",
                contents = [
                    ButtonComponent(
                        style = "primary",
                        action = MessageAction(
                            label = "確認開團",
                            text = "確認開團"
                        )
                    )
                ]
            )
        )
    )
    return sumer

# #請把Flexmessage集中在這邊

# #活動類型（選單）(by Tina)
#     elif text == "活動類型":
#         message = TextSendMessage(
#                 text = "請選擇您的活動類型",
#                 quick_reply = QuickReply(
#                     items = [
#                         QuickReplyButton(
#                             action = MessageAction(label = "登山踏青", text = "登山踏青")
#                             ),
#                         QuickReplyButton(
#                             action = MessageAction(label = "桌遊麻將", text = "桌遊麻將")
#                             ),
#                         QuickReplyButton(
#                             action = MessageAction(label = "吃吃喝喝", text = "吃吃喝喝")
#                             ),
#                         QuickReplyButton(
#                             action = MessageAction(label = "唱歌跳舞", text = "唱歌跳舞")
#                             )
#                         ]))
        
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )


# #活動名稱 (by Tina)
#     if text == "活動名稱":
#         bubble = BubbleContainer(
#             direction = "ltr",
#             body = BoxComponent(
#                 layout = "vertical",
#                 contents = [
#                     TextComponent(text = "活動名稱", weight = "bold", size = "lg", align = "center"),
#                     BoxComponent(layout = "baseline", margin = "md", contents = [
#                         TextComponent(text = "請問您的活動名稱要叫什麼呢？", size = "md", flex = 0, color = "#666666")
#                         ]
#                                  )
#                     ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請填寫活動名稱", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #活動時間
# if text == "活動時間":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請選擇活動時間",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 ),
#                 footer=BoxComponent(
#                   layout= "horizontal",
#                   contents= [
#                     ButtonComponent(
#                       DatetimePickerAction(
#                         label= "點我選時間",
#                         data="Activity_time",
#                         mode= "datetime",
#                         initial= "2020-05-26T15:25",
#                         max= "2021-05-26T15:25",
#                         min= "2019-05-26T15:25"
#                       )
#                     )
#                   ]
#                 )
#             )
   
#         message = FlexSendMessage(alt_text = "請挑選活動時間", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )


# #地點 (line.me/R/nv/location)(by Lipet)
# if text == "活動地點":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請選擇活動地點",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 ),
#                 footer=BoxComponent(
#                   layout= "horizontal",
#                   contents= [
#                     ButtonComponent(
#                       URIAction(
#                         label= "點我選地點",
#                         uri= "https://line.me/R/nv/location"
#                       )
#                     )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請挑選活動地點", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )


# #預期人數（最低最高）(By Lipet)
# if text == "活動人數":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請填寫活動參加人數",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請填寫人數", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #預計支出(By Lipet)
# if text == "活動支出":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請填寫預計支出",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請填寫預計支出", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #報名截止日期(line 內建可用)(By Lipet)
# if text == "截止時間":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請選擇報名截止時間",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 ),
#                 footer=BoxComponent(
#                   layout= "horizontal",
#                   contents= [
#                     ButtonComponent(
#                       DatetimePickerAction(
#                         label= "點我選時間",
#                         data="Activity_time",
#                         mode= "datetime",
#                         initial= "2020-05-26T15:25",
#                         max= "2021-05-26T15:25",
#                         min= "2019-05-26T15:25"
#                       )
#                     )
#                   ]
#                 )
#             )
   
#         message = FlexSendMessage(alt_text = "請挑選報名截止時間", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )


# #活動的描述(optional)(By Lipet)
# if text == "活動描述":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請填寫詳細活動內容",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請填寫活動內容", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #活動照片(optional)(By Lipet)
# if text == "活動照片":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請提供照片網址，若無網址請先上船隻網路平台（imgurl...等）",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請提供照片網址", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #主揪姓名(By Lipet)
# if text == "主揪姓名":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請提供您的姓名或是可以辨識之暱稱",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請提供名稱", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )


# #主揪電話(Bt Lipet)
# if text == "主揪電話":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請提供可以聯絡您的電話號碼",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請提供電話", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #主揪e-mail
# if text == "主揪信箱":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請提供可以聯絡您的電子信箱",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請提供信箱", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #參加者姓名
# if text == "跟團姓名":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請提供您的姓名或是可以辨識之暱稱",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請提供名稱", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #參加者電話
# if text == "跟團電話":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請提供可以聯絡您的電話號碼",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請提供電話", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )


# #參加者e-mail
# if text == "主揪信箱":
#         bubble =BubbleContainer(
#                 direction= "ltr",
#                 body=BoxComponent(
#                   layout= "vertical",
#                   contents=[
#                   TextComponent(
#                       text="請提供可以聯絡您的電子信箱",
#                       size= "lg",
#                       align= "center",
#                       weight= "bold"
#                       )
#                   ]
#                 )
#             )
        
#         message = FlexSendMessage(alt_text = "請提供信箱", contents = bubble)
#         line_bot_api.reply_message(
#             event.reply_token,
#             message
#             )

# #開團Summary


# #報名Summary
