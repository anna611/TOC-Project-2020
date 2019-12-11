from transitions.extensions import GraphMachine
from crawler_test import *
from utils import *
from linebot.models import *

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    def is_going_to_fsm(self,event):
        text = event.message.text
        return text.lower() == "fsm"
    def on_enter_fsm(self,event):   
        send_img(event.source.user_id,"https://qqhiiiiiii.herokuapp.com/show-fsm")
        self.go_back()
    def is_going_to_start(self, event):
        text = event.message.text
        if text.lower() == "start" or text.lower() == "menu":
            return True


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
                    label='fsm',
                    text='fsm'
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
        global a
        a = 1
        global index
        index = 0
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url= crawler_img(index,a),
                title='這是搜尋出來的浪浪',
                text='點擊更多資訊可以得到更多浪浪的資訊喔！'+'\n'+'也可以下載浪浪的照片><',
                actions=[
                    MessageTemplateAction(
                        label='下載圖片',
                        text='下載圖片'
                    ),
                    URITemplateAction(
                        label='更多資訊',
                        uri= crawler_url(index,a)
                    )
                ]
            )
        ]
        )
        )
        send_choose_message(event.source.user_id,Carousel_template)
    
    def is_going_to_cat(self, event):
        text = event.message.text
        return text.lower() == "貓"

    def on_enter_cat(self, event):
        print("I'm entering cat")
        global a
        a = 2
        global index
        index = 0
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url= crawler_img(index,a),
                title='這是搜尋出來的浪浪',
                text='點擊更多資訊可以得到更多浪浪的資訊喔！'+'\n'+'也可以下載浪浪的照片><',
                actions=[
                    MessageTemplateAction(
                        label='下載圖片',
                        text='下載圖片'
                    ),
                    URITemplateAction(
                        label='更多資訊',
                        uri= crawler_url(index,a)
                    )
                ]
            )
        ]
        )
        )
        send_choose_message(event.source.user_id,Carousel_template)
    
    def is_going_to_pic(self,event):
        text = event.message.text
        return text.lower() == "下載圖片"
    def on_enter_pic(self,event):
        send_img(event.source.user_id,crawler_img(index,a))

    def is_going_to_more(self, event):
        text = event.message.text
        return text.lower() == "下一個"

    def on_enter_more(self, event):
        print("I'm entering result")
        global a
        global index
        index = index + 1
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url= crawler_img(index,a),
                title='這是搜尋出來的浪浪',
                text='點擊更多資訊可以得到更多浪浪的資訊喔！'+'\n'+'也可以下載浪浪的照片><',
                actions=[
                    MessageTemplateAction(
                        label='下載圖片',
                        text='下載圖片'
                    ),
                    URITemplateAction(
                        label='更多資訊',
                        uri= crawler_url(index,a)
                    )
                ]
            )
        ]
        )
        )
        send_choose_message(event.source.user_id,Carousel_template)

