'''Class for logging out'''
from tkinter import constants, ttk


class Logout:
    '''View when the user logs out'''

    def __init__(self, root, logout_success):
        self._root = root
        self._frame = None
        self.logout_success = logout_success
        self._init_view()
        logout_success()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def _init_view(self):
        # self.destroy()
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text="Olet kirjautunut ulos.", foreground="blue")

        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)

        self.pack()
