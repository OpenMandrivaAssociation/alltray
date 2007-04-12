%define	name	alltray
%define	version 0.66
%define	release	%mkrel 3
%define	major	0
%define	libname	%mklibname %{name} %{major}

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
BuildRequires:  GConf2
Requires:	%{libname} = %{epoch}:%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
With AllTray you can dock any application into the system
tray/notification area. A highlight feature is that a click on the
"close" button will minimize to system tray.

%package -n	%{libname}
Summary:	Shared library for alltray
Group:		System/Libraries
Provides:       %{_lib}%{name} = %{epoch}:%{version}-%{release}

%description -n	%{libname}
Shared library for alltray.

%package -n	%{libname}-devel
Summary:	Development libraries for alltray
Group:          Development/C
Requires:       %{libname} = %{epoch}:%{version}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{_lib}%{name}-devel = %{epoch}:%{version}-%{release}

%description -n %{libname}-devel
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
%{_libdir}/lib*.la

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.so

