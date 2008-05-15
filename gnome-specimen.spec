Summary:	GNOME Specimen - a tool for previewing and comparing fonts
Name:		gnome-specimen
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://uwstopia.nl/geek/projects/gnome-specimen/releases/%{name}-%{version}.tar.gz
# Source0-md5:	c1af774ee4ab5bd1289699b4094368b3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.36.2
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-gnome-devel >= 2.6.0
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool for previewing and comparing files.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{py_sitedir}/specimen/*.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-specimen.schemas
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gnome-specimen.schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gnome-specimen
%{_datadir}/%{name}
%{_desktopdir}/gnome-specimen.desktop
%{_iconsdir}/hicolor/*/apps/gnome-specimen.png
%{_iconsdir}/hicolor/*/apps/gnome-specimen.svg
%dir %{py_sitedir}/specimen
%{py_sitedir}/specimen/*.py[co]
%{_sysconfdir}/gconf/schemas/gnome-specimen.schemas
