Name:		adapta-gtk-theme
Version:	3.21.2.132
Release:	1%{?dist}
Summary:	Adapta GTK theme for GNOME
Group:		User Interface/Desktops

License:	GPLv2
URL:		https://github.com/tista500/Adapta
Source0:	https://github.com/tista500/Adapta/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	automake
BuildRequires:	gtk3-devel

%if 0%{?fedora} >= 25
Requires:	gtk3 >= 3.21
%endif

%if 0%{?fedora} == 24
Requires:	gtk3 >= 3.20
%endif

%if 0%{?fedora} == 23
Requires:	gtk3 >= 3.18
%endif

BuildArch:	noarch

%description
Adapta GTK theme for GNOME.


%prep
%setup -q -n Adapta-%{version}

%build
autoreconf --force --install --warnings=all
%configure --enable-chrome
make

%install
%{make_install}

rm -rf %{buildroot}%{_datadir}/themes/Adapta*/gtk-3.??

# fix some rpmlint issues
chmod -x %{buildroot}%{_datadir}/themes/Adapta-Nokto/index.theme
chmod -x %{buildroot}%{_datadir}/themes/Adapta/index.theme
chmod -x %{buildroot}%{_datadir}/themes/Adapta/gtk-2.0/Others/null.svg
chmod -x %{buildroot}%{_datadir}/themes/Adapta-Nokto/gtk-2.0/Others/null.svg


%files
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_datadir}/themes/Adapta*

%changelog
* Mon Jun 20 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.21.2.132-1.R
- update to 3.21.2.132

* Tue Jun  7 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.21.2.98-1.R
- update to 3.21.2.98

* Wed May 25 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.21.1.242-1.R
- update to 3.21.1.242

* Thu May 12 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.21.1.141-2.R
- enable chromium support

* Thu May 12 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.21.1.141-1.R
- update to 3.21.1.141

* Wed May  4 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.21.1.62-1.R
- update to 3.21.1.62
- added support of gtk 3.21

* Thu Apr 21 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.20.3.70-1.R
- update to 3.20.3.70

* Mon Apr 18 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.20.3.50-1.R
- update to 3.20.3.50

* Mon Apr 18 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.20.3.45-1.R
- update to 3.20.3.45

* Thu Apr 14 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.20.3.16-1.R
- initial build
