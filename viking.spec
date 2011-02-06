%define name	viking
%define version	1.0.2
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Global positioning system (GPS) and mapping manager
Version: 	%{version}
Release: 	%{release}

Source:		http://download.sourceforge.net/viking/%{name}-%{version}.tar.gz
URL:		http://viking.sourceforge.net
License:	GPLv2+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgtk+2.0-devel
BuildRequires:	expat-devel
BuildRequires:	curl-devel
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	gpsd-devel
BuildRequires:	gnome-doc-utils >= 0.3.2
Requires:	gpsbabel

%description
Viking is a free/open source program to manage GPS data. You can import and
plot tracks and waypoints, show Terraserver maps under it, add coordinate
lines, make new tracks and waypoints, hide different things, etc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README COPYING TODO
%{_bindir}/%name
%{_bindir}/%name-remote
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/omf/%name/viking-C.omf
