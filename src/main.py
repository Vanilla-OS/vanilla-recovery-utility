# main.py
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

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from typing import Callable

from .window import RecoveryUtilityWindow


class RecoveryUtilityApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self) -> None:
        super().__init__(
            application_id='org.vanillaos.RecoveryUtility',
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS
        )
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self) -> None:
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win: RecoveryUtilityWindow = self.props.active_window
        if not win:
            win: RecoveryUtilityWindow = RecoveryUtilityWindow(application=self)
        win.present()

    def on_about_action(self, *args) -> None:
        """Callback for the app.about action."""
        about: Adw.AboutWindow = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name='recovery-utility',
            application_icon='org.vanillaos.RecoveryUtility',
            developer_name='Mirko',
            version='0.1.0',
            developers=['Mirko Brombin'],
            copyright='© 2023 Mirko Brombin and Vanilla OS Contributors'
        )
        about.present()

    def on_preferences_action(self, *args) -> None:
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name: str, callback: Callable, shortcuts: list = None) -> None:
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action: Gio.SimpleAction = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version: str) -> int:
    """The application's entry point."""
    app: RecoveryUtilityApplication = RecoveryUtilityApplication()
    return app.run(sys.argv)
