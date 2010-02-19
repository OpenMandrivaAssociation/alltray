%define	major	0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Docks any application into the system tray
Name:		alltray
Version:	0.70
Release:	%mkrel 4
Epoch:		0
Group:		Graphical desktop/Other
License:	GPL
Url:		http://alltray.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sourceforge/alltray/alltray-%{version}.tar.gz
Patch0:		alltray-0.70-fix-link.patch
BuildRequires:	gtk+2-devel
BuildRequires:  GConf2
BuildRequires:  libGConf2-devel
Requires:	%{libname} = %{epoch}:%{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
With AllTray you can dock any application into the system
tray/notification area. A highlight feature is that a click on the
"close" button will minimize to system tray.

%package -n	%{libname}
Summary:	Shared library for alltray
Group:		System/Libraries
Provides:       %{_lib}%{name} = %{epoch}:%{version}-%{release}
Conflicts:	%{_lib}%{name}0-devel < %{epoch}:%{version}-%{release}

%description -n	%{libname}
Shared library for alltray.

%package -n %{develname}
Summary:	Development libraries for alltray
Group:          Development/C
Requires:       %{libname} = %{epoch}:%{version}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{_lib}%{name}-devel = %{epoch}:%{version}-%{release}
Conflicts:	%{_lib}%{name}0 < %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname alltray 0}-devel

%description -n %{develname}
Development libraries for alltray.

%prep
%setup -q
%patch0 -p0

%build
%{configure2_5x}
%{make}
 
%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files 
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/lib*.so.%{major}
%{_libdir}/lib*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root,0755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la

