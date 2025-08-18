%global commit 7c4bd90199c5bda61984347ea68c32521e82a637
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20250818

Name:           gshogi
Version:        0.5.1^%{snapshotdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        GTK front end for the GNU Shogi engine

License:        GPL-3.0-or-later
URL:            https://github.com/johncheetham/gshogi
Source0:        https://github.com/johncheetham/gshogi/archive/%{commit}/gshogi-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(pip)
BuildRequires:  python3-gobject

Requires:       hicolor-icon-theme
Requires:       python3-gobject

Provides:       bundled(gnushogi)

%description
gshogi is a GTK-based graphical front end for the GNU Shogi engine.
It provides a simple user interface to play shogi, in contrast to the
command-line interface offered by the engine itself.

%prep
%autosetup -n gshogi-%{commit}
# Remove ez_setup cruft and data_files kwarg (handled manually below)
sed -i -e '/^[[:space:]]*import[[:space:]]\+ez_setup/d' \
       -e '/^[[:space:]]*from[[:space:]]\+ez_setup[[:space:]]\+import[[:space:]]\+.*/d' \
       -e '/ez_setup[.]use_setuptools[[:space:]]*(/d' \
       -e '/^[[:space:]]*data_files[[:space:]]*=[[:space:]]*data_files[[:space:]]*,[[:space:]]*$/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l gshogi
install -Dm0644 gshogi.desktop %{buildroot}%{_datadir}/applications/gshogi.desktop
install -Dm0644 gshogi.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gshogi.png
desktop-file-validate %{buildroot}%{_datadir}/applications/gshogi.desktop

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/gshogi
%{_datadir}/applications/gshogi.desktop
%{_datadir}/icons/hicolor/64x64/apps/gshogi.png
%doc README.rst

%changelog
* Mon Aug 18 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1^20250818.git%{shortcommit}-1
- Remove data_files kwarg from setup(); package CLI; install/validate desktop+icon.

