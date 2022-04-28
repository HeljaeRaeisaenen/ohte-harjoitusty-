'''index'''
from tkinter import Tk, ttk
from ui.ui import UI


WINDOW = Tk()
WINDOW.title("Plassiapuri – Placement helper")
style = ttk.Style(WINDOW)
style.theme_use('clam')
USER_INTERFACE = UI(WINDOW)
USER_INTERFACE.start()

WINDOW.mainloop()
