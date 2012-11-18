#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Format Perl module - various subroutines to format text
Summary(pl.UTF-8):	Moduł Perla Text::Format - różne funkcje do formatowania tekstu
Name:		perl-Text-Format
Version:	0.58
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Format-%{version}.tar.gz
# Source0-md5:	e9577b0d46f527d64f954b133ea0fbcf
URL:		http://search.cpan.org/dist/Text-Format/
%{?with_tests:BuildRequires:	perl-Test-Simple}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Format Perl module provides various subroutines to format text.

%description -l pl.UTF-8
Moduł Perla Text::Format udostępnia różne funkcje do formatowania
tekstu.

%prep
%setup -q -n Text-Format-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/Format.pm
%{_mandir}/man3/Text::Format.3pm*
