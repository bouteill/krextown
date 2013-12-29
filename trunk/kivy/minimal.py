import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.button import Button


class MinimalApp(App):

  def build(self):
    return Button(text='OK')



if __name__ == '__main__':
  first_app = MinimalApp()
  first_app.run()

