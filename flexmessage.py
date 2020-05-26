#請把Flexmessage集中在這邊

#活動類型（選單）(by Tina)
    elif text == "活動類型":
        message = TextSendMessage(
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
        
        line_bot_api.reply_message(
            event.reply_token,
            message
            )


#活動名稱 (by Tina)
    if text == "活動名稱":
        bubble = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
                layout = "vertical",
                contents = [
                    TextComponent(text = "活動名稱", weight = "bold", size = "lg", align = "center"),
                    BoxComponent(layout = "baseline", margin = "md", contents = [
                        TextComponent(text = "請問您的活動名稱要叫什麼呢？", size = "md", flex = 0, color = "#666666")
                        ]
                                 )
                    ]
                )
            )
        
        message = FlexSendMessage(alt_text = "請填寫活動名稱", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#活動時間
if text == "活動時間":
        bubble =BubbleContainer(
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
   
        message = FlexSendMessage(alt_text = "請挑選活動時間", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )


#地點 (line.me/R/nv/location)(by Lipet)
if text == "活動地點":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請挑選活動地點", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )


#預期人數（最低最高）


#預計支出


#報名截止日期(line 內建可用)


#活動的描述(optional)


#活動照片(optional)


#主揪姓名


#主揪電話


#主揪e-mail


#參加者姓名


#參加者電話


#參加者e-mail


#開團Summary


#報名Summary


