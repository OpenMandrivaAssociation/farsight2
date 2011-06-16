%define api 0.10
%define major 0
%define libname %mklibname %{name}_%{version_lib}
%define develname %mklibname -d %{name}

%define version_lib %{api}-%{major}

%define	name    farsight2
%define	version 0.0.29
%define	release %mkrel 1

%define nicever 0.1.0

Summary:	An audio/video conferencing framework
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
URL:		http://farsight.sourceforge.net/	
Group:		Networking/Instant messaging
Source0:  	http://farsight.freedesktop.org/releases/farsight2/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  gtk-doc
BuildRequires:  libgstreamer-plugins-base-devel
BuildRequires:  gupnp-igd-devel 
BuildRequires:	nice-devel >= %nicever
BuildRequires:	gstreamer0.10-python-devel
BuildRequires:	python-devel


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
Requires:	%{name} >= %version

%description -n %{libname}
Library for %{name}

%package -n	gstreamer0.10-%{name}
Summary:	Set of plugins for Gstreamer used Audio/Video conferencing
Group:		Sound
Requires:	%{libname} >= %version
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-libnice >= %nicever
# can not hard requires packages from contrib
Suggests:	gstreamer0.10-voip

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
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}

%{makeinstall_std}

find %{buildroot} -name *.la | xargs rm

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgstfarsight-%{api}.so.%{major}*
%{_libdir}/%{name}-0.0/*.so
%dir %_datadir/farsight2
%_datadir/farsight2/0.0

%files -n gstreamer0.10-%{name}
%defattr(-,root,root)
%{_libdir}/gstreamer-0.10/*.so

%files -n python-%{name}
%defattr(-,root,root,-)
%{python_sitearch}/farsight.so

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog
%{_includedir}/gstreamer-0.10/gst/farsight/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/libgstfarsight-%{api}.so
%{_datadir}/gtk-doc/html/%{name}-libs-%{api}/*
%{_datadir}/gtk-doc/html/%{name}-plugins-%{api}/*
