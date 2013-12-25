import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

  def build(self):
    return Label(text="Let's move!")



if __name__ == '__main__':
  first_app = MyApp()
  first_app.run()

