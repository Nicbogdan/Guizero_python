from guizero import App, Text, PushButton

def say_hello():
    text.value = "hello world"

def e_str():
    text.value =""

app = App()
text = Text(app)
button = PushButton(app, command=say_hello)
button2 = PushButton(app, command=e_str)
app.display()
