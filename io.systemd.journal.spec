%define build_date %(date +"%%a %%b %%d %%Y")
%define build_timestamp %(date +"%%Y%%m%%d.%%H%m%%S")

Name:           io.systemd.journal
Version:        1
Release:        %{build_timestamp}%{?dist}
Summary:        Systemd Journal Interface
License:        ASL2.0
URL:            https://github.com/varlink/io.systemd.journal
Source0:        https://github.com/varlink/io.systemd.journal/archive/v%{version}.tar.gz
BuildRequires:  autoconf automake pkgconfig
BuildRequires:  libvarlink-devel
BuildRequires:  systemd-devel

%description
Service to access the systemd journal.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license AUTHORS
%license COPYRIGHT
%license LICENSE
%{_bindir}/io.systemd.journal

%changelog
* %{build_date} <info@varlink.org> %{version}-%{build_timestamp}
- %{name} %{version}
