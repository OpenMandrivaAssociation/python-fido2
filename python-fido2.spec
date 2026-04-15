%define module fido2

Name:		python-fido2
Version:	2.2.0
Release:	1
Summary:	FIDO2/WebAuthn library for implementing clients and servers
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://pypi.org/project/fido2
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cryptography) >= 2.6
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
# For unittests
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pyscard)
Requires:	python%{pyver}dist(cryptography) >= 2.6
# Optional dependency
Recommends:	python%{pyver}dist(pyscard)

%description
FIDO2/WebAuthn library for implementing clients and servers.

%check
%{__python3} -m unittest discover -v

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
