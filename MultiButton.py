from _Framework.ButtonElement import ButtonElement

class MultiButtonHost(object):
  """
  Button class that allows a button to have different behaviors for single tap,
  double tap, hold, etc.
  """

  # How long we wait before forwarding a button press.
  # Delay is needed to differentiate between the type of button press.
  DELAY = 300

  def __init__(self, button): # TODO: What else do we need here?
    """Initializes a MultiButtonHost

    :param button: The ButtonElement we're extending
    """
    # TODO
    pass

  def single_tap_button():
    # TODO: Return a (Multi)?ButtonElement that triggers when we want it to
    pass

  def double_tap_button():
    # TODO
    pass

  def hold_button():
    # TODO
    pass
