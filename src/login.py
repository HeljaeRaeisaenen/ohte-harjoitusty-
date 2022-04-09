'''Login view'''
from tkinter import Tk, constants, ttk

class Login:
    '''user interface'''
    def __init__(self, root):
        self._root = root
        self._entry_name = None
        self._entry_pass = None

    def start(self):
        '''start'''
        label = ttk.Label(master=self._root, text="Placement generator")
        name_label = ttk.Label(master=self._root, text="Käyttäjänimi:")
        pass_label = ttk.Label(master=self._root, text="Salasana:")

        startbutton = ttk.Button(
            master=self._root,
            text="Aloita",
            command=self._handle_startbutton_press())
        
        self._entry_name = ttk.Entry(master=self._root)
        self._entry_pass = ttk.Entry(master=self._root)
        checkbutton = ttk.Checkbutton(master=self._root, text="Check button")
        
        label.grid(row=0, column=0, columnspan=3, sticky=constants.W, padx=20, pady=20)
        startbutton.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
        pass_label.grid(row=3, column=1, padx=5, pady=5)
        name_label.grid(row=1, column=1, padx=5, pady=5)
        self._entry_name.grid(row=2, column=1, padx=5, pady=5)
        self._entry_pass.grid(row=4, column=1, padx=5, pady=5)
        #checkbutton.pack(row=6, column=1)
        
        self._root.grid_columnconfigure(1, weight=1, minsize=300)

    def _handle_startbutton_press(self):
        password_value = self._entry_pass.get()
        username_value = self._entry_name.get()
