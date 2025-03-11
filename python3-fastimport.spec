#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	fastimport
Summary:	Python parser for fastimport (VCS interchange format)
Summary(pl.UTF-8):	Pythonowy parser formatu fastimport (do wymiany VCS)
Name:		python3-%{module}
Version:	0.9.14
Release:	5
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/project/simple/
Source0:	https://files.pythonhosted.org/packages/source/f/fastimport/%{module}-%{version}.tar.gz
# Source0-md5:	be8e2780fadd9e4047c7b37b91e20751
URL:		https://pypi.org/project/fastimport/
BuildRequires:	python3-modules >= 1:3.6
%if %{with tests}
BuildRequires:	python3-nose
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

%description -l pl.UTF-8
Pythonowy parser, oryginalnie stworzony na potrzeby bzr-fastimport,
ale wyciągnięty do osobnego modułu, dzięki czemu może być używany
przez inne projekty.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
nosetests-%{py3_ver} fastimport
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{module}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/fast-import-filter
%attr(755,root,root) %{_bindir}/fast-import-info
%attr(755,root,root) %{_bindir}/fast-import-query
%{py3_sitescriptdir}/fastimport
%{py3_sitescriptdir}/fastimport-%{version}-py*.egg-info
