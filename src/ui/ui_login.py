'''Login view'''
from tkinter import constants, ttk, StringVar
from file_and_database_functions.database_functions import Logging
from file_and_database_functions.database_connection import get_db_connection


class Login:
    '''user interface for logging in'''

    def __init__(self, root, login_success):
        self._root = root
        self._entry_name = None
        self._entry_pass = None
        self._frame = None
        self.login_success = login_success
        self._language = "FI"

        self._title_label = StringVar()
        self._2_label = StringVar()
        self._3_label = StringVar()
        self._more_label = StringVar()
        self._usr_label = StringVar()
        self._pass_label = StringVar()
        self._start_label = StringVar()
        self._lang_label = StringVar()
        self._error_label = StringVar()

        self._init_strvars_fi()
        self._init_view()

    def pack(self):
        '''pack'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def login_failure(self):
        errorlabel = ttk.Label(
            master=self._frame, textvariable=self._error_label, foreground="red")
        errorlabel.grid(row=1, column=0, padx=15, pady=15)
        self.pack()

    def _init_strvars_fi(self):
        self._title_label.set("Plassigeneraattori")
        self._2_label.set("Älä käytä mitään salasanaa, jota käytät muualla.")
        self._3_label.set("Salasanan voi jättää tyhjäksi.",)
        self._more_label.set("Jos käyttäjätunnusta ei ole, se luodaan.")
        self._usr_label.set("Käyttäjätunnus:")
        self._pass_label.set("Salasana:")
        self._start_label.set("Kirjaudu sisään")
        self._lang_label.set("In English")
        self._error_label.set("Väärä salasana")

    def _init_strvars_en(self):
        self._title_label.set("Placement Generator")
        self._2_label.set("Do not use a password you use elsewhere.")
        self._3_label.set("The password field can be left empty.",)
        self._more_label.set(
            "If the username doesn't exist, it is created.")
        self._usr_label.set("Username:")
        self._pass_label.set("Password:")
        self._start_label.set("Login")
        self._lang_label.set("Suomeksi")
        self._error_label.set("Wrong password")

    def _init_view(self):
        '''start'''
        self.destroy()
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            textvariable=self._title_label,
            foreground="black",
            width=20)
        label.config(font=("Comic Sans MS", 20))
        label2 = ttk.Label(
            master=self._frame,
            textvariable=self._2_label,
            foreground="black",
            width=20)
        label3 = ttk.Label(
            master=self._frame,
            textvariable=self._3_label,
            foreground="black",
            width=20)
        more_label = ttk.Label(
            master=self._frame,
            textvariable=self._more_label,
            foreground="black",
            width=20)
        startbutton = ttk.Button(
            master=self._frame,
            textvariable=self._start_label,
            command=self._handle_startbutton_press)
        langbutton = ttk.Button(
            master=self._frame,
            textvariable=self._lang_label,
            command=self._handle_langbutton_press)

        name_label = ttk.Label(
            master=self._frame, textvariable=self._usr_label)
        pass_label = ttk.Label(
            master=self._frame, textvariable=self._pass_label)
        self._entry_name = ttk.Entry(master=self._frame)
        self._entry_pass = ttk.Entry(master=self._frame, show="*")

        self._frame.grid_columnconfigure(0, weight=1, minsize=200)
        self._frame.grid(columnspan=2)
        langbutton.grid(row=0, column=0,
                        sticky=constants.E, padx=10, pady=10)
        label.grid(row=0, column=0, columnspan=1,
                   sticky=constants.EW, padx=75, pady=25)
        label2.grid(row=2, column=0, columnspan=2,
                    sticky=constants.EW, padx=100, pady=10)
        label3.grid(row=3, column=0, columnspan=2,
                    sticky=constants.EW, padx=100, pady=10)
        startbutton.grid(row=9, column=0, columnspan=1,
                         sticky=constants.EW, padx=200, pady=25)
        pass_label.grid(row=6, column=0, sticky=constants.EW,
                        padx=150, pady=10)
        name_label.grid(row=4, column=0, sticky=constants.EW,
                        padx=150, pady=10)
        self._entry_name.grid(row=5, column=0, padx=100, pady=10)
        self._entry_pass.grid(row=7, column=0, padx=100, pady=10)
        more_label.grid(row=8, column=0, sticky=constants.EW,
                        columnspan=1, padx=100, pady=15)

    def _handle_langbutton_press(self):
        if self._language == "FI":
            self._language = "EN"
            self._init_strvars_en()
            self._init_view()
        else:
            self._language = "FI"
            self._init_strvars_fi()
            self._init_view()

    def _handle_startbutton_press(self):
        password_value = self._entry_pass.get()
        username_value = self._entry_name.get()
        if username_value == "":
            self.login_failure()
        else:
            log = Logging(get_db_connection())
            is_username = log.find_username(username_value)
            if not is_username:
                log.create_username(username_value, password_value)
                log.close_connection()
                self.login_success(username_value, self._language)
                return
            verify = log.verify_password(username_value, password_value)
            if verify:
                log.close_connection()
                self.login_success(username_value, self._language)
                return
            self.login_failure()
