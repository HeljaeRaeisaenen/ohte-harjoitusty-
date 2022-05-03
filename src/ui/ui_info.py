'''Info screen view'''
from tkinter import ttk, constants, StringVar


class InfoView:
    def __init__(self, root, return_view, user, language) -> None:
        self._root = root
        self._frame = None
        self._return = return_view
        self._user = user
        self._language = language
        self._labl_str = StringVar()
        self._l2_str = StringVar()
        self._l3_str = StringVar()
        self._l5_str = StringVar()
        self._back_str = StringVar()
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
        if self._language == "FI":
            self._labl_str.set(
                "Csv-tiedostossa tulee olla vain 2 saraketta, joista ensimmäisessä")
            self._l2_str.set(
                "tulee olla osallistujien nimet (Etunimi Sukunimi), ja toisessa toivotut")
            self._l3_str.set("seuralaiset pilkulla eroteltuna.")
            self._l5_str.set(
                "Tiedoston solujen erottimena tulle olla pilkku (,).")
            self._back_str.set("Takaisin")
        else:
            self._labl_str.set(
                "The csv file can only have 2 columns, of which the first must have")
            self._l2_str.set(
                "the names of the participants (Firstname Lastname), and the other")
            self._l3_str.set("the wished company, separated by commas.")
            self._l5_str.set("The delimiter of the filemust be a comma (,).")
            self._back_str.set("Back")

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame, textvariable=self._labl_str)
        l2 = ttk.Label(
            master=self._frame, textvariable=self._l2_str)
        l3 = ttk.Label(master=self._frame, textvariable=self._l3_str)
        l4 = ttk.Label(master=self._frame, text="                ")
        l5 = ttk.Label(
            master=self._frame, textvariable=self._l5_str)
        returnbutton = ttk.Button(
            master=self._frame,
            textvariable=self._back_str,
            command=self._handle_return)
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

    def _handle_return(self):
        self._return(self._user, self._language)
