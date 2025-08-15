%global commit 7c4bd90199c5bda61984347ea68c32521e82a637

Name:           gshogi
Version:        0.5.1
Release:        1%{?dist}
Summary:        GTK front-end for the GNU Shogi engine

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
gshogi is a GTK-based graphical front end for the GNU Shogi engine. It provides
a simple user interface to play shogi, in contrast to the command-line
interface offered by the engine itself.

%prep
%autosetup -n gshogi-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Clean up old setuptools bug: site-packages/usr/
rm -rf %{buildroot}%{python3_sitearch}/usr

# Fix .desktop: no extension for Icon, add GTK category
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --set-icon=gshogi \
  --add-category=GTK \
  gshogi.desktop

# Place the icon
install -Dm0644 gshogi.png \
  %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gshogi.png

%pyproject_save_files gshogi

# License and doc
install -Dm0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/gshogi
%{_datadir}/applications/gshogi.desktop
%{_datadir}/icons/hicolor/64x64/apps/gshogi.png
%license %{_datadir}/licenses/%{name}/LICENSE
%doc README.rst

%changelog
* Fri Aug 15 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1-1
- Switch to pyproject macros, fix doc and icon handling, description wrapped.
- Provides: bundled(gnushogi) and build fixes per review.

