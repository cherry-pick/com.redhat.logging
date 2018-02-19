Name:           com.redhat.logging
Version:        2
Release:        1%{?dist}
Summary:        System Logging Interface
License:        ASL2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  libvarlink-devel
BuildRequires:  systemd-devel

%description
Service to access the system log.

%prep
%setup -q

%build
%meson
%meson_build

%check
export LC_CTYPE=C.utf8
%meson_test

%install
%meson_install

%files
%license LICENSE
%{_bindir}/com.redhat.logging

%changelog
* Tue Aug 29 2017 <info@varlink.org> 2-1
- com.redhat.logging 2
