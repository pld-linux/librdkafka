Summary:	Apache Kafka C library
Summary(pl.UTF-8):	Biblioteka C do protokołu Apache Kafka
Name:		librdkafka
Version:	2.8.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/edenhill/librdkafka/releases
Source0:	https://github.com/edenhill/librdkafka/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ab7f14e916cbefa7f0e7d1fb06e08bfd
Patch0:		%{name}-pc.patch
URL:		https://github.com/edenhill/librdkafka
BuildRequires:	cmake >= 3.5
BuildRequires:	curl-devel
BuildRequires:	cyrus-sasl-devel >= 2.1.26
BuildRequires:	libstdc++-devel
BuildRequires:	lz4-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librdkafka is the C/C++ client library implementation of the Apache
Kafka protocol, containing both Producer and Consumer support.

This package contains C library.

%description -l pl.UTF-8
librdkafka to biblioteka kliencka C/C++ implementująca protokół Apache
Kafka, zawierająca obsługę zarówno producenta, jak i konsumenta.

Ten pakiet zawiera bibliotekę C.

%package devel
Summary:	Header files for rdkafka library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki rdkafka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	cyrus-sasl-devel >= 2.1.26
Requires:	openssl-devel
Requires:	lz4-devel
Requires:	zlib-devel
Requires:	zstd-devel

%description devel
Header files for rdkafka library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki rdkafka.

%package c++
Summary:	Apache Kafka C++ library
Summary(pl.UTF-8):	Biblioteka C++ do protokołu Apache Kafka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
librdkafka is the C/C++ client library implementation of the Apache
Kafka protocol, containing both Producer and Consumer support.

This package contains C++ library.

%description c++ -l pl.UTF-8
librdkafka to biblioteka kliencka C/C++ implementująca protokół Apache
Kafka, zawierająca obsługę zarówno producenta, jak i konsumenta.

Ten pakiet zawiera bibliotekę C++.

%package c++-devel
Summary:	Header files for rdkafka library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki rdkafka
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for rdkafka library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki rdkafka.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/licenses/librdkafka/LICENSES.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONFIGURATION.md INTRODUCTION.md LICENSE LICENSE.{cjson,crc32c,fnv1a,hdrhistogram,murmur2,nanopb,opentelemetry,pycrc,queue,regexp,tinycthread} LICENSES.txt README.md STATISTICS.md
%attr(755,root,root) %{_libdir}/librdkafka.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librdkafka.so
%dir %{_includedir}/librdkafka
%{_includedir}/librdkafka/rdkafka.h
%{_includedir}/librdkafka/rdkafka_mock.h
%{_pkgconfigdir}/rdkafka.pc
%{_libdir}/cmake/RdKafka

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librdkafka++.so.1

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librdkafka++.so
%{_includedir}/librdkafka/rdkafkacpp.h
%{_pkgconfigdir}/rdkafka++.pc
