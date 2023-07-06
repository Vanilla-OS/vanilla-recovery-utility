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

from gi.repository import Gtk, Adw, GLib


@Gtk.Template(resource_path='/org/vanillaos/RecoveryUtility/gtk/window.ui')
class RecoveryUtilityWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'RecoveryUtilityWindow'

    stack_main: Adw.ViewStack = Gtk.Template.Child()
    headerbar: Adw.HeaderBar = Gtk.Template.Child()

    btn_disclaimer_cancel: Gtk.Button = Gtk.Template.Child()
    btn_disclaimer_agree: Gtk.Button = Gtk.Template.Child()

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
        self.row_browser.connect('activated', self.__on_cmd_action, 'epiphany-browser https://handbook.vanillaos.org')
        self.row_disks.connect('activated', self.__on_cmd_action, 'gparted')
        self.row_fsck.connect('activated', self.__on_cmd_action, 'kgx -e echo "Not implemented yet"')
        self.row_reset.connect('activated', self.__on_reset_row_activate)
        self.row_shell.connect('activated', self.__on_shell_row_activate, 'kgx')
        self.btn_reset_cancel.connect('clicked', self.__on_reset_action)
        self.btn_reset_confirm.connect('clicked', self.__on_reset_action)
        self.btn_completed_cancel.connect('clicked', self.__on_completed_action)
        self.btn_completed_restart.connect('clicked', self.__on_completed_action)
        self.btn_fail_cancel.connect('clicked', self.__on_fail_cancel)

    def __on_disclaimer_action(self, button: Gtk.Button):
        if button == self.btn_disclaimer_cancel:
            self.close()
        elif button == self.btn_disclaimer_agree:
            self.stack_main.set_visible_child_name('welcome')
            self.headerbar.add_css_class('flat')

    def __on_cmd_action(self, button: Gtk.Button, cmd: str):
        GLib.spawn_command_line_async(cmd)

    def __on_reset_row_activate(self, row: Adw.ActionRow):
        self.stack_main.set_visible_child_name('reset')

    def __on_reset_action(self, button: Gtk.Button):
        if button == self.btn_reset_cancel:
            self.stack_main.set_visible_child_name('welcome')
        elif button == self.btn_reset_confirm:
            self.stack_main.set_visible_child_name('completed')

    def __on_completed_action(self, button: Gtk.Button):
        if button == self.btn_completed_cancel:
            self.stack_main.set_visible_child_name('welcome')
        elif button == self.btn_completed_restart:
            self.stack_main.set_visible_child_name('welcome')

    def __on_fail_cancel(self, button: Gtk.Button):
        self.stack_main.set_visible_child_name('welcome')
