import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()
machine = {}
app = Flask(__name__, static_url_path="")
# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: "+body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400) 
    #multiple user
    for event in events:
        global sender_id
        sender_id = event.source.user_id
        if sender_id not in machine:
            machine[sender_id] = TocMachine(
                states=["user", "start", "choose1","dog","cat","more","fsm","pic"],
                transitions=[
                    {
                        "trigger": "advance",
                        "source": "start",
                        "dest": "fsm",
                        "conditions": "is_going_to_fsm",
                    },
                    {
                        "trigger": "advance",
                        "source": "fsm",
                        "dest": "start",
                        "conditions": "is_going_to_start",
                    },
                    {
                        "trigger": "advance",
                        "source": "user",
                        "dest": "start",
                        "conditions": "is_going_to_start",
                    },
                    {
                        "trigger": "advance",
                        "source": "start",
                        "dest": "choose1",
                        "conditions": "is_going_to_choose1",
                    },
                    {
                        "trigger": "advance",
                        "source": "choose1",
                        "dest": "dog",
                        "conditions": "is_going_to_dog",
                    },
                    {
                        "trigger": "advance",
                        "source": "choose1",
                        "dest": "cat",
                        "conditions": "is_going_to_cat",
                    },
                    {
                        "trigger": "advance",
                        "source": "dog",
                        "dest": "more",
                        "conditions": "is_going_to_more",
                    },
                    {
                        "trigger": "advance",
                        "source": "cat",
                        "dest": "more",
                        "conditions": "is_going_to_more",
                    },
                    {
                        "trigger": "advance",
                        "source": "cat",
                        "dest": "pic",
                        "conditions": "is_going_to_pic",
                    },
                    {
                        "trigger": "advance",
                        "source": "dog",
                        "dest": "pic",
                        "conditions": "is_going_to_pic",
                    },
                    {
                        "trigger": "advance",
                        "source": "more",
                        "dest": "start",
                        "conditions": "is_going_to_start",
                    },
                    {
                        "trigger": "advance",
                        "source": "pic",
                        "dest": "more",
                        "conditions": "is_going_to_more",
                    },
                    {
                        "trigger": "advance",
                        "source": "more",
                        "dest": "more",
                        "conditions": "is_going_to_more",
                    },
                    {"trigger": "go_back", "source": ["start", "choose1","dog","cat","more","fsm","pic"], "dest": "user"},
                ],
                initial="user",
                auto_transitions=False,
                show_conditions=True,
            )
        if not isinstance(event,MessageEvent):
            continue
        print("\nFSM STATE: "+machine[sender_id].state)
        print("REQUEST BODY: \n"+body)
        response = machine[sender_id].advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")
    return "OK"    

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine[sender_id].get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
