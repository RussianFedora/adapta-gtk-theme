Name:           adapta-gtk-theme
Version:        3.93.0.12
Release:        1%{?dist}.R
Summary:        An adaptive Gtk+ theme based on Material Design Guidelines

License:        GPLv2 and CC-BY-SA
URL:            https://github.com/adapta-project/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  inkscape >= 0.91
BuildRequires:  parallel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  sassc    >= 3.3

Requires:       gnome-themes-standard
Requires:       google-noto-sans-fonts
Requires:       google-roboto-fonts
Requires:       gtk2-engines

Obsoletes:	adapta-gtk-theme < 3.92.2.63

%description
%{summary}.


%package        gedit
Summary:        Gedit style addon for %{name}

Requires:       %{name} == %{version}-%{release}
Requires:       gtksourceview3

%if 0%{?fedora} || 0%{?rhel} >= 8
Supplements:    (%{name} and gtksourceview3)
%endif

%description    gedit
Gedit style addon for %{name}.


%package        plank
Summary:        Plank dock theme addon for %{name}

Requires:       %{name} == %{version}-%{release}
%if 0%{?fedora}
Requires:       plank
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
Supplements:    (%{name} and plank)
%endif

%description    plank
Plank dock theme addon for %{name}.


%prep
%autosetup
%{_bindir}/autoreconf -fiv


%build
%configure \
  --disable-silent-rules \
  --disable-unity        \
  --enable-chrome        \
  --enable-gtk_next      \
  --enable-plank         \
  --enable-telegram
%make_build


%install
%make_install
for f in COPYING LICENSE_CC_BY_SA4 README.md; do
  %{_bindir}/find %{buildroot} -type f -name "$f" -print -delete
done

# Add the gedit styles addon to the right location.
%{__mkdir} -p %{buildroot}%{_datadir}/gtksourceview-3.0/styles
%{__ln_s} %{_datadir}/themes/Adapta/gedit/adapta.xml \
  %{buildroot}%{_datadir}/gtksourceview-3.0/styles/adapta.xml

# Add the plank addon to the right location.
%{__mkdir} -p %{buildroot}%{_datadir}/plank/themes/Adapta
%{__ln_s} %{_datadir}/themes/Adapta/plank/dock.theme \
  %{buildroot}%{_datadir}/plank/themes/Adapta/dock.theme

%fdupes -s %{buildroot}%{_datadir}/themes


%files
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/Adapta*


%files          gedit
%doc extra/gedit/README.md
%{_datadir}/gtksourceview-3.0/styles/adapta.xml


%files          plank
%if 0%{?fedora}
%{_datadir}/plank/themes/Adapta
%else
%{_datadir}/plank
%endif


%changelog
* Mon Jan  8 2018 Arkady L. Shane <ashejn@russianfedora.pro> - 3.93.0.12-1.R
- update to 3.93.0.12

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 3.92.2.63-1
- Initial import (#1529593)

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 3.92.2.63-0.4
- Fix Summary and %%description for plank sub-package

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 3.92.2.63-0.3
- Fix source url

* Thu Dec 28 2017 Björn Esser <besser82@fedoraproject.org> - 3.92.2.63-0.2
- Add sub-packages for gedit / xed and plank

* Thu Dec 28 2017 Björn Esser <besser82@fedoraproject.org> - 3.92.2.63-0.1
- Initial rpm release (#1529593)
