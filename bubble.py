import flet as ft
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def sentiment_analysis():
    thought = input("What are you feeling today?\n")
    res = classifier(thought)
    print(res[0]['label'])
    return str(thought), str(res[0]['label'])

def main(page: ft.Page):
    page.title = "Elevated buttons with custom content"
    page.bgcolor = "#f2b835" # Yellow mustard-ish colour
    page.horizontal_alignment = 'CENTER'
    page.vertical_alignment = 'CENTER'

    chat = ft.Column()
    new_message = ft.TextField()

    c = ft.Container(
        content=ft.Text(
            "",
            color=ft.colors.BLACK,
        ),
        width=150,
        height=150,
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor="#d4d4d4",
        border_radius=100,
        blur=10,
        animate_opacity=300,
        
    )
    
    def send_click(e):
        ft.Text(new_message.value)
        
        #global result = lst[1]
        c.content = ft.Text(
            new_message.value,
            color=ft.colors.BLACK,
        )
        c.update()
        

    

    def animate_opacity(e):
        thought, result = sentiment_analysis(new_message.value)
        new_message.value = ""
        page.update()
        if result == "NEGATIVE":
            c.opacity = 0 if c.opacity == 1 else 1
        else:
            c.bgcolor="green"
        c.update()

    page.add(
        c,
        ft.FilledButton(
            "click",
            on_click=animate_opacity,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.TRANSPARENT,
            )
        ),
        chat, 
        ft.Row(
            controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)],
            vertical_alignment=ft.CrossAxisAlignment.END,
            horizontal_alignment=ft.MainAxisAlignment.END,
        ),
    )

sentiment_analysis()
ft.app(target=main)
