%define	major	0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Docks any application into the system tray
Name:		alltray
Version:	0.71a
Release:	%mkrel 1
Epoch:		0
Group:		Graphical desktop/Other
License:	GPL
Url:		http://alltray.trausch.us/
Source0:	http://launchpad.net/alltray/old-maintenance/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:		alltray-0.71a-fix_linking.patch
BuildRequires:	gtk+2-devel
BuildRequires:  GConf2
BuildRequires:  libGConf2-devel
Requires:	%{libname} = %{epoch}:%{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
AllTray is a program you can use on systems running the X Window System to
dock any application which doesn't have a native tray icon into the system
tray/notification area. AllTray works with many desktop environments and
window managers, including Metacity  on GNOME, KWin  on KDE  and OpenBox,
both standalone and with GNOME or KDE.

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

#fix .desktop file
sed -i -e 's|%{name}.png|%{name}|' -e 's|Application;|GTK;|' %{name}.desktop

%build
%{configure2_5x}
%{make}
 
%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

#we don't want this
%{__rm} -rf %{buildroot}%{_libdir}/liballtray.la

%clean
%{__rm} -rf %{buildroot}

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

