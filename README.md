
gshogi for Fedora 44
====================

GTK front-end for the GNU Shogi engine (gnushogi).

Overview
--------
gshogi is a simple GTK-based GUI for the GNU Shogi (gnushogi) engine.
While gnushogi provides only a command-line interface, gshogi offers a more user-friendly way to play shogi.
This package provides only the GUI; you will also need the gnushogi engine installed.

Build & Install (Fedora)
------------------------

Requirements:
- Fedora 44 (or compatible)
- gnushogi
- gcc, python3-devel, python3-setuptools, desktop-file-utils, hicolor-icon-theme

Build from SRPM:
  sudo dnf install gcc python3-devel python3-setuptools desktop-file-utils hicolor-icon-theme
  rpmbuild --rebuild gshogi-0.5.1-1.fc44.src.rpm

Or build from spec:
  rpmbuild -ba gshogi.spec

Install:
  sudo dnf install ./gshogi-0.5.1-1.fc44.x86_64.rpm

Notes
-----
- Images in this package are assumed to be public domain, but please confirm before redistribution.
- Pre-built data files (e.g., opening.bbk) are included for convenience; they can also be generated with create_book.py.

License
-------
GPL-3.0-or-later

Author
------
Packaged for Fedora by Akiyoshi Kurita (redadmin-k)

Repository
----------
https://github.com/redadmin-k/gshogi-fedora44
