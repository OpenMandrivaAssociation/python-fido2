%define module fido2

Name:		python-fido2
Version:	2.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	FIDO2/WebAuthn library for implementing clients and servers
URL:		https://pypi.org/project/fido2/
License:	BSD-2-Clause
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cryptography) >= 2.6
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(pytest)
Requires:	python%{pyver}dist(cryptography) >= 2.6

%description
FIDO2/WebAuthn library for implementing clients and servers.

%check
%{__python3} -m unittest discover -v

%files
%license COPY*
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
