#請把Flexmessage集中在這邊

#活動類型（選單）(quick_reply)


#活動名稱
#push到heroku上目前還沒成功QQ (by Tina)
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
        
        message = FlexSendMessage(alt_text = f"flex 活動名稱", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#活動時間


#地點 (line.me/R/nv/location)


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


