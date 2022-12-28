from guizero import App, Window, PushButton

def open_window():
    window.show()

def close_window():
    window.hide()

app = App(title="Main window")

window = Window(app, title="Second window")
window.hide()

open_button = PushButton(app, text="Open", command=open_window)
close_button = PushButton(app, text="Close", command=close_window)

app.display()
