'''Login view'''
from tkinter import constants, ttk
from login import Logging
from database_connection import get_database_connection


class Login:
    '''user interface for logging in'''

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
            master=self._frame, text="Väärä salasana", foreground="red")
        errorlabel.grid(row=1, column=0, padx=15, pady=15)
        self.pack()

    def _init_view(self):
        '''start'''
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Plassigeneraattori",
            
            foreground="black",
            width=20)
        label.config(font=("Comic Sans MS", 20))
        label2 = ttk.Label(
            master=self._frame,
            text="Älä käytä mitään salasanaa, jota käytät muualla.",
            foreground="black",
            width=20)
        label3 = ttk.Label(
            master=self._frame,
            text="Salasanan voi jättää tyhjäksi.",
            foreground="black",
            width=20)
        more_label = ttk.Label(
            master=self._frame,
            text="Jos käyttäjätunnusta ei ole, se luodaan",
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

        self._frame.grid_columnconfigure(0, weight=1, minsize=200)
        #self._frame.grid_columnconfigure(1, weight=1, minsize=200)
        self._frame.grid(columnspan=2)
        label.grid(row=0, column=0, columnspan=1,
                   sticky=constants.EW, padx=100, pady=25)
        label2.grid(row=2, column=0, columnspan=2,
                    sticky=constants.EW, padx=100, pady=10)
        label3.grid(row=3, column=0, columnspan=2,
                   sticky=constants.EW, padx=100, pady=10)
        startbutton.grid(row=9, column=0, columnspan=1, sticky=constants.EW, padx=200, pady=25)
        pass_label.grid(row=6, column=0, sticky=constants.EW, padx=150, pady=10)
        name_label.grid(row=4, column=0, sticky=constants.EW, padx=150, pady=10)
        self._entry_name.grid(row=5, column=0, padx=100, pady=10)
        self._entry_pass.grid(row=7, column=0, padx=100, pady=10)
        more_label.grid(row=8, column=0, sticky=constants.EW,
                        columnspan=1, padx=100, pady=15)



    def _handle_startbutton_press(self):
        password_value = self._entry_pass.get()
        username_value = self._entry_name.get()
        if username_value == "":
            self.login_failure()
        else:
            log = Logging(get_database_connection())
            is_username = log.find_username(username_value)
            if not is_username:
                log.create_username(username_value, password_value)
                log.close_connection()
                self.login_success(username_value)
                return
            verify = log.verify_password(username_value, password_value)
            if verify:
                log.close_connection()
                self.login_success(username_value)
                return
            self.login_failure()
