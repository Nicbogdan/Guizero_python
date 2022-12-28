from guizero import App, Window,Text

app = App(title="Main window")
window = Window(app, title="Second window")
text = Text(window, text="This text will show up in the second window")

app.display()
