from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_choose1(self, event):
        text = event.message.text
        return text.lower() == "我要領養"

    def on_enter_start(self, event):
        print("I'm entering start")

        reply_token = event.reply_token
        send_text_message(reply_token, "您好！歡迎來到QQ醬><，是一個提供認養寵物的平台！"+"可以輸入：\"我要領養\" 或者是 \"我要上傳\" ")
        self.go_back()

    def on_exit_start(self):
        print("Leaving start")

    def on_enter_choose(self, event):
        print("I'm entering choose")

        reply_token = event.reply_token
        send_text_message(reply_token, "請問你想要領養哪種動物？"+"\n"+"日前可以選擇有：狗、貓")
        self.go_back()

    def on_exit_choose(self):
        print("Leaving state2")
