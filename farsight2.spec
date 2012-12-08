%define api		0.10
%define major		0
%define libname		%mklibname %{name}_%{version_lib}
%define develname	%mklibname -d %{name}

%define version_lib %{api}-%{major}

Summary:		An audio/video conferencing framework
Name:		farsight2
Version:		0.0.31
Release:		2
License:		LGPLv2+
URL:		http://farsight.freedesktop.org/wiki/	
Group:		Networking/Instant messaging
Source0:  	http://farsight.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gstreamer-app-0.10) >= 0.10.33
BuildRequires:	pkgconfig(gupnp-igd-1.0)
BuildRequires:	pkgconfig(nice) >= 0.1.0
BuildRequires:	pkgconfig(gst-python-0.10)
BuildRequires:	pkgconfig(python)

%description
FarSight2 is an audio/video conferencing framework 
specifically designed for Instant Messengers. It 
aims to provide a code structure that will be able 
to absorb as many video conferencing protocols as 
possible. It also offers an interface to those Instant 
Messengers, allowing them to embed the video feeds and 
controls into them.

FarSight is not a standalone application. It provides two 
APIs, one for interfacing with the different "protocol modules" 
and one for interfacing with the Instant Messenger GUI. There will 
also be a default GUI for those who don't wish to embed the feeds 
into their Instant Messenger's GUI.

%package -n %{libname}
Summary:	Farsight2 library
Group:		System/Libraries
Provides: 	%{name} = %{version}-%{release}

%description -n %{libname}
Library for %{name}

%package -n	gstreamer0.10-%{name}
Summary:	Set of plugins for Gstreamer used Audio/Video conferencing
Group:		Sound
Requires:	%{libname} = %{version}-%{release}
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-nice >= 0.1.0
Requires:	gstreamer0.10-voip
Conflicts:	gstreamer0.10-farstream >= 0.1.1

%description -n gstreamer0.10-%{name}
This is a set of plugins for Gstreamer that will be used by Farsight2
for Audio/Video conferencing.

%package -n   	python-%{name}
Summary:	Python binding for %{name}
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}

%description -n	python-%{name}
Python bindings for %{name}.

%package -n %{develname}
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-package-name="%{_vendor} %{name}" \
	--with-package-origin="http://www.mandriva.com"
%make

%install
%{makeinstall_std}

find %{buildroot} -name '*.la' | xargs rm

%files -n %{libname}
%{_libdir}/libgstfarsight-%{api}.so.%{major}*
%{_libdir}/%{name}-0.0/*.so

%files -n gstreamer0.10-%{name}
%{_libdir}/gstreamer-0.10/*.so
%{_datadir}/farsight2/0.0/fsrtpconference/default-codec-preferences
%{_datadir}/farsight2/0.0/fsrtpconference/default-element-properties

%files -n python-%{name}
%{python_sitearch}/farsight.so

%files -n %{develname}
%doc ChangeLog
%{_includedir}/gstreamer-0.10/gst/farsight/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/libgstfarsight-%{api}.so
%{_datadir}/gtk-doc/html/%{name}-libs-%{api}/*
%{_datadir}/gtk-doc/html/%{name}-plugins-%{api}/*


%changelog
* Thu May 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.0.31-2
+ Revision: 795347
- rel bump and rebuild

* Wed May 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.0.31-1
+ Revision: 795074
- version update 0.0.31

* Wed May 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.0.29-2
+ Revision: 795072
- rebuild for new libnice
- rebuild for new libnice

* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 0.0.29-1
+ Revision: 685503
- update to new version 0.0.29

* Sun May 15 2011 Götz Waschk <waschk@mandriva.org> 0.0.28-1
+ Revision: 674963
- new version
- update file list
- bump nice dep

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.22-2
+ Revision: 664264
- mass rebuild

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.0.22-1mdv2011.0
+ Revision: 592277
- new version 0.0.22

* Fri Jul 23 2010 Jani Välimaa <wally@mandriva.org> 0.0.21-1mdv2011.0
+ Revision: 557316
- new version 0.0.21

* Thu Jan 07 2010 Jani Välimaa <wally@mandriva.org> 0.0.17-2mdv2010.1
+ Revision: 487208
- rebuild for new gupnp-igd

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 0.0.17-1mdv2010.1
+ Revision: 486867
- update to new version 0.0.17

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.16-1mdv2010.1
+ Revision: 462617
- update to new version 0.0.16

* Tue Sep 22 2009 Frederic Crozat <fcrozat@mandriva.com> 0.0.15-2mdv2010.0
+ Revision: 447363
- Ensure gstreamer subpackage suggests gstreamer0.10-voip package
- remove python module from gstreamer package
- Add plugins-good as requirement of gstreamer package

* Mon Sep 07 2009 Emmanuel Andry <eandry@mandriva.org> 0.0.15-1mdv2010.0
+ Revision: 432543
- New version 0.0.15

* Wed Aug 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.14-1mdv2010.0
+ Revision: 410389
- Update to new version 0.0.14

* Sun Jun 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.12-2mdv2010.0
+ Revision: 387852
- Rebuild for new libgupnp-igd2

* Fri May 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.12-1mdv2010.0
+ Revision: 381157
- update to new version 0.0.12

* Wed May 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.11-1mdv2010.0
+ Revision: 380278
- Add BuildRequires: python-devel
- Update to new version 0.0.11

* Fri May 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.9-1mdv2010.0
+ Revision: 373490
- Update to new version 0.0.9
- Remove patch included upstream

* Mon Mar 23 2009 Emmanuel Andry <eandry@mandriva.org> 0.0.8-3mdv2009.1
+ Revision: 360746
- diff patch from git to fix compatibility issues with latest gst-plugins-farsight

* Tue Mar 17 2009 Emmanuel Andry <eandry@mandriva.org> 0.0.8-1mdv2009.1
+ Revision: 356333
- New version 0.0.8
- fix BR
- update files list

* Thu Jan 22 2009 Emmanuel Andry <eandry@mandriva.org> 0.0.7-1mdv2009.1
+ Revision: 332670
- New version 0.0.7
- create python package

* Sat Jan 03 2009 Emmanuel Andry <eandry@mandriva.org> 0.0.6-1mdv2009.1
+ Revision: 323994
- New version
- fix library summary

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.0.4-2mdv2009.1
+ Revision: 320292
- rebuild for new python

* Sun Nov 30 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.4-1mdv2009.1
+ Revision: 308519
- import farsight2

