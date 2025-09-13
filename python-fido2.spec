Name:		python-fido2
Version:	2.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/fido2/fido2-%{version}.tar.gz
Summary:	FIDO2/WebAuthn library for implementing clients and servers.
URL:		https://pypi.org/project/fido2/
License:	BSD-2-Clause
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(poetry-core)

BuildSystem:	python
BuildArch:	noarch

%description
FIDO2/WebAuthn library for implementing clients and servers.

%files
%license COPY*
%{py_sitedir}/fido2
%{py_sitedir}/fido2-*.*-info
