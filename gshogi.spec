%global commit 7c4bd90199c5bda61984347ea68c32521e82a637

Name:           gshogi
Version:        0.5.1
Release:        1%{?dist}
Summary:        GTK front end for the GNU Shogi engine

License:        GPL-3.0-or-later
URL:            https://github.com/johncheetham/gshogi
Source0:        https://github.com/johncheetham/gshogi/archive/%{commit}/gshogi-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-gobject
BuildRequires:  gtk3

Provides:       bundled(gnushogi)

%description
gshogi is a GTK-based graphical front end for the GNU Shogi engine.
It provides a simple user interface to play shogi, in contrast to the
command-line interface offered by the engine itself.

%prep
%autosetup -n gshogi-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Clean up possible wrongly installed files by old setuptools
rm -rf %{buildroot}%{python3_sitearch}/usr

# Desktop entry: fix icon key and add GTK category
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --set-icon=gshogi \
  --add-category=GTK \
  gshogi.desktop

# Place the icon in the correct directory
install -Dm0644 gshogi.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gshogi.png

# Save python-installed files and license
%pyproject_save_files -l gshogi

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/gshogi
%{_datadir}/applications/gshogi.desktop
%{_datadir}/icons/hicolor/64x64/apps/gshogi.png
%doc README.rst
%license LICENSE

%changelog
* Fri Aug 15 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1-1
- All Fedora review/rpmlint issues fixed: 80-char description wrap,
  license/source audit, hicolor-icon-theme, doc/readme

