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


#預期人數（最低最高）(By Lipet)
if text == "活動人數":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請填寫人數", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#預計支出(By Lipet)
if text == "活動支出":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請填寫預計支出", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#報名截止日期(line 內建可用)(By Lipet)
if text == "截止時間":
        bubble =BubbleContainer(
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
   
        message = FlexSendMessage(alt_text = "請挑選報名截止時間", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )


#活動的描述(optional)(By Lipet)
if text == "活動描述":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請填寫活動內容", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#活動照片(optional)(By Lipet)
if text == "活動照片":
        bubble =BubbleContainer(
                direction= "ltr",
                body=BoxComponent(
                  layout= "vertical",
                  contents=[
                  TextComponent(
                      text="請提供照片網址，若無網址請先上船隻網路平台（imgurl...等）",
                      size= "lg",
                      align= "center",
                      weight= "bold"
                      )
                  ]
                )
            )
        
        message = FlexSendMessage(alt_text = "請提供照片網址", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#主揪姓名(By Lipet)
if text == "主揪姓名":
        bubble =BubbleContainer(
                direction= "ltr",
                body=BoxComponent(
                  layout= "vertical",
                  contents=[
                  TextComponent(
                      text="請提供您的姓名或是可以辨識之暱稱",
                      size= "lg",
                      align= "center",
                      weight= "bold"
                      )
                  ]
                )
            )
        
        message = FlexSendMessage(alt_text = "請提供名稱", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )


#主揪電話(Bt Lipet)
if text == "主揪電話":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請提供電話", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#主揪e-mail
if text == "主揪信箱":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請提供信箱", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#參加者姓名
if text == "跟團姓名":
        bubble =BubbleContainer(
                direction= "ltr",
                body=BoxComponent(
                  layout= "vertical",
                  contents=[
                  TextComponent(
                      text="請提供您的姓名或是可以辨識之暱稱",
                      size= "lg",
                      align= "center",
                      weight= "bold"
                      )
                  ]
                )
            )
        
        message = FlexSendMessage(alt_text = "請提供名稱", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#參加者電話
if text == "跟團電話":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請提供電話", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )


#參加者e-mail
if text == "主揪信箱":
        bubble =BubbleContainer(
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
        
        message = FlexSendMessage(alt_text = "請提供信箱", contents = bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
            )

#開團Summary
{
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "請確認開團資訊",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#000000"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "活動類型",
              "align": "start",
              "action": {
                "type": "postback",
                "label": "activity_type",
                "text": "activity_type",
                "data": "activity_type"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "Input"
              },
              "margin": "none",
              "height": "sm"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "活動名稱",
              "action": {
                "type": "postback",
                "label": "activity_name",
                "text": "activity_name",
                "data": "activity_name"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "Input"
              },
              "margin": "none",
              "height": "sm"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "活動時間",
              "action": {
                "type": "postback",
                "label": "activity_time",
                "text": "activity_time",
                "data": "activity_time"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "活動地點",
              "action": {
                "type": "postback",
                "label": "location",
                "text": "location",
                "data": "location"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "預期人數(最低/最高)",
              "action": {
                "type": "postback",
                "label": "people",
                "text": "people",
                "data": "people"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "預計支出",
              "action": {
                "type": "postback",
                "label": "cost",
                "text": "cost",
                "data": "cost"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "報名截止日期",
              "action": {
                "type": "postback",
                "label": "due_time",
                "text": "due_time",
                "data": "due_time"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "活動敘述(optional)",
              "action": {
                "type": "postback",
                "label": "description",
                "text": "description",
                "data": "description"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "活動照片(optional)",
              "action": {
                "type": "postback",
                "label": "photo",
                "text": "photo",
                "data": "photo"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "您的姓名(報名完成後提供給團員)",
              "action": {
                "type": "postback",
                "label": "your_name",
                "text": "your_name",
                "data": "your_name"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "您的電話(報名完成後提供給團員)",
              "action": {
                "type": "postback",
                "label": "your_phone",
                "text": "your_phone",
                "data": "your_phone"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "您的email(報名完成後提供給團員)",
              "action": {
                "type": "postback",
                "label": "your_mail",
                "text": "your_mail",
                "data": "your_mail"
              }
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "更改",
                "data": "使用者輸入"
              },
              "gravity": "top"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "確認",
            "text": "確認"
          },
          "margin": "md"
        }
      ]
    }
  }
}

#報名Summary


