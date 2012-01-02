
FULLSCREEN = 0

try:
    import Tkinter
    root = Tkinter.Tk()
    FULLSCREEN_WINDOW_SIZE = root.winfo_screenwidth(), root.winfo_screenheight()
    root.destroy()
except ImportError: #lol.  Sucks to be you.
    FULLSCREEN_WINDOW_SIZE = 640, 480

WINDOW_SIZE = 900, 600

BLUR = 0
FPS = 60
