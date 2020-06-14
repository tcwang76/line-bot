from linebot.models import (
    TextSendMessage, MessageAction, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent, FillerComponent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,CarouselContainer
)
import datetime as dt
import json
# 給報名者用的
def extend(j,date,progress):
    if type(j)==str:
        if j=='attendee_name':
            j=3
        elif j=='phone':
            j=4

    return flex(j+9,date,progress)

# 給開團者用的
def flex(i,date,progress):
    if i == 1 or i == "activity_name":
        msg = activity_name(progress)
    elif i == 2 or i == "activity_date":
        msg = activity_time(progress)
    elif i == 3 or i == "location":
        msg=location(progress)
    elif i == 5 or i == "people":
        msg = people(progress)
    elif i == 8 or i == "cost":
        msg = cost(progress)
    elif i == "due_date":
        msg = due_time(date)
    elif i == 10 or i == "description":
        msg = description
    elif i == 11 or i == "photo":
        msg = photo
    elif i == "name" or i == 9 or i==12:
        msg = name(progress)
    elif i == 13 or i == "phone":
        msg = phone(progress)
    elif i == "mail" or i ==14:
        msg = mail
    elif i == "activity_type":
        msg = activity_type
    else:
        msg = TextSendMessage(text = "FlexMessage Bug 爆發中...")
    return msg

activity_type = TextSendMessage(
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
activity_type_for_attendee = TextSendMessage(
    text = "請選擇活動類型",
    quick_reply = QuickReply(
        items = [
            QuickReplyButton(
                action = PostbackAction(label = "登山踏青", data = "登山踏青",  display_text='登山踏青')
                ),
            QuickReplyButton(
                action = PostbackAction(label = "桌遊麻將", data = "桌遊麻將", display_text = "桌遊麻將")
                ),
            QuickReplyButton(
                action = PostbackAction(label = "吃吃喝喝", data = "吃吃喝喝", display_text = "吃吃喝喝")
                ),
            QuickReplyButton(
                action = PostbackAction(label = "唱歌跳舞", data = "唱歌跳舞", display_text = "唱歌跳舞")
                )
            ]))
def activity_name(progress):
    activity_name = FlexSendMessage(
        alt_text = "請填寫活動名稱", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
                layout = "vertical",
                contents = [
                    TextComponent(text = "活動名稱", weight = "bold", size = "lg", align = "center"),
                    BoxComponent(layout = "baseline", 
                                 margin = "lg", 
                                 contents = [
                                     TextComponent(text = "請問您的活動名稱要叫什麼呢？", 
                                                   size = "md", 
                                                   flex = 0, 
                                                   color = "#666666"
                                                  )
                                 ]
                                )
                ]
            ),
            #進度條的本體
            footer=BoxComponent(
                layout = "vertical",
                margin = "md",
                contents = [TextComponent(text = f"{progress[1]} / {progress[0]} ", weight = "bold", size = "md"),
                            BoxComponent(layout = "vertical",
                                         margin = "md",
                                         contents = [
                                             BoxComponent(layout = "vertical", 
                                                          contents = [FillerComponent()]
                                                         )
                                         ],
                                         width = f"{int(progress[1] / progress[0] * 100 + 0.5 )}%",
                                         background_color = "#3DE1D0",
                                         height = "6px"
                                        )
                           ]
            )
            #進度條的本體/
        )
    )
    return activity_name

def activity_time(progress):
    activity_time = FlexSendMessage(
        alt_text = "請挑選活動時間", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
                layout = "vertical",
                contents =[
                    TextComponent(
                        text = "請選擇活動時間",
                        size = "lg",
                        align = "center",
                        weight = "bold"
                    )
                ]
            ),
            footer = BoxComponent(
              layout = "vertical",
              contents = [
                  BoxComponent(layout = "vertical",
                                 margin = "md",
                                 contents = [TextComponent(text = f"{progress[2]} / {progress[0]} ", weight = "bold", size = "md"),
                                             BoxComponent(layout = "vertical",
                                                          margin = "md",
                                                          contents = [
                                                              BoxComponent(layout = "vertical", 
                                                                           contents = [FillerComponent()]
                                                                          )
                                                          ],
                                                          width = f"{int(progress[2] / progress[0] * 100 + 0.5 )}%",
                                                          background_color = "#3DE1D0",
                                                          height = "6px"
                                                         )

                                            ]
                              ),
                  BoxComponent(layout = "vertical",
                                 margin = "md",
                                 contents = [
                                     ButtonComponent(
                                         DatetimePickerAction(
                                             label = "點我選時間",
                                             data = "Activity_time",
                                             mode = "datetime",
                                             min = f"{'T'.join(str(dt.datetime.today()+dt.timedelta(hours=8))[:16].split())}"
                                         ),
                                         height = "sm",
                                         margin = "none",
                                         style = "primary",
                                         color = "#A7D5E1",
                                         gravity = "bottom"
                                     )
                                 ]
                              )          
              ]
            )
        )
    )
    return activity_time

def location(progress):
    location = FlexSendMessage(
        alt_text = "請挑選活動地點", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
              layout = "vertical",
              contents = [
              TextComponent(
                  text = "請選擇活動地點",
                  size = "lg",
                  align = "center",
                  weight = "bold"
                  )
              ]
            ),
            #進度條的本體
            footer = BoxComponent(
                layout = "vertical",
                margin = "md",
                contents = [BoxComponent(layout = "vertical",
                                 margin = "md",
                                 contents = [TextComponent(text = f"{progress[3]} / {progress[0]} ", 
                                                           weight = "bold", 
                                                           size = "md"),
                                             BoxComponent(layout = "vertical",
                                                          margin = "md",
                                                          contents = [
                                                              BoxComponent(layout = "vertical", 
                                                                           contents = [FillerComponent()]
                                                                          )
                                                          ],
                                                          width = f"{int(progress[3] / progress[0] * 100 + 0.5 )}%",
                                                          background_color = "#3DE1D0",
                                                          height = "6px"
                                                         )

                                            ]
                              ),
            #進度條的本體/
            BoxComponent(
              layout = "horizontal",
                margin = "md",
              contents = [
                ButtonComponent(
                    URIAction(
                        label = "點我選地點",
                        uri = "https://line.me/R/nv/location"
                    ),
                    height = "sm",
                    margin = "none",
                    style = "primary",
                    color = "#A7D5E1",
                    gravity = "bottom"
                )
              ]
            )
                           ]
            )
        )
    )
    return location

def people(progress):
    people = FlexSendMessage(
        alt_text = "請填寫人數", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
              layout = "vertical",
              contents =[
              TextComponent(
                  text = "請填寫活動參加人數",
                  size = "lg",
                  align = "center",
                  weight = "bold"
                  )
              ]
            ),
            #進度條的本體
            footer=BoxComponent(
                layout = "vertical",
                margin = "md",
                contents = [TextComponent(text = f"{progress[4]} / {progress[0]} ", weight = "bold", size = "md"),
                            BoxComponent(layout = "vertical",
                                         margin = "md",
                                         contents = [
                                             BoxComponent(layout = "vertical", 
                                                          contents = [FillerComponent()]
                                                         )
                                         ],
                                         width = f"{int(progress[4] / progress[0] * 100 + 0.5 )}%",
                                         background_color = "#3DE1D0",
                                         height = "6px"
                                        )
                           ]
            )
            #進度條的本體/
        )
    )
    return people
def cost(progress):
    cost = FlexSendMessage(
        alt_text = "請填寫預計支出", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
              layout = "vertical",
              contents = [
              TextComponent(
                  text = "請填寫預計支出",
                  size = "lg",
                  align = "center",
                  weight = "bold"
                  )
              ]
            ),
            #進度條的本體
            footer=BoxComponent(
                layout = "vertical",
                margin = "md",
                contents = [TextComponent(text = f"{progress[5]} / {progress[0]} ", weight = "bold", size = "md"),
                            BoxComponent(layout = "vertical",
                                         margin = "md",
                                         contents = [
                                             BoxComponent(layout = "vertical", 
                                                          contents = [FillerComponent()]
                                                         )
                                         ],
                                         width = f"{int(progress[5] / progress[0] * 100 + 0.5 )}%",
                                         background_color = "#3DE1D0",
                                         height = "6px"
                                        )
                           ]
            )
            #進度條的本體/
        )
    )
    return cost

def due_time(date):
    due = FlexSendMessage(
        alt_text = "請挑選截止日期", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
              layout = "vertical",
              contents = [
              TextComponent(
                  text = "請選擇報名截止日期",
                  size = "lg",
                  align = "center",
                  weight = "bold"
                  )
              ]
            ),
            #進度條的本體
        footer=
        #進度條的本體/
            BoxComponent(
                layout = "horizontal",
                contents = [ButtonComponent(
                    DatetimePickerAction(
                        label = "點我選時間",
                        data = "Due_time",
                        mode = "date",
                        max = str(date[3])
                    ),
                    height = "sm",
                    margin = "none",
                    style = "primary",
                    color = "#A7D5E1",
                    gravity = "bottom"
                )
              ]
            )
        )
    )
    return due

description = FlexSendMessage(
    alt_text = "請填寫活動內容", 
    contents = BubbleContainer(
        direction = "ltr",
        body = BoxComponent(
          layout = "vertical",
          contents = [
          TextComponent(
              text = "請填寫詳細活動內容",
              size = "lg",
              align = "center",
              weight = "bold"
              )
          ]
        )
    )
)

photo = FlexSendMessage(
    alt_text = "請提供照片網址", 
    contents = BubbleContainer(
        direction = "ltr",
        body = BoxComponent(
          layout = "vertical",
          contents = [
          TextComponent(
              text = "請傳送一張照片",
              size = "md",
              wrap = True,
              align = "center",
              weight = "bold"
              )
          ]
        )
    )
)
def name(progress):
    name = FlexSendMessage(
        alt_text = "請提供名稱", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
              layout = "vertical",
              contents = [
              TextComponent(
                  text = "請提供您的姓名或是可以辨識之暱稱",
                  size = "md",
                  wrap = True,
                  align = "center",
                  weight = "bold"
                  )
              ]
            ),
            #進度條的本體
            footer=BoxComponent(
                layout = "vertical",
                margin = "md",
                contents = [TextComponent(text = f"{progress[6]} / {progress[0]} ", weight = "bold", size = "md"),
                            BoxComponent(layout = "vertical",
                                         margin = "md",
                                         contents = [
                                             BoxComponent(layout = "vertical", 
                                                          contents = [FillerComponent()]
                                                         )
                                         ],
                                         width = f"{int(progress[6] / progress[0] * 100 + 0.5 )}%",
                                         background_color = "#3DE1D0",
                                         height = "6px"
                                        )
                           ]
            )
            #進度條的本體/
        )
    )
    return name

def phone(progress):
    phone = FlexSendMessage(
        alt_text = "請提供電話", 
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
              layout = "vertical",
              contents = [
              TextComponent(
                  text = "請提供可以聯絡您的電話號碼",
                  size = "lg",
                  align = "center",
                  weight = "bold"
                  )
              ]
            ),
            #進度條的本體
            footer=BoxComponent(
                layout = "vertical",
                margin = "md",
                contents = [TextComponent(text = f"{progress[7]} / {progress[0]} ", weight = "bold", size = "md"),
                            BoxComponent(layout = "vertical",
                                         margin = "md",
                                         contents = [
                                             BoxComponent(layout = "vertical", 
                                                          contents = [FillerComponent()]
                                                         )
                                         ],
                                         width = f"{int(progress[7] / progress[0] * 100 + 0.5 )}%",
                                         background_color = "#3DE1D0",
                                         height = "6px"
                                        )
                           ]
            )
            #進度條的本體/
        )
    )
    return phone

mail = FlexSendMessage(
    alt_text = "請提供信箱", 
    contents = BubbleContainer(
        direction = "ltr",
        body = BoxComponent(
          layout = "vertical",
          contents = [
          TextComponent(
              text = "請提供可以聯絡您的電子信箱",
              size = "lg",
              align = "center",
              weight = "bold"
              )
          ]
        )
    )
)
def summary(data):
    if data[12]=='無':
        act=None
        col="#444444"
    else:
        act=URIAction(uri = f"{data[12]}")
        col="#229C8F"
    sumer = FlexSendMessage(
        alt_text = "請確認開團資訊",
        contents = BubbleContainer(
            direction = "ltr",
            header = BoxComponent(
              layout = "vertical",
              contents = [
              TextComponent(
                  text = "請確認開團資訊",
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
                                text = f"活動類型 {data[1]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "activity_type"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動名稱 {data[2]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "activity_name"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動時間 {data[3]} {str(data[4])[:5]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "activity_date"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動地點 {data[5]}",
                                size = "md",
                                flex = 10,
                                wrap = True,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "location"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動人數 {data[8]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "people"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動費用 {data[9]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "cost"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"報名截止日 {data[10]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "due_date"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動敘述 {data[11]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "description"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"活動照片 {data[12]}",
                                size = "md",
                                flex = 10,
                                align = "start",
                                action= act,
                                wrap = True,
                                color = f"{col}"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "photo"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"主揪姓名 {data[13]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ), 
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "name"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"主揪電話 {data[14]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "phone"
                                )
                            )
                        ]
                    )
                ]
            ),
            footer = BoxComponent(
                layout = "horizontal",
                contents = [
                    ButtonComponent(
                        style = "link",
                        height = "sm",
                        margin = "none",
                        color = "#229C8F",
                        gravity = "bottom",
                        action = MessageAction(
                            label = "確認開團",
                            text = "確認開團"
                        )
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style = "link",
                        height = "sm",
                        margin = "none",
                        color = "#229C8F",
                        gravity = "bottom",
                        action = MessageAction(
                            label = "取消開團",
                            text = "取消"
                        )
                    )
                ]
            )
        )
    )
    return sumer


def summary_for_attend(data):
    sumer = FlexSendMessage(
        alt_text = "請確認報名資訊",
        contents = BubbleContainer(
            direction = "ltr",
            body = BoxComponent(
                layout = "vertical",
                contents = [
                    BoxComponent(
                        layout = "vertical",
                        contents = [
                            TextComponent(
                                text = "請確認報名資訊",
                                weight = "bold",
                                size = "xl",
                                align = "start",
                                color = "#000000"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",
                                margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "vertical",
                        contents = [
                            TextComponent(
                                text = f"活動名稱 {data[2]}",
                                size = "lg",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",
                                margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"姓名 {data[3]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",
                                margin = "lg"
                            )
                        ]
                    ), 
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "attendee_name"
                                )
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = f"電話 {data[4]}",
                                size = "md",
                                flex = 10,
                                align = "start"
                            ),
                            SeparatorComponent(
                                color = "#FFFFFF",
                                margin = "lg"
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        contents = [
                            TextComponent(
                                text = "修改",
                                size = "md",
                                align = "end",
                                gravity = "top",
                                weight = "bold",
                                action = MessageAction(
                                    text = "phone"
                                )
                            )
                        ]
                    )
                ]
            ),
            footer = BoxComponent(
                layout = "horizontal",
                contents = [
                    ButtonComponent(
                        style = "link",
                        height = "sm",
                        margin = "none",
                        color = "#229C8F",
                        gravity = "bottom",
                        action = MessageAction(
                            label = "確認報名",
                            text = "確認報名"
                        )
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style = "link",
                        height = "sm",
                        margin = "none",
                        color = "#229C8F",
                        gravity = "bottom",
                        action = MessageAction(
                            label = "取消報名",
                            text = "取消"
                        )
                    )
                ]
            )
        )
    )
    return sumer


#詳細資訊summary
def MoreInfoSummary(data):
    if "https://i.imgur.com/" not in data[12]:
        act=None
        col="#444444"
        hero= None
    else:
        act=URIAction(uri = f"{data[12]}")
        col="#229C8F"
        hero=ImageComponent(
            size = "full",
            aspectMode = "cover",
            margin ="none",
            url = f"{data[12]}"
            )
        
    sumer = FlexSendMessage(
        alt_text = "詳細活動資訊",
        contents = BubbleContainer(
            direction = "ltr",
            margin= "none",
            header = BoxComponent(
                layout = "vertical",
                contents = [
                    TextComponent(
                        text = f"{data[2]}\n活動資訊如下",
                        weight = "bold",
                        size = "lg",
                        align = "start",
                        color = "#000000"
                    )
                ]
            ),
            hero=hero,
            body = BoxComponent(
                  layout = "vertical",
                  contents = [
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動類型 {data[1]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start",
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動名稱 {data[2]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動時間 {data[3]} {str(data[4])[:5]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動地點 {data[5]}",
                                  size = "md",
                                  flex = 10,
                                  wrap = True,
                                  align = "start"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動人數 {data[8]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動費用 {data[9]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"報名截止日 {data[10]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動敘述 {data[11]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"活動照片 {data[12]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start",
                                  action=act,
                                  color = f"{col}"
                              )
                          ]
                      ),
                      BoxComponent(
                          layout = "horizontal",
                          contents = [
                              TextComponent(
                                  text = f"主揪姓名 {data[13]}",
                                  size = "md",
                                  flex = 10,
                                  align = "start"
                              )
                          ]
                      )
                  ]
              ),
              footer = BoxComponent(
                  layout = "vertical",
                  contents = [
                      ButtonComponent(
                          style = "link",
                          height = "sm",
                          margin = "none",
                          color = "#229C8F",
                          gravity = "bottom",
                          action = PostbackAction(
                              label = "立即報名",
                              data = f"立即報名_{data[0]}_{data[2]}_{data[3]}",
                              display_text = f"我要報名 {data[2]}"
                          )
                      )
                  ]
              )
        )
    )
    return sumer

#我的開團列表
def GroupLst(data,_ = 0): 
    if _==0:
        ii=0
    else:
        ii=_-8

    if data:
        
        group_lst = []

        #row [activity_no, activity_type, activity_name, activity_date, activity_time, activity_title, ...]
        for i in range(_,len(data)):
            print("i = ",i)
            activity =f'''{{
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {{
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {{
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                        "flex": 1,
                        "align": "start",
                        "size": "sm"
                     }}
                     ]
                }},
                {{
                  "type": "text",
                  "text": "{data[i][2]}",
                  "flex": 9,
                  "size": "md",
                  "align" :  "start",
                  "color" : "#227C9D",
                  "weight" :  "regular",
                  "margin": "sm",
                  "action": {{
                  "type": "postback",
                  "data": "開團資訊 {data[i][0]}"
                  }}
                    
                }}
              ]
            }}'''

#             activity = BoxComponent(
#                 layout = "horizontal",
#                 flex = 1,
#                 contents = [
#                     BoxComponent(
#                         layout =  "horizontal",
#                         contents = [ 
#                             ImageComponent(
#                                 url =  "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
#                                 size =  "sm",
#                                 flex = 1
                                
#                             ),
#                             TextComponent(
#                                 text =  f'{row[2]}', #activity_name
#                                 align =  "start",
#                                 size = "md",
#                                 color = "#227C9D",
#                                 weight =  "regular",
#                                 margin= "sm",
#                                 flex = 9,
#                                 action = PostbackAction(
#                                     data = f"開團資訊 {row[0]}"  #activity_no
#                                     )
#                                 )
#                             ]
#                         )
#                     ]
#                 )
            group_lst.append(json.loads(activity))

            if len(group_lst) > 7:
                break
            
        index = BubbleContainer(
            size = "kilo",
            direction = "ltr",
            header = BoxComponent(
            layout = "horizontal",
            contents = [ 
                TextComponent(
                    text =  "我的開團列表",
                    size =  "lg",
                    weight =  "bold",
                    color =  "#AAAAAA"
                )
            ]
            ),
            body = BoxComponent(
                layout = "vertical",
                spacing =  "md",
                contents = group_lst
            ),
            footer = BoxComponent(
                layout = "horizontal",
                contents = [ 
                    ButtonComponent(
                        action = PostbackAction(
                            label =  "上一頁",
                            data =  f"backward_group_{ii}"
                        ),
                        height = "sm",
                        style = "primary",
                        color = "#A7D5E1",
                        gravity = "bottom"
                    ),
                    SeparatorComponent(
                        margin = "sm",
                        color = "#FFFFFF"
                    ),
                    ButtonComponent(          
                        action = PostbackAction(
                        label = "下一頁",
                        data =  f"forward_group_{i+1}"
                        ),
                        height = "sm",
                        style = "primary",
                        color = "#A7D5E1",
                        gravity = "bottom"
                    )
                ]
            )
        )

    msg = FlexSendMessage(
        alt_text = "我的開團",
        contents = index
        )
    return msg

#開團資訊
def MyGroupInfo(data):
    if data:
        if "https://i.imgur.com/" not in data[12]:
            link="https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg"
        else:
            link=f"{data[12]}"
        bubble = BubbleContainer(
            size = "kilo",
            direction = "ltr", 
            hero = ImageComponent(
                size = "full",
                aspectMode = "cover",
                aspectRatio = "320:213",
                url = f"{link}"
                ),
            body = BoxComponent(
                layout = "vertical",
                contents = [
                    TextComponent(
                        text = f"{data[2]}",
                        weight = "bold",
                        size = "md",
                        wrap = True
                        ),
                    BoxComponent(
                        layout = "vertical",
                        contents = [
                            BoxComponent(
                                layout = "vertical",
                                spacing = "sm",
                                contents = [
                                    TextComponent(
                                        text = f"地點 {data[5]}",
                                        wrap = True,
                                        size = "sm",
                                        flex = 5,
                                        ),
                                    TextComponent(
                                        text = f"時間 {data[3]} {str(data[4])[:5]}",
                                        size = "sm",
                                        ),
                                    TextComponent(
                                        text = f"費用 {data[9]}",
                                        size = "sm",
                                        ),
                                    TextComponent(
                                        text = f"已報名人數 {data[15]}/{data[8]}",
                                        size = "sm",
                                        ),
                                    TextComponent(
                                        text = f"狀態 {data[16]}",
                                        size = "sm",
                                        )
                                    ]
                                )
                            ]
                        )
                    ],
                paddingAll = "13px",
                spacing = "md",
                ),
            footer = BoxComponent(
                layout = "horizontal",
                contents = [
                    ButtonComponent(
                        style = "primary",
                        action = PostbackAction(
                            label = "報名者資訊",
                            data = f"報名者資訊 {data[0]}",  #activity_no
                            display_text = "查看報名者資訊"
                            ),
                        height = "sm",
                        margin = "none",
                        gravity = "bottom",
                        color = "#A7D5E1"
                        ),
                    SeparatorComponent(
                        margin = "sm",
                        color = "#FFFFFF"
                        ),
                    ButtonComponent(
                        style = "primary",
                        action = PostbackAction(
                            label = "結束報名",
                            data = f"結束報名 {data[0]}",  #activity_no
                            display_text = "結束報名"
                            ),
                        height = "sm",
                        margin = "none",
                        gravity = "bottom",
                        color = "#A7D5E1"
                        )
                    ]
                    )
                )
    else:
        bubble = BubbleContainer(
            direction = "ltr", 
            body = BoxComponent(
                size="xs",
                layout = "vertical",
                spacing =  "md",
                contents = [
                    TextComponent(
                        text =  "目前無開團資料",
                        size =  "lg",
                        weight =  "bold",
                        color =  "#AAAAAA"
                    )
                ]
            )
        )
    
    msg = FlexSendMessage(
        alt_text = "我的開團資訊",
        contents = bubble
            )
    return msg

#我的報名列表
def registration_list(data,i=0):
    if i==0:
        ii=0
    else:
        ii=i-8
        
    if data:
        tem=[]
        for _ in range(i, len(data)):
            print(data[_])
            te = BoxComponent(
                layout = "horizontal",
                contents = [
                    BoxComponent(
                        layout = "horizontal",
                        flex = 1,
                        contents = [ 
                            BoxComponent(
                                layout =  "baseline",
                                flex =  1,
                                contents = [ 
                                    IconComponent(
                                        url =  "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        size =  "md"
                                    )
                                ]
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        flex =  9,
                        contents = [ 
                            TextComponent(
                                text =  f"{data[_][2]}",
                                align =  "start",
                                size = "md",
                                color = "#227C9D",
                                weight =  "regular",
                                margin= "sm",
                                action = PostbackAction(
                                    label = f"{data[_][2]}查報名",
                                    data = f"{data[_][1]}_查報名"
                                )    
                            )
                        ]
                    )
                ]
            )
            tem.append(te)
            if len(tem)>7:
                break

        bubble = BubbleContainer(
            size = "kilo",
            direction = "ltr",
            header = BoxComponent(
            layout = "vertical",
            contents = [ 
                TextComponent(
                    text =  "我的報名列表",
                    size =  "lg",
                    weight =  "bold",
                    color =  "#AAAAAA"
                ),
                TextComponent(
                    text =  "（依照活動日期排列）",
                    size =  "md",
                    weight =  "regular",
                    color =  "#AAAAAA"
                )
            ]
            ),
            body = BoxComponent(
                layout = "vertical",
                spacing = "md",
                contents = tem
            ),
            footer = BoxComponent(
                layout = "horizontal",
                contents = [ 
                    ButtonComponent(
                        action = PostbackAction(
                            label =  "上一頁",
                            data =  f"backward_registration_{ii}"
                        ),
                        height = "sm",
                        style = "primary",
                        color = "#A7D5E1",
                        gravity = "bottom"
                    ),
                    SeparatorComponent(
                        margin = "sm",
                        color = "#FFFFFF"
                    ),
                    ButtonComponent(          
                        action = PostbackAction(
                        label = "下一頁",
                        data =  f"forward_registration_{_+1}"
                        ),
                        height = "sm",
                        style = "primary",
                        color = "#A7D5E1",
                        gravity = "bottom"
                    )
                ]
            )
        )

    else:
        bubble = BubbleContainer(
            direction = "ltr", 
            body = BoxComponent(
                size="xs",
                layout = "vertical",
                spacing =  "md",
                contents = [
                    TextComponent(
                        text =  "目前無報名資料",
                        size =  "lg",
                        weight =  "bold",
                        color =  "#AAAAAA"
                    )
                ]
            )
        )

    msg_regis = FlexSendMessage(
        alt_text = "報名列表",
        contents = bubble
    )

    return msg_regis

 #活動資訊與報名資訊carousel
def carousel_registration(data,data2):
    if "https://i.imgur.com/" not in data[12]:
        link="https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg"
    else:
        link=f"{data[12]}"
    group_info = BubbleContainer(
        size = "kilo",
        direction = "ltr",
        hero = ImageComponent(
            size = "full",
            aspectRatio = "16:9",
            aspectMode = "cover",
            url = f"{link}"
        ),
        body = BoxComponent(
            layout = "vertical",
            contents = [
                TextComponent(
                    text = f"活動詳細資訊",
                    weight = "bold",
                    size = "md",
                    wrap = True
                ),
                TextComponent(
                    text = f"{data[2]}",
                    weight = "bold",
                    size = "md",
                    wrap = True
                ),
                BoxComponent(
                    layout = "vertical",
                    contents = [
                        BoxComponent(
                            layout = "vertical",
                            spacing = "sm",
                            contents = [
                                TextComponent(
                                    text = f"地點 {data[5]}",
                                    wrap = True,
                                    size = "sm",
                                    flex = 5
                                ),
                                TextComponent(
                                    text = f"時間 {data[3]} {str(data[4])[:5]}",
                                    size = "sm"
                                ),
                                TextComponent(
                                    text = f"費用 {data[9]}",
                                    size = "sm"
                                ),
                                TextComponent(
                                    text = f"主揪 {data[13]}",
                                    size = "sm"
                                ),
                                TextComponent(
                                    text = f"主揪電話 {data[14]}",
                                    size = "sm"
                                )
                            ]
                        )
                    ]
                )
            ],
        paddingAll = "13px",
        spacing = "md"
        )
    )

    bubbles = [group_info]

    for row in data2:
        temp = BubbleContainer(
            size = "kilo",
            direction = "ltr",
            header = BoxComponent(
                layout = "vertical",
                contents = [
                    TextComponent(
                        text = "報名資訊",
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
                        layout = "vertical",
                        contents = [
                            BoxComponent(
                                layout = "vertical",
                                spacing = "sm",
                                contents = [
                                    TextComponent(
                                        text = f"活動名稱 {row[2]}",
                                        size = "sm"
                                    ),
                                    TextComponent(
                                        text = f"姓名 {row[3]}",
                                        size = "sm"
                                    ),
                                    TextComponent(
                                        text = f"電話 {row[4]}",
                                        size = "sm"
                                    )
                                ]
                            )
                        ]    
                    )
                ]
            ),
            footer = BoxComponent(
                layout = "horizontal",
                contents = [
                    ButtonComponent(
                        action = PostbackAction(
                            label = '取消報名',
                            display_text = "取消報名",
                            data = f"{row[0]}_{row[1]}_取消報名"
                        ),
                        height = "sm",
                        style = "primary",
                        color = "#A7D5E1",
                        gravity = "bottom"
                    )
                ]    
            )     
        )
        bubbles.append(temp)

    info_carousel = FlexSendMessage(
        alt_text = "活動資訊與報名資訊",
        contents = CarouselContainer(
            contents = bubbles
        )
    )
    return info_carousel


#尚需加入活動index bubble
def carousel(data,i=0): 
    if i==0:
        ii=0
    else:
        ii=i-8
        

    if data:
        tem=[]
        for _ in range(i,len(data)):
            print("_",_)
            te=BoxComponent(
                layout = "horizontal",
                contents = [
                    BoxComponent(
                        layout = "horizontal",
                        flex =  1,
                        contents = [ 
                            BoxComponent(
                                layout =  "baseline",
                                flex =  1,
                                contents = [ 
                                    IconComponent(
                                        url =  "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        size =  "sm"
                                    )
                                ]
                            )
                        ]
                    ),
                    BoxComponent(
                        layout = "horizontal",
                        flex =  9,
                        contents = [ 
                            TextComponent(
                                text =  f"{data[_][2]}",
                                align =  "start",
                                weight =  "regular",
                                color = "#227C9D",
                                action = PostbackAction(
                                        displat_text = "詳細資訊",
                                        data = f"{data[_][0]}_詳細資訊"
                                        )
                            )
                        ]
                    )
                ]
            )
            tem.append(te)

            if len(tem)>8:
                break
        index=BubbleContainer(
            size = "kilo",
            direction = "ltr",
            header = BoxComponent(
            layout = "horizontal",
            contents = [ 
                TextComponent(
                    text =  "揪團列表",
                    size =  "lg",
                    weight =  "bold",
                    color =  "#AAAAAA"
                )
            ]
            ),
            body = BoxComponent(
                layout = "vertical",
                spacing =  "md",
                contents = tem
            ),
            footer=BoxComponent(
                layout = "horizontal",
                contents = [ 
                    ButtonComponent(
                        action = PostbackAction(
                            label =  "上一頁",
                            data =  f"backward_activity_{data[0][1]}_{ii}"
                        ),
                        height = "sm",
                        margin = "none",
                        color = "#229C8F",
                        gravity = "bottom",
                        style = "link"
                    ),
                    SeparatorComponent(
                    ),
                    ButtonComponent(          
                        action = PostbackAction(
                        label = "下一頁",
                        data =  f"forward_activity_{data[0][1]}_{_+1}"
                        ),
                        height = "sm",
                        margin = "none",
                        color = "#229C8F",
                        gravity = "bottom",
                        style = "link"
                    )
                ]
            )
        )
        bubbles = [index]
        for _ in range(i,len(data)):
            
            if "https://i.imgur.com/" not in data[_][12]:
                link="https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg"
            else:
                link=f"{data[_][12]}"
            print(f"data[{_}][12] = ",data[_][12],"link = ",link)
            temp = BubbleContainer(
                        size = "kilo",
                        direction = "ltr", 
                        hero = ImageComponent(
                            size = "full",
                            aspectMode = "cover",
                            aspectRatio = "320:213",
                            url = f"{link}"
                            ),
                        body = BoxComponent(
                            layout = "vertical",
                            contents = [
                                TextComponent(
                                    text = f"{data[_][2]}",
                                    weight = "bold",
                                    size = "md",
                                    wrap = True
                                    ),
                                BoxComponent(
                                    layout = "vertical",
                                    contents = [
                                        BoxComponent(
                                            layout = "vertical",
                                            spacing = "sm",
                                            contents = [
                                                TextComponent(
                                                    text = f"地點 {data[_][5]}",
                                                    wrap = True,
                                                    color = "#8c8c8c",
                                                    size = "xs",
                                                    flex = 5,
                                                    ),
                                                TextComponent(
                                                    text = f"時間 {data[_][3]} {str(data[_][4])[:5]}",
                                                    color = "#8c8c8c",
                                                    size = "xs",
                                                    ),
                                                TextComponent(
                                                    text = f"費用 {data[_][9]}",
                                                    color = "#8c8c8c",
                                                    size = "xs",
                                                    ),
                                                ]
                                            )
                                        ]
                                    )
                                ],
                            paddingAll = "13px",
                            spacing = "md",
                            ),
                        footer = BoxComponent(
                            layout = "horizontal",
                            contents = [
                                ButtonComponent(
                                    style = "link",
                                    action = PostbackAction(
                                        label = "立即報名",
                                        data = f"立即報名_{data[_][0]}_{data[_][2]}_{data[_][3]}",
                                        display_text=f"我要報名{data[_][2]}"
                                    ),
                                    height = "sm",
                                    margin = "none",
                                    color = "#229C8F",
                                    gravity = "bottom"
                                    ),
                                SeparatorComponent(),
                                ButtonComponent(
                                    style = "link",
                                    action = PostbackAction(
                                        label = "詳細資訊",
                                        data = f"{data[_][0]}_詳細資訊",
                                        display_text = f"請告訴我這個活動詳細資訊"
                                        ),
                                    height = "sm",
                                    margin = "none",
                                    color = "#229C8F",
                                    gravity = "bottom"
                                    )
                                ]
                            )
                        )
            bubbles.append(temp)
            if len(bubbles) > 9:
                break
    else:
        bubbles=[BubbleContainer(
            direction = "ltr", 
            body = BoxComponent(
                size="xs",
                layout = "vertical",
                spacing =  "md",
                contents = [
                    TextComponent(
                        text =  "目前無資料",
                        size =  "lg",
                        weight =  "bold",
                        color =  "#AAAAAA"
                    )
                ]
            )
        )]

    msg_carousel = FlexSendMessage(
        alt_text = "可報名活動",
        contents = CarouselContainer(
            contents = bubbles
            )
        )
    return msg_carousel

#下一頁、上一頁的index carousel



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
