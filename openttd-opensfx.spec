%define realname opensfx

Name:           openttd-%{realname}
Version:        0.2.3
Release:        4
Summary:        OpenSFX sound replacement set for OpenTTD

Group:          Games/Strategy
License:        Creative Commons Sampling Plus 1.0 License
URL:            http://dev.openttdcoop.org/projects/opensfx
Source0:        http://bundles.openttdcoop.org/opensfx/releases/%{realname}-%{version}-source.tar.gz
BuildArch:      noarch
BuildRequires:  catcodec
Conflicts:      openttd < 1.0.0-2mdv

%description
OpenSFX is an open source replacement for the original Transport Tycoon
Deluxe base sounds used by OpenTTD.

%prep
%setup -q -n %{realname}-%{version}-source

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/openttd/data
%make install INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/data

%check
%make check

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%{_gamesdatadir}/openttd/data/%{realname}-%{version}.tar
