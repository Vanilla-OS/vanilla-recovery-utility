# window.py
#
# Copyright 2023 Mirko
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-only

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/vanillaos/RecoveryUtility/gtk/window.ui')
class RecoveryUtilityWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'RecoveryUtilityWindow'

    stack_main: Adw.ViewStack = Gtk.Template.Child()
    headerbar: Adw.HeaderBar = Gtk.Template.Child()

    btn_disclaimer_cancel: Gtk.Button = Gtk.Template.Child()
    btn_disclaimer_agree: Gtk.Button = Gtk.Template.Child()

    btn_reset: Gtk.Button = Gtk.Template.Child()
    btn_disks: Gtk.Button = Gtk.Template.Child()
    btn_shell: Gtk.Button = Gtk.Template.Child()
    btn_browser: Gtk.Button = Gtk.Template.Child()
    btn_fsck: Gtk.Button = Gtk.Template.Child()
    row_reset: Adw.ActionRow = Gtk.Template.Child()
    row_disks: Adw.ActionRow = Gtk.Template.Child()
    row_shell: Adw.ActionRow = Gtk.Template.Child()
    row_browser: Adw.ActionRow = Gtk.Template.Child()
    row_fsck: Adw.ActionRow = Gtk.Template.Child()

    btn_reset_cancel: Gtk.Button = Gtk.Template.Child()
    btn_reset_confirm: Gtk.Button = Gtk.Template.Child()

    btn_completed_cancel: Gtk.Button = Gtk.Template.Child()
    btn_completed_restart: Gtk.Button = Gtk.Template.Child()

    btn_fail_cancel: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__build_ui()

    def __build_ui(self):
        self.btn_disclaimer_cancel.connect('clicked', self.__on_disclaimer_action)
        self.btn_disclaimer_agree.connect('clicked', self.__on_disclaimer_action)

    def __on_disclaimer_action(self, button: Gtk.Button):
        if button == self.btn_disclaimer_cancel:
            self.close()
        elif button == self.btn_disclaimer_agree:
            self.stack_main.set_visible_child_name('welcome')
            self.headerbar.add_css_class('flat')
