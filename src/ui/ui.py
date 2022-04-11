'''Backbone of the UI'''
from ui.ui_login import Login
from ui.ui_main_view import Begin, Finished


class UI:
    '''user interface'''

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def _destroy_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_login_view(self):
        self._current_view = Login(self._root, self._show_main_view)
        self._current_view.pack()

    def start(self):
        self._destroy_current_view()
        self._show_login_view()

    def _show_main_view(self):
        self._destroy_current_view()
        self._current_view = Begin(self._root, self._show_finished_view)

    def _show_finished_view(self, file_to_write):
        self._destroy_current_view()
        self._current_view = Finished(self._root, file_to_write)
