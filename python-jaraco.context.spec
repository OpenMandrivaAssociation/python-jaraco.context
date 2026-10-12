Name:		python-jaraco.context
Version:	6.1.2
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.context/jaraco_context-%{version}.tar.gz
Summary:	Useful decorators and context managers
URL:		https://pypi.org/project/jaraco.context/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(coherent.licensed)
BuildSystem:	python
BuildArch:	noarch

%description
Useful decorators and context managers

%build -p
# The sdist is not a git checkout, so setuptools_scm needs the version.
# Without this the wheel was published as 0.0.0.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/jaraco/context
%{py_sitedir}/jaraco_context-*.*-info
