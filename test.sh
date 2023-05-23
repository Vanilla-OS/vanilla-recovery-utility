#!/bin/bash
rm -rf run mesonbuild
meson --prefix $PWD/run mesonbuild
ninja -C mesonbuild
ninja -C mesonbuild install

XDG_DATA_DIRS=$PWD/run/share:$XDG_DATA_DIRS ./run/bin/recovery-utility

