Name:		python-jaraco.context
Version:	6.0.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.context/jaraco_context-%{version}.tar.gz
Summary:	Useful decorators and context managers
URL:		https://pypi.org/project/jaraco.context/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Useful decorators and context managers

%files
%{py_sitedir}/jaraco/context
%{py_sitedir}/jaraco_context-*.*-info
