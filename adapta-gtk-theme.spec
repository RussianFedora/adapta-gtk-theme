Name:		adapta-gtk-theme
Version:	3.21.1.141
Release:	1%{?dist}
Summary:	Adapta GTK theme for GNOME
Group:		User Interface/Desktops

License:	GPLv2
URL:		https://github.com/tista500/Adapta
Source0:	https://github.com/tista500/Adapta/archive/%{version}.tar.gz

BuildRequires:	automake

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
./autogen.sh
make

%install
%{make_install}

%if 0%{?fedora} >= 25
rm -rf %{buildroot}%{_datadir}/themes/Adapta/gtk-3.0
mv %{buildroot}%{_datadir}/themes/Adapta/gtk-3.22 \
    %{buildroot}%{_datadir}/themes/Adapta/gtk-3.0
%endif

%if 0%{?fedora} == 24
rm -rf %{buildroot}%{_datadir}/themes/Adapta/gtk-3.0
mv %{buildroot}%{_datadir}/themes/Adapta/gtk-3.20 \
    %{buildroot}%{_datadir}/themes/Adapta/gtk-3.0
%endif

%if 0%{?fedora} == 23
rm -rf %{buildroot}%{_datadir}/themes/Adapta/gtk-3.20
%endif

%files
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_datadir}/themes/Adapta*

%changelog
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