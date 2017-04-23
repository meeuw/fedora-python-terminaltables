%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%global pypi_name terminaltables

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Generate simple tables in terminals from a nested list of strings.
License:        MIT
URL:            https://github.com/Robpol86/terminaltables
Source0:        https://github.com/Robpol86/%{pypi_name}/archive/v%{version}.tar.gz
BuildArch:      noarch

%description
Easily draw tables in terminal/console applications from a list of lists of
strings. Supports multi-line rows.

%package -n     python2-%{pypi_name}
Summary:        Generate simple tables in terminals from a nested list of strings.
%{?python_provide:%python_provide python2-%{pypi_name}}
%{?el6:Provides: python-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description -n python2-%{pypi_name}
Easily draw tables in terminal/console applications from a list of lists of
strings. Supports multi-line rows.

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        Generate simple tables in terminals from a nested list of strings.
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
%endif # with python3

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if %{with python3}
%py3_build
%endif # with python3

%install
%if %{with python3}
%py3_install
%endif # with python3
%py2_install


%files -n python2-%{pypi_name}
%{!?_licensedir:%global license %doc}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with python3

%changelog
* Sun Apr 23 2017 Dick Marinus <dick@mrns.nl> - 3.1.0-1
- Initial package.
