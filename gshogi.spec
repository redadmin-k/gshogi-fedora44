Name:           gshogi
Version:        0.5.1
Release:        1%{?dist}
Summary:        GTK front-end for the GNU Shogi engine

License:        GPL-3.0-or-later
URL:            https://github.com/johncheetham/gshogi
Source0:        https://github.com/johncheetham/gshogi/archive/7c4bd90.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme

Requires:       gnushogi

%description
gshogi is a GTK front-end for the gnushogi engine. It provides a user-friendly
GUI in contrast to the CLI provided by gnushogi itself.
(Debian only packages the engine, not this GUI.)

%prep
%autosetup -n gshogi-7c4bd90199c5bda61984347ea68c32521e82a637

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Remove wrongly-installed files under site-packages/usr
rm -rf %{buildroot}%{python3_sitearch}/usr

install -Dm644 gshogi.desktop %{buildroot}%{_datadir}/applications/gshogi.desktop
install -Dm644 gshogi.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gshogi.png
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/gshogi.desktop

%files
%{_bindir}/gshogi
%{python3_sitearch}/gshogi/
%{python3_sitearch}/gshogi-*.dist-info/
%{_datadir}/applications/gshogi.desktop
%{_datadir}/icons/hicolor/64x64/apps/gshogi.png
%license %{_datadir}/licenses/%{name}/LICENSE

%changelog
* Thu Aug 14 2025 Akiyoshi Kurita <redadmin@fedoraproject.org> - 0.5.1-1
- Remove extraneous files under site-packages/usr, final Fedora packaging

