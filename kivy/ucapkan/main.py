import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from plyer import tts

import subprocess


class Ucapkan(BoxLayout):
  ucapkan_text = ObjectProperty(None)

  def say_something(self, text):
    #subprocess.call(["espeak", text])
    try:
      tts.speak(text)
    except NotImplementedError:
      popup = Popup(title='Text-to-Speech not implemented',
          content=Label(text='Sorry, TTS is not available.'),
          size_hint=(None, None),
          size=(300, 300))
      popup.open()

  def clear(self):
    self.ucapkan_text.text = ""
    self.ucapkan_text.focus = True

    
class UcapkanApp(App):
  def build(self):
    return Ucapkan()


if __name__ == '__main__':
  myapp = UcapkanApp()
  myapp.run()

