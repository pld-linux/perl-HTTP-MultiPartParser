#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	MultiPartParser
Summary:	HTTP::MultiPartParser - HTTP MultiPart Parser
#Summary(pl.UTF-8):	
Name:		perl-HTTP-MultiPartParser
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b07ebac54ce3288c044a23ba60196d2
URL:		http://search.cpan.org/dist/HTTP-MultiPartParser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Deep
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides a low-level API for processing MultiPart MIME data streams 
conforming to MultiPart types as defined in RFC 2616.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/*.pm
%{perl_vendorlib}/HTTP/MultiPartParser.pod
%{_mandir}/man3/HTTP::MultiPartParser.3*
%{_examplesdir}/%{name}-%{version}
