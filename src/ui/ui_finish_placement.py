'''View once the program has done its thing'''

from tkinter import filedialog, ttk, constants, StringVar
from file_and_database_functions.readwrite import filewrite
from file_and_database_functions.database_functions import Logging
from file_and_database_functions.database_connection import get_db_connection


class Finished:
    '''View where user saves the file and logs out'''

    def __init__(self, root, user, file, wish_rate, another_round, finish, language):
        self._root = root
        self._user = user
        self._frame = None
        self._file = file
        self._wish_rate = round(wish_rate)
        self._new_placement = another_round
        self._finish_logout = finish
        self._languge = language
        self._label_str = StringVar()
        self._wish_str = StringVar()
        self._l1_str = StringVar()
        self._save_str = StringVar()
        self._out_strvar = StringVar()
        self._new_str = StringVar()
        if language == "FI":
            self._init_strvars_fi()
        if language == "EN":
            self._init_strvars_en()

        self._save_stats()
        self._init_view()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Destroy the view'''
        self._frame.destroy()

    def _save_stats(self):
        log = Logging(get_db_connection())
        log.add_statistics(self._user, self._wish_rate)
        log.close_connection()

    def _init_strvars_fi(self):
        self._label_str.set("Valmista!")
        self._wish_str.set(f"{self._wish_rate}% plaseeraustoiveista täytetty.")
        self._l1_str.set("Tiedosto tallentuu csv-muodossa")
        self._save_str.set("Tallenna tiedosto")
        self._new_str.set("Luo uusi plaseeraus")
        self._out_strvar.set("Kirjaudu ulos")

    def _init_strvars_en(self):
        self._label_str.set("All done!")
        self._wish_str.set(
            f"{self._wish_rate}% of the seating wishes have been fulfilled.")
        self._l1_str.set("The file will be saved in csv format.")
        self._save_str.set("Save file")
        self._new_str.set("Create a new placement")
        self._out_strvar.set("Logout")

    def _init_view(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, textvariable=self._label_str)
        labelwish = ttk.Label(master=self._frame, textvariable=self._wish_str)
        label1 = ttk.Label(master=self._frame,
                           textvariable=self._l1_str)
        savebutton = ttk.Button(
            master=self._frame,
            textvariable=self._save_str,
            command=self._handle_save_button_press)
        newbutton = ttk.Button(
            master=self._frame,
            textvariable=self._new_str,
            command=self._handle_new_button_press)
        logoutbutton = ttk.Button(
            master=self._frame,
            textvariable=self._out_strvar,
            command=self._handle_logout_button_press
        )
        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)
        labelwish.grid(row=1, column=0, columnspan=3,
                       sticky=constants.EW, padx=200, pady=10)
        savebutton.grid(row=3, column=0, padx=200, pady=10)
        label1.grid(row=2, column=0, padx=200, pady=10)
        newbutton.grid(row=4, column=0, padx=200, pady=10)
        logoutbutton.grid(row=5, column=0, padx=200, pady=10)
        self.pack()

    def _handle_save_button_press(self):
        savepath = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV file", "*.csv")])
        if savepath:
            filewrite(self._file, savepath)
            writing_success_label = ttk.Label(
                master=self._frame, text="Tallennus onnistui", foreground="blue")
            writing_success_label.grid(row=3, column=0, padx=200, pady=10)
            self.pack()

    def _handle_logout_button_press(self):
        self._finish_logout(self._languge)

    def _handle_new_button_press(self):
        self._new_placement(self._user, self._languge)
