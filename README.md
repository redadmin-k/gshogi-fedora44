gshogi for Fedora 44
====================

GTK front-end for the GNU Shogi engine (gnushogi).

Overview
--------
gshogi is a simple GTK-based GUI for the GNU Shogi (gnushogi) engine.
While gnushogi provides only a command-line interface, gshogi offers a more user-friendly way to play shogi.

Build and Install (RPM)
-----------------------

Requirements:

- Fedora 44 (or compatible)
- gnushogi
- gcc, python3-devel, python3-setuptools, desktop-file-utils, hicolor-icon-theme

Build from source RPM:

  # Install dependencies
  sudo dnf install gcc python3-devel python3-setuptools desktop-file-utils hicolor-icon-theme

  # Rebuild the package (if you have SRPM)
  rpmbuild --rebuild gshogi-0.1-1.fc44.src.rpm

  # Or build directly from spec
  rpmbuild -ba gshogi.spec

Install the built RPM:

  sudo dnf install ./gshogi-0.1-1.fc44.x86_64.rpm

License
-------
GPL-3.0-or-later

Author
------
Packaged for Fedora by Akiyoshi Kurita (redadmin-k)

Repository
----------
https://github.com/redadmin-k/gshogi-fedora44

