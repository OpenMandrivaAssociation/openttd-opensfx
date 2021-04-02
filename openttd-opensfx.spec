%define realname opensfx

Name:           openttd-%{realname}
Version:        1.0.1
Release:        1
Summary:        OpenSFX sound replacement set for OpenTTD

Group:          Games/Strategy
License:        CC BY-SA 3.0, GPLv2+, CDDL 1.1 
URL:            http://dev.openttdcoop.org/projects/opensfx
Source0:        https://cdn.openttd.org/opensfx-releases/%{version}/opensfx-%{version}-source.tar.xz
BuildArch:      noarch
BuildRequires:  catcodec

%description
OpenSFX is an open source replacement for the original Transport Tycoon
Deluxe base sounds used by OpenTTD.

%prep
%setup -q -n %{realname}-%{version}-source

%build
%make_build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/openttd/data
%make_install INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/data

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%{_gamesdatadir}/openttd/data/%{realname}-%{version}.tar
