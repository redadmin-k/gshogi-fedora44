%global forgeurl https://github.com/johncheetham/gshogi
%global commit 7c4bd90199c5bda61984347ea68c32521e82a637
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20250818

%forgemeta

Name:           gshogi
Version:        0.5.1^%{snapshotdate}.git%{shortcommit}
Release:        2%{?dist}
Summary:        GTK front end for the GNU Shogi engine

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource0}
Patch0:         0001-drop-data_files-and-ez_setup.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python3-gobject
BuildRequires:  gobject-introspection
BuildRequires:  gtk3

# gshogi bundles its own copy of the gnushogi engine sources
Provides:       bundled(gnushogi)

%description
gshogi is a GTK-based graphical front end for the GNU Shogi engine.
It provides a simple user interface to play shogi.

%prep
# %{forgesetupargs} は %forgemeta が作る展開先名を使う
%forgeautosetup -p1

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
%{_bindir}/gshogi
%{_datadir}/applications/gshogi.desktop
%{_datadir}/icons/hicolor/64x64/apps/gshogi.png
%doc README.rst

%changelog
* Tue Aug 19 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1^20250818.git7c4bd90-2
- Switch to Forge macros (%forgemeta, %{forgesource0}, %forgeautosetup) to stabilize source fetching
- Keep Patch0: drop ez_setup.py and data_files; run desktop-file-validate in %%check
- Use %%pyproject_buildrequires; add Provides: bundled(gnushogi)

