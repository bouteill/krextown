import kivy
kivy.require('1.7.2')

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button


class MyPaintWidget(Widget):
  
  def on_touch_down(self, touch):
    color = (random(), 1, 1)
    with self.canvas:
      #Color(1, 1, 0)
      Color(*color, mode='hsv')
      xFactor = 1.0
      yFactor = 1.0
      d = 30.
      Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
      touch.ud['line'] = Line(points=(touch.x, touch.y))

  def on_touch_move(self, touch):
    #print(touch)
    if 'angle' in touch.profile:
      print('The touch angle is', touch.a)
    touch.ud['line'].points += [touch.x, touch.y]


class MyApp(App):

  def build(self):
    parent = Widget()
    painter = MyPaintWidget()
    clearbtn = Button(text="Clear")
    parent.add_widget(painter)
    parent.add_widget(clearbtn)

    def clear_canvas(obj):
      painter.canvas.clear()

    clearbtn.bind(on_release=clear_canvas)

    return parent


if __name__ == '__main__':
  first_app = MyApp()
  first_app.run()

