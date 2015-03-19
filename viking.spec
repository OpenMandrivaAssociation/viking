Name:		viking
Summary:	Global positioning system (GPS) and mapping manager
Version:	1.5.1
Release:	1

Source0:	http://download.sourceforge.net/viking/%{name}-%{version}.tar.bz2
URL:		http://viking.sourceforge.net
License:	GPLv2+
Group:		Communications
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	expat-devel
BuildRequires:	curl-devel
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	magic-devel
BuildRequires:	gpsd-devel
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.3.2
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
%configure
%make

%install
%makeinstall_std
%find_lang %name --with-gnome

%files -f %name.lang
%doc README COPYING TODO
%{_bindir}/%name
#%{_bindir}/%name-remote
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/%name
