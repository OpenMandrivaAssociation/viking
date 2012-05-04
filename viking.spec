%define name	viking
%define version	1.3
%define release %mkrel 1

Name:		%{name}
Summary: 	Global positioning system (GPS) and mapping manager
Version: 	%{version}
Release: 	%{release}

Source0:	http://download.sourceforge.net/viking/%{name}-%{version}.tar.gz
URL:		http://viking.sourceforge.net
License:	GPLv2+
Group:		Communications
BuildRequires:	gtk+2-devel
BuildRequires:	expat-devel
BuildRequires:	curl-devel
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	gpsd-devel
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	pkgconfig(libexif)
BuildRequires:	scrollkeeper
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
%makeinstall_std
%find_lang %name --with-gnome

%files -f %name.lang
%defattr(-,root,root)
%doc README COPYING TODO
%{_bindir}/%name
#%{_bindir}/%name-remote
%{_datadir}/applications/*
%{_datadir}/icons/*
#%{_datadir}/omf/%name/viking-C.omf
