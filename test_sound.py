import flet as ft
from gtts import gTTS
import os

language = 'en'

class Message():
    def __init__(self, user: str, text: str, message_type: str):
        self.user = user
        self.text = text
        self.message_type = message_type

def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField()

    page.title = "WordsofAffirmation"
    page.bgcolor = "#f2b835"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.Text(size=30, color="black", value="Welcome to Affirmations!"))

    def on_message(message: Message):
        if message.message_type == "chat_message":
            chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        elif message.message_type == "login_message":
            chat.controls.append(
                ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=15)
            )
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        message_text = new_message.value
        if message_text:
            page.pubsub.send_all(Message(user=page.session.get('user_name'), text=message_text, message_type="chat_message"))
            new_message.value = ""
            page.update()
            # Generate speech from the message text and play it
            generate_and_play_speech(message_text)

    user_name = ft.TextField(label="Enter your name")

    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Name cannot be blank!"
            user_name.update()
        else:
            page.session.set("user_name", user_name.value)
            page.dialog.open = False
            page.pubsub.send_all(Message(user=user_name.value, text=f"{user_name.value} has joined the chat", message_type="login_message"))
            page.update()

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text(color='white',value="Welcome!"),
        content=ft.Column([user_name], tight=True,),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end",
    )

    page.add(chat, ft.Row([new_message, ft.ElevatedButton("Send", on_click=send_click)]))

#def generate_and_play_speech(text):
 #   myobj = gTTS(text=text, lang=language, slow=False)
   # myobj.save("chat.mp3")
    #os.system("mpg321 chat.mp3")

import pyttsx3

def generate_and_play_speech(text):
    #myobj = gTTS(text=text, lang=language, slow=False)
    #myobj.save("chat.mp3")
    #os.system("mpg321 chat.mp3")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

ft.app(target=main, view=ft.WEB_BROWSER)

ft.app(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
