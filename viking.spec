%define name	viking
%define version	0.9.2
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Global positioning system (GPS) and mapping manager
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/viking/%{name}-%{version}.tar.gz
URL:		http://gpsmaps.org/viking/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgtk+2.0-devel
BuildRequires:	expat-devel curl-devel
BuildRequires:	ImageMagick
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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Viking
Comment=GPS data manager
Exec=%{name}
Icon=%name.png
Terminal=false
Type=Application
Categories=GTK;DataVisualization;Geography;Science;
EOF

# icons
mkdir -p %buildroot/%{_miconsdir}
convert -size 16x16 src/icons/viking_icon.png %buildroot/%{_miconsdir}/%name.png
mkdir -p %buildroot/%{_iconsdir}
convert -size 32x32 src/icons/viking_icon.png %buildroot/%{_iconsdir}/%name.png
mkdir -p %buildroot/%{_liconsdir}
convert -size 48x48 src/icons/viking_icon.png %buildroot/%{_liconsdir}/%name.png

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
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
