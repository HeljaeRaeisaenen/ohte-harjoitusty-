'''Backbone of the UI'''
from ui.ui_login import Login
from ui.ui_begin import Begin
from ui.ui_finish import Finished
from ui.ui_logout import Logout
from time import sleep


class UI:
    '''User interface.
    Attributes:
        _root = the window
        _current_view = the view currently shown
        _current_user = the user who is logged in
        '''

    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._current_user = None

    def start(self):
        '''Start the UI'''
        self._destroy_current_view()
        self._show_login_view()

    def _destroy_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_login_view(self):
        self._destroy_current_view()
        self._current_view = Login(self._root, self._show_main_view)
        self._current_view.pack()

    def _show_main_view(self, user, language):
        self._destroy_current_view()
        self._current_user = user
        self._current_view = Begin(
            self._root, user, self._show_finished_view, language)

    def _show_finished_view(self, user, file_to_write, language):
        self._destroy_current_view()
        self._current_view = Finished(
            self._root, user, file_to_write, self._show_main_view, self.show_logout_view, language)

    def show_logout_view(self, language):
        self._destroy_current_view()
        self._current_view = Logout(self._root, language)
        self._current_user = None
        self._current_view.pack()
        sleep(1)
        self._show_login_view()
