%define name	viking
%define version	0.1.3
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Global positioning system (GPS) and mapping manager
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/viking/%{name}-%{version}.tar.bz2
URL:		http://gpsmaps.org/viking/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgtk+2.0-devel
BuildRequires:	expat-devel
Requires:	gpsbabel

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
section="More Applications/Other" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Viking
Comment=GPS data manager
Exec=%{name}
Icon=more_applications_other_section.png
Terminal=false
Type=Application
Categories=GTK;DataVisualization;Geography;X-MandrivaLinux-MoreApplications-Other;
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
%{_datadir}/applications/*
%{_menudir}/%name
