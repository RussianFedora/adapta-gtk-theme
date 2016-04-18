Name:		adapta-gtk-theme
Version:	3.20.3.50
Release:	1%{?dist}
Summary:	Adapta GTK theme for Gnome
Group:		User Interface/Desktops

License:	GPLv2
URL:		https://github.com/tista500/Adapta
Source0:	https://github.com/tista500/Adapta/archive/%{version}.tar.gz

BuildRequires:	automake

Requires:	gtk3 >= 3.20

BuildArch:	noarch

%description
Adapta GTK theme for GNOME 3.20.


%prep
%setup -q -n Adapta-%{version}

%build
./autogen.sh
make

%install
%{make_install}

rm -rf %{buildroot}%{_datadir}/themes/Adapta/gtk-3.20

%files
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_datadir}/themes/Adapta*

%changelog
* Mon Apr 18 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.20.3.50-1.R
- update to 3.20.3.50

* Mon Apr 18 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.20.3.45-1.R
- update to 3.20.3.45

* Thu Apr 14 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 3.20.3.16-1.R
- initial build
