%include	/usr/lib/rpm/macros.perl
Summary:	Text-Format perl module
Summary(pl):	Modu³ perla Text-Format
Name:		perl-Text-Format
Version:	0.52
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Text/Text-Format%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Format - various subroutines to format text.

%description -l pl
Text-Format - ró¿ne subrutyny do formatowania tekstu.

%prep
%setup -q -n Text-Format%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Format.pm
%{_mandir}/man3/*
