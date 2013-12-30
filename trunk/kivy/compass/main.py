'''
http://python-for-android.readthedocs.org/en/latest/examples/
'''
import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.properties import NumericProperty
from pyjnius import autoclass


Hardware = autoclass('org.renpy.android.Hardware')


class CompassApp(App):
  needle_angle = NumericProperty(0)

  def build(self):
    self._anim = None
    Hardware.magneticFieldSensorEnable(True)
    Clock.schedule_interval(self.update_compass, 1 / 10.)

  def update_compass(self, *args):
    (x, y, z) = Hardware.magneticFieldSensorReading()

    needle_angle = Vector(x, y).angle((0, 1)) + 90.

    if self._anim:
      self._anim.stop(self)
    self._anim = Animation(needle_angle=needle_angle, d=.2,
        t='out_quad')
    self._anim.start(self)

  def on_pause(self):
    Hardware.magneticFieldSensorEnable(False)
    return True

  def on_resume(self):
    Hardware.magneticFieldSensorEnable(True)


if __name__ == '__main__':
  myapp = CompassApp()
  myapp.run()

