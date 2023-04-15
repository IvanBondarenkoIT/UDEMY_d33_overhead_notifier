from tkinter import Tk, Canvas, PhotoImage, Button

from JsonManage import JsonManage


class KanyeQuote:
    def __init__(self, url_to_get: str):
        self.url_to_get = url_to_get
        window = Tk()
        window.title("Kanye Says...")
        window.config(padx=50, pady=50)

        self.canvas = Canvas(width=300, height=414)
        background_img = PhotoImage(file="kanye-quotes-img/background.png")
        self.canvas.create_image(150, 207, image=background_img)
        self.quote_text = self.canvas.create_text(150, 207, text="Quotes", width=250, font=("Arial", 30, "bold"), fill="white")
        self.get_quote()
        self.canvas.grid(row=0, column=0)

        kanye_img = PhotoImage(file="kanye-quotes-img/kanye.png")
        kanye_button = Button(image=kanye_img, highlightthickness=0, command=self.get_quote)
        kanye_button.grid(row=1, column=0)

        window.mainloop()

    def get_quote(self):
        manage = JsonManage(url_to_get_json=self.url_to_get)
        self.canvas.itemconfig(self.quote_text, text=manage.get_json()["quote"])
