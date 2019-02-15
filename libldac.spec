%global archivename ldacBT
%global sonamebase 2

Name:           libldac
Version:        %{sonamebase}.0.2.2
Release:        3%{?dist}
Summary:        A lossy audio codec for Bluetooth connections

License:        ASL 2.0
URL:            https://github.com/EHfive/ldacBT
Source0:        %{url}/releases/download/v%{version}/%{archivename}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description
LDAC is an audio coding technology developed by Sony.
It enables the transmission of High-Resolution Audio content,
even over a Bluetooth connection.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{archivename}

%build
%{cmake3} \
    -DLDAC_SOFT_FLOAT=OFF \
    -DINSTALL_LIBDIR=%{_libdir} \
    ./

%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libldacBT_abr.so.%{sonamebase}
%{_libdir}/libldacBT_abr.so.%{sonamebase}.*
%{_libdir}/libldacBT_enc.so.%{sonamebase}
%{_libdir}/libldacBT_enc.so.%{sonamebase}.*

%files devel
%dir %{_includedir}/ldac
%{_includedir}/ldac/ldacBT_abr.h
%{_includedir}/ldac/ldacBT.h
%{_libdir}/pkgconfig/ldacBT-abr.pc
%{_libdir}/pkgconfig/ldacBT-enc.pc
%{_libdir}/libldacBT_abr.so
%{_libdir}/libldacBT_enc.so

%changelog
* Thu Feb 7 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.2-3
- Minor fixes before Fedora submission

* Wed Jan 30 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.2-2
- Fix package reviewer suggestions

* Tue Jan 29 2019 Gergely Gombos <gombosg@gmail.com> - 2.0.2.2-1
- Update to 2.0.2.2, fix file listing

* Sun Jan 27 2019 Gergely Gombos <gombosg@gmail.com>
- Rename to libldac, prepare for RPMFusion submission

* Sun Dec 16 2018 Gergely Gombos <gombosg@gmail.com>
- Packaged 1.1
