import kivy
from kivy.app import App    
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty

__version__ = '0.0.2'



class Count:
    def __init__(self) :
        self.i = 0
    def increment(self):
        self.i+=1
    def decrement(self):
        if(self.i>0):
            self.i-=1
    def reset(self):
        self.i = 0
    def result(self) -> str:
        return str(self.i)

class Container(BoxLayout): 2
    label_widget = ObjectProperty()

    app = Count()
    def inc(self):
        self.app.increment()
        self.label_widget.text = self.app.result()
    def dec(self):
        self.app.decrement()
        self.label_widget.text = self.app.result()
    def res(self):
        self.app.reset()
        self.label_widget.text = self.app.result()

    

class CounterApp(App):
    def build(self):    
        return Container()

if __name__ == '__main__':
    CounterApp().run()