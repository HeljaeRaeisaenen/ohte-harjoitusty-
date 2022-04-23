'''View once user has logged in'''
from tkinter import filedialog, ttk, constants, StringVar
from tkinter.simpledialog import askinteger
from placement import Placement
from participants_repo import ParticipantsRepo


class Begin:
    '''if login was succesful, show this view'''

    def __init__(self, root, user, placement_is_finished):
        self._root = root
        self._current_view = None
        self._current_user = user
        self._frame = None
        self._tables_n = None
        self._filepath = None
        self._file_strvar = StringVar()
        self._file_strvar.set("            ")
        self._button_strvar = StringVar()
        self._button_strvar.set("            ")
        self._placement_is_finished = placement_is_finished
        self._init_view()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Destroy the view'''
        if self._frame:
            self._frame.destroy()

    def _init_view(self):
        self.destroy()
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Valitse tiedosto (csv)")
        openbutton = ttk.Button(
            master=self._frame,
            text="Avaa tiedosto",
            command=self._handle_open_button_press)
        # possibility to select the venue, which automatically sets the number of tables
        infobutton = ttk.Button(
            master=self._frame,
            text="Infoa – lue minut",
            command=self._handle_info_button_press)
        tablesbutton = ttk.Button(
            master=self._frame,
            text="Pöytien määrä",
            command=self._handle_tables_button_press)
        tables_label = ttk.Label(
            master=self._frame, text="Kuinka monta pöytää?")
        filesuccess = ttk.Label(
            master=self._frame, textvariable=self._file_strvar, foreground="red")
        if self._filepath:
            filesuccess = ttk.Label(
                master=self._frame, text="Tiedosto valittu", foreground="blue")

        if self._tables_n:
            buttonsuccess = ttk.Label(
                master=self._frame, textvariable=self._button_strvar, foreground="blue")
        else:
            buttonsuccess = ttk.Label(
                master=self._frame, textvariable=self._button_strvar, foreground="red")
        beginbutton = ttk.Button(
            master=self._frame,
            text="Aloita",
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

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Oletko varma?")
        label2 = ttk.Label(master=self._frame,
                           text=f"{self._tables_n} pöytää?")
        button_yes = ttk.Button(
            master=self._frame,
            text="Kyllä",
            command=self._init_view)
        button_no = ttk.Button(
            master=self._frame,
            text="Ei",
            command=self._handle_tables_button_press)

        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)
        label2.grid(row=1, column=0, padx=200, pady=10)
        button_yes.grid(row=2, column=0, padx=200, pady=10)
        button_no.grid(row=3, column=0, padx=200, pady=10)
        self.pack()

    def _handle_tables_button_press(self):
        self._tables_n = askinteger("Input", "Input an Integer")
        self._button_strvar.set(f"Pöytien määrä valittu: {self._tables_n}")
        if self._tables_n:
            if self._tables_n > 5 or self._tables_n == 0:
                self._tables_n_verification_view()
                return
        self._init_view()

    def _handle_open_button_press(self):
        self._filepath = filedialog.askopenfilename(
            filetypes=[("CSV file", "*.csv")])  # add initialdir=""
        if not self._filepath:
            self._file_strvar.set("Et valinnut tiedostoa")
        self._init_view()

    def _handle_info_button_press(self):
        self.destroy()
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame, text="Csv-tiedostossa tulee olla vain 2 kolumnia, joista ensimmäisessä")
        l2 = ttk.Label(
            master=self._frame, text="tulee olla nimet (Etunimi Sukunimi), ja toisessa toivotut seuralaiset")
        l3 = ttk.Label(master=self._frame, text="pilkulla eroteltuna.")
        l4 = ttk.Label(master=self._frame, text="                ")
        l5 = ttk.Label(
            master=self._frame, text="Tiedoston solujen erottimena tulle olla pilkku (,).")
        returnbutton = ttk.Button(
            master=self._frame,
            text="Takaisin",
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
            self._file_strvar.set("Et valinnut tiedostoa")
        if not self._tables_n:
            self._button_strvar.set("Et valinnut pöytien määrää")
        self.pack()
        if self._filepath and self._tables_n:
            try:
                pla = Placement(self._tables_n, ParticipantsRepo(self._filepath))
                self._placement_is_finished(pla.fin_placement)
            except Exception as eror:
                self.errors(eror)

    def errors(self, errname):
        self.destroy()
        if isinstance(errname, IndexError):
            errname = "Tiedostossa oli liian vähän tai paljon rivejä tai sarakkeita."
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text=f"Tapahtui virhe: {errname}")
        label2 = ttk.Label(master=self._frame,
                           text="Tarkista tiedostosi muoto ja sisältö")
        returnbutton = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._init_view)
        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=100, pady=10)
        label2.grid(row=1, column=0, columnspan=3,
                    sticky=constants.EW, padx=100, pady=10)
        returnbutton.grid(row=2, column=0, columnspan=3,
                          sticky=constants.EW, padx=100, pady=10)
        self.pack()
