'''index'''
from tkinter import Tk
from ui.ui import UI


WINDOW = Tk()
WINDOW.title("Plassiapuri – Placement helper")
USER_INTERFACE = UI(WINDOW)
USER_INTERFACE.start()

WINDOW.mainloop()
