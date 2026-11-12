#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	fastimport
Summary:	Python parser for fastimport (VCS interchange format)
Summary(pl.UTF-8):	Pythonowy parser formatu fastimport (do wymiany VCS)
Name:		python3-%{module}
Version:	0.9.16
Release:	1
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/project/simple/
Source0:	https://files.pythonhosted.org/packages/source/f/fastimport/%{module}-%{version}.tar.gz
# Source0-md5:	c5cc05ba12f6ed9ce7e1057816162d2e
Patch0:	%{name}-scripts-bytes-params.patch
Patch1:	%{name}-query-all-fields.patch
URL:		https://pypi.org/project/fastimport/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:61.2
%if %{with tests}
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
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
%patch -P0 -p1
%patch -P1 -p1

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m unittest fastimport.tests.test_suite
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/fast-import-filter
%attr(755,root,root) %{_bindir}/fast-import-info
%attr(755,root,root) %{_bindir}/fast-import-query
%{py3_sitescriptdir}/fastimport
%{py3_sitescriptdir}/fastimport-%{version}.dist-info
