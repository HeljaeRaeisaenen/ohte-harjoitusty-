'''Class for logging out'''
from tkinter import constants, ttk


class Logout:
    '''View when the user logs out'''

    def __init__(self, root, lang):
        self._root = root
        self._frame = None
        self._language = lang
        self._init_view()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Destroy the view'''
        if self._frame:
            self._frame.destroy()

    def _init_view(self):
        # self.destroy()
        self._frame = ttk.Frame(master=self._root)

        if self._language == "FI":
            label = ttk.Label(master=self._frame,
                              text="Olet kirjautunut ulos.", foreground="blue")
        else:
            label = ttk.Label(master=self._frame,
                              text="You have been logged out.", foreground="blue")

        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)

        self.pack()
