'''View once user has logged in'''
from tkinter import ttk, constants, StringVar
from file_and_database_functions.database_connection import get_db_connection
from file_and_database_functions.database_functions import Logging


class First:
    '''if login was succesful, show this view'''

    def __init__(self, root, user, make_placement, info_button, info_return_command, log_out, language="FI"):
        self._root = root
        self._current_view = None
        self._current_user = user
        self._language = language
        self._frame = None
        self._make_placement = make_placement
        self._info_button = info_button
        self._info_return = info_return_command
        self._pass_entry = None
        self._log_out = log_out

        self._label_label = StringVar()
        self._begin_plac_label = StringVar()
        self._info_var = StringVar()
        self._stats_var = StringVar()
        self._back_str = StringVar()
        self._del_user_var = StringVar()
        self._change_pwd_var = StringVar()
        self._logout_var = StringVar()

        self._used_var = StringVar()
        self._avg_var = StringVar()

        self._new_pass_var = StringVar()
        self._success_var = StringVar()

        self._init_view()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Destroy the view'''
        if self._frame:
            self._frame.destroy()

    def _init_strvars_fi(self):
        self._label_label.set(f"Tervetuloa {self._current_user}")
        self._info_var.set("Infoa – lue minut")
        self._begin_plac_label.set("Aloita plaseeraus")
        self._stats_var.set("Tarkastele tietojasi")
        self._change_pwd_var.set("Vaihda salasana")
        self._del_user_var.set("Poista käyttäjäsi ja sen tiedot")
        self._back_str.set("Takaisin")
        self._logout_var.set("Kirjaudu ulos")

        self._new_pass_var.set("Kirjoita uusi salasana:")
        self._success_var.set("Salasanan vaihto onnistui")

    def _init_strvars_en(self):
        self._label_label.set(f"Welcome {self._current_user}")
        self._info_var.set("Info – read me")
        self._begin_plac_label.set("Begin placement")
        self._stats_var.set("View your information")
        self._change_pwd_var.set("Change your password")
        self._del_user_var.set("Delete user and its data")
        self._back_str.set("Back")
        self._logout_var.set("Logout")

        self._new_pass_var.set("Write a new password:")
        self._success_var.set("Password change successful")

    def _init_view(self):
        self.destroy()
        if self._language == "FI":
            self._init_strvars_fi()
        else:
            self._init_strvars_en()

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, textvariable=self._label_label)
        start_plac_button = ttk.Button(
            master=self._frame,
            textvariable=self._begin_plac_label,
            command=self._handle_plac_button_press)
        infobutton = ttk.Button(
            master=self._frame,
            textvariable=self._info_var,
            command=self._handle_info_button_press)
        statbutton = ttk.Button(
            master=self._frame,
            textvariable=self._stats_var,
            command=self._handle_stats_button_press)
        logoutbutton = ttk.Button(
            master=self._frame,
            textvariable=self._logout_var,
            command=self._handle_logout_button_press)
        passbutton = ttk.Button(
            master=self._frame,
            textvariable=self._change_pwd_var,
            command=self._handle_pass_button_press)
        delbutton = ttk.Button(
            master=self._frame,
            textvariable=self._del_user_var,
            command=self._handle_del_button_press)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)
        infobutton.grid(row=0, column=0, padx=5, pady=10)
        start_plac_button.grid(
            row=2, column=0, columnspan=2, padx=200, pady=10)
        statbutton.grid(row=4, column=0, columnspan=2, padx=200, pady=10)
        passbutton.grid(row=5, column=0, columnspan=2, padx=200, pady=10)
        if self._pass_entry:
            succlabel = ttk.Label(
                master=self._frame, textvariable=self._success_var, foreground="blue")
            succlabel.grid(row=6, column=0, columnspan=2, padx=200, pady=10)

        delbutton.grid(row=8, column=0, columnspan=2, padx=200, pady=10)
        logoutbutton.grid(row=9, column=0, columnspan=2, padx=200, pady=10)

        self.pack()

    def _handle_plac_button_press(self):
        self._make_placement(self._current_user, self._language)

    def _handle_stats_button_press(self):
        log = Logging(get_db_connection())
        stats = log.view_statistics(self._current_user)
        log.close_connection()

        self.destroy()
        if self._language == "FI":
            if stats[0] == 1:
                self._used_var.set(f"Olet tehnyt {stats[0]} plaseerauksen.")
            else:
                self._used_var.set(f"Olet tehnyt {stats[0]} plaseerausta.")
            if stats[0] != 0:
                self._avg_var.set(
                    f"Keskimäärin {stats[1]}% osallistujien toiveista \n on toteutettu plaseerauksissa.")
        if self._language == "EN":
            if stats[0] == 1:
                self._used_var.set(f"You have made {stats[0]} seating placement.")
            else:
                self._used_var.set(f"You have made {stats[0]} seating placements.")
            if stats[0] != 0:
                self._avg_var.set(
                    f"On average, {stats[1]}% of the wishes of participants \nhave been filled in the placements.")

        self._frame = ttk.Frame(master=self._root)
        label1 = ttk.Label(master=self._frame, textvariable=self._used_var)
        label2 = ttk.Label(master=self._frame, textvariable=self._avg_var)
        backbutton = ttk.Button(
            master=self._frame,
            textvariable=self._back_str,
            command=self._init_view)

        label1.grid(row=0, column=0, columnspan=2,
                    sticky=constants.W, padx=200, pady=10)
        label2.grid(row=2, column=0, columnspan=2,
                    sticky=constants.W, padx=200, pady=10)
        backbutton.grid(row=3, column=0, columnspan=2, padx=200, pady=10)
        self.pack()

    def _handle_pass_button_press(self):
        self.destroy()

        self._frame = ttk.Frame(master=self._root)
        pass_change = ttk.Label(
            master=self._frame, textvariable=self._new_pass_var)
        self._pass_entry = ttk.Entry(master=self._frame, show="*")
        donebutton = ttk.Button(
            master=self._frame,
            text="OK",
            command=self._change_pass)

        pass_change.grid(row=0, column=0, columnspan=2,
                         sticky=constants.W, padx=200, pady=10)
        self._pass_entry.grid(row=2, column=0, columnspan=2,
                              sticky=constants.W, padx=200, pady=10)
        donebutton.grid(row=3, column=0, columnspan=2, padx=200, pady=10)
        self.pack()

    def _change_pass(self):
        log = Logging(get_db_connection())
        log.change_password(self._current_user, str(self._pass_entry.get()))

        self._init_view()

    def _handle_del_button_press(self):
        log = Logging(get_db_connection())
        log.delete_user(self._current_user)
        self._log_out()

    def _handle_logout_button_press(self):
        self._log_out()

    def _handle_info_button_press(self):
        self._info_button(self._info_return,
                          self._current_user, self._language)
