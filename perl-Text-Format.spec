#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Format perl module
Summary(pl):	Modu³ perla Text::Format
Name:		perl-Text-Format
Version:	0.52
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Format%{version}.tar.gz
# Source0-md5:	9b1936e65ee05d904bb329e32259814f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Format - various subroutines to format text.

%description -l pl
Text::Format - ró¿ne subrutyny do formatowania tekstu.

%prep
%setup -q -n Text-Format%{version}

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
%doc Changes README
%{perl_vendorlib}/Text/Format.pm
%{_mandir}/man3/*
