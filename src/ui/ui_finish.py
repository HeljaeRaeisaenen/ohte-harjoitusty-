'''View once the program has done its thing'''

from tkinter import filedialog, ttk, constants, StringVar
from readwrite import filewrite


class Finished:
    '''View where user saves the file and logs out'''

    def __init__(self, root, file, finish, language):
        self._root = root
        self._frame = None
        self._file = file
        self._finish_logout = finish
        self._languge = language
        self._label_str = StringVar()
        self._l1_str = StringVar()
        self._save_str = StringVar()
        self._out_strvar = StringVar()
        if language == "FI":
            self._init_strvars_fi()
        if language == "EN":
            self._init_strvars_en()

        self._init_view()

    def pack(self):
        '''Pack the view'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''Destroy the view'''
        self._frame.destroy()

    def _init_strvars_fi(self):
        self._label_str.set("Valmista!")
        self._l1_str.set("Tiedosto tallentuu csv-muodossa")
        self._save_str.set("Tallenna tiedosto")
        self._out_strvar.set("Kirjaudu ulos")

    def _init_strvars_en(self):
        self._label_str.set("All done!")
        self._l1_str.set("The file will be saved in csv format.")
        self._save_str.set("Save file")
        self._out_strvar.set("Logout")

    def _init_view(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, textvariable=self._label_str)
        label1 = ttk.Label(master=self._frame,
                           textvariable=self._l1_str)
        savebutton = ttk.Button(
            master=self._frame,
            textvariable=self._save_str,
            command=self._handle_save_button_press)
        logoutbutton = ttk.Button(
            master=self._frame,
            textvariable=self._out_strvar,
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
            defaultextension=".csv", filetypes=[("CSV file", "*.csv")])
        if savepath:
            filewrite(self._file, savepath)
            writing_success_label = ttk.Label(
                master=self._frame, text="Tallennus onnistui", foreground="blue")
            writing_success_label.grid(row=3, column=0, padx=200, pady=10)
            self.pack()

    def _handle_logout_button_press(self):
        self._finish_logout(self._languge)
