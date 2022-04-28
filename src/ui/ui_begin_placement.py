'''View where user can make placement'''
from tkinter import filedialog, ttk, constants, StringVar
from tkinter.simpledialog import askinteger
from placement import Placement, TablesException
from participants_repo import ParticipantsRepo


class Begin:
    '''if login was succesful, show this view'''

    def __init__(self, root, user, placement_is_finished, language="FI"):
        self._root = root
        self._current_view = None
        self._current_user = user
        self._language = language
        self._frame = None
        self._tables_n = None
        self._filepath = None
        self._file_strvar = StringVar()
        self._file_strvar.set("               ")
        self._button_strvar = StringVar()
        self._placement_is_finished = placement_is_finished

        self._label_label = StringVar()
        self._open_label = StringVar()
        self._info_var = StringVar()
        self._tables_n_var = StringVar()
        self._tables_var = StringVar()
        self._begin_var = StringVar()

        self.labl_str = StringVar()
        self.l2_str = StringVar()
        self.l3_str = StringVar()
        self.l5_str = StringVar()
        self.back_str = StringVar()

        self._init_view()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Destroy the view'''
        if self._frame:
            self._frame.destroy()

    def _init_strvars_en(self):
        self._label_label.set("Select the file (csv)")
        self._open_label.set("Open file")
        self._info_var.set("Info – read me")
        self._tables_n_var.set("Number of tables")
        self._tables_var.set("How many tables?")
        self._begin_var.set("Start")

    def _init_strvars_fi(self):
        self._label_label.set("Valitse tiedosto (csv)")
        self._open_label.set("Avaa tiedosto")
        self._info_var.set("Infoa – lue minut")
        self._tables_n_var.set("Pöytien määrä")
        self._tables_var.set("Kuinka monta pöytää?")
        self._begin_var.set("Aloita")

    def _init_view(self):
        self.destroy()
        if self._language == "FI":
            self._init_strvars_fi()
        else:
            self._init_strvars_en()

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, textvariable=self._label_label)
        openbutton = ttk.Button(
            master=self._frame,
            textvariable=self._open_label,
            command=self._handle_open_button_press)
        # possibility to select the venue, which automatically sets the number of tables
        infobutton = ttk.Button(
            master=self._frame,
            textvariable=self._info_var,
            command=self._handle_info_button_press)
        tablesbutton = ttk.Button(
            master=self._frame,
            textvariable=self._tables_var,
            command=self._handle_tables_button_press)
        tables_label = ttk.Label(
            master=self._frame, textvariable=self._tables_var)
        filesuccess = ttk.Label(
            master=self._frame, textvariable=self._file_strvar, foreground="red")
        if self._filepath:
            filesuccess = ttk.Label(
                master=self._frame, textvariable=self._file_strvar, foreground="blue")

        if self._tables_n:
            buttonsuccess = ttk.Label(
                master=self._frame, textvariable=self._button_strvar, foreground="blue")
        else:
            buttonsuccess = ttk.Label(
                master=self._frame, textvariable=self._button_strvar, foreground="red")
        beginbutton = ttk.Button(
            master=self._frame,
            textvariable=self._begin_var,
            command=self._handle_begin_button_press)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
        infobutton.grid(row=0, column=0, padx=5, pady=10)
        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)
        openbutton.grid(row=2, column=0, columnspan=2, padx=200, pady=10)
        filesuccess.grid(row=3, column=0, columnspan=2, padx=200, pady=10)
        tables_label.grid(row=4, column=0, columnspan=2, padx=200, pady=10)
        tablesbutton.grid(row=5, column=0, columnspan=2, padx=200, pady=10)
        buttonsuccess.grid(row=6, column=0, columnspan=2, padx=200, pady=10)
        beginbutton.grid(row=7, column=0, columnspan=2, padx=200, pady=50)

        self.pack()

    def _tables_n_verification_view(self):
        self.destroy()
        self._tables_labl_str = StringVar()
        self._tables_labl2_str = StringVar()
        self._butt_str = StringVar()
        self._butt2_str = StringVar()

        if self._language == "FI":
            self._tables_labl_str.set("Oletko varma?")
            self._tables_labl2_str.set(f"{self._tables_n} pöytää?")
            self._butt_str.set("Kyllä")
            self._butt2_str.set("Ei")
        else:
            self._tables_labl_str.set("Are you sure?")
            self._tables_labl2_str.set(f"{self._tables_n} tables?")
            self._butt_str.set("Yes")
            self._butt2_str.set("No")

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          textvariable=self._tables_labl_str)
        label2 = ttk.Label(master=self._frame,
                           textvariable=self._tables_labl2_str)
        button_yes = ttk.Button(
            master=self._frame,
            textvariable=self._butt_str,
            command=self._init_view)
        button_no = ttk.Button(
            master=self._frame,
            textvariable=self._butt2_str,
            command=self._handle_tables_button_press)

        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)
        label2.grid(row=1, column=0, padx=200, pady=10)
        button_yes.grid(row=2, column=0, padx=200, pady=10)
        button_no.grid(row=3, column=0, padx=200, pady=10)
        self.pack()

    def _handle_tables_button_press(self):
        self._tables_n = askinteger("Input", "Input an Integer")
        if self._language == "FI":
            self._button_strvar.set(f"Pöytien määrä valittu: {self._tables_n}")
        else:
            self._button_strvar.set(
                f"Number of tables selected: {self._tables_n}")
        if self._tables_n:
            if self._tables_n > 5 or self._tables_n == 0:
                self._tables_n_verification_view()
                return
        self._init_view()

    def _handle_open_button_press(self):
        self._filepath = filedialog.askopenfilename(
            filetypes=[("CSV file", "*.csv")])  # add initialdir=""
        if not self._filepath:
            if self._language == "FI":
                self._file_strvar.set("Et valinnut tiedostoa")
            else:
                self._file_strvar.set("No file selected")
        else:
            if self._language == "FI":
                self._file_strvar.set("Tiedosto valittu")
            else:
                self._file_strvar.set("File selected")
        self._init_view()

    def _handle_info_button_press(self):
        self.destroy()

        if self._language == "FI":
            self.labl_str.set(
                "Csv-tiedostossa tulee olla vain 2 saraketta, joista ensimmäisessä")
            self.l2_str.set(
                "tulee olla osallistujien nimet (Etunimi Sukunimi), ja toisessa toivotut")
            self.l3_str.set("seuralaiset pilkulla eroteltuna.")
            self.l5_str.set(
                "Tiedoston solujen erottimena tulle olla pilkku (,).")
            self.back_str.set("Takaisin")
        else:
            self.labl_str.set(
                "The csv file can only have 2 columns, of which the first must have")
            self.l2_str.set(
                "the names of the participants (Firstname Lastname), and the other")
            self.l3_str.set("the wished company, separated by commas.")
            self.l5_str.set("The delimiter of the filemust be a comma (,).")
            self.back_str.set("Back")

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame, textvariable=self.labl_str)
        l2 = ttk.Label(
            master=self._frame, textvariable=self.l2_str)
        l3 = ttk.Label(master=self._frame, textvariable=self.l3_str)
        l4 = ttk.Label(master=self._frame, text="                ")
        l5 = ttk.Label(
            master=self._frame, textvariable=self.l5_str)
        returnbutton = ttk.Button(
            master=self._frame,
            textvariable=self.back_str,
            command=self._init_view)
        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=50, pady=10)
        l2.grid(row=1, column=0, columnspan=3,
                sticky=constants.EW, padx=50, pady=10)
        l3.grid(row=3, column=0, columnspan=3,
                sticky=constants.EW, padx=50, pady=10)
        l4.grid(row=4, column=0, columnspan=3,
                sticky=constants.EW, padx=50, pady=10)
        l5.grid(row=5, column=0, columnspan=3,
                sticky=constants.EW, padx=50, pady=10)
        returnbutton.grid(row=6, column=0, columnspan=3,
                          sticky=constants.EW, padx=50, pady=10)
        self.pack()

    def _handle_begin_button_press(self):
        if not self._filepath:
            if self._language == "FI":
                self._file_strvar.set("Et valinnut tiedostoa")
            else:
                self._file_strvar.set("No file selected")
        if not self._tables_n:
            if self._language == "FI":
                self._button_strvar.set("Et valinnut pöytien määrää")
            else:
                self._button_strvar.set("No amount of tables selected")
        self.pack()
        if self._filepath and self._tables_n:
            try:
                pla = Placement(
                    self._tables_n, ParticipantsRepo(self._filepath))
                wish_rate = (pla.wishes_placed / pla.total_wishes) * 100
                self._placement_is_finished(self._current_user, pla.fin_placement, wish_rate, self._language)
            except Exception as eror:
                self.errors(eror)

    def errors(self, errname):
        self.destroy()

        self._lable_str = StringVar()
        self._label2_str = StringVar()
        self._return_str = StringVar()
        err = None

        if isinstance(errname, IndexError):
            if self._language == "FI":
                err = "Tiedostossa oli liian vähän tai paljon rivejä tai sarakkeita."
            else:
                err = "The file had too many or too few rows or columns."
        if isinstance(errname, TablesException):
            err = errname.value
            if self._language == "FI":
                err = "Pöytiä oli enemmän kuin osallistujia"

        if self._language == "FI":
            if err:
                self._lable_str.set(f"Tapahtui virhe: {err}")
            else:
                self._lable_str.set(f"Tapahtui virhe.")
            self._label2_str.set("Tarkista tiedostosi muoto ja sisältö")
            self._return_str.set("Takaisin")
        else:
            if err:
                self._lable_str.set(f"An error occurred: {err}")
            else:
                self._lable_str.set(f"An error occurred.")
            self._label2_str.set(
                "Please check the form and contents of your file")
            self._return_str.set("Back")

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          textvariable=self._lable_str)
        label2 = ttk.Label(master=self._frame,
                           textvariable=self._label2_str)
        returnbutton = ttk.Button(
            master=self._frame,
            textvariable=self._return_str,
            command=self._init_view)
        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=100, pady=10)
        label2.grid(row=1, column=0, columnspan=3,
                    sticky=constants.EW, padx=100, pady=10)
        returnbutton.grid(row=2, column=0, columnspan=3,
                          sticky=constants.EW, padx=100, pady=10)
        self.pack()
