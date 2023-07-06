pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
coredir = join_paths(pkgdatadir, 'recovery_utility/core')

sources = [
  '__init__.py',
  'recovery.py',
]

install_data(sources, install_dir: coredir)