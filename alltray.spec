%define	major	0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Docks any application into the system tray
Name:		alltray
Version:	0.71b
Release:	2
Group:		Graphical desktop/Other
License:	GPL
Url:		http://alltray.trausch.us/
Source0:	http://launchpad.net/alltray/old-maintenance/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:		alltray-0.71a-fix_linking.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(gconf-2.0)

%description
AllTray is a program you can use on systems running the X Window System to
dock any application which doesn't have a native tray icon into the system
tray/notification area. AllTray works with many desktop environments and
window managers, including Metacity  on GNOME, KWin  on KDE  and OpenBox,
both standalone and with GNOME or KDE.

%package -n	%{libname}
Summary:	Shared library for alltray
Group:		System/Libraries

%description -n	%{libname}
Shared library for alltray.

%package -n %{develname}
Summary:	Development libraries for alltray
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development libraries for alltray.

%prep
%setup -q
%patch0 -p0

#fix .desktop file
sed -i -e 's|%{name}.png|%{name}|' -e 's|Application;|GTK;|' %{name}.desktop

%build
%configure2_5x
%make
 
%install
%makeinstall_std

%files 
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so

