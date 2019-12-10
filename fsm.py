from transitions.extensions import GraphMachine

from utils import *
from linebot.models import *

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def on_enter_start(self, event):
        print("I'm entering start")
        Confirm_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='start',
            text='您好！歡迎來到QQ醬><!這裡是一個提供認養寵物的平台！',
            actions=[                              
                PostbackTemplateAction(
                    label='我要領養',
                    text='我要領養',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='我要上傳',
                    text='我要上傳'
                )
            ]
        )
        )
        send_choose_message(event.source.user_id,Confirm_template)
        #self.go_back()

    def is_going_to_choose1(self, event):
        text = event.message.text
        return text.lower() == "我要領養"

    def on_enter_choose1(self, event):
        print("I'm entering choose1")
        Confirm_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='choose',
            text='請問你想要領養哪種動物？',
            actions=[                              
                PostbackTemplateAction(
                    label='狗',
                    text='狗',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='貓',
                    text='貓'
                )
            ]
        )
        )
        send_choose_message(event.source.user_id,Confirm_template)
        
        #self.go_back()

    def is_going_to_dog(self, event):
        text = event.message.text
        return text.lower() == "狗"

    def on_enter_dog(self, event):
        print("I'm entering dog")
        Confirm_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='gender',
            text='請問你想要領養哪種性別？',
            actions=[                              
                PostbackTemplateAction(
                    label='公',
                    text='公',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='母',
                    text='母'
                )
            ]
        )
        )
        send_choose_message(event.source.user_id,Confirm_template)
    
    def is_going_to_cat(self, event):
        text = event.message.text
        return text.lower() == "貓"

    def on_enter_cat(self, event):
        print("I'm entering cat")
        Confirm_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='gender',
                text='請問你想要領養哪種性別？',
                actions=[                              
                    PostbackTemplateAction(
                        label='公',
                        text='公',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='母',
                        text='母'
                    )
                ]
            )
            )
        send_choose_message(event.source.user_id,Confirm_template)
    
    def is_going_to_boy(self, event):
        text = event.message.text
        return text.lower() == "公"

    def on_enter_boy(self, event):
        print("I'm entering boy")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入您希望認養的地區，EX：，EX：彰化市、麻豆區…")
        #self.go_back()
    
    def is_going_to_girl(self, event):
        text = event.message.text
        return text.lower() == "母"

    def on_enter_girl(self, event):
        print("I'm entering girl")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入您希望認養的地區，EX：，EX：彰化市、麻豆區…")
        #self.go_back()

    def is_going_to_location(self, event):
        text = event.message.text
        return True

    def on_enter_location(self, event):
        print("I'm entering location")

        reply_token = event.reply_token
        send_text_message(reply_token, "以下為根據您的條件搜尋出來的浪浪們：")
       
        self.go_back()
