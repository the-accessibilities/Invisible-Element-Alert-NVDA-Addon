import api
import speech
import ui
import controlTypes
from globalPluginHandler import GlobalPlugin

def isElementVisible(obj):
    """Checks if the focused element is visible on the screen."""
    states = obj.states
    if controlTypes.State.INVISIBLE in states or controlTypes.State.OFFSCREEN in states:
        return False
    return True

class GlobalPlugin(GlobalPlugin):
    """NVDA add-on to alert when focus moves to an invisible element."""
    def event_gainFocus(self, obj, nextHandler):
        nextHandler()
        if not isElementVisible(obj):
            speech.speak("Warning: this element is not visible on the screen.")
            ui.message("Warning: this element is not visible on the screen.")
