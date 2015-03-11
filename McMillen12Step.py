from __future__ import with_statement

import Live
from _Framework.ButtonElement import ButtonElement
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.SessionComponent import SessionComponent

class McMillen12Step(ControlSurface):
  """
  Script for Keith McMillen Instruments' 12 Step Controller
  """

  CHANNEL = 0

  # All notes in [C4, C5] except F#, G#, and A#
  CLIP_CONTROL_NOTES = [48, 49, 50, 51, 52, 53, 55, 57, 59, 60]
  STOP_ALL_NOTE = 54 # F# 4
  SCENE_SWITCH_NOTE = 56 # G# 4
  PAGE_TURN_NOTE = 58 # A# 4

  def __init__(self, c_instance):
    super(McMillen12Step, self).__init__(c_instance)

    with self.component_guard():
      is_momentary = True
      self.session = SessionComponent(len(self.CLIP_CONTROL_NOTES), 1)

      # Clip control
      for index, note in enumerate(self.CLIP_CONTROL_NOTES):
        # TODO: Use MultiButton(Host|Element) instead to implement double tap,
        # hold, etc.
        launch_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE,
            self.CHANNEL, note)
        self.session.scene(0).clip_slot(index).set_launch_button(launch_button)

      # TODO: Stop all note
      # TODO: Scene switch note
      # TODO: Page turn note

  def _on_selected_scene_changed(self):
    super(McMillen12Step, self)._on_selected_scene_changed()

    # Get the index of the currently selected scene
    scene_index = list(self.song().scenes).index(self.song().view.selected_scene)

    self.session.set_offsets(self.session._track_offset, scene_index)
