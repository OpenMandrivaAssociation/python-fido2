%define module fido2
# pyscard is not built for Python 3.15
%bcond tests 0

Name:		python-fido2
Version:	2.2.1
Release:	2
Summary:	FIDO2/WebAuthn library for implementing clients and servers
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://pypi.org/project/fido2
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cryptography) >= 2.6
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pyscard)
%endif
Requires:	python%{pyver}dist(cryptography) >= 2.6
# Optional dependency
Recommends:	python%{pyver}dist(pyscard)

%description
FIDO2/WebAuthn library for implementing clients and servers.

%if %{with tests}
%check
python -m unittest discover -v
%endif

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
