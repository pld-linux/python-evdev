#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	evdev
Summary:	Python bindings for the Linux input subsystem
Name:		python-%{module}
Version:	1.0.0
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/e/evdev/%{module}-%{version}.tar.gz
# Source0-md5:	1c9830c5a87ef5147cabfadfefc91a20
URL:		https://github.com/gvalkov/python-evdev
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings to the generic input event interface in
Linux. The evdev interface serves the purpose of passing events
generated in the kernel directly to userspace through character
devices that are typically located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle input
devices that can inject events directly into the input subsystem.

%package -n python3-%{module}
Summary:	Python bindings for the Linux input subsystem
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This package provides bindings to the generic input event interface in
Linux. The evdev interface serves the purpose of passing events
generated in the kernel directly to userspace through character
devices that are typically located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle input
devices that can inject events directly into the input subsystem.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif
