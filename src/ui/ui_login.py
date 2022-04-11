'''Login view'''
from tkinter import constants, ttk


class Login:
    '''user interface'''

    def __init__(self, root, login_success):
        self._root = root
        self._entry_name = None
        self._entry_pass = None
        self._frame = None
        self.login_success = login_success
        self._init_view()

    def pack(self):
        '''pack'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def login_failure(self):
        errorlabel = ttk.Label(
            master=self._frame, text="Väärä käyttäjätunnus tai salasana", foreground="red")
        errorlabel.grid(row=1, column=1, padx=15, pady=15)
        self.pack()

    def _init_view(self):
        '''start'''
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Plassigeneraattori",
            foreground="black",
            width=20)
        more_label = ttk.Label(
            master=self._frame,
            text="TEXT",
            foreground="black",
            width=20)
        startbutton = ttk.Button(
            master=self._frame,
            text="Aloita",
            command=self._handle_startbutton_press)

        name_label = ttk.Label(master=self._frame, text="Käyttäjänimi:")
        pass_label = ttk.Label(master=self._frame, text="Salasana:")
        self._entry_name = ttk.Entry(master=self._frame)
        self._entry_pass = ttk.Entry(master=self._frame)
        # button to selsct language?
        # button to view a help/info-page, which exxplains things

        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.W, padx=300, pady=25)
        startbutton.grid(row=7, column=0, columnspan=3, padx=200, pady=15)
        pass_label.grid(row=4, column=1, sticky=constants.W, padx=200, pady=10)
        name_label.grid(row=2, column=1, sticky=constants.W, padx=200, pady=10)
        self._entry_name.grid(row=3, column=1, padx=200, pady=10)
        self._entry_pass.grid(row=5, column=1, padx=200, pady=10)
        more_label.grid(row=6, column=1, columnspan=3, padx=200, pady=15)

        self._root.grid_columnconfigure(1, weight=1, minsize=200)

    def _handle_startbutton_press(self):
        password_value = self._entry_pass.get()
        username_value = self._entry_name.get()
        if username_value == "":
            self.login_failure()
        else:
            self.login_success()
