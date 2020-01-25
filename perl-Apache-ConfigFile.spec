#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Apache
%define		pnam	ConfigFile
Summary:	Apache::ConfigFile - parse an Apache style httpd.conf config file
Summary(pl.UTF-8):	Apache::ConfigFile - analiza pliku konfiguracyjnego httpd.conf w stylu Apache
Name:		perl-Apache-ConfigFile
Version:	1.18
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-authors/id/N/NW/NWIGER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a7e1e1aca947f98a9a974150b722bff
URL:		http://search.cpan.org/dist/Apache-ConfigFile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses the Apache httpd.conf, or any compatible config
file, and provides methods for you to access the values from the
config file. The basic usage of this module boils down to reading a
given config file and then using the cmd_config() and cmd_context()
functions to access its information.

%description -l pl.UTF-8
Ten moduł analizuje plik Apache'a httpd.conf lub dowolny kompatybilny
plik konfiguracyjny i udostępnia metody pozwalające na dostęp do
wartości z tego pliku. Podstawowe używanie tego modułu sprowadza się
do przeczytania podanego pliku konfiguracyjnego, a następnie używania
funkcji cmd_config() i cmd_context() do odczytywania informacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
