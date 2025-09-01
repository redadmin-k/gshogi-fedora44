%global commit 7c4bd90199c5bda61984347ea68c32521e82a637
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20250818

Name:           gshogi
Version:        0.5.1^%{snapshotdate}.git%{shortcommit}
Release:        7%{?dist}
Summary:        A graphical GTK interface for playing GNU Shogi

License:        GPL-3.0-or-later
URL:            https://github.com/johncheetham/gshogi
Source0: 	https://github.com/johncheetham/gshogi/archive/%{commit}/gshogi-%{commit}.tar.gz

# If any Fedora-specific bugfixes, add Patch here. No Patch for artifact removal.
Patch0:         0001-drop-data_files-and-ez_setup.patch

# For compiling the bundled gnushogi C engine
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  gtk3-devel
BuildRequires:  desktop-file-utils
# Core package for GObject Introspection, needed for %%check
BuildRequires:  gobject-introspection
# Python bindings for gobject/cairo, needed for %%check
BuildRequires:  python3-gobject
BuildRequires:  python3-cairo

# Manually added runtime deps, as they are loaded dynamically
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       hicolor-icon-theme

# gshogi bundles its own copy of the gnushogi engine sources
Provides:       bundled(gnushogi)

%description
gshogi is a GTK-based graphical front end for the GNU Shogi engine.
It provides a simple user interface to play shogi against the computer.

%prep
%autosetup -p1 -n gshogi-%{commit}
rm ez_setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l gshogi
install -Dm0644 gshogi.desktop %{buildroot}%{_datadir}/applications/gshogi.desktop
install -Dm0644 gshogi.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gshogi.png

%check
%pyproject_check_import
desktop-file-validate %{buildroot}%{_datadir}/applications/gshogi.desktop

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/gshogi
%{_datadir}/applications/gshogi.desktop
%{_datadir}/icons/hicolor/64x64/apps/gshogi.png

%changelog
* Thu Aug 21 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1^20250818.git7c4bd90-7
- Fix license file name from COPYING to LICENSE

* Thu Aug 21 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1^20250818.git7c4bd90-6
- Add gobject-introspection to BuildRequires to finally fix %%check

* Thu Aug 21 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1^20250818.git7c4bd90-5
- Add python3-gobject and python3-cairo to BuildRequires to fix %%check

* Thu Aug 21 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1^20250818.git7c4bd90-4
- Add explicit runtime Requires for python3-gobject and python3-cairo
- Clean up BuildRequires and rely more on pyproject macros
- Add %%license file to package

* Wed Aug 20 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1^20250818.git7c4bd90-3
- Use Patch0 with %%autosetup -p1; drop data_files and ez_setup.py via patch
- Run desktop-file-validate in %%check; use %%pyproject_buildrequires
- Add Provides: bundled(gnushogi) since gshogi ships its own engine sources

