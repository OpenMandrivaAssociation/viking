Name:		viking
Summary:	Global positioning system (GPS) and mapping manager
Version:	1.3.2.1
Release:	2

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
%configure2_5x
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
%if %{mdvver} < 201200
%{_datadir}/omf/%name/viking-C.omf
%endif


%changelog
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.3-1mdv2011.0
+ Revision: 796239
- fix for backporting

* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.3-1
+ Revision: 796111
- update to 1.3

* Fri Jun 17 2011 Funda Wang <fwang@mandriva.org> 1.2.1-1
+ Revision: 685732
- update to new version 1.2.1

* Fri Jun 03 2011 Funda Wang <fwang@mandriva.org> 1.2-1
+ Revision: 682543
- update to new version 1.2

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.1-1
+ Revision: 645477
- update to new version 1.1

  + Funda Wang <fwang@mandriva.org>
    - update to new version 1.0.2

* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 609622
- update to new version 1.0.1

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 1.0-1mdv2011.0
+ Revision: 602212
- new version 1.0

* Wed Sep 08 2010 Funda Wang <fwang@mandriva.org> 0.9.95-1mdv2011.0
+ Revision: 576731
- new version 0.9.95

* Fri Apr 16 2010 Funda Wang <fwang@mandriva.org> 0.9.93-1mdv2010.1
+ Revision: 535310
- update to new version 0.9.93

* Wed Mar 17 2010 Funda Wang <fwang@mandriva.org> 0.9.92-1mdv2010.1
+ Revision: 522690
- update to new version 0.9.92

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 0.9.91-1mdv2010.1
+ Revision: 503698
- New version 0.9.91

* Fri Jan 22 2010 Emmanuel Andry <eandry@mandriva.org> 0.9.9-2mdv2010.1
+ Revision: 495085
- fix build against gpsd 2.90 with p0 from debian

* Thu Oct 15 2009 Olivier Blin <blino@mandriva.org> 0.9.9-1mdv2010.0
+ Revision: 457590
- 0.9.9 (fixes build with latest libgps)

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.9.8-1mdv2010.0
+ Revision: 369355
- New version 0.9.8

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.9.7-1mdv2009.1
+ Revision: 332940
- New upstream release

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Sep 28 2008 Olivier Blin <blino@mandriva.org> 0.9.6-2mdv2009.0
+ Revision: 289002
- remove duplicate menu and icons, they are provided upstream (as of 0.9.5)

* Fri Sep 26 2008 Olivier Blin <blino@mandriva.org> 0.9.6-1mdv2009.0
+ Revision: 288615
- buildrequire intltool
- 0.9.6 (adapt to new google API)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Funda Wang <fwang@mandriva.org>
    - New version 0.9.5

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Austin Acton <austin@mandriva.org> 0.9.4-1mdv2009.0
+ Revision: 217828
- new version
- lang files

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - fix URL
    - Clearify license

* Tue Oct 23 2007 Funda Wang <fwang@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 101508
- update to new version 0.9.3
- fix file list

* Wed Sep 05 2007 Funda Wang <fwang@mandriva.org> 0.9.2-1mdv2008.0
+ Revision: 80139
- New version 0.9.2

* Mon Sep 03 2007 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 78438
- New version 0.9.1

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Wed Jul 18 2007 Austin Acton <austin@mandriva.org> 0.9-1mdv2008.0
+ Revision: 53160
- buildrequires curl-devel
- new version
- use own icon

* Fri Jun 15 2007 Austin Acton <austin@mandriva.org> 0.1.3-2mdv2008.0
+ Revision: 39825
- requires gpsbabel

* Fri May 18 2007 Austin Acton <austin@mandriva.org> 0.1.3-1mdv2008.0
+ Revision: 27742
- new version

* Mon Apr 30 2007 Austin Acton <austin@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 19640
- XDG menu
- buildrequires expat
- new version
- Import viking



* Fri Mar 11 2005 Austin Acton <austin@mandrake.org> 0.1.0-1mdk
- 0.1.0
- source URL
- cflags
- fix menu

* Fri Feb 20 2004 David Baudens <baudens@mandrakesoft.com> 0.0.5-2mdk
- Fix menu

* Wed Jul 16 2003 Austin Acton <aacton@yorku.ca> 0.0.5-1mdk
- initial package
