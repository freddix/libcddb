Summary:	Library to access data on a CDDB server
Name:		libcddb
Version:	1.3.2
Release:	5
License:	LGPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/libcddb/%{name}-%{version}.tar.bz2
# Source0-md5:	8bb4a6f542197e8e9648ae597cd6bc8a
URL:		http://libcddb.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org/). It
tries to be as cross-platform as possible.

%package devel
Summary:	Header files for libcddb library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcddb library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/cddb
%{_pkgconfigdir}/*.pc

