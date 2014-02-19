%bcond_with x

Name:           libxkbfile
Version:        1.0.8
Release:        1
License:        MIT
Summary:        X.Org xkbfile library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libxkbfile.manifest
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%if !%{with x}
ExclusiveArch:
%endif

%description
X.Org X11 libxkbfile runtime library.

%package devel
Summary:        X.Org xkbfile library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libxkbfile development package

%prep
%setup -q
cp %{SOURCE1001} .

%build
# FIXME: We use -fno-strict-aliasing, to work around the following bug:
# maprules.c:1373: warning: dereferencing type-punned pointer will break strict-aliasing rules)
export CFLAGS="${CFLAGS} %{optflags} -fno-strict-aliasing"
%configure --disable-static
make %{?_smp_mflags}

%install

%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libxkbfile.so.1
%{_libdir}/libxkbfile.so.1.0.2

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/XKBbells.h
%{_includedir}/X11/extensions/XKBconfig.h
%{_includedir}/X11/extensions/XKBfile.h
%{_includedir}/X11/extensions/XKBrules.h
%{_includedir}/X11/extensions/XKM.h
%{_includedir}/X11/extensions/XKMformat.h
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc
