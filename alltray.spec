%define	name	alltray
%define	version 0.69
%define	release	%mkrel 2
%define	major	0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Docks any application into the system tray
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		0
Group:		Graphical desktop/Other
License:	GPL
Url:		http://alltray.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel
BuildRequires:  GConf2 libGConf2-devel
Requires:	%{libname} = %{epoch}:%{version}

%description
With AllTray you can dock any application into the system
tray/notification area. A highlight feature is that a click on the
"close" button will minimize to system tray.

%package -n	%{libname}
Summary:	Shared library for alltray
Group:		System/Libraries
Provides:       %{_lib}%{name} = %{epoch}:%{version}-%{release}
Conflicts:	liballtray0-devel < 0:0.69

%description -n	%{libname}
Shared library for alltray.

%package -n %{develname}
Summary:	Development libraries for alltray
Group:          Development/C
Requires:       %{libname} = %{epoch}:%{version}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{_lib}%{name}-devel = %{epoch}:%{version}-%{release}
Conflicts:	liballtray0 < 0:0.69
Obsoletes:	%{mklibname alltray 0}-devel

%description -n %{develname}
Development libraries for alltray.

%prep
%setup -q

%build
%configure2_5x
%make
 
%install
rm -rf %{buildroot}
%makeinstall

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.la

