'''Backbone of the UI'''
from ui.ui_login import Login
from ui.ui_firstview import First
from ui.ui_begin_placement import Begin
from ui.ui_finish_placement import Finished
from ui.ui_info import InfoView


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
        self._current_view = Login(self._root, self._show_first_view)
        self._current_view.pack()

    def _show_first_view(self, user, language):
        self._destroy_current_view()
        self._current_view = First(
            self._root, user, self._show_main_view, self._show_info_view, self._show_first_view, self._show_login_view, language)

    def _show_main_view(self, user, language):
        self._destroy_current_view()
        self._current_user = user
        self._current_view = Begin(
            self._root, user, self._show_info_view, self._show_main_view, self._show_finished_view, language)

    def _show_finished_view(self, user, file_to_write, wish_average, language):
        self._destroy_current_view()
        self._current_view = Finished(
            self._root, user, file_to_write, wish_average, self._show_main_view, self._show_login_view, language)

    def _show_info_view(self, return_view, user, language):
        self._destroy_current_view()
        self._current_view = InfoView(self._root, return_view, user, language)
