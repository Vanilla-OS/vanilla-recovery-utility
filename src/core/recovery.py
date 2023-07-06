# recovery.py
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

import os
import json
import tempfile
import subprocess

from enum import Enum
from pathlib import Path


class RecoveryResult(Enum):
    SUCCESS = 0
    ALBIUS_ERROR = 1
    NO_DISKS_FOUND = 2
    DISKS_IMPROPERLY_CONFIGURED = 3

part_labels: list[str] = ['vos-a', 'vos-b', 'vos-boot']


class Recovery:
    def __init__(self) -> None:
        self.disks: dict[str, str] = {}

    def check_disks(self) -> RecoveryResult:
        for label in part_labels:
            if device := self.get_device(label):
                self.disks[label] = device
            else:
                return RecoveryResult.DISKS_IMPROPERLY_CONFIGURED

        if not self.disks:
            return RecoveryResult.NO_DISKS_FOUND

        return RecoveryResult.SUCCESS

    def generate_recipe(self) -> Path:
        recipe = {}
        # TODO: implement recipe generation
        
        temp = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp.write(json.dumps(recipe))
        temp.close()

        return Path(temp.name)

    def reset(self) -> RecoveryResult:
        recipe: Path = self.generate_recipe()

        try:
            subprocess.run(['albius', str(recipe)], check=True)
        except subprocess.CalledProcessError:
            return RecoveryResult.ALBIUS_ERROR
            
        return RecoveryResult.SUCCESS
