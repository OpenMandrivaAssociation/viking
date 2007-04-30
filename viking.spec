%define name	viking
%define version	0.1.2
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Global positioning system (GPS) data manager
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/viking/%{name}-%{version}.tar.bz2
URL:		http://gpsmaps.org/viking/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgtk+2.0-devel
BuildRequires:	expat-devel

%description
Viking is a free/open source program to manage GPS data. You can import and
plot tracks and waypoints, show Terraserver maps under it, add coordinate
lines, make new tracks and waypoints, hide different things, etc. 

%prep
%setup -q

%build
%configure2_5x
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" \
icon="more_applications_other_section.png" \
needs="x11" \
title="Viking" \
longtitle="GPS data manager" \
section="More Applications/Other"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README COPYING TODO doc/M*
%{_bindir}/%name
%{_bindir}/%name-remote
%{_menudir}/%name
