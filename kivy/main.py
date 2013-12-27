import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty


class Controller(FloatLayout):
  '''Create a controller that receives a custom widget from the kv
  lang file. Add an action to be called from the kva lang file.
  '''
  label_wid = ObjectProperty()
  info = StringProperty()
  information = StringProperty()

  def do_action(self):
    self.label_wid_text = "My label after button press"
    self.info = "New info text"

  def do_process_information(self):
    self.info = "Back to old text"

    
class ControllerApp(App):

  def build(self):
    return Controller(info="Let's move!", information='I have a name.')



if __name__ == '__main__':
  kv_lang_app = ControllerApp()
  kv_lang_app.run()

