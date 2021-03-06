Name:           MultiMC5
Version:        1.4
Release:        4%{?dist}
Summary:        A local install wrapper for MultiMC

License:        ASL 2.0
URL:            https://multimc.org
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       zenity %{?suse_version:lib}qt5-qtbase wget xrandr
Provides:       multimc = %{version}
Provides:       MultiMC = %{version}
Provides:       multimc5 = %{version}



%description
A local install wrapper for MultiMC

%prep


%build

%install
mkdir -p %{buildroot}/opt/multimc
install -m 0644 ../ubuntu/multimc/opt/multimc/icon.svg %{buildroot}/opt/multimc/icon.svg
install -m 0755 ../ubuntu/multimc/opt/multimc/run.sh %{buildroot}/opt/multimc/run.sh
mkdir -p %{buildroot}/%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications ../ubuntu/multimc/usr/share/applications/multimc.desktop

mkdir -p %{buildroot}/%{_datadir}/metainfo
install -m 0644 ../ubuntu/multimc/usr/share/metainfo/multimc.metainfo.xml %{buildroot}/%{_metainfodir}/multimc.metainfo.xml
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 ../ubuntu/multimc/usr/share/man/man1/multimc.1 %{buildroot}/%{_mandir}/man1/multimc.1

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/multimc.metainfo.xml

%files
%dir /opt/multimc
/opt/multimc/icon.svg
/opt/multimc/run.sh
%{_datadir}/applications/multimc.desktop
%{_metainfodir}/multimc.metainfo.xml
%dir %{_mandir}/man1
%{_mandir}/man1/multimc.1*

%changelog
* Fri Jan 28 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4-4
- Update spec to support OpenSuse and conform to Fedora guidelines

* Sun Oct 03 2021 imperatorstorm <30777770+ImperatorStorm@users.noreply.github.com>
- added manpage

* Tue Jun 01 2021 kb1000 <fedora@kb1000.de> - 1.4-2
- Add xrandr to the dependencies

* Tue Dec 08 00:34:35 CET 2020 joshua-stone <joshua.gage.stone@gmail.com>
- Add metainfo.xml for improving package metadata

* Wed Nov 25 22:53:59 CET 2020 kb1000 <fedora@kb1000.de>
- Initial version of the RPM package, based on the Ubuntu package
