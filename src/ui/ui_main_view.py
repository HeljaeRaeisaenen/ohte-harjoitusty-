'''View once user has logged in'''
from tkinter import filedialog, ttk, constants, StringVar
from tkinter.simpledialog import askinteger
from placement import Placement
from readwrite import filewrite


class Begin:
    '''if login was succesful, show this view'''

    def __init__(self, root, placement_is_finished):
        self._root = root
        self._current_view = None
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
        if self._current_view:
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
        tablesbutton = ttk.Button(
            master=self._frame,
            text="Pöytien määrä",
            command=self._handle_tables_button_press)
        tables_label = ttk.Label(
            master=self._frame, text="Kuinka monta pöytää?")
        filesuccess = ttk.Label(
            master=self._frame, textvariable=self._file_strvar, foreground="red")
        buttonsuccess = ttk.Label(
            master=self._frame, textvariable=self._button_strvar, foreground="red")
        beginbutton = ttk.Button(
            master=self._frame,
            text="Aloita",
            command=self._handle_begin_button_press)

        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)
        openbutton.grid(row=1, column=0, padx=200, pady=10)
        filesuccess.grid(row=2, column=0, padx=200, pady=10)
        tables_label.grid(row=3, column=0, padx=200, pady=10)
        tablesbutton.grid(row=4, column=0, padx=200, pady=10)
        buttonsuccess.grid(row=5, column=0, padx=200, pady=10)
        beginbutton.grid(row=6, column=0, padx=200, pady=50)

        self.pack()

    def _tables_n_verification_view(self):
        self.destroy()

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Oletko varma?")
        label2 = ttk.Label(master=self._frame, text="{self._tables_n} pöytää?")
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
        if self._tables_n > 5:
            self._tables_n_verification_view()
        self._init_view()
            

    def _handle_open_button_press(self):
        self._filepath = filedialog.askopenfilename(
            filetypes=[("CSV file", "*.csv")])  # add initialdir=""
        if self._filepath:
            filesuccess = ttk.Label(
                master=self._frame, text="Tiedosto valittu", foreground="blue")
            filesuccess.grid(row=2, column=0, padx=20, pady=20)
            self.pack()

    def _handle_begin_button_press(self):
        if not self._filepath:
            self._file_strvar.set("Et valinnut tiedostoa")
        if not self._tables_n:
            self._button_strvar.set("Et valinnut pöytien määrää")
        self.pack()
        if self._filepath and self._tables_n:
            pla = Placement(self._tables_n, self._filepath)
        # What now?? todo
        #
        #
        #
            self._placement_is_finished(pla.finished_placement)


class Finished:
    '''View where user saves the file and logs out'''

    def __init__(self, root, file):
        self._root = root
        self._frame = None
        self._file = file
        self._init_view()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Destroy the view'''
        self._frame.destroy()

    def _init_view(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Valmista!")
        label1 = ttk.Label(master=self._frame,
                           text="Tiedosto tallentuu csv-muodossa")
        savebutton = ttk.Button(
            master=self._frame,
            text="Tallenna tiedosto",
            command=self._handle_save_button_press)
        logoutbutton = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._handle_logout_button_press
        )
        label.grid(row=0, column=0, columnspan=3,
                   sticky=constants.EW, padx=200, pady=10)
        savebutton.grid(row=2, column=0, padx=200, pady=10)
        label1.grid(row=1, column=0, padx=200, pady=10)
        logoutbutton.grid(row=4, column=0, padx=200, pady=10)
        self.pack()

    def _handle_save_button_press(self):
        savepath = filedialog.asksaveasfilename(
            defaultextension="*.csv", filetypes=[("CSV file", "*.csv")])
        if savepath:
            filewrite(self._file, savepath)
            writing_success_label = ttk.Label(
                master=self._frame, text="Tallennus onnistui", foreground="blue")
            writing_success_label.grid(row=3, column=0, padx=200, pady=10)
            self.pack()

    def _handle_logout_button_press(self):
        pass
