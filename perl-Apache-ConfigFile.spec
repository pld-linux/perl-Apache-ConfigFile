#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	ConfigFile
Summary:	Apache::ConfigFile - Parse an Apache style httpd.conf config file
Summary(pl):	Apache::ConfigFile - analiza pliku konfiguracyjnego httpd.conf w stylu Apache
Name:		perl-Apache-ConfigFile
Version:	0.14
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses the Apache httpd.conf, or any compatible config
file, and provides methods for you to access the values from the
config file. The basic usage of this module boils down to reading a
given config file and then using the cmd_config() and cmd_context()
functions to access its information.

%description -l pl
Ten modu³ analizuje plik Apache'a httpd.conf lub dowolny kompatybilny
plik konfiguracyjny i udostêpnia metody pozwalaj±ce na dostêp do
warto¶ci z tego pliku. Podstawowe u¿ywanie tego modu³u sprowadza siê
do przeczytania podanego pliku konfiguracyjnego, a nastêpnie u¿ywania
funkcji cmd_config() i cmd_context() do odczytywania informacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
